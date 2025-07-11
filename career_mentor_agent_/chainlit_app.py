import chainlit as cl
from agents.career_agent import career_agent
from agents.skill_agent import skill_agent
from agents.job_agent import job_agent


@cl.on_chat_start
async def start():
    await cl.Message(content="🎓 Welcome to Career Mentor Agent!").send()

@cl.on_message
async def handle(message: cl.Message):
    interest = message.content
    careers = career_agent(interest)
    await cl.Message(content=f"📋 Suggested Careers:\n{careers}").send()

    await cl.Message(content="✏️ Please type one career from above to get roadmap:").send()
    res = await cl.AskUserMessage(content="Career choice?", timeout=60).send()
    selected = res["output"]

    skills = skill_agent(selected)
    await cl.Message(content=f"📚 Required Skills:\n{skills}").send()

    jobs = job_agent(selected)
    await cl.Message(content=f"💼 Job Roles:\n{jobs}").send()
