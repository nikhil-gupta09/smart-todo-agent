# =========================================================
# 📘 Smart To-Do Assistant — Streamlit App
# =========================================================

import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# =========================================================
# 🧩 Smart To-Do Agent Class
# =========================================================
class SmartToDoAgent:
    def __init__(self):
        self.tasks = pd.DataFrame(columns=['Task', 'Deadline', 'Priority', 'Status'])

    def add_task(self, task_name, deadline, priority):
        """Add a task"""
        self.tasks = pd.concat([self.tasks, pd.DataFrame({
            'Task': [task_name],
            'Deadline': [pd.to_datetime(deadline)],
            'Priority': [priority],
            'Status': ['Pending']
        })], ignore_index=True)

    def mark_done(self, task_index):
        """Mark task as done"""
        if 0 <= task_index < len(self.tasks):
            self.tasks.at[task_index, 'Status'] = 'Done'

    def suggest_task(self):
        """Suggest next task based on priority and urgency"""
        pending = self.tasks[self.tasks['Status'] == 'Pending'].copy()
        if pending.empty:
            return "✅ All tasks completed!"
        today = pd.to_datetime(datetime.today().date())
        pending['DaysLeft'] = (pending['Deadline'] - today).dt.days
        pending = pending.sort_values(by=['Priority', 'DaysLeft'])
        next_task = pending.iloc[0]
        return f"🧭 Next Task: {next_task['Task']} | ⏰ Deadline: {next_task['Deadline'].date()} | ⭐ Priority: {next_task['Priority']}"

# =========================================================
# 🚀 Streamlit Interface
# =========================================================
st.set_page_config(page_title="Smart To-Do Assistant", page_icon="🧠", layout="centered")

st.title("🤖 Smart To-Do Assistant")
st.markdown("An AI-inspired task prioritization assistant that helps you plan your day efficiently.")

# Initialize session state
if "agent" not in st.session_state:
    st.session_state.agent = SmartToDoAgent()

agent = st.session_state.agent

# =========================================================
# 📤 Upload CSV
# =========================================================
st.sidebar.header("📁 Import Tasks from CSV")
uploaded_file = st.sidebar.file_uploader("Upload CSV (Task, Deadline, Priority)", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df['Deadline'] = pd.to_datetime(df['Deadline'])
    df['Status'] = 'Pending'
    agent.tasks = pd.concat([agent.tasks, df], ignore_index=True)
    st.sidebar.success("✅ Tasks imported successfully!")

# =========================================================
# ➕ Add New Task
# =========================================================
st.subheader("➕ Add a New Task")
task_name = st.text_input("Task Name")
deadline = st.date_input("Deadline")
priority = st.selectbox("Priority (1 = High, 2 = Medium, 3 = Low)", [1, 2, 3])

if st.button("Add Task"):
    if task_name:
        agent.add_task(task_name, deadline, priority)
        st.success(f"✅ Task '{task_name}' added successfully!")
    else:
        st.warning("⚠️ Please enter a task name.")

# =========================================================
# 📋 Display All Tasks
# =========================================================
st.subheader("📋 All Tasks")
if not agent.tasks.empty:
    st.dataframe(agent.tasks.sort_values(by=['Status', 'Priority', 'Deadline']).reset_index(drop=True))

    done_task = st.number_input("Enter task index to mark as done (starting from 0)", min_value=0, step=1)
    if st.button("Mark as Done"):
        agent.mark_done(done_task)
        st.success("✅ Task marked as done!")

else:
    st.info("No tasks available yet. Add one above or upload a CSV.")

# =========================================================
# 🎯 Suggest Next Task
# =========================================================
st.subheader("🎯 Suggested Next Task")
st.markdown(agent.suggest_task())

# =========================================================
# 📊 Visualization
# =========================================================
if not agent.tasks.empty:
    st.subheader("📅 Task Deadline Visualization")
    plt.figure(figsize=(8, 4))
    plt.barh(agent.tasks['Task'], (agent.tasks['Deadline'] - pd.Timestamp.now()).dt.days, color='skyblue')
    plt.xlabel("Days Left Until Deadline")
    plt.ylabel("Tasks")
    plt.tight_layout()
    st.pyplot(plt)

# =========================================================
# 💾 Download Updated Tasks
# =========================================================
st.subheader("💾 Download Updated Task List")
csv_data = agent.tasks.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Download CSV",
    data=csv_data,
    file_name="updated_tasks.csv",
    mime="text/csv"
)

