import itertools

def solve():
    # Open file line by line
    columns = []
    with open('input.csv') as f:
        for line in f:
            row = list(filter(None, line.split()))
            if not columns:
                # initialize columns lists
                columns = [[] for _ in row]
            for i, val in enumerate(row):
                columns[i].append(val)

    ans = 0
    for col in columns:
        # Last item is operator
        *numbers, op = col
        # Convert numbers to integers
        numbers = list(map(int, numbers))
        
        # Apply operator
        if op == '*':
            result = 1
            for n in numbers:
                result *= n
        elif op == '+':
            result = sum(numbers)
        else:
            result = None  # handle unexpected operator
        
        if result:
            ans += result
    
    return ans



if __name__=="__main__":
    ans = solve()
    print(ans)