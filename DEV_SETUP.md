# Dev Setup

Two ways to run the SDX React app locally:

1. **Real SDX stack** — full integration via the `sdx-end-to-end-tests` repo
2. **Flask mock** — offline UI dev, no SDX dependencies

---

## Scenario 1: Real SDX stack (full integration)

```bash
# 1. Bring up SDX (Apple Silicon needs the platform var)
export DOCKER_DEFAULT_PLATFORM=linux/amd64
cd /Users/cesar/Documents/GitHub/sdx-end-to-end-tests
docker compose up -d
./wait-mininet-ready.sh
./scripts/run-mininet-interactive.sh

# 2. Force topology push to the controller
for oxp in ampath sax tenet; do
  docker compose exec -T $oxp curl -s -X POST http://localhost:8181/api/kytos/sdx/topology/2.0.0
  echo
done

# 3. Verify the controller has topology (expect HTTP 200)
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:8090/SDX-Controller/topology

# 4. Make sure backend/.env points at the real controller:
#    SDX_API_BASE_URL=http://host.docker.internal:8090/SDX-Controller

# 5. Bring up the React app
cd /Users/cesar/Documents/GitHub/sdx-react-app
docker compose up -d   # or `docker compose restart backend` if already running
```

Open <http://127.0.0.1:5002/>.

### Notes

- The `docker-compose.override.yml` in the `sdx-end-to-end-tests` repo publishes the SDX Controller on host port **8090** (the default 8080 collides with `kafka-ui`).
- The `run-mininet-interactive.sh` step is required — without it, mininet's switches never connect to the OXPs and the controller's `/topology` returns 204 No Content.
- After topology has been pushed once, the OXPs continue pushing on their own interval, so you usually only need step 2 right after a fresh bring-up.

---

## Scenario 2: Flask mock (offline UI dev)

```bash
# 1. Run the mock (serves on :6098)
cd /Users/cesar/Documents/GitHub/sdx-react-app
python backend/mocks/topology.py

# 2. Edit backend/.env — switch the active line to:
#    SDX_API_BASE_URL=http://host.docker.internal:6098

# 3. Restart the backend
docker compose restart backend
```

The mock currently implements `GET /topology` (sample data) and `GET /l2vpn/1.0` (returns `{}`). `POST/PATCH/DELETE` for L2VPNs are **not** mocked — for create/edit/delete flows, use Scenario 1.

---

## Shutdown

```bash
# Real SDX stack
cd /Users/cesar/Documents/GitHub/sdx-end-to-end-tests && docker compose down

# React app
cd /Users/cesar/Documents/GitHub/sdx-react-app && docker compose down
```

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `no matching manifest for linux/arm64/v8` | Apple Silicon pulling amd64-only images | `export DOCKER_DEFAULT_PLATFORM=linux/amd64` |
| `/api/topology` returns 500, error "Internal server error while fetching topology" | Controller returned 204 (no topology yet) — Node backend can't parse empty body | Run step 2 of Scenario 1 (force topology push) |
| `/api/topology` 500 right after switching `.env` | Backend hasn't reloaded env vars | `docker compose restart backend` |
| `/SDX-Controller/topology` returns Spring-style 404 | Hitting `kafka-ui` on port 8080 instead of the controller | Use port **8090** (the override) |
| OXP `switches: {}` and topology push returns code 424 | Mininet hasn't connected switches to OXPs | Run `./scripts/run-mininet-interactive.sh` |

---

## One-time setup tips

- Add `export DOCKER_DEFAULT_PLATFORM=linux/amd64` to `~/.zshrc` so you don't need to set it each session.
- Enable Rosetta in Docker Desktop (*Settings → General → "Use Rosetta for x86/amd64 emulation on Apple Silicon"*) for better emulation performance.
