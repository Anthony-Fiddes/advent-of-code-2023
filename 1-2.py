import fileinput


def get_calibration_value(line: str):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    values = {digit: str(digits.index(digit) + 1) for digit in digits}
    lfinds = {digit: -1 for digit in digits}
    rfinds = {digit: -1 for digit in digits}
    left_most_digit = ""
    left_most_index = -1
    right_most_digit = ""
    right_most_index = -1
    for digit in digits:
        lfind = line.find(digit)
        lfinds[digit] = lfind
        if lfind != -1:
            if left_most_index == -1 or lfind < left_most_index:
                left_most_index = lfind
                left_most_digit = digit

        rfind = line.rfind(digit)
        rfinds[digit] = rfind
        if rfind != -1:
            if right_most_index == -1 or rfind > right_most_index:
                right_most_index = rfind
                right_most_digit = digit

    # Replace only the outer most digit strings
    if left_most_index != -1:
        # I didn't read the problem properly when first designing this. A line like "oneight" should
        # produce 18. By replacing "one" here with "1one", make it so that our
        # part 1 code works again.
        line = line.replace(
            left_most_digit, values[left_most_digit] + left_most_digit, 1
        )
        right_most_index = line.rfind(right_most_digit)
    if right_most_index != -1:
        line = line[0:right_most_index] + line[right_most_index:].replace(
            right_most_digit, values[right_most_digit], 1
        )

    for i, digit in enumerate(digits):
        val = i + 1
        line = line.replace(digit, str(val))

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
