from sdk_fallback import agent

@agent
def job_agent(career: str) -> str:
    jobs = {
        "Data Scientist": "Data Analyst, ML Engineer, AI Researcher",
        "Web Developer": "Frontend Dev, Backend Dev, Full Stack Dev",
        "Graphic Designer": "UI Designer, Branding Specialist",
        "Teacher": "School Teacher, Online Tutor, Education Consultant",
        "Writer": "Content Writer, Copywriter, Blogger",
        "Entrepreneur": "Startup Founder, Product Owner, Business Consultant"
    }
    return jobs.get(career, "No job roles found.")
