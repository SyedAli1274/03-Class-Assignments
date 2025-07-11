import chainlit as cl
from tools.dice_roller import roll_dice
from tools.event_generator import generate_event
from game_state import GameState
from agents.narrator import NarratorAgent
from agents.monster import MonsterAgent
from agents.item import ItemAgent
import random

user_states = {}

def get_user_state(user_id):
    if user_id not in user_states:
        user_states[user_id] = GameState()
    return user_states[user_id]

narrator = NarratorAgent()
monster_agent = MonsterAgent()
item_agent = ItemAgent()

@cl.on_message
async def main(message: cl.Message):
    user_id = message.author
    state = get_user_state(user_id)
    user_input = message.content.strip()
    user_input_lower = user_input.lower()

    # Show welcome message before the first story message
    if state.story_progress == 0 and not hasattr(state, 'welcomed'):
        await cl.Message(content="👋 Welcome to the Fantasy Adventure Game!\nType or click an option to begin your journey.").send()
        state.welcomed = True
        return

    if state.in_combat:
        result, finished = monster_agent.resolve_combat(state, user_input)
        if result == "Invalid action.":
            await cl.Message(content="Invalid action. Valid actions: Fight, Run").send()
            return
        await cl.Message(content=result).send()
        if finished is True:
            reward = random.choice(["Potion", "Gold Coin", "Magic Ring"])
            await cl.Message(content=item_agent.add_item(state, reward)).send()
            state.last_event = generate_event()
            state.story_progress += 1
        elif finished is False:
            await cl.Message(content="Game Over. Type 'restart' to play again.").send()
            user_states[user_id] = GameState()
            return
        return
    elif user_input_lower == "inventory":
        await cl.Message(content=item_agent.show_inventory(state)).send()
        return
    elif user_input_lower == "restart":
        user_states[user_id] = GameState()
        await cl.Message(content="Game restarted!").send()
        return
    elif state.story_progress == 0:
        story, options = narrator.narrate(state)
        # Partial/case-insensitive match for options
        matched = False
        for opt in options:
            if user_input_lower in opt.lower():
                state.last_event = None
                state.story_progress += 1
                matched = True
                break
        if not matched and user_input != "":
            await cl.Message(content=story + "\nOptions: " + ", ".join(options) + "\n(Type or click one of the options above)").send()
            return
        await cl.Message(content=story + "\nOptions: " + ", ".join(options)).send()
        state.story_progress += 1
        return
    else:
        state.last_event = generate_event()
        if state.last_event == "A wild monster appears!":
            await cl.Message(content=monster_agent.start_combat(state)).send()
            await cl.Message(content="Type 'Fight' or 'Run'").send()
            return
        else:
            story, options = narrator.narrate(state)
            # Partial/case-insensitive match for options
            matched = False
            for opt in options:
                if user_input_lower in opt.lower():
                    matched = True
                    break
            if not matched and user_input != "":
                await cl.Message(content=story + "\nOptions: " + ", ".join(options) + "\n(Type or click one of the options above)").send()
                return
            await cl.Message(content=story + "\nOptions: " + ", ".join(options)).send()
            return