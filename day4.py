def solve():
    ans = 0
    dir = [
        (-1, 0), # up
        (1, 0), # down
        (0, -1), # left
        (0, 1), # right
        (-1, 1), # up right
        (-1, -1), # up left
        (1, 1), # down right
        (1, -1), # down left
    ]

    with open("input.txt", "r") as file:
        windows = file.readlines()

        R = len(windows)
        C = len(windows[0].strip())

        for r in range(R):
            for c in range(C):

                if (windows[r][c]=='@'):
                    roll_acess_count = 0
                    for dx,dy in dir:
                        ri = r + dx
                        ci = c + dy

                        if (0 <= ri < R) and (0 <= ci < C) and (windows[ri][ci]=='@'):
                            roll_acess_count += 1

                    if roll_acess_count<4:
                        ans += 1
    return ans

class RollingList(list):
    def __init__(self, max_size, iterable=()):
        self.max_size = max_size
        super().__init__(iterable[-max_size:])

    def append(self, item):
        if len(self) >= self.max_size:
            self.pop(0)  # remove oldest
        super().append(item)

def process_window(windows, write_output:bool):
    dir = [
        (-1, 1), (-1, 0), (-1, -1), 
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1), 
    ]
    
    ans = 0

    # process all cols in row 1
    R = 3
    r = 1

    curr = windows[1]
    C = len(curr)

    output = curr

    for c in range(C):
        if (windows[r][c]=='@'):
            roll_acess_count = 0
            for dx,dy in dir:
                ri = r + dx
                ci = c + dy

                if (0 <= ri < R) and (0 <= ci < C) and (windows[ri][ci]=='@'):
                    roll_acess_count += 1

            if roll_acess_count<4:
                output = output[:c] + "x" + output[c+1:]
                ans += 1
    
    if write_output:
        with open("input_temp.txt", "a") as f:
            f.write(output+'\n')

    return ans

def solve2(write_output:bool):
    # process in max windows of size 3
    ans = 0

    with open("input.txt", "r") as file:
        windows = RollingList(3, [])

        first_line = file.readline().strip()
        C = len(first_line)

        windows.append('.'*C)
        windows.append(first_line)


        for line in file:
            windows.append(line.strip())

            if len(windows)==3:
                ans += process_window(windows, write_output)

        windows.append('.'*C)
        ans += process_window(windows, write_output)

    return ans

def solve3():
    ans = 0

    while True:
        # clear input file
        open("input.txt", "w").close()

        # copy input from temp file
        with open("input_temp.txt", "r") as src, open("input.txt", "w") as dst:
            for line in src:
                dst.write(line)
        
        # clear temp file
        open("input_temp.txt", "w").close()

        curr = solve2(True)
        ans += curr

        if curr==0:
            break
    
    return ans


if __name__=="__main__":
    # brute force
    # max_paper_rolls = solve()

    # window optimized
    # max_paper_rolls = solve2()
    
    # for part 2
    max_paper_rolls = solve3()
    print(max_paper_rolls)
    


