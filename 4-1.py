import fileinput

sum = 0
for line in fileinput.input():
    numbers_string = line.split(":")[1]
    number_sets = numbers_string.split("|")
    winning_nums_str = number_sets[0].strip()
    winning_nums = {int(x) for x in winning_nums_str.split()}
    card_nums_str = number_sets[1].strip()
    card_nums = {int(x) for x in card_nums_str.split()}

    matching_nums = len(winning_nums & card_nums)
    if matching_nums == 0:
        points = 0
    else:
        points = 2 ** (matching_nums - 1)
    sum += points

print(f"Result: {sum}")
