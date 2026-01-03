"""
11=>R8 => (11+8)%100 = 19 => L19 => (19-19)%100 => 0
5=>L10 => (5-10+100)%100 = 95 => R5 => (95+5)%100 => 0

Number of times dial is left pointing to 0 after any rotation in squence
50
L86 => 50-68+100 %100 => 82
L30 => 82-30 %100 => 52
R48 => 52+48 %100 => 0
L5 => 0-5+100 %100 =>95
"""

def solve():
    ans = 0
    start = 50
    with open("input.txt", "r") as file:
        for line in file:
            direction, rotation = line[0], int(line[1:])
            if direction == 'L':
                start = (start - rotation + 100)%100
            elif direction == 'R':
                start = (start + rotation + 100)%100
            else:
                pass
            
            if start==0:
                ans += 1
    
    return ans

def solve2():
    ans = 0
    start = 50

    with open("input.txt", "r") as file:
        for line in file:
            direction, rotation = line[0], int(line[1:])
            hits = 0
            if direction == 'L':
                hits = max(0, (rotation-start+99)//100)
                start = (start - rotation)%100
            elif direction == 'R':
                hits = max(0, (start + rotation)//100)
                start = (start + rotation)%100
            else:
                pass
            
            ans += hits
            continue
    return ans

if __name__=="__main__":
    # password = solve()
    password = solve2()
    print(password)