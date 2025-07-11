import random

def generate_event():
    events = [
        "You find a mysterious cave.",
        "A wild monster appears!",
        "You discover a hidden treasure chest.",
        "A traveling merchant offers you goods.",
        "You fall into a trap!"
    ]
    return random.choice(events)