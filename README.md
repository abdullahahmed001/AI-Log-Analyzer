# 📊 AI Log Analyzer

An AI-powered log analysis tool that parses application logs, detects errors and warnings, and generates intelligent incident summaries using LLMs. Built with Flask, Python, and Chart.js.

## 🚀 Features

- 📂 Upload log files (.txt / .log)
- 🔍 Automatic log parsing (ERROR / WARNING detection)
- 🤖 AI-powered incident analysis (Groq / LLM integration)
- 📊 Visual dashboard with Chart.js
- 🧠 Root cause analysis and recommendations
- 🪵 Raw log viewer

---

## 🏗️ Tech Stack

- **Backend:** Flask (Python)
- **AI:** Groq / OpenAI-compatible API (LLaMA 3)
- **Frontend:** HTML, CSS, JavaScript
- **Visualization:** Chart.js

---

## 📁 Project Structure
ai-log-analyzer/
│
├── app.py # Flask backend
├── parser.py # Log parsing logic
├── ai_service.py # AI integration layer
├── templates/
│ ├── index.html # Upload page
│ └── results.html # Dashboard UI
├── uploads/ # Uploaded logs
├── static/ # CSS/JS assets
└── requirements.txt


---

## ⚙️ How It Works

1. User uploads a log file
2. Backend saves and parses the file
3. Extracts errors and warnings
4. Sends logs to the AI model for analysis
5. Displays structured insights + charts

---

## 📊 Example Output

- Major Issues
- Recurring Failures
- Root Causes
- Recommendations
- Error vs Warning visualization

---

## 🧠 Key Learning Outcomes

- Backend API development with Flask
- File handling and log parsing
- AI API integration and prompt engineering
- Data visualization with Chart.js
- Full-stack application architecture

---

## 📸 Screenshots

(Add screenshots of your dashboard here)
<img width="1024" height="768" alt="image" src="https://github.com/user-attachments/assets/4a73c130-1ec6-48b1-a7c9-6219398ab7d7" />

<img width="1024" height="768" alt="image" src="https://github.com/user-attachments/assets/2e6edd63-668d-4afa-b1dc-1140cadac94a" />



## 🚀 Future Improvements

- Docker containerization
- Real-time log streaming
- Service-level error grouping
- Time-series analytics
- Deployment to cloud (AWS / Render)

## 👨‍💻 Author

Built by Abdullah Ahmed
