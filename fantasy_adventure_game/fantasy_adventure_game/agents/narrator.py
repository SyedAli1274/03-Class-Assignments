class NarratorAgent:
    def narrate(self, state):
        if state.story_progress == 0:
            return (
                "Your adventure begins in a small village at the edge of a dark forest. What do you do?",
                ["Explore the forest", "Visit the tavern"]
            )
        elif state.last_event == "A wild monster appears!":
            return ("A monster blocks your path! Prepare for battle!", ["Fight", "Run"])
        else:
            return (f"{state.last_event} What do you do next?", ["Continue"])