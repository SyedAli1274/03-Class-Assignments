class ExploreAgent:
    def suggest_experiences(self, destination):
        # Mock data for attractions and food
        experiences = {
            'Maldives': ['Snorkeling', 'Seafood BBQ'],
            'New Zealand': ['Bungee Jumping', 'Lamb Roast'],
            'Rome': ['Colosseum Tour', 'Gelato'],
            'Paris': ['Eiffel Tower', 'Croissants']
        }
        return experiences.get(destination, ['City Tour', 'Local Cuisine']) 