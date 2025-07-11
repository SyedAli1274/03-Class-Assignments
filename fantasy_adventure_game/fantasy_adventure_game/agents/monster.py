import random
from tools.dice_roller import roll_dice

class MonsterAgent:
    def start_combat(self, state):
        state.in_combat = True
        state.monster_hp = random.randint(5, 12)
        return f"A monster appears with {state.monster_hp} HP!"

    def resolve_combat(self, state, action):
        action = action.strip().lower()
        if action == "fight":
            player_roll = roll_dice(6, 1)[0]
            monster_roll = roll_dice(6, 1)[0]
            state.monster_hp -= player_roll
            state.hp -= monster_roll
            if state.monster_hp <= 0:
                state.in_combat = False
                return "You defeated the monster!", True
            elif state.hp <= 0:
                return "You were defeated by the monster... Game Over.", False
            else:
                return (
                    f"You hit the monster for {player_roll} damage. "
                    f"Monster hits you for {monster_roll} damage. "
                    f"(Your HP: {state.hp}, Monster HP: {state.monster_hp})", None
                )
        elif action == "run":
            state.in_combat = False
            return "You escaped from the monster!", True
        else:
            return "Invalid action.", None