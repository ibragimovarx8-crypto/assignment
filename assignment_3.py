def replace_value(values, index, new_value):
    values[index] = new_value

def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def summarize(values):
    return min(values), max(values), sum(values)

days = int(input("Enter number of days: "))

original = []

for i in range(days):
    value = int(input("Enter a value: "))
    original.append(value)

updated = original[:]

index = int(input("Enter index to replace: "))
new_value = int(input("Enter new value: "))

replace_value(updated, index, new_value)

target = int(input("Enter target value: "))

first_index = find_first(updated, target)
matching_values = updated.count(target)

minimum, maximum, total = summarize(updated)

sorted_values = sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_values}")
print(f"Minimum number of puzzles: {minimum}")
print(f"Maximum number of puzzles: {maximum}")
print(f"Total number of puzzles: {total}")

if first_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {first_index}")

print(f"Matching values: {matching_values}")
