import sys
from pathlib import Path
from collections import defaultdict
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data

def get_rules_and_updates(data):
    split_data = data.split("\n\n")
    rules_text = split_data[0].split("\n")
    updates_text = split_data[1].split("\n")
    rules = defaultdict(list)
    for rule in rules_text:
        key, value = rule.split("|")
        rules[key].append(value)
    updates = [y.split(",") for y in updates_text if y]
    return rules, updates

def is_valid(rules, update):
    valid = True
    for i, u in enumerate(update):
        before = update[:i-1] if i > 0 else None
        after = update[i+1:] if i < len(update)-1 else None
        if before is not None:
            for b in before:
                if u not in rules[b]:
                    valid = False
                    return valid
        if after is not None:
            for a in after:
                if u in rules[a]:
                    valid = False
                    return valid
    return valid

def solve(data):
    rules, updates = get_rules_and_updates(data)
    count=0
    for u in updates:
        n=len(u)
        if is_valid(rules, u):
            idx = int(n/2)
            count += int(u[idx])
    return count

def main():
    data = get_days_data(2024, 5)
    print(solve(data))


if __name__ == "__main__":
    main()