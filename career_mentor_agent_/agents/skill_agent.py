from sdk_fallback import agent
from tools.roadmap_tool import get_career_roadmap

@agent
def skill_agent(career: str) -> str:
    return get_career_roadmap(career)
