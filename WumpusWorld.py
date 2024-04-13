import random

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.agent_pos = (0, 0)
        self.gold_pos = self.generate_random_position()
        self.wumpus_pos = self.generate_random_position(exclude=[self.agent_pos, self.gold_pos])
        self.pit_pos = [self.generate_random_position(exclude=[self.agent_pos, self.gold_pos, self.wumpus_pos]) for _ in range(size)]
        self.percept = ''

    def generate_random_position(self, exclude=[]):
        while True:
            pos = (random.randint(0, self.size-1), random.randint(0, self.size-1))
            if pos not in exclude:
                return pos

    def print_grid(self):
        for row in self.grid:
            print(' | '.join(row))
            print('-' * (4 * self.size - 1))

    def update_percept(self):
        self.percept = ''
        x, y = self.agent_pos
        if self.wumpus_pos == self.agent_pos:
            self.percept += 'You smell a terrible stench!\n'
        if any(pit == self.agent_pos for pit in self.pit_pos):
            self.percept += 'You feel a draft!\n'
        if self.gold_pos == self.agent_pos:
            self.percept += 'You see a glimmer!\n'

    def move_agent(self, direction):
        x, y = self.agent_pos
        if direction == 'up' and x > 0:
            self.agent_pos = (x - 1, y)
        elif direction == 'down' and x < self.size - 1:
            self.agent_pos = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.agent_pos = (x, y - 1)
        elif direction == 'right' and y < self.size - 1:
            self.agent_pos = (x, y + 1)
        self.update_percept()

    def run(self):
        print("Welcome to Wumpus World!")
        while True:
            self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
            self.grid[self.agent_pos[0]][self.agent_pos[1]] = 'A'
            self.grid[self.gold_pos[0]][self.gold_pos[1]] = 'G'
            self.grid[self.wumpus_pos[0]][self.wumpus_pos[1]] = 'W'
            for pit_pos in self.pit_pos:
                self.grid[pit_pos[0]][pit_pos[1]] = 'P'
            self.print_grid()
            print(self.percept)
            if self.agent_pos == self.wumpus_pos:
                print("Game Over! You are eaten by the Wumpus!")
                break
            elif self.agent_pos in self.pit_pos:
                print("Game Over! You fell into a pit!")
                break
            elif self.agent_pos == self.gold_pos:
                print("Congratulations! You found the gold!")
                break
            action = input("Enter action (up/down/left/right): ")
            self.move_agent(action)

wumpus_world = WumpusWorld()
wumpus_world.run()
