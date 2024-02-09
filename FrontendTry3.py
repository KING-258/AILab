import tkinter as tk
from tkinter import messagebox
from Puzzle import Puzzle, a_star

class PuzzleSolverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Puzzle Solver")

        self.source_matrix = [[1, 2, 3],
                              [5, 6, 0],
                              [7, 8, 4]]
        self.goal_matrix = [[1, 2, 3],
                            [5, 8, 6],
                            [0, 7, 4]]

        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()

        self.tiles = {}
        self.init_board()

        solve_button = tk.Button(master, text="Solve Puzzle", command=self.solve_puzzle)
        solve_button.pack()

    def init_board(self):
        for i in range(3):
            for j in range(3):
                if self.source_matrix[i][j] != 0:
                    x0, y0 = j * 100, i * 100
                    x1, y1 = x0 + 100, y0 + 100
                    self.tiles[self.source_matrix[i][j]] = self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
                    self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(self.source_matrix[i][j]))

    def move_tile(self, tile_value):
        i, j = self.find_tile_position(tile_value)
        possible_moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for move in possible_moves:
            new_i, new_j = i + move[0], j + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3 and self.source_matrix[new_i][new_j] == 0:
                self.source_matrix[i][j], self.source_matrix[new_i][new_j] = self.source_matrix[new_i][new_j], self.source_matrix[i][j]
                self.update_board()
                return

    def find_tile_position(self, tile_value):
        for i in range(3):
            for j in range(3):
                if self.source_matrix[i][j] == tile_value:
                    return i, j

    def update_board(self):
        for i in range(3):
            for j in range(3):
                tile_value = self.source_matrix[i][j]
                if tile_value != 0:
                    x0, y0 = j * 100, i * 100
                    x1, y1 = x0 + 100, y0 + 100
                    self.canvas.coords(self.tiles[tile_value], x0, y0, x1, y1)
                    self.canvas.itemconfig(self.tiles[tile_value], text=str(tile_value))

    def solve_puzzle(self):
        src = Puzzle(1, 2, self.goal_matrix, self.source_matrix)
        src.heuristic()
        solution = a_star(src, self.goal_matrix)

        if solution:
            messagebox.showinfo("Solution", "Puzzle solved successfully!")
        else:
            messagebox.showerror("Error", "Failed to solve puzzle.")

def main():
    root = tk.Tk()
    app = PuzzleSolverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
