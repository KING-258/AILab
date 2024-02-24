from Q import Queue as Queue
class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))
    def __str__(self):
        return f'({self.x}, {self.y})'
def is_valid(state, x, y):
    return 0 <= state.x <= x and 0 <= state.y <= y
def water_jug_bfs(x, y, target):
    start_state = State(0, 0)
    visited = set()
    queue = Queue()
    queue.enqueue(start_state)
    while not queue.is_empty():
        current_state = queue.dequeue()
        if current_state == target:
            return True
        if current_state in visited:
            continue
        visited.add(current_state)
        next_states = [
            State(x, current_state.y),  
            State(current_state.x, y),  
            State(0, current_state.y),  
            State(current_state.x, 0),  
            State(min(x, current_state.x + current_state.y), max(0, current_state.x + current_state.y - x)),  
            State(max(0, current_state.x + current_state.y - y), min(y, current_state.x + current_state.y))   
        ]
        for state in next_states:
            if is_valid(state, x, y):
                queue.enqueue(state)
    return False
if __name__ == "__main__":
    x = int(input("Enter the capacity of jug x: "))
    y = int(input("Enter the capacity of jug y: "))
    target_x = int(input("Enter the target amount of water in jug: "))
    target = State(target_x,0)
    if water_jug_bfs(x, y, target):
        print(f"Yes, it's possible to achieve the target state {target}.")
    else:
        print(f"No, it's not possible to achieve the target state {target}.")