import sys
from pathlib import Path
from collections import defaultdict
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data
from day05.puzzle_1 import get_rules_and_updates, is_valid

def reorder(rules, update):
    new_update = []
    i = 0
    while len(new_update) < len(update) and i < 100:
        remaining = [u for u in update if u not in new_update]
        for u in remaining:
            if set(set(remaining) - {u}).issubset(set(rules[u])):
                new_update.append(u)
        i += 1
    return new_update

def solve(data):
    rules, updates = get_rules_and_updates(data)
    count=0
    for u in updates:
        if not is_valid(rules, u):
            n=len(u)
            u = reorder(rules, u)
            idx = int(n/2)
            count += int(u[idx])
    return count

def main():
    data = get_days_data(2024, 5)
    print(solve(data))

if __name__ == "__main__":
    main()
    