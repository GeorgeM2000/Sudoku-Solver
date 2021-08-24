class SudokuSolver():
    def __init__(self):
        # All sub grids
        self.sub_grid_01 = [[i,j] for j in range(0,3) for i in range(0,3)]
        self.sub_grid_02 = [[i,j] for j in range(3,6) for i in range(0,3)]
        self.sub_grid_03 = [[i,j] for j in range(6,9) for i in range(0,3)]

        self.sub_grid_04 = [[i,j] for j in range(0,3) for i in range(3,6)]
        self.sub_grid_05 = [[i,j] for j in range(3,6) for i in range(3,6)]
        self.sub_grid_06 = [[i,j] for j in range(6,9) for i in range(3,6)]


        self.sub_grid_07 = [[i,j] for j in range(0,3) for i in range(6,9)]
        self.sub_grid_08 = [[i,j] for j in range(3,6) for i in range(6,9)]
        self.sub_grid_09 = [[i,j] for j in range(6,9) for i in range(6,9)]


        # Numbers 1-9
        self.Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


    # Function to retrieve a subgrid
    # This function takes the coordinates(x,y) of the current cell and returns it's subgrid
    def retrieve_sub_grid(self, grid, x, y):
        if (0 <= y <= 2) and (0 <= x <= 2): return self.sub_grid_01
        elif (3 <= y <= 5) and (0 <= x <= 2): return self.sub_grid_02
        elif (6 <= y <= 8) and (0 <= x <= 2): return self.sub_grid_03

        elif (0 <= y <= 2) and (3 <= x <= 5): return self.sub_grid_04
        elif (3 <= y <= 5) and (3 <= x <= 5): return self.sub_grid_05
        elif (6 <= y <= 8) and (3 <= x <= 5): return self.sub_grid_06

        elif (0 <= y <= 2) and (6 <= x <= 8): return self.sub_grid_07
        elif (3 <= y <= 5) and (6 <= x <= 8): return self.sub_grid_08
        elif (6 <= y <= 8) and (6 <= x <= 8): return self.sub_grid_09
    
    # Function to retrieve a row
    # This function takes the current cell row number and returns the whole row
    def retrieve_row(self, grid, y):
        return grid[y][:]

    # Function to retrieve a column
    # This function takes the current cell column number and returns the whole column
    def retrieve_col(self, grid, x):
        return [col[x] for col in Grid]

    # Function to check if the cell value is valid in the current subgrid
    def check_sub_grid(self, grid, x, y, cell_value):
        choosen_sub_grid = self.retrieve_sub_grid(grid, x, y)
        for row in range(0,len(choosen_sub_grid)):
            if grid[choosen_sub_grid[row][0]][choosen_sub_grid[row][1]] == cell_value: 
                return False
        return True

    # Function to check if the cell value is valid in the current column
    def check_col(self, grid, y, cell_value):
        choosen_col = self.retrieve_col(grid, y)
        for element in choosen_col:
            if element == cell_value: 
                return False
        return True

    # Function to check if the cell value is valid in the current row
    def check_row(self, grid, x, cell_value):
        choosen_row = self.retrieve_row(grid, x)
        for element in choosen_row:
            if element == cell_value: 
                return False
        return True

    # Function to find an  available cell
    def find_available_cell(self, grid):
        for row in range(0, 9):
            for col in range(0, 9):
                if grid[row][col] == "-":
                    return (row, col)
        return False

    # Function to print the grid
    def print_grid(self, grid):
        for row in range(0, 9):
            for col in range(0, 9):
                print(grid[row][col] + " ", end=" ")
            print()

    # Function to solve Sudoku
    def solve(self, grid):
        
        find = self.find_available_cell(grid)
        if not find:
            return True
        else:
            row, col = find
        
        for possible_number in self.Numbers:
            if self.check_col(grid, col, possible_number) and self.check_row(grid, row, possible_number) and self.check_sub_grid(grid, row, col, possible_number):
                grid[row][col] = possible_number

                if self.solve(grid):
                    return True
                
                grid[row][col] = "-"

        return False


if __name__ == "__main__":
    Grid = [
        ["7","8","-","4","-","-","1","2","-"],
        ["6","-","-","-","7","5","-","-","9"],
        ["-","-","-","6","-","1","-","7","8"],
        ["-","-","7","-","4","-","2","6","-"],
        ["-","-","1","-","5","-","9","3","-"],
        ["9","-","4","-","6","-","-","-","5"],
        ["-","7","-","3","-","-","-","1","2"],
        ["1","2","-","-","-","7","4","-","-"],
        ["-","4","9","2","-","6","-","-","7"]
        ]

    
    solver = SudokuSolver()
    solver.solve(Grid)
    solver.print_grid(Grid)
    

    
    
        
    

