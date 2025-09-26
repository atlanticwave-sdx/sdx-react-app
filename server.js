// server.js
import express from "express";
import bodyParser from "body-parser";
import axios from "axios";
import dotenv from "dotenv";

dotenv.config();
const app = express();
const PORT = process.env.PORT || 5000;

app.use(bodyParser.json());

// POST /verify-captcha
app.post("/verify-captcha", async (req, res) => {
  const { token } = req.body;

  if (!token) {
    return res.status(400).json({ success: false, message: "Missing token" });
  }

  try {
    const googleRes = await axios.post(
      "https://www.google.com/recaptcha/api/siteverify",
      null,
      {
        params: {
          secret: process.env.RECAPTCHA_SECRET,
          response: token,
        },
      }
    );

    if (googleRes.data.success) {
      return res.json({ success: true, score: googleRes.data.score ?? null });
    } else {
      return res.json({
        success: false,
        errors: googleRes.data["error-codes"] || [],
      });
    }
  } catch (err) {
    console.error("Captcha verification error:", err);
    return res.status(500).json({ success: false, message: "Server error" });
  }
});

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
