🧠 Smart To-Do Assistant

AI / Agentic Productivity Tool | Built with Python & Streamlit

📘 Overview

Smart To-Do Assistant is a rule-based AI productivity agent that helps users organize, prioritize, and visualize daily tasks.
It acts like an agentic AI assistant, intelligently suggesting what to focus on next based on urgency, importance, and deadlines — all in a simple Streamlit web app.

🚀 Features

🧩 AI-based prioritization using rule-based logic for smart task suggestions.

✍️ Add tasks manually or import tasks via CSV for quick setup.

✅ Mark tasks as done dynamically with instant updates.

📅 Visualize task timelines with deadline-based bar charts.

💾 Download updated task lists anytime for record keeping.

🧭 Agentic behavior simulation – suggests the “Next Best Task” based on real-time urgency and priority.

🧰 Tech Stack

Python 3.10+

Streamlit – interactive web app framework

Pandas – task data handling

Matplotlib – task visualization

🧩 How It Works

Upload a CSV file with columns:
Task, Deadline (YYYY-MM-DD), Priority (1=High, 2=Med, 3=Low)

Or add tasks manually from the UI.

The agent automatically sorts tasks by urgency and priority.

Displays next actionable task and a visual timeline of all tasks.




# 1️⃣ Clone the repository
git clone https://github.com/your-username/smart-todo-assistant.git
cd smart-todo-assistant

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the app
streamlit run app.py
