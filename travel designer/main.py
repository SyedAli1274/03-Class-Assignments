import os
from agents.destination_agent import DestinationAgent
from agents.booking_agent import BookingAgent
from agents.explore_agent import ExploreAgent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Main orchestration
if __name__ == "__main__":
    print("Welcome to the 🧳 AI Travel Designer Agent!")
    mood = input("What is your travel mood? (relax/adventure): ").strip().lower()
    interests = input("Any interests? (comma separated, e.g. history, food): ").strip().lower().split(",")
    interests = [i.strip() for i in interests if i.strip()]

    # Step 1: Suggest destination
    dest_agent = DestinationAgent()
    destination = dest_agent.suggest_destination(mood, interests)
    print(f"\nSuggested Destination: {destination}")

    # Step 2: Book trip (flights & hotels)
    book_agent = BookingAgent()
    booking = book_agent.book_trip(destination)
    print(f"\nFlight: {booking['flight']}")
    print(f"Hotel: {booking['hotel']}")

    # Step 3: Suggest experiences
    explore_agent = ExploreAgent()
    experiences = explore_agent.suggest_experiences(destination)
    print(f"\nTop Experiences in {destination}:")
    for exp in experiences:
        print(f"- {exp}")

    print("\nHave a great trip!") 