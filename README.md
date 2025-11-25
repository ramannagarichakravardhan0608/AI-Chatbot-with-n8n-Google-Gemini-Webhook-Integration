# 🤖 AI Chatbot using n8n, Google Gemini & Webhook (with Memory)

A fully automated **AI chatbot system** built using **n8n**, **Google Gemini Chat Model**, **Webhook**, and **Simple Memory**.  
This chatbot supports **dynamic conversations**, **memory retention**, and can be integrated into **websites, WhatsApp, Telegram, mobile apps**, or **custom APIs**.

---

## 🚀 Key Features

✔️ Dynamic AI chatbot using Google Gemini  
✔️ Stores conversation context using Simple Memory  
✔️ Accepts user input via Webhook (POST requests)  
✔️ Generates human-like responses  
✔️ API-ready (can be used in websites, apps, chat widgets)  
✔️ Easy to customize for domain-specific chatbots (Education, Health, Business etc.)

---

## 🧠 Workflow Structure

User Message → Webhook → AI Agent → Gemini Model → Memory → Response


---

## 📎 Chatbot API Usage

You can send a POST request to your n8n Webhook endpoint:

`📥 JSON Request Format

{
  "message": "Tell me about AI in healthcare"
}

🔄 JSON Response Format

{
  "reply": "AI helps improve diagnosis accuracy, patient monitoring, predictive analytics, and personalized treatment plans..."
}

💡 Usecases for this Chatbot

| Use Case             | Description                                      |
| -------------------- | ------------------------------------------------ |
| Customer Support Bot | Answer FAQs, product details, ticket automation  |
| Business Chatbot     | Appointment booking, lead generation, follow-ups |
| Education Chatbot    | Personalized tutoring, interactive Q&A           |
| Healthcare Bot       | Appointment scheduling, symptom checker, advice  |
| AI Content Assistant | Generates blogs, emails, scripts, summaries      |

🧰 Technologies Used


| Component        | Technology               |
| ---------------- | ------------------------ |
| AI Model         | Google Gemini Chat Model |
| Workflow Engine  | n8n                      |
| Memory           | Simple Memory Node       |
| API Interface    | Webhook Node             |
| Response Handler | Respond to Webhook       |


⚙️ Setup Instructions

1️⃣ Start n8n

npm install -g n8n
n8n start

2️⃣ Load the Workflow

Import the exported .json workflow.

3️⃣ Set Google Gemini Credentials

In the Gemini node, configure your API key.

4️⃣ Get Webhook URL

Copy the Webhook URL (POST endpoint)

5️⃣ Test in Postman or CURL

📂 Project Structure

|
├── README.md
├── chatbot-workflow.json
├── app.py              (if used for testing)
└── images/screenshot.png

📸 Screenshot (Chatbot Workflow in n8n)
<img width="1440" height="591" alt="Screenshot 2025-11-25 at 10 14 29 AM" src="https://github.com/user-attachments/assets/f6fc2bab-fffe-4387-b479-b709bfbdcd34" />

🌟 Future Enhancements

🗣️ Add voice support (Speech-to-Text and Text-to-Speech)
💬 Connect to WhatsApp, Telegram, Dialogflow, Twilio
⚡ Deploy via Render / Vercel / n8n Cloud
🧠 Use Pinecone or MongoDB for advanced memory

🤝 Contributing

Contributions, improvements, and feature ideas are always welcome!

# ⭐ Support the Project

If this project helped you or inspired your own AI chatbot workflow 🚀  
please consider giving it a **GitHub Star ⭐**

It helps others discover the project, and motivates further improvements!

👉 How to Star the Repo:
1. Go to the top of this repository
2. Click the ⭐ Star button (top-right corner)

Thank you for your support! 🙌  
