from sdk_fallback import tool

@tool
def get_career_roadmap(career: str) -> str:
    # 👇 Debug line (aap chaho to hata bhi sakte ho)
    print(f"DEBUG: Career received = '{career}'")

    # 👇 Normalize case to lowercase
    career = career.lower()

    # 👇 Career roadmaps
    data = {
        "data scientist": "1. Python\n2. Stats\n3. ML\n4. SQL\n5. Communication",
        "web developer": "1. HTML/CSS\n2. JavaScript\n3. React\n4. Django\n5. APIs",
        "graphic designer": "1. Photoshop\n2. Illustrator\n3. Branding\n4. UI/UX\n5. Portfolio",
        "teacher": "1. Subject Expertise\n2. Teaching Certificate\n3. Communication Skills\n4. Classroom Management\n5. Lesson Planning",
        "writer": "1. Grammar\n2. Creative Thinking\n3. Research\n4. SEO\n5. Editing",
        "entrepreneur": "1. Business Idea\n2. Market Research\n3. Product Validation\n4. Marketing\n5. Fundraising"
    }

    return data.get(career, "No roadmap found.")
