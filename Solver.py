import sys

grid = []
# ─ │ ┌ ┐ ┘ └ ├ ┬ ┤ ┴ ┼
#\033[93m yellow
#\033[0m white
#\033[94m blue
def print_map():
    print("\033[0m┌───┬───┬───┐")
    for i in range(9):
        if i % 3 == 0 and i > 0:
            print("├───┼───┼───┤")
        current_line = '│'
        for j in range(9):
            if grid[i][j]['solid'] == True or grid[i][j]['number'] is '.':
                current_line += str(grid[i][j]['number'])
            elif grid[i][j]['check'] == True:
                grid[i][j]['check'] = False
                current_line += '\033[93m' + str(grid[i][j]['number']) + '\033[0m'
            else:
                current_line += '\033[94m' + str(grid[i][j]['number']) + '\033[0m'
            if j % 3 == 2:
                current_line += '│'
        print(current_line)
    print("└───┴───┴───┘")

def initial_mark():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] is not '.':
                for r in range(9):
                    grid[r][j]['mark'][grid[i][j]['number']] = False
                for c in range(9):
                    grid[c][j]['mark'][grid[i][j]['number']] = False
                offset_r = i - i % 3
                offset_c = j - j % 3
                for a in range(3):
                    for b in range(3):
                        grid[a + offset_r][b + offset_c]['mark'][grid[i][j]['number']] = False

def find_one():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j]['mark'].count(True) == 2 and grid[i][j]['number'] == '.':
                grid[i][j]['number'] = grid[i][j]['mark'].index(True, 1)
                grid[i][j]['check'] = True

if __name__ == "__main__":
    with open('./from.txt', mode = 'r') as f:
        line = f.readlines()
        offset = 0
        for i in range(9):
            grid.append([0]*9)
            if i % 3 == 0 and i > 0:
                offset += 1
            a = line[i + offset].replace(' ',  '')
            for j in range(9):
                grid[i][j] = {'number' : a[j],
                              'mark'   : [True]*10,
                              'check'  : False,
                              'solid'  : False if a[j] is '.' else True}
        
        print_map()