import random

size = 100
test_num = 1000000
change_win_count = 0
unchange_win_count = 0

for test in range(test_num):
    door = [0 for i in range(size)]  # initializing doors
    prize = random.randint(1, size) - 1
    door[prize] = 1  # inserting prize to a random slot
    selection = random.randint(1, size) - 1
    open_door = -1
    while True:
        open_door = random.randint(1, size) - 1
        if open_door != selection and open_door != prize:
            break

    change_door_list = [v for i, v in enumerate(door) if i not in [selection, open_door]]
    change_selection = change_door_list[random.randint(1, len(change_door_list)) - 1]

    if selection == prize:
        unchange_win_count += 1
    if change_selection == 1:
        change_win_count += 1

print(f"change win count = {change_win_count}")
print(f"unchange win count = {unchange_win_count}")