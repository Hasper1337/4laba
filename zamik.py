import random


def unique_values():
    seen = set()

    def add(value):
        if value not in seen:
            seen.add(value)
            return True
        else:
            return False

    return add


unique = unique_values()
unique_values_list = []
for i in range(10):
    value = random.randint(1, 10)
    if unique(value):
        unique_values_list.append(value)

print(unique_values_list)
