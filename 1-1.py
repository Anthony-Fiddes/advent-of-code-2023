import fileinput


def get_calibration_value(line: str):
    first = None
    last = None

    for char in line:
        if char >= "0" and char <= "9":
            first = char
            break
    for char in line[::-1]:
        if char >= "0" and char <= "9":
            last = char
            break

    return int(first + last)


sum = 0
for line in fileinput.input():
    sum += get_calibration_value(line)
print(f"Result: {sum}")
