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
            grid[i][j]['mark'][0] = False
            if grid[i][j]['number'] is not '.':
                for r in range(9):
                    grid[r][j]['mark'][grid[i][j]['number']] = False
                for c in range(9):
                    grid[i][c]['mark'][grid[i][j]['number']] = False
                offset_r = i - i % 3
                offset_c = j - j % 3
                for a in range(3):
                    for b in range(3):
                        grid[a + offset_r][b + offset_c]['mark'][grid[i][j]['number']] = False

def find_one():
    global grid
    checked = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j]['mark'].count(True) == 1 and grid[i][j]['number'] == '.':
                grid[i][j]['number'] = grid[i][j]['mark'].index(True, 1)
                grid[i][j]['check'] = True
                if i == 4 and j == 4:
                    print(1)
                initial_mark()
                checked += 1
    return checked

def find_be_one(): 
    global grid
    checked = 0
    #row
    for i in range(9):
        count = [0] * 10
        for j in range(9):
            for k in range(1,10):
                if grid[i][j]['mark'][k] == True and grid[i][j]['number'] == '.':
                    count[k] += 1
        offset = 1
        while True:
            try:
                l = count.index(1, offset)
                for c in range(9):
                    if grid[i][c]['mark'][l] == True and grid[i][c]['number'] == '.':
                        grid[i][c]['number'] = l
                        grid[i][c]['check'] = True
                        if i == 4 and c == 4:
                            print(count)
                            print(2)
                        initial_mark()
                        checked += 1
                        break
                offset = l + 1
            except:
                break

    #col
    for j in range(9):
        count = [0] * 10
        for i in range(9):
            for k in range(1,10):
                if grid[i][j]['mark'][k] == True and grid[i][j]['number'] == '.':
                    count[k] += 1
        offset = 1
        while True:
            try:
                l = count.index(1, offset)
                for r in range(9):
                    if grid[r][j]['mark'][l] == True and grid[r][j]['number'] == '.':
                        grid[r][j]['number'] = l
                        grid[r][j]['check'] = True
                        if r == 4 and j == 4:
                            print(3)
                        initial_mark()
                        checked += 1
                        break
                offset = l + 1
            except:
                break

    #box
    for i in range(3):
        for j in range(3):
            count = [0] * 10
            for a in range(3):
                for b in range(3):
                    for k in range(1,10):
                        if grid[i * 3 + a][j * 3 + b]['mark'][k] == True and grid[i * 3 + a][j * 3 + b]['number'] == '.':
                            count[k] += 1
            offset = 1
            while True:
                try:
                    l = count.index(1, offset)
                    for r in range(3):
                        for c in range(3):
                            if grid[i * 3 + r][j * 3 + c]['mark'][l] == True and grid[i * 3 + r][j * 3 + c]['number'] == '.':
                                grid[i * 3 + r][j * 3 + c]['number'] = l
                                grid[i * 3 + r][j * 3 + c]['check'] = True
                                if i * 3 + r == 4 and j * 3 + c == 4:
                                    print(1)
                                initial_mark()
                                checked += 1
                                break
                    offset = l + 1
                except:
                    break
    return checked

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
                grid[i][j] = {'number' : a[j] if a[j] is '.' else int(a[j]),
                              'mark'   : [True]*10,
                              'check'  : False,
                              'solid'  : False if a[j] is '.' else True}
                
        print_map()
        initial_mark()
        while True:
            # checked = 0
            checked1 = find_one()
            checked2 = find_be_one()
            print('\n\n')
            print_map()
            if checked1 + checked2 == 0:
                print('done!')
                break
            input("checked: " + str(checked1) + ' ' + str(checked2))