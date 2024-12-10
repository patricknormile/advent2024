import sys
from pathlib import Path
import re
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data

def data_parse(data):
    rows = data.split("\n")
    data_keys = [int(re.findall("^(\d+): ", x)[0]) for x in rows if x]
    data_numbers = [[*map(int,re.findall(" (\d+)", x))] for x in rows if x]
    return data_keys, data_numbers



def solve_row(answer, numbers):
    add = lambda x, y: x + y
    mult = lambda x, y: x * y
    n = len(numbers)
    for funcchain in permute([add, mult],n-1):
        possible = numbers[0]
        for i in range(1,n):
            possible = funcchain[i-1](possible, numbers[i])
        if answer == possible:
            return True
    return False


def permute(options, n):
    permutations = []
    total = bin(2**n)[2:]
    for i in range(2**(n+1)):
        iteration = []
        binary = bin(i)[2:]
        if len(binary) < len(total):
            binary = "0" * (len(total) - len(binary)) + binary
        for j in binary:
            if j == "1":
                iteration.append(options[1])
            else:
                iteration.append(options[0])
        permutations.append(iteration)
    return permutations
            
def main():
    data = get_days_data(2024, 7)
    parsed = data_parse(data)
    count = 0
    for i, j in zip(*parsed):
        if solve_row(i, j):
            count += i
    print(count)


if __name__ == "__main__":
    main()
    