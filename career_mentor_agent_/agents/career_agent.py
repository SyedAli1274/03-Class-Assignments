from sdk_fallback import agent

@agent
def career_agent(user_input: str) -> str:
    interest = user_input.lower()
    if "tech" in interest:
        return "Data Scientist, Web Developer"
    elif "design" in interest:
        return "Graphic Designer, UI/UX Designer"
    else:
        return "Teacher, Writer, Entrepreneur"
