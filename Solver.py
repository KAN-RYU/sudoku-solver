import sys

grid = []
# ─ │ ┌ ┐ ┘ └ ├ ┬ ┤ ┴ ┼

def print_map():
    print("┌───┬───┬───┐")
    for i in range(9):
        if i % 3 == 0 and i > 0:
            print("├───┼───┼───┤")
        print("│"+str(grid[i][0])+str(grid[i][1])+str(grid[i][2])+
              "│"+str(grid[i][3])+str(grid[i][4])+str(grid[i][5])+
              "│"+str(grid[i][6])+str(grid[i][7])+str(grid[i][8])+"│", end='')
        print()        
    print("└───┴───┴───┘")

if __name__ == "__main__":
    with open('./from.txt', mode = 'r') as f:
        line = f.readlines()
        offset = 0
        for i in range(9):
            grid.append([0]*9)
            if i % 3 == 0 and i > 0:
                offset += 1
            a = line[i + offset].replace(' ',  '')
            print(a)
            for j in range(9):
                print(i, j)
                grid[i][j] = a[j]
        
        print_map()