class ItemAgent:
    def add_item(self, state, item):
        state.inventory.append(item)
        return f"You received: {item}!"

    def show_inventory(self, state):
        if state.inventory:
            return "Your inventory: " + ", ".join(state.inventory)
        else:
            return "Your inventory is empty."