
from agents.career_agent import career_agent
from agents.skill_agent import skill_agent
from agents.job_agent import job_agent

def main():
    print("🎓 Welcome to Career Mentor Agent")

    interest = input("Apka interest kya hai? (e.g., tech, design, education): ")
    careers = career_agent(interest)
    print("\n👉 Suggested Careers:\n" + careers)

    career = input("\nIn me se aik career choose karein: ")
    skills = skill_agent(career)
    print("\n📚 Required Skills:\n" + skills)

    jobs = job_agent(career)
    print("\n💼 Real World Jobs:\n" + jobs)

if __name__ == "__main__":
    main()
