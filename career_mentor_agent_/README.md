
# 💼 Career Mentor Agent

## 🧠 What It Does
- Suggests career options based on interest
- Shows skill roadmap using tool
- Displays real-world job roles

## 🧩 Agents
- `career_agent` → Suggests careers
- `skill_agent` → Returns required skills (via tool)
- `job_agent` → Shows job titles

## 🛠️ Tool
- `get_career_roadmap(career)` → Skill plan for each career

## 🔁 Flow
User → CareerAgent → SkillAgent (Tool) → JobAgent

## 🖥️ Run CLI
```bash
python main.py
```

## 🌐 Run Web App
```bash
chainlit run chainlit_app.py
```

## ✅ Requirements
- Python 3.10+
- Chainlit, OpenAI SDK, Agents
