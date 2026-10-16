wooden_strips = int(input("Enter the number of wooden strips: "))
total = 0
below_range = 0
in_range = 0
above_range = 0
def classify(value):
    if value < 198:
        return "Below range"
    elif 198 <= value <= 202:
        return "In range"
    else:
        return "Above range"
for i in range(wooden_strips):
    value = int(input("Enter the wooden strips length: "))
    cat = classify(value)
    print(cat)
    total = total + value
    if cat == "Below range":
        below_range += 1
    elif cat == "In range":
        in_range+1=1
    else:
        above_range += 1
def average_cal(total, wooden_strips):
    return total/wooden_strips
print(f"Total length: {total} mm")
print(f"Average length: {average_cal} mm")
print(f"Below range: {below_range}")
print(f"In range: {in_range}")
print(f"Above range: {above_range}")
