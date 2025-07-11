class DestinationAgent:
    def suggest_destination(self, mood, interests):
        # Mock logic for destination suggestion
        if mood == 'relax':
            return 'Maldives'
        elif mood == 'adventure':
            return 'New Zealand'
        elif 'history' in interests:
            return 'Rome'
        else:
            return 'Paris' 