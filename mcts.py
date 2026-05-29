import random
class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0
    # Add child node
    def add_child(self, child_state):
        child = Node(child_state, self)
        self.children.append(child)
        return child
    # Update statistics
    def update(self, result):
        self.visits += 1
        self.wins += result
# Random simulation
def simulate_random_game():
    # Randomly returns:
    # 1 = win
    # 0 = loss
    return random.choice([0, 1])
# Root node
root = Node("Start")
# Run simulations
for i in range(5):
    # Expansion
    child = root.add_child(f"Move_{i}")
    # Simulation
    result = simulate_random_game()
    # Backpropagation
    child.update(result)
    root.update(result)

# Final Output
print("Root Visits:", root.visits)
print("Root Wins:", root.wins)
print("\nChildren Statistics:\n")
for child in root.children:
    print("State:", child.state)
    print("Visits:", child.visits)
    print("Wins:", child.wins)
    print()