from flask import Flask
# from flask_httpauth import HTTPBasicAuth
# auth = HTTPBasicAuth()

# USER_DATA = {
#     "admin": "SuperSecretPwd"
# }


# @auth.verify_password
# def verify(username, password):
#     if not (username and password):
#         return False
#     return USER_DATA.get(username) == password

app = Flask(__name__)


@app.route('/l2vpn/1.0', methods=['GET'])
def list_l2vpns():
    return {}


@app.route('/topology')
# @auth.login_required
def hello_world():

    return {
  "id": "urn:sdx:topology:",
  "links": [
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:interdomain:amlight.net:MIA-MI1-SW16:30:sax.net:FOR-ACB-SW01:et-1/1/4",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-FTZ-Monet--et-1/1/4",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW16:30",
        "urn:sdx:port:sax.net:FOR-ACB-SW01:et-1/1/4"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:interdomain:amlight.net:SAO-SP4-SW03:1:sax.net:FOR-ACB-SW01:et-0/1/4",
      "latency": 0,
      "measurement_period": "null",
      "name": "FOR-ABC-SW01_et-0/1/4_-_Monet_--et-0/1/4",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW03:1",
        "urn:sdx:port:sax.net:FOR-ACB-SW01:et-0/1/4"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:ATL-LUM-SW01/12_ATL-LUM-SW01/26",
      "latency": 0,
      "measurement_period": "null",
      "name": "ATL-LUM-SW01/12_ATL-LUM-SW01/26",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:ATL-LUM-SW01:12",
        "urn:sdx:port:amlight.net:ATL-LUM-SW01:26"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 0,
      "bandwidth": 2000,
      "id": "urn:sdx:link:sax.net:FOR-ACB-SW01/ae1_FOR-LAN-SW02/ae1",
      "latency": 0,
      "measurement_period": "null",
      "name": "FOR-ACB-SW01/ae1_FOR-LAN-SW02/ae1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:sax.net:FOR-ACB-SW01:ae1",
        "urn:sdx:port:sax.net:FOR-LAN-SW02:ae1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:ATL-LUM-SW01_ATL-LUM-SW02-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "ATL-LUM-SW01_ATL-LUM-SW02-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:ATL-LUM-SW01:2",
        "urn:sdx:port:amlight.net:ATL-LUM-SW02:2"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:BCT-MI3-SW03_BCT-MI3-SW04-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "BCT-MI3-SW03_BCT-MI3-SW04-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BCT-MI3-SW03:31",
        "urn:sdx:port:amlight.net:BCT-MI3-SW04:31"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:BCT-MI3-SW03_BCT-MI3-SW04-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "BCT-MI3-SW03_BCT-MI3-SW04-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BCT-MI3-SW03:2",
        "urn:sdx:port:amlight.net:BCT-MI3-SW04:2"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW03_SAO-SP4-SW04-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW03_SAO-SP4-SW04-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW03:31",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:31"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:JAX-LUM-SW01_JAX-LUM-SW02-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "JAX-LUM-SW01_JAX-LUM-SW02-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:JAX-LUM-SW01:2",
        "urn:sdx:port:amlight.net:JAX-LUM-SW02:2"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SCL-100G-01",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SCL-100G-01",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:1",
        "urn:sdx:port:amlight.net:SCL-CIR-SW03:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SJU-PTY-100G-01",
      "latency": 0,
      "measurement_period": "null",
      "name": "SJU-PTY-100G-01",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:1",
        "urn:sdx:port:amlight.net:SJU-H787-SW03:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-FOR-MIA-100G-01",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-FOR-MIA-100G-01",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SCL-CIR-SW03_SCL-CIR-SW04-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "SCL-CIR-SW03_SCL-CIR-SW04-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SCL-CIR-SW03:2",
        "urn:sdx:port:amlight.net:SCL-CIR-SW04:2"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:BUE-BTW-SW01_BUE-BTW-SW02-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "BUE-BTW-SW01_BUE-BTW-SW02-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BUE-BTW-SW01:31",
        "urn:sdx:port:amlight.net:BUE-BTW-SW02:31"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SJU-H787-SW02_SJU-H787-SW03-10",
      "latency": 0,
      "measurement_period": "null",
      "name": "SJU-H787-SW02_SJU-H787-SW03-10",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SJU-H787-SW02:2",
        "urn:sdx:port:amlight.net:SJU-H787-SW03:2"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:ATL-LUM-SW01_ATL-LUM-SW02-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "ATL-LUM-SW01_ATL-LUM-SW02-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:ATL-LUM-SW01:31",
        "urn:sdx:port:amlight.net:ATL-LUM-SW02:31"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW14_MIA-MI1-SW15-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW14_MIA-MI1-SW15-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW14:2",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:2"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:BCT-SAO-100G-02",
      "latency": 0,
      "measurement_period": "null",
      "name": "BCT-SAO-100G-02",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BCT-MI3-SW04:30",
        "urn:sdx:port:amlight.net:SAO-SP4-SW03:2"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:BUE-SCL-100G-01",
      "latency": 0,
      "measurement_period": "null",
      "name": "BUE-SCL-100G-01",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BUE-BTW-SW01:30",
        "urn:sdx:port:amlight.net:SCL-CIR-SW03:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-BCT-100G-01",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-BCT-100G-01",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BCT-MI3-SW03:32",
        "urn:sdx:port:amlight.net:MIA-MI1-SW14:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW03_SAO-SP4-SW04-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW03_SAO-SP4-SW04-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW03:3",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:3"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW14_MIA-MI1-SW18-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW14_MIA-MI1-SW18-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW14:28",
        "urn:sdx:port:amlight.net:MIA-MI1-SW18:3"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-BUE-100G-05",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-BUE-100G-05",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BUE-BTW-SW02:1",
        "urn:sdx:port:amlight.net:SAO-SP4-SW03:4"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SJU-H787-SW02_SJU-H787-SW03-10",
      "latency": 0,
      "measurement_period": "null",
      "name": "SJU-H787-SW02_SJU-H787-SW03-10",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SJU-H787-SW02:31",
        "urn:sdx:port:amlight.net:SJU-H787-SW03:31"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-BCT-100G-03",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-BCT-100G-03",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BCT-MI3-SW03:29",
        "urn:sdx:port:amlight.net:MIA-MI1-SW16:29"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-BUE-100G-02",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-BUE-100G-02",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BUE-BTW-SW02:3",
        "urn:sdx:port:amlight.net:SAO-SP4-SW03:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-SCL-100G-01",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-SCL-100G-01",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:2",
        "urn:sdx:port:amlight.net:SCL-CIR-SW04:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW14_MIA-MI1-SW17-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW14_MIA-MI1-SW17-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW14:30",
        "urn:sdx:port:amlight.net:MIA-MI1-SW17:4"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 10,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-BCT-100G-02",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-BCT-100G-02",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BCT-MI3-SW04:32",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-JAX-100G-01",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-JAX-100G-01",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:JAX-LUM-SW02:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW16:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-JAX-100G-02",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-JAX-100G-02",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:JAX-LUM-SW01:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW18:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-SJU-100G-01",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-SJU-100G-01",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW14:1",
        "urn:sdx:port:amlight.net:SJU-H787-SW02:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:BCT-ATL-100G-02",
      "latency": 0,
      "measurement_period": "null",
      "name": "BCT-ATL-100G-02",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:ATL-LUM-SW02:1",
        "urn:sdx:port:amlight.net:BCT-MI3-SW04:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW03_SAO-SP4-SW04-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW03_SAO-SP4-SW04-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW03:5",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:5"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:BCT-ATL-100G-01",
      "latency": 0,
      "measurement_period": "null",
      "name": "BCT-ATL-100G-01",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:ATL-LUM-SW01:1",
        "urn:sdx:port:amlight.net:BCT-MI3-SW03:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-BUE-100G-01",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-BUE-100G-01",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BUE-BTW-SW01:1",
        "urn:sdx:port:amlight.net:SAO-SP4-SW03:30"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:BCT-SAO-100G-01",
      "latency": 0,
      "measurement_period": "null",
      "name": "BCT-SAO-100G-01",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BCT-MI3-SW03:30",
        "urn:sdx:port:amlight.net:SAO-SP4-SW03:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:BUE-BTW-SW01_BUE-BTW-SW02-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "BUE-BTW-SW01_BUE-BTW-SW02-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BUE-BTW-SW01:2",
        "urn:sdx:port:amlight.net:BUE-BTW-SW02:2"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:JAX-ATL-100G-01",
      "latency": 0,
      "measurement_period": "null",
      "name": "JAX-ATL-100G-01",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:ATL-LUM-SW01:29",
        "urn:sdx:port:amlight.net:JAX-LUM-SW01:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15_MIA-MI1-SW16-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15_MIA-MI1-SW16-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:3",
        "urn:sdx:port:amlight.net:MIA-MI1-SW16:3"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15_MIA-MI1-SW18-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15_MIA-MI1-SW18-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:28",
        "urn:sdx:port:amlight.net:MIA-MI1-SW18:29"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 0.00100000000000477,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:JAX-LUM-SW01_JAX-LUM-SW02-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "JAX-LUM-SW01_JAX-LUM-SW02-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:JAX-LUM-SW01:31",
        "urn:sdx:port:amlight.net:JAX-LUM-SW02:31"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SCL-CIR-SW03_SCL-CIR-SW04-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "SCL-CIR-SW03_SCL-CIR-SW04-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SCL-CIR-SW03:31",
        "urn:sdx:port:amlight.net:SCL-CIR-SW04:31"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW14_MIA-MI1-SW16-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW14_MIA-MI1-SW16-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW14:4",
        "urn:sdx:port:amlight.net:MIA-MI1-SW16:4"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-FTZ-SAO-100G-01",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-FTZ-SAO-100G-01",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15_MIA-MI1-SW17-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15_MIA-MI1-SW17-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:30",
        "urn:sdx:port:amlight.net:MIA-MI1-SW17:5"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-BUE-100G-03",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-BUE-100G-03",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BUE-BTW-SW01:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW03:23"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-BUE-100G-04",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-BUE-100G-04",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:BUE-BTW-SW02:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW03:28"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW03_SAO-SP4-SW04-100G",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW03_SAO-SP4-SW04-100G",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW03:27",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:27"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "enabled",
      "status": "up",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/1_MIA-MI1-SW15/1",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:1"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "latency": 0,
      "measurement_period": "null",
      "name": "MIA-MI1-SW15/16_MIA-MI1-SW15/16",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
        "urn:sdx:port:amlight.net:MIA-MI1-SW15:16"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:PTY-TON-SW01/6_PTY-TON-SW01/6",
      "latency": 0,
      "measurement_period": "null",
      "name": "PTY-TON-SW01/6_PTY-TON-SW01/6",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
        "urn:sdx:port:amlight.net:PTY-TON-SW01:6"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    },
    {
      "availability": 100,
      "bandwidth": 100,
      "id": "urn:sdx:link:amlight.net:SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "latency": 0,
      "measurement_period": "null",
      "name": "SAO-SP4-SW04/32_SAO-SP4-SW04/32",
      "packet_loss": 0,
      "ports": [
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
        "urn:sdx:port:amlight.net:SAO-SP4-SW04:32"
      ],
      "private_attributes": "null",
      "residual_bandwidth": 100,
      "short_name": "null",
      "state": "disabled",
      "status": "down",
      "timestamp": "null"
    }
  ],
  "model_version": "2.0.0",
  "name": "SAX",
  "nodes": [
    {
      "id": "urn:sdx:node:sax.net:FOR-ACB-SW01",
      "location": {
        "address": "null",
        "iso3166_2_lvl4": "null",
        "latitude": -4,
        "longitude": -38
      },
      "name": "FOR-ACB-SW01",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-0/1/0",
          "name": "et-0/1/0",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-0/1/1",
          "name": "et-0/1/1",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-0/1/2",
          "name": "et-0/1/2",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-0/1/3",
          "name": "et-0/1/3",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-0/1/4",
          "name": "et-0/1/4",
          "nni": "urn:sdx:port:amlight.net:SAO-SP4-SW03:1",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-0/1/5",
          "name": "et-0/1/5",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-0/1/8",
          "name": "et-0/1/8",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-0/1/9",
          "name": "et-0/1/9",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "RNP - National Education and Research Network in Brazil - Fortaleza"
          ],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-1/1/0",
          "name": "et-1/1/0",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-1/1/2",
          "name": "et-1/1/2",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-1/1/3",
          "name": "et-1/1/3",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-1/1/4",
          "name": "et-1/1/4",
          "nni": "urn:sdx:port:amlight.net:MIA-MI1-SW16:30",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-1/1/7",
          "name": "et-1/1/7",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "TENET - Tertiary Education and Research Network of South Africa - CapeTown"
          ],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-1/1/8",
          "name": "et-1/1/8",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-1/1/9",
          "name": "et-1/1/9",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:ae1",
          "name": "ae1",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "Other",
          "vlan_range": "null"
        },
        {
          "entities": [
            "RedClara - Latin American Cooperation of Advanced Networks - Fortaleza"
          ],
          "id": "urn:sdx:port:sax.net:FOR-ACB-SW01:ae3",
          "name": "ae3",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-ACB-SW01",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "Other",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:sax.net:FOR-LAN-SW02",
      "location": {
        "address": "null",
        "iso3166_2_lvl4": "null",
        "latitude": -4,
        "longitude": -39
      },
      "name": "FOR-LAN-SW02",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-LAN-SW02:et-0/0/1",
          "name": "et-0/0/1",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-LAN-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-LAN-SW02:et-0/0/2",
          "name": "et-0/0/2",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-LAN-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:sax.net:FOR-LAN-SW02:ae1",
          "name": "ae1",
          "nni": "",
          "node": "urn:sdx:node:sax.net:FOR-LAN-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "Other",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
      "location": {
        "address": "Datacenter MI1",
        "iso3166_2_lvl4": "US-FL",
        "latitude": 45,
        "longitude": -50
      },
      "name": "MIA-MI1-SW14",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:1",
          "name": "SJU-H787-SW02_port_1_-_FIU035W",
          "nni": "urn:sdx:link:amlight.net:MIA-SJU-100G-01",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:2",
          "name": "MIA-MI1-SW15_port_2_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW14_MIA-MI1-SW15-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:3",
          "name": "novi_port_3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:4",
          "name": "MIA-MI1-SW16_port_4_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW14_MIA-MI1-SW16-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:7",
          "name": "novi_port_7",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:8",
          "name": "novi_port_8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "AmLight Router - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:9",
          "name": "MIA-MI1-RT04_et-0/0/1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:10",
          "name": "novi_port_10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:13",
          "name": "loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:14",
          "name": "novi_port_14",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:15",
          "name": "novi_port_15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:16",
          "name": "novi_port_16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:19",
          "name": "loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-mia-new ens1f0np0 - perfsonar testpoint - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:20",
          "name": "ps-mia-new_ens1f0np0",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "FIU - Florida International University - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:23",
          "name": "FIU-WR1_Hu0/0/0/1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3846",
                "3848"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:28",
          "name": "MIA-MI1-SW18_port_3_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW14_MIA-MI1-SW18-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:30",
          "name": "MIA-MI1-SW17_port_4",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW14_MIA-MI1-SW17-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:31",
          "name": "novi_port_31",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:32",
          "name": "BCT-MI3-SW02_port_32",
          "nni": "urn:sdx:link:amlight.net:MIA-BCT-100G-01",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "UVI - University of the Virgin Islands - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:114",
          "name": "UVI",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:214",
          "name": "novi_port_214",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW14:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW14",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
      "location": {
        "address": "Datacenter MI1",
        "iso3166_2_lvl4": "US-FL",
        "latitude": 45,
        "longitude": -10
      },
      "name": "MIA-MI1-SW15",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:1",
          "name": "MON_FOR-LAN-SW02_et-0/0/2_--_F",
          "nni": "urn:sdx:link:amlight.net:MIA-FTZ-SAO-100G-01",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:2",
          "name": "MIA-MI1-SW14_port_2_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW14_MIA-MI1-SW15-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:3",
          "name": "MIA-MI1-SW16_port_3_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW15_MIA-MI1-SW16-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:7",
          "name": "novi_port_7",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:8",
          "name": "novi_port_8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "AmLight Router - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:9",
          "name": "MIA-MI1-RT05_et-0/0/1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "4015-4019",
                "2990-2999",
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "RedClara - Latin American Cooperation of Advanced Networks - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:10",
          "name": "RedClara_rtr-core-mia_0/0/0/0",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3828",
                "3831-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:13",
          "name": "loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:14",
          "name": "novi_port_14",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:15",
          "name": "loop-16,shimlayer-link-PTY-FOR",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "2840-2841"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:16",
          "name": "loop-15,virtual-link-PTY-FOR-M",
          "nni": "urn:sdx:link:amlight.net:PTY-FOR-MIA-100G-01",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:19",
          "name": "loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-mia-new ens1f1np1 - perfsonar testpoint - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:20",
          "name": "ps-mia-new_ens1f1np1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:23",
          "name": "FIU-Optix01_1/3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:28",
          "name": "MIA-MI1-SW18_port_29_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW15_MIA-MI1-SW18-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:30",
          "name": "MIA-MI1-SW17_port_5",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW15_MIA-MI1-SW17-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:31",
          "name": "novi_port_31",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:32",
          "name": "BCT-MI3-SW02_port_27",
          "nni": "urn:sdx:link:amlight.net:MIA-BCT-100G-02",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-mia-public enp1s0 - perfsonar testpoint - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:114",
          "name": "ps-mia-public_enp1s0",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:214",
          "name": "novi_port_214",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW15:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW15",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
      "location": {
        "address": "Datacenter MI1",
        "iso3166_2_lvl4": "US-FL",
        "latitude": 35,
        "longitude": -45
      },
      "name": "MIA-MI1-SW16",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:1",
          "name": "JAX-LUM-SW02_1_-_FLR_East",
          "nni": "urn:sdx:link:amlight.net:MIA-JAX-100G-01",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:2",
          "name": "novi_port_2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:3",
          "name": "MIA-MI1-SW14_port_3_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW15_MIA-MI1-SW16-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:4",
          "name": "MIA-MI1-SW14_port_4_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW14_MIA-MI1-SW16-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:7",
          "name": "novi_port_7",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:8",
          "name": "novi_port_8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:9",
          "name": "novi_port_9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:10",
          "name": "RedClara_rtr-core-mia_0/1/0/0",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:13",
          "name": "loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:14",
          "name": "novi_port_14",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:15",
          "name": "novi_port_15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:16",
          "name": "novi_port_16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:19",
          "name": "loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:23",
          "name": "novi_port_23",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:29",
          "name": "MON_BCT-MI3-SW03_port_29",
          "nni": "urn:sdx:link:amlight.net:MIA-BCT-100G-03",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:30",
          "name": "MIA-FTZ-Monet",
          "nni": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-1/1/4",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "4015-4019",
                "2990-2999"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:31",
          "name": "novi_port_31",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:32",
          "name": "novi_port_32",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:114",
          "name": "novi_port_114",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:214",
          "name": "novi_port_214",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW16:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW16",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
      "location": {
        "address": "Miami MI1",
        "iso3166_2_lvl4": "US-FL",
        "latitude": 28,
        "longitude": -30
      },
      "name": "MIA-MI1-SW17",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:1",
          "name": "novi_port_1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:2",
          "name": "novi_port_2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:3",
          "name": "novi_port_3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:4",
          "name": "MIA-MI1-SW14_port_30",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW14_MIA-MI1-SW17-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:5",
          "name": "MIA-MI1-SW15_port_30",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW15_MIA-MI1-SW17-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:6",
          "name": "StormMaker_A2_Slot_2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "FABRIC FIU - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:7",
          "name": "FABRIC_FIU_-_NAP-OPTIX01_1/4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "4015-4017",
                "4019-4094",
                "2990-2999",
                "3800-3848"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "AmLight DTN - MIA-MI1-SRV02 - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:8",
          "name": "MIA-MI1-SRV02",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3848"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:9",
          "name": "novi_port_9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:10",
          "name": "loop-10-11-Netbrain-shimlayer",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "NRP-k8s-gen4-02 - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:12",
          "name": "Igrok-7_JOHN_PRP_Node",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:13",
          "name": "Loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:14",
          "name": "MIA-MI1-SW08_Port_1/3/4_Trunk",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "RNP - National Education and Research Network in Brazil - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:15",
          "name": "RNP_MX10kMIA2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3848"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:16",
          "name": "MIA-MI1-SW05_x_MIA-MI1-SW17_Re",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:17",
          "name": "RNP_MXMIA1_et-1/0/5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "PATh Network Switch - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:18",
          "name": "PATh_Network_Switch",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "Netbrane - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:19",
          "name": "Netbrane-OVS03/TAP-p4p1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-mia p1p2 - perfsonar testpoint - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:20",
          "name": "ps-mia_p1p2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "2990-2999",
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "NRP-k8s-ceph-01-eno1 - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:21",
          "name": "NRP-k8s-ceph-01-eno1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "NRP-k8s-ceph-02-eno1 - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:22",
          "name": "NRP-k8s-ceph-02-eno1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "NRP-k8s-gen4-01-eno2 - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:23",
          "name": "NRP-k8s-gen4-01-eno2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "4015-4019",
                "2990-2999",
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:24",
          "name": "MIA-MI1-TOR01_Hu1/32",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:25",
          "name": "MIA-MI1-TOR02_Hu1/32",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "AmLight TelemetryFeed - MIA-MI1-SW12 - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:27",
          "name": "Telemetry_Source",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3000-3002",
                "2990-2999",
                "4015-4094",
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:29",
          "name": "NRP-k8s-gen4-01-eno1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "AmLight TestbedQFactor - MIA-MI1-SW12 - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:30",
          "name": "MIA-MI1-SW12_Port_32",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:31",
          "name": "novi_port_31",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:32",
          "name": "novi_port_32",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:114",
          "name": "VMWware04_-_10G",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:214",
          "name": "novi_port_214",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW17:1000",
          "name": "novi_lport1000",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW17",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "Other",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
      "location": {
        "address": "MIA-MI1-SW18",
        "iso3166_2_lvl4": "US-FL",
        "latitude": 35,
        "longitude": -15
      },
      "name": "MIA-MI1-SW18",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:1",
          "name": "JAX-LUM-SW01_1_-_FLR_West",
          "nni": "urn:sdx:link:amlight.net:MIA-JAX-100G-02",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:2",
          "name": "novi_port_2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:3",
          "name": "MIA-MI1-SW14_Port_28",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW14_MIA-MI1-SW18-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:7",
          "name": "novi_port_7",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "AmLight DTN - OX Server - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:8",
          "name": "OX_Server",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "2990-2999",
                "3800-3828",
                "3830-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "RARE-AmLight-MIA0021 - GP4Lab/Global P4 Lab - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:9",
          "name": "RARE_Router",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3829",
                "3831-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "AmLight TestbedINT - Novi06 - Miami"
          ],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:10",
          "name": "Novi06",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:13",
          "name": "loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:14",
          "name": "novi_port_14",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:15",
          "name": "Loop-15-16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:16",
          "name": "novi_port_16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:19",
          "name": "novi_port_19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:23",
          "name": "FIU_Trunk",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:24",
          "name": "FLR_Trunk",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:29",
          "name": "MIA-MI1-SW15_Port_28",
          "nni": "urn:sdx:link:amlight.net:MIA-MI1-SW15_MIA-MI1-SW18-100G",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:30",
          "name": "novi_port_30",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:31",
          "name": "novi_port_31",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:MIA-MI1-SW18:32",
          "name": "novi_port_32",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:MIA-MI1-SW18",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
      "location": {
        "address": "Lumen Jacksonville",
        "iso3166_2_lvl4": "US-FL",
        "latitude": 55,
        "longitude": -20
      },
      "name": "JAX-LUM-SW01",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:1",
          "name": "MIA-MI1-SW18_1_-_FLR_West",
          "nni": "urn:sdx:link:amlight.net:MIA-JAX-100G-02",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:2",
          "name": "JAX-LUM-SW02_port_2_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:JAX-LUM-SW01_JAX-LUM-SW02-100G",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:3",
          "name": "novi_port_3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:7",
          "name": "JAX-INT01_100G_-_1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:8",
          "name": "novi_port_8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "40GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:9",
          "name": "JAX-LUM-RT01_et-0/0/0",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:10",
          "name": "novi_port_10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:13",
          "name": "Loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:14",
          "name": "JAX-LUM-FW01_xe-0/0/17_-_Disas",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:15",
          "name": "Loop-15-16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:16",
          "name": "Loop-15-16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:19",
          "name": "Loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:21",
          "name": "Loop-19-21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "4001-4019",
                "2990-2999"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:23",
          "name": "novi_port_23",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:30",
          "name": "novi_port_30",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:31",
          "name": "JAX-LUM-SW02_port_31_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:JAX-LUM-SW01_JAX-LUM-SW02-100G",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:32",
          "name": "ATL-LUM-SW01_port_32_via_Inter",
          "nni": "urn:sdx:link:amlight.net:JAX-ATL-100G-01",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:114",
          "name": "JAX-LUM-MG01_xe-0/1/1_-_In-ban",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-jax 10G p2p2 - perfsonar testpoint - Jacksonville"
          ],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:214",
          "name": "ps-jax_10G_p2p2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:314",
          "name": "JAX-SFLOW01_Te1/33",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW01:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
      "location": {
        "address": "Lumen Jacksonville",
        "iso3166_2_lvl4": "US-FL",
        "latitude": 55,
        "longitude": -40
      },
      "name": "JAX-LUM-SW02",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:1",
          "name": "MIA-MI1-SW16_1_-_FLR_East",
          "nni": "urn:sdx:link:amlight.net:MIA-JAX-100G-01",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:2",
          "name": "JAX-LUM-SW01_port_2_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:JAX-LUM-SW01_JAX-LUM-SW02-100G",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:3",
          "name": "novi_port_3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:6",
          "name": "JAX-INT01_Netronome_1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "40GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:7",
          "name": "JAX-INT01_100G_-_1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:8",
          "name": "JAX-INT01_Netronome_2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "40GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:9",
          "name": "JAX-LUM-RT01_et-0/0/1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:10",
          "name": "Internet2_AL2S_-_I2-JACK-JACK-",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:13",
          "name": "Loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:14",
          "name": "JAX-LUM-FW01_xe-0/0/18_-_Disas",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "Internet2 - Jacksonville"
          ],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:15",
          "name": "Internet2_UNI_loop-16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3801",
                "3803-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:16",
          "name": "Internet2_Shimlayer_loop-15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:17",
          "name": "Loop-17-18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:18",
          "name": "Loop-17-18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:19",
          "name": "Loop-19-INT-Reports",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:23",
          "name": "novi_port_23",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:30",
          "name": "novi_port_30",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:31",
          "name": "JAX-LUM-SW01_port_31_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:JAX-LUM-SW01_JAX-LUM-SW02-100G",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:32",
          "name": "novi_port_32",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:114",
          "name": "JAX-LUM-MG01_xe-0/1/0_-_In-ban",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-jax 10G p2p1 - perfsonar testpoint - Jacksonville"
          ],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:214",
          "name": "ps-jax_10G_p2p1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:JAX-LUM-SW02:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:JAX-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
      "location": {
        "address": "Equinix MI3",
        "iso3166_2_lvl4": "US-FL",
        "latitude": 23,
        "longitude": -50
      },
      "name": "BCT-MI3-SW03",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:1",
          "name": "ATL-LUM-SW01_port_1_-_Ressurge",
          "nni": "urn:sdx:link:amlight.net:BCT-ATL-100G-01",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:2",
          "name": "BCT-MI3-SW04_port_2_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:BCT-MI3-SW03_BCT-MI3-SW04-100G",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:3",
          "name": "FOR-ACB-SW01_et-0/1/2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:4",
          "name": "SAO-SP4-SW03_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:7",
          "name": "novi_port_7",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:8",
          "name": "novi_port_8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:9",
          "name": "novi_port_9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:10",
          "name": "novi_port_10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:13",
          "name": "Loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:14",
          "name": "BCT-MI3-FW01_xe-0/0/17_-_Disas",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:15",
          "name": "novi_port_15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:16",
          "name": "novi_port_16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:19",
          "name": "Loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:23",
          "name": "novi_port_23",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:28",
          "name": "FOR-ACB-SW01_et-1/1/9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:29",
          "name": "MON_MIA-MI1-SW16_port_29",
          "nni": "urn:sdx:link:amlight.net:MIA-BCT-100G-03",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:30",
          "name": "SAO-SP4-SW03_port_30_-_Monet_R",
          "nni": "urn:sdx:link:amlight.net:BCT-SAO-100G-01",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:31",
          "name": "BCT-MI3-SW04_port_31_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:BCT-MI3-SW03_BCT-MI3-SW04-100G",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:32",
          "name": "MIA-MI1-SW14_port_32_-_Miami_2",
          "nni": "urn:sdx:link:amlight.net:MIA-BCT-100G-01",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:114",
          "name": "BCT-MI3-MG01_xe-0/1/0_-_In-ban",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-bct 10G #1 - perfsonar testpoint - BocaRaton"
          ],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:214",
          "name": "ps-bct_10G_1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW03:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
      "location": {
        "address": "Equinix MI3",
        "iso3166_2_lvl4": "US-FL",
        "latitude": 23,
        "longitude": -10
      },
      "name": "BCT-MI3-SW04",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:1",
          "name": "ATL-LUM-SW01_port_32_-_Ressurg",
          "nni": "urn:sdx:link:amlight.net:BCT-ATL-100G-02",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:2",
          "name": "BCT-MI3-SW03_port_2_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:BCT-MI3-SW03_BCT-MI3-SW04-100G",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:3",
          "name": "FOR-ACB-SW01_et-0/1/9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:7",
          "name": "novi_port_7",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:8",
          "name": "novi_port_8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:9",
          "name": "novi_port_9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:10",
          "name": "novi_port_10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:13",
          "name": "Loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:14",
          "name": "BCT-MI3-FW01_xe-0/0/18_-_Disas",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:15",
          "name": "novi_port_15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:16",
          "name": "novi_port_16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:19",
          "name": "Loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:23",
          "name": "novi_port_23",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:28",
          "name": "FOR-ACB-SW01_et-1/1/9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:30",
          "name": "SAO-SP4-SW03_port_2_-_Monet_sh",
          "nni": "urn:sdx:link:amlight.net:BCT-SAO-100G-02",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:31",
          "name": "BCT-MI3-SW03_port_31_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:BCT-MI3-SW03_BCT-MI3-SW04-100G",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:32",
          "name": "MIA-MI1-SW15_port_32_-_Miami_2",
          "nni": "urn:sdx:link:amlight.net:MIA-BCT-100G-02",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:114",
          "name": "BCT-MI3-MG01_xe-0/1/1_-_In-ban",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-bct 10G #2 - perfsonar testpoint - BocaRaton"
          ],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:214",
          "name": "ps-bct_10G_2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BCT-MI3-SW04:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BCT-MI3-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
      "location": {
        "address": "Lumen Atlanta",
        "iso3166_2_lvl4": "US-GA",
        "latitude": 40,
        "longitude": 10
      },
      "name": "ATL-LUM-SW01",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:1",
          "name": "BCT-MI3-SW03_port_1_-_Resurgen",
          "nni": "urn:sdx:link:amlight.net:BCT-ATL-100G-01",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:2",
          "name": "ATL-LUM-SW02_port_2_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:ATL-LUM-SW01_ATL-LUM-SW02-100G",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:3",
          "name": "novi_port_3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:7",
          "name": "ATL-INT01_100G_-_1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:8",
          "name": "novi_port_8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "40GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:9",
          "name": "ATL-LUM-RT01_et-0/0/0",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ESnet - Atlanta"
          ],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:10",
          "name": "ESnet_-_Shared_-_ATL-TAP01_por",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3801",
                "3803-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:12",
          "name": "Dell_Z9100_-_SFLOW",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:13",
          "name": "Loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:14",
          "name": "ATL-LUM-FW01_xe-0/0/17_-_Disas",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:15",
          "name": "Loop-15-16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:16",
          "name": "Loop-16-15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:19",
          "name": "Loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:22",
          "name": "ATL-LUM-SW03_port_1/0",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:23",
          "name": "ATL-LUM-SW03_port_1/6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:26",
          "name": "ESnet_-_Rubin_Obs_-_1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:29",
          "name": "MON_JAX-LUM-SW01_port_32_via_I",
          "nni": "urn:sdx:link:amlight.net:JAX-ATL-100G-01",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:30",
          "name": "novi_port_30",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:31",
          "name": "ATL-LUM-SW02_port_31_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:ATL-LUM-SW01_ATL-LUM-SW02-100G",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:32",
          "name": "JAX-LUM-SW01_port_32_via_Inter",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:114",
          "name": "ATL-LUM-MG01_xe-0/1/0_-_In-ban",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-atl 10G #1 - perfsonar testpoint - Atlanta"
          ],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:214",
          "name": "ps-atl_10G_1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW01:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
      "location": {
        "address": "Lumen Atlanta",
        "iso3166_2_lvl4": "US-GA",
        "latitude": 25,
        "longitude": 10
      },
      "name": "ATL-LUM-SW02",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:1",
          "name": "BCT-MI3-SW04_port_1_-_Resurgen",
          "nni": "urn:sdx:link:amlight.net:BCT-ATL-100G-02",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:2",
          "name": "ATL-LUM-SW01_port_2_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:ATL-LUM-SW01_ATL-LUM-SW02-100G",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:3",
          "name": "novi_port_3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:7",
          "name": "ATL-INT01_100G_-_2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:8",
          "name": "novi_port_8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "40GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:9",
          "name": "ATL-LUM-RT01_et-0/0/0",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:10",
          "name": "novi_port_10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:13",
          "name": "Loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:14",
          "name": "ATL-LUM-FW01_xe-0/0/18_-_Disas",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:15",
          "name": "novi_port_15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:16",
          "name": "novi_port_16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:19",
          "name": "Loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:23",
          "name": "novi_port_23",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:26",
          "name": "ESnet_Router_-_Vera_Rubin",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:30",
          "name": "novi_port_30",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:31",
          "name": "ATL-LUM-SW01_port_31_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:ATL-LUM-SW01_ATL-LUM-SW02-100G",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:32",
          "name": "novi_port_32",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:114",
          "name": "ATL-LUM-MG01_xe-0/1/1_-_In-ban",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-atl enp1s0f1np1 - perfsonar testpoint - Atlanta"
          ],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:214",
          "name": "ps-atl_enp1s0f1np1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:ATL-LUM-SW02:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:ATL-LUM-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:SJU-H787-SW02",
      "location": {
        "address": "San Juan H787",
        "iso3166_2_lvl4": "US-PR",
        "latitude": 30,
        "longitude": -110
      },
      "name": "SJU-H787-SW02",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:1",
          "name": "MIA-MI1-SW14_port_1_-_FIU035WM",
          "nni": "urn:sdx:link:amlight.net:MIA-SJU-100G-01",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:2",
          "name": "SJU-H787-SW03_port_2_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:SJU-H787-SW02_SJU-H787-SW03-10",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:3",
          "name": "novi_port_3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "UPR - University of Puerto Rico - SanJuan"
          ],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:7",
          "name": "UPR",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:8",
          "name": "novi_port_8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:9",
          "name": "novi_port_9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:10",
          "name": "novi_port_10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:13",
          "name": "Loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:14",
          "name": "SJU-H787-FW01_xe-0/0/17_-_Disa",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:15",
          "name": "novi_port_15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:16",
          "name": "novi_port_16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:19",
          "name": "Loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:23",
          "name": "novi_port_23",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:30",
          "name": "novi_port_30",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:31",
          "name": "SJU-H787-SW03_port_31_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:SJU-H787-SW02_SJU-H787-SW03-10",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:32",
          "name": "novi_port_32",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:114",
          "name": "SJU-H787-MG01_xe-0/1/0_-_In-ba",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-sju 10G #1 - perfsonar testpoint - SanJuan"
          ],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:214",
          "name": "ps-sju_10G_1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW02:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:SJU-H787-SW03",
      "location": {
        "address": "San Juan H787",
        "iso3166_2_lvl4": "US-PR",
        "latitude": 22,
        "longitude": -90
      },
      "name": "SJU-H787-SW03",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:1",
          "name": "PTY-TON-SW01_port_1_-_FIU031WC",
          "nni": "urn:sdx:link:amlight.net:SJU-PTY-100G-01",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:2",
          "name": "SJU-H787-SW02_port_2_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:SJU-H787-SW02_SJU-H787-SW03-10",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:3",
          "name": "novi_port_3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:7",
          "name": "UPR_router02",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:8",
          "name": "novi_port_8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:9",
          "name": "novi_port_9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:10",
          "name": "novi_port_10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:13",
          "name": "Loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:14",
          "name": "SJU-H787-FW01_xe-0/0/18_-_Disa",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:15",
          "name": "novi_port_15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:16",
          "name": "novi_port_16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:19",
          "name": "Loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:23",
          "name": "novi_port_23",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:30",
          "name": "novi_port_30",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:31",
          "name": "SJU-H787-SW03_port_31_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:SJU-H787-SW02_SJU-H787-SW03-10",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:32",
          "name": "novi_port_32",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:114",
          "name": "SJU-H787-MG01_xe-0/1/1_-_In-ba",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-sju 10G #2 - perfsonar testpoint - SanJuan"
          ],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:214",
          "name": "ps-sju_10G_2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SJU-H787-SW03:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SJU-H787-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:PTY-TON-SW01",
      "location": {
        "address": "Datacenter TON",
        "iso3166_2_lvl4": "PA-PA",
        "latitude": 9,
        "longitude": -79
      },
      "name": "PTY-TON-SW01",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:1",
          "name": "MON_SJU-H878-SW01_eth6/1_-_FIU",
          "nni": "urn:sdx:link:amlight.net:SJU-PTY-100G-01",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:2",
          "name": "MON_SCL-CLK-SW01_eth3/1_-_FIU0",
          "nni": "urn:sdx:link:amlight.net:PTY-SCL-100G-01",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:3",
          "name": "rtr-core-pty_Hu0/0/0/0",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:4",
          "name": "rtr-core-pty_Hu0/1/0/0",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:5",
          "name": "Loop-6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:6",
          "name": "Loop-5",
          "nni": "urn:sdx:link:amlight.net:PTY-FOR-MIA-100G-01",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:7",
          "name": "novi_port_7",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:8",
          "name": "novi_port_8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:9",
          "name": "novi_port_9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:10",
          "name": "novi_port_10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:13",
          "name": "novi_port_13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:14",
          "name": "novi_port_14",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:15",
          "name": "novi_port_15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:16",
          "name": "novi_port_16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-pty p1p2 - throughput - perfsonar testpoint - Panama"
          ],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:17",
          "name": "ps-pty_p1p2_-_throughput",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:18",
          "name": "RedClara-Shim-Cisco3750",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:19",
          "name": "novi_port_19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:23",
          "name": "novi_port_23",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:30",
          "name": "novi_port_30",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:31",
          "name": "novi_port_31",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:32",
          "name": "novi_port_32",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:117",
          "name": "novi_port_117",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:118",
          "name": "RedClara-Shim-UFINET-1",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:119",
          "name": "novi_port_119",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:121",
          "name": "novi_port_121",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:122",
          "name": "novi_port_122",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:217",
          "name": "novi_port_217",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:218",
          "name": "novi_port_218",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:219",
          "name": "novi_port_219",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:221",
          "name": "novi_port_221",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:222",
          "name": "novi_port_222",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:317",
          "name": "novi_port_317",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:318",
          "name": "RedClara-Shim-RENATA-TelxiusCo",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:319",
          "name": "novi_port_319",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:321",
          "name": "novi_port_321",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:322",
          "name": "novi_port_322",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "RedClara - Latin American Cooperation of Advanced Networks - Panama"
          ],
          "id": "urn:sdx:port:amlight.net:PTY-TON-SW01:1000",
          "name": "RedClara-LAG_rtr-core-pty",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:PTY-TON-SW01",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "Other",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
      "location": {
        "address": "Datacenter CLK",
        "iso3166_2_lvl4": "CL-RM",
        "latitude": -38,
        "longitude": -58
      },
      "name": "SCL-CIR-SW03",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:1",
          "name": "SAO-SP4-SW04_port_1_-_FIU033",
          "nni": "urn:sdx:link:amlight.net:SAO-SCL-100G-01",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:2",
          "name": "SCL-CIR-SW04_port_2_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:SCL-CIR-SW03_SCL-CIR-SW04-100G",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:3",
          "name": "novi_port_3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:7",
          "name": "novi_port_7",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:8",
          "name": "SCL-CIR-DTN01_ens1f1_-_100G",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:9",
          "name": "novi_port_9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:10",
          "name": "novi_port_10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:13",
          "name": "Loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:14",
          "name": "novi_port_14",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:15",
          "name": "Loop-15-16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:16",
          "name": "Loop-16-15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:17",
          "name": "Loop-17-18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:18",
          "name": "Loop-18-17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:19",
          "name": "loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:23",
          "name": "REUNA_Backup_100G",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:26",
          "name": "Rubin_Observatory_rubinobs-br0",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "40GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:30",
          "name": "novi_port_30",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:31",
          "name": "SCL-CIR-SW04_port_31_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:SCL-CIR-SW03_SCL-CIR-SW04-100G",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:32",
          "name": "SAO-SP4-SW03_port_30_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:BUE-SCL-100G-01",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:114",
          "name": "novi_port_114",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-scl p2p2 - 10G - perfsonar testpoint - Santiago"
          ],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:214",
          "name": "ps-scl_p2p2_-_10G",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW03:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
      "location": {
        "address": "Cirion Technologies - Santiago/Huechuraba",
        "iso3166_2_lvl4": "CL-RM",
        "latitude": -38,
        "longitude": -80
      },
      "name": "SCL-CIR-SW04",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:1",
          "name": "PTY-TON-SW01_port_2_-_FIU036",
          "nni": "urn:sdx:link:amlight.net:PTY-SCL-100G-01",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:2",
          "name": "SCL-CIR-SW03_port_2_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:SCL-CIR-SW03_SCL-CIR-SW04-100G",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:3",
          "name": "novi_port_3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "RedClara - Latin American Cooperation of Advanced Networks - Santiago"
          ],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:7",
          "name": "RedClara_-_dwdm-core-scl3_1/3_",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "AmLight DTN - SCL-CIR-DTN01 - Santiago"
          ],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:8",
          "name": "SCL-CIR-DTN01_ens1f0_-_100G",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:9",
          "name": "novi_port_9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:10",
          "name": "novi_port_10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:13",
          "name": "Loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:14",
          "name": "novi_port_14",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:15",
          "name": "Loop-15-16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:16",
          "name": "Loop-16-15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:19",
          "name": "loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "REUNA - National Research and Education Network in Chile - Santiago"
          ],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:23",
          "name": "REUNA_Primary_100G",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3848"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:26",
          "name": "Rubin_Observatory_rubinobs-br0",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:30",
          "name": "novi_port_30",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:31",
          "name": "SCL-CIR-SW03_port_31_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:SCL-CIR-SW03_SCL-CIR-SW04-100G",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:32",
          "name": "novi_port_32",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:114",
          "name": "novi_port_114",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-scl p2p2 - 10G - perfsonar testpoint - Santiago"
          ],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:214",
          "name": "ps-scl_p2p2_-_10G",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SCL-CIR-SW04:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SCL-CIR-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
      "location": {
        "address": "Buenos Aires",
        "iso3166_2_lvl4": "AR-BA",
        "latitude": -38,
        "longitude": -38
      },
      "name": "BUE-BTW-SW01",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:1",
          "name": "SAO-SP4-SW03_port_30_-_FIU039",
          "nni": "urn:sdx:link:amlight.net:SAO-BUE-100G-01",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:2",
          "name": "novi_port_2",
          "nni": "urn:sdx:link:amlight.net:BUE-BTW-SW01_BUE-BTW-SW02-100G",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:3",
          "name": "novi_port_3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:7",
          "name": "novi_port_7",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:8",
          "name": "novi_port_8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:9",
          "name": "novi_port_9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:10",
          "name": "novi_port_10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:13",
          "name": "novi_port_13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:14",
          "name": "novi_port_14",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:15",
          "name": "novi_port_15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:16",
          "name": "novi_port_16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:19",
          "name": "novi_port_19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:23",
          "name": "novi_port_23",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:30",
          "name": "novi_port_30",
          "nni": "urn:sdx:link:amlight.net:BUE-SCL-100G-01",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:31",
          "name": "novi_port_31",
          "nni": "urn:sdx:link:amlight.net:BUE-BTW-SW01_BUE-BTW-SW02-100G",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:32",
          "name": "SAO-SP4-SW03_port_23",
          "nni": "urn:sdx:link:amlight.net:SAO-BUE-100G-03",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:114",
          "name": "novi_port_114",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:214",
          "name": "novi_port_214",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW01:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW01",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
      "location": {
        "address": "Buenos Aires",
        "iso3166_2_lvl4": "AR-BA",
        "latitude": -38,
        "longitude": -18
      },
      "name": "BUE-BTW-SW02",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:1",
          "name": "SAO-SP4-SW03_port_4_-_L-79",
          "nni": "urn:sdx:link:amlight.net:SAO-BUE-100G-05",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:2",
          "name": "novi_port_2",
          "nni": "urn:sdx:link:amlight.net:BUE-BTW-SW01_BUE-BTW-SW02-100G",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:3",
          "name": "novi_port_3",
          "nni": "urn:sdx:link:amlight.net:SAO-BUE-100G-02",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:5",
          "name": "novi_port_5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "RedClara - Latin American Cooperation of Advanced Networks - BuenosAires"
          ],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:7",
          "name": "RedClara_rtr-core-bue_0/1/0/2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:8",
          "name": "novi_port_8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:9",
          "name": "novi_port_9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:10",
          "name": "novi_port_10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:13",
          "name": "novi_port_13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:14",
          "name": "novi_port_14",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:15",
          "name": "novi_port_15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:16",
          "name": "novi_port_16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:19",
          "name": "novi_port_19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:23",
          "name": "novi_port_23",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:24",
          "name": "novi_port_24",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:27",
          "name": "novi_port_27",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:30",
          "name": "novi_port_30",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:31",
          "name": "novi_port_31",
          "nni": "urn:sdx:link:amlight.net:BUE-BTW-SW01_BUE-BTW-SW02-100G",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:32",
          "name": "SAO-SP4-SW03_port_28_-_FIU040",
          "nni": "urn:sdx:link:amlight.net:SAO-BUE-100G-04",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:114",
          "name": "novi_port_114",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:214",
          "name": "novi_port_214",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:BUE-BTW-SW02:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:BUE-BTW-SW02",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
      "location": {
        "address": "Datacenter SP4",
        "iso3166_2_lvl4": "BR-SP",
        "latitude": -22,
        "longitude": -38
      },
      "name": "SAO-SP4-SW03",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:1",
          "name": "FOR-ABC-SW01_et-0/1/4_-_Monet_",
          "nni": "urn:sdx:port:sax.net:FOR-ACB-SW01:et-0/1/4",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:2",
          "name": "MON_BCT-MI3-SW02_30_-_Monet",
          "nni": "urn:sdx:link:amlight.net:BCT-SAO-100G-02",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:3",
          "name": "SAO-SP4-SW04_port_3",
          "nni": "urn:sdx:link:amlight.net:SAO-SP4-SW03_SAO-SP4-SW04-100G",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:4",
          "name": "MON_SCL-CLK-SW03_port_4_-_L-79",
          "nni": "urn:sdx:link:amlight.net:SAO-BUE-100G-05",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:5",
          "name": "SAO-SP4-SW04_port_5_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:SAO-SP4-SW03_SAO-SP4-SW04-100G",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:6",
          "name": "BUE-BTW-SW02_port_3_-_FIU037",
          "nni": "urn:sdx:link:amlight.net:SAO-BUE-100G-02",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:7",
          "name": "novi_port_7",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "RARE-RNP-SAO0021 - GP4Lab/Global P4 Lab - SaoPaulo"
          ],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:8",
          "name": "RNP-RARE_Freertr-SAO0021",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:9",
          "name": "novi_port_9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:10",
          "name": "loop-10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:11",
          "name": "loop-11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:13",
          "name": "FOR-ACB-SW01_et-0/1/8",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:14",
          "name": "FOR-ACB-SW01_et-1/1/7",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:15",
          "name": "novi_port_15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:16",
          "name": "FOR-ACB-SW01_et-0/1/5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:17",
          "name": "FOR-ACB-SW01_et-0/1/3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:18",
          "name": "BCT-MI3-SW03_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:19",
          "name": "loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:20",
          "name": "FOR-ACB-SW01_et-1/1/3",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:21",
          "name": "novi_port_21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:22",
          "name": "novi_port_22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:23",
          "name": "BUE-BTW-SW01_port_32_-_FIU038",
          "nni": "urn:sdx:link:amlight.net:SAO-BUE-100G-03",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "RNP - National Education and Research Network in Brazil - SaoPaulo"
          ],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:24",
          "name": "RNP_BSP4_et-0/0/0",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:25",
          "name": "RNP_CSP2_et-0/1/9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:26",
          "name": "novi_port_26",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:27",
          "name": "SAO-SP4-SW04_port_27_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:SAO-SP4-SW03_SAO-SP4-SW04-100G",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:28",
          "name": "BUE-BTW-SW02_port_32_-_FIU040",
          "nni": "urn:sdx:link:amlight.net:SAO-BUE-100G-04",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:29",
          "name": "RedClara_-_SAO_x_BUE_-_rtr-cor",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:30",
          "name": "BUE-BTW-SW01_port_1_-_FIU039",
          "nni": "urn:sdx:link:amlight.net:SAO-BUE-100G-01",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:31",
          "name": "MON_SAO-SP4-SW04_port_31_-_XC_",
          "nni": "urn:sdx:link:amlight.net:SAO-SP4-SW03_SAO-SP4-SW04-100G",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW03:32",
          "name": "MON_BCT-MI3-SW02_port_30_-_Mon",
          "nni": "urn:sdx:link:amlight.net:BCT-SAO-100G-01",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW03",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    },
    {
      "id": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
      "location": {
        "address": "Datacenter SP4",
        "iso3166_2_lvl4": "BR-SP",
        "latitude": -22,
        "longitude": -58
      },
      "name": "SAO-SP4-SW04",
      "ports": [
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:32",
          "name": "MON_FIU034_-_SAX_FOR-LAN-SW02_",
          "nni": "urn:sdx:link:amlight.net:MIA-FTZ-SAO-100G-01",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:1",
          "name": "MON_SCL-CLK-SW03_port_2_-_FIU0",
          "nni": "urn:sdx:link:amlight.net:SAO-SCL-100G-01",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:2",
          "name": "novi_port_2",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:3",
          "name": "SAO-SP4-SW03_port_3",
          "nni": "urn:sdx:link:amlight.net:SAO-SP4-SW03_SAO-SP4-SW04-100G",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:4",
          "name": "novi_port_4",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:5",
          "name": "SAO-SP4-SW03_port_5_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:SAO-SP4-SW03_SAO-SP4-SW04-100G",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:6",
          "name": "novi_port_6",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:7",
          "name": "novi_port_7",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "NCC-UNESP - NCC at Sao Paulo State University - SaoPaulo"
          ],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:8",
          "name": "NCC-Unesp",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:9",
          "name": "novi_port_9",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:10",
          "name": "novi_port_10",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:11",
          "name": "novi_port_11",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:12",
          "name": "novi_port_12",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:13",
          "name": "loop-13",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "ps-sao-10g - perfsonar testpoint - SaoPaulo"
          ],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:14",
          "name": "new-perfsonar-sao-10g",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:15",
          "name": "Loop-16",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:16",
          "name": "Loop-15",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:17",
          "name": "novi_port_17",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:18",
          "name": "novi_port_18",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:19",
          "name": "loop-19",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:20",
          "name": "novi_port_20",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:21",
          "name": "Loop-22",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:22",
          "name": "Loop-21",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:23",
          "name": "novi_port_23",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:24",
          "name": "NCC-UNESP-ELLA-Link",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:25",
          "name": "novi_port_25",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "RedClara - Latin American Cooperation of Advanced Networks - SaoPaulo"
          ],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:26",
          "name": "RedClara_rtr-core-sao_Hu0/1/0/",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:27",
          "name": "SAO-SP4-SW03_port_27_-_Trunk",
          "nni": "urn:sdx:link:amlight.net:SAO-SP4-SW03_SAO-SP4-SW04-100G",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:28",
          "name": "novi_port_28",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:29",
          "name": "novi_port_29",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:30",
          "name": "novi_port_30",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:31",
          "name": "MON_SAO-SP4-SW03_port_31_-_XC_",
          "nni": "urn:sdx:link:amlight.net:SAO-SP4-SW03_SAO-SP4-SW04-100G",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "100GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:114",
          "name": "FIU020_-_MIA-MI1-SW01_eth2/5",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:120",
          "name": "novi_port_120",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:214",
          "name": "novi_port_214",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:220",
          "name": "novi_port_220",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:314",
          "name": "novi_port_314",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:320",
          "name": "novi_port_320",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "disabled",
          "status": "down",
          "type": "10GE",
          "vlan_range": "null"
        },
        {
          "entities": [
            "rednesp - Research and Education Network of Sao Paulo - SaoPaulo"
          ],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:1000",
          "name": "rednesp_SPO-REDNESP-01",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": {
            "l2vpn_ptmp": {

            },
            "l2vpn_ptp": {
              "vlan_range": [
                "3800-3849"
              ]
            },
            "monitoring_capability": "null",
            "owner": "null",
            "private_attributes": "null",
            "provisioning_system": "null",
            "provisioning_url": "null",
            "vendor": "null"
          },
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "Other",
          "vlan_range": "null"
        },
        {
          "entities": [],
          "id": "urn:sdx:port:amlight.net:SAO-SP4-SW04:1001",
          "name": "rednesp_SPO-REDNESP-02",
          "nni": "",
          "node": "urn:sdx:node:amlight.net:SAO-SP4-SW04",
          "private_attributes": "null",
          "services": "null",
          "short_name": "null",
          "state": "enabled",
          "status": "up",
          "type": "Other",
          "vlan_range": "null"
        }
      ],
      "private_attributes": [],
      "short_name": "null",
      "state": "enabled",
      "status": "up"
    }
  ],
  "private_attributes": "null",
  "services": {
    "l2vpn_ptmp": ["null"],
    "l2vpn_ptp": ["null"],
    "monitoring_capability": "null",
    "owner": "null",
    "private_attributes": "null",
    "provisioning_system": "null",
    "provisioning_url": "null",
    "vendor": "null"
  },
  "timestamp": "2026-03-06T17:30:25.751980",
  "version": "9412"
}


if __name__ == '__main__':
    print('Starting app')
    app.run(host='0.0.0.0', debug=True, port=6098)



