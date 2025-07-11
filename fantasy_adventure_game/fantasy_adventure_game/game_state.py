class GameState:
    def __init__(self):
        self.story_progress = 0
        self.inventory = []
        self.in_combat = False
        self.hp = 10
        self.monster_hp = 0
        self.last_event = None