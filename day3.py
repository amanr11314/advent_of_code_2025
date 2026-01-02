from collections import defaultdict

def solve():
    ans = 0
    with open("input.txt", "r") as file:
        for line in file:
            batteries = line.strip()
            
            max_power_1 = max(int(b) for b in batteries[:-1])

            l_idx = batteries.index(str(max_power_1))
            
            max_power_r = max(int(b) for b in batteries[1+l_idx:])
            
            maximum_joltage = max_power_1*10 + max_power_r

            ans += maximum_joltage
    return ans

if __name__=="__main__":
    total_output_joltage = solve()
    print(total_output_joltage)
    


