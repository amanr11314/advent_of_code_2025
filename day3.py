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

def solve2():
    ans = 0
    n = 12
    
    def maxmimum_subsequence_greedy(s: str, n:int):
        drop = len(s)-n
        st = []
        for d in s:
            # pop stack digit if curr digit > stack.top() and can_drop(drop>0)
            while drop and st and st[-1] < d:
                st.pop()
                drop -= 1
            st.append(d)
        
        return int("".join(st[:n]))
    
    with open("input.txt", "r") as file:
        for line in file:
            batteries = line.strip()
            curr = maxmimum_subsequence_greedy(batteries, n)
            ans += curr

    return ans

if __name__=="__main__":
    # total_output_joltage = solve()
    total_output_joltage = solve2()
    print(total_output_joltage)
    


