def isinvaid_number_in_range(num:int, l:int, r:int):
    return l<=num<=r

def solve():
    ans = 0
    # invalid_ids = []
    with open("input.txt", "r") as file:
        for line in file:
            for input_range in line.split(','):
                l, r = input_range.split("-")

                # generate all invalid numbers in range [l,r]
                # generate numbers with digits upto [1, no_of_diigts(r)]
                # then concatenante the generated number to form a repeating sequence
                # just check if thhis generated number sequence lies in range [l,r] => invalid_id

                max_n = len(r)
                for n_digit in range(1, max_n//2 + 1):
                    start = 10**(n_digit-1)
                    end = 10**n_digit - 1

                    # generate n_digit numbers between start-end
                    for rep_num in range(start, end+1):
                        num = int(f"{rep_num}{rep_num}")
                        if isinvaid_number_in_range(num, int(l), int(r)):
                            # invalid_ids.append(num)
                            ans = ans + num

    return ans

if __name__=="__main__":
    invalid_ids_sum = solve()
    print(invalid_ids_sum)
    


