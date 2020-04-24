import copy

# ─ │ ┌ ┐ ┘ └ ├ ┬ ┤ ┴ ┼
#\033[93m yellow
#\033[0m white
#\033[94m blue
#\033[91m red
def numbers(grid):
    count = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j]['number'] is not '.':
                count += 1
    return count

def print_map(grid):
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
            elif grid[i][j]['branch'] == True:
                grid[i][j]['branch'] = False
                current_line += '\033[91m' + str(grid[i][j]['number']) + '\033[0m'
            else:
                current_line += '\033[94m' + str(grid[i][j]['number']) + '\033[0m'
            if j % 3 == 2:
                current_line += '│'
        print(current_line)
    print("└───┴───┴───┘")

def initial_mark(grid):
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

def find_one(grid):
    checked = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j]['mark'].count(True) == 1 and grid[i][j]['number'] == '.':
                grid[i][j]['number'] = grid[i][j]['mark'].index(True, 1)
                grid[i][j]['check'] = True
                if i == 4 and j == 4:
                    print(1)
                initial_mark(grid)
                checked += 1
    return checked

def find_be_one(grid): 
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
                        initial_mark(grid)
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
                        initial_mark(grid)
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
                                initial_mark(grid)
                                checked += 1
                                break
                    offset = l + 1
                except:
                    break
    return checked

if __name__ == "__main__":
    with open('./from.txt', mode = 'r') as f:
        stack = []
        grid = []
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
                              'solid'  : False if a[j] is '.' else True,
                              'branch' : False}
                
        print_map(grid)
        initial_mark(grid)
        while True:
            # checked = 0
            checked1 = find_one(grid)
            checked2 = find_be_one(grid)
            if checked1 + checked2 == 0:
                if numbers(grid) == 81:
                    print('done!')
                    break
                else:
                    returnFlag = True
                    for i in range(9):
                        for j in range(9):
                            if grid[i][j]['mark'].count(True) == 2:
                                returnFlag = False
                                a = copy.deepcopy(grid)
                                l = grid[i][j]['mark'].index(True)
                                a[i][j]['number'] = l
                                a[i][j]['branch'] = True
                                initial_mark(a)

                                b = copy.deepcopy(grid)
                                b[i][j]['number'] = grid[i][j]['mark'].index(True, l + 1)
                                b[i][j]['branch'] = True
                                initial_mark(b)

                                grid = a
                                stack.append(b)
                                break
                        if not returnFlag:
                            print('branch')
                            break
                    if returnFlag:
                        print('back')
                        if len(stack) == 0:
                            print('fail')
                            break
                        grid = stack.pop()
            else:
                print('\n\n')
                print_map(grid)
            input("checked: " + str(checked1) + ' ' + str(checked2))