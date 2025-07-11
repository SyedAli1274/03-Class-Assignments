import chainlit as cl
from agents.destination_agent import DestinationAgent
from agents.booking_agent import BookingAgent
from agents.explore_agent import ExploreAgent

def get_content(message):
    if isinstance(message, dict):
        return message.get("content", "")
    return getattr(message, "content", "")

@cl.on_chat_start
async def start():
    cl.user_session.set("step", "mood")
    await cl.Message(content="\U0001F9D1\u200D\U0001F5FA️ Welcome! Yeh AI Travel Designer hai.\nAap apna mood ya interest enter karein (e.g., adventure, relax, beach, history, food)").send()
    await cl.AskUserMessage(content="Aap ka mood kya hai? (relax/adventure)").send()

@cl.on_message
async def main(message):
    step = cl.user_session.get("step", "mood")
    content = get_content(message)
    if step == "mood":
        mood = content.strip().lower()
        cl.user_session.set("mood", mood)
        cl.user_session.set("step", "interests")
        await cl.Message(content=f"Aap ka mood: {mood}").send()
        await cl.AskUserMessage(content="Aap ke interests kya hain? (comma separated, e.g. history, food)").send()
    elif step == "interests":
        interests = [i.strip() for i in content.strip().lower().split(",") if i.strip()]
        cl.user_session.set("interests", interests)
        await cl.Message(content=f"Aap ke interests: {', '.join(interests)}").send()
        # Proceed with agent handoff
        mood = cl.user_session.get("mood", "relax")
        await cl.Message(content="\U0001F3D6 DestinationAgent: User ke mood/interests ke mutabiq jagah dhoond raha hai...").send()
        dest_agent = DestinationAgent()
        destination = dest_agent.suggest_destination(mood, interests)
        await cl.Message(content=f"\U0001F4CD Suggested Destination: {destination}").send()
        await cl.Message(content="\U0001F5FA BookingAgent: Flights aur hotels dhoond raha hai...").send()
        book_agent = BookingAgent()
        booking = book_agent.book_trip(destination)
        await cl.Message(content=f"\U0001F6EB Flight: {booking['flight']}\n\U0001F3E8 Hotel: {booking['hotel']}").send()
        await cl.Message(content=f"\U0001F30D ExploreAgent: {destination} mein kya explore karna hai, yeh batata hai...").send()
        explore_agent = ExploreAgent()
        experiences = explore_agent.suggest_experiences(destination)
        exp_list = '\n'.join(f"- {exp}" for exp in experiences)
        await cl.Message(content=f"\U0001F4D6 Top Experiences in {destination}:\n{exp_list}").send()
        await cl.Message(content="\U0001F389 Aap ka safar tayyar hai! Mazay ka trip ho!").send()
        cl.user_session.set("step", "done")
    else:
        await cl.Message(content="Aap ka safar already plan ho chuka hai! Dobara shuru karne ke liye chat refresh karein.").send() 