import tkinter as tk
class stack:
    def __init__(self):
        self.a=[]
    def push(self,b):
        self.a.append(b)
    def pop(self):
        return self.a.pop()
    def top(self):
        return self.a[len(a)-1]

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    for i in range(9):
        if board[i][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def solve_sudoku(board):
    stac = stack()
    stac.push(board.a)

    while stac.a:
        current_board = stac.pop()

        empty_cell = find_empty_cell(current_board)
        if not empty_cell:
            return current_board  

        row, col = empty_cell

        
        for num in range(1, 10):
            if is_valid(current_board, row, col, num):
                current_board[row][col] = num
                print(stac.a)
                stac.push([x[:] for x in current_board])
              
                current_board[row][col] = 0  

    return None


def solve_button_clicked():
    board = stack()
    x=0
    for i in range(9):
        row = stack()
        for j in range(9):
            value = int(entries[i][j].get())
            if(value in row.a and value!=0):
                x=1
                solution=None
                break
            for k in range(i):
                if(value==board.a[k][j] and value!=0):
                    x=1
                    solution=None
                    break
                
            if(x==1):
                break
            row.push(value)
        if(x==1):
            break
        board.push(row.a)
    

    if(x!=1):
        solution = solve_sudoku(board)
        
    
    if solution:
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(tk.END, str(solution[i][j]))
    else:
        if(x!=1):
            message_label.config(text="No solution exists.")
        else:
            message_label.config(text="Invalid inputs.")

def apply_grid_colors():
    for i in range(9):
        for j in range(9):
            if (i // 3 + j // 3) % 2 == 0:
                entries[i][j].config(bg="light blue")
            else:
                entries[i][j].config(bg="light yellow")

window = tk.Tk()
window.title("Sudoku Solver")

entries = []
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(window, width=2, font=("Arial", 16))
        entry.grid(row=i, column=j)
        row_entries.append(entry)
    entries.append(row_entries)

apply_grid_colors()
solve_button = tk.Button(window, text="do", command=solve_button_clicked)
solve_button.grid(row=9, column=4,pady=10)
message_label = tk.Label(window, font=("Arial", 14))
message_label.grid(row=10, columnspan=9,pady=10)
window.mainloop()
