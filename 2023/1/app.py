# find first digit from left
# find last digit from right
# if only one digit, use it twice
# concat the two digits together e.g. 7 and 7 is 77
# find the total of all numbers

from codes import codes
from digits import digits


def convert_word_to_digit(word: str) -> str:
    match word:
        case 'one':
            return '1'
        case 'two':
            return '2'
        case 'three':
            return '3'
        case 'four':
            return '4'
        case 'five':
            return '5'
        case 'six':
            return '6'
        case 'seven':
            return '7'
        case 'eight':
            return '8'
        case 'nine':
            return '9'
        case _:
            return word


def main():
    total = 0

    for code in codes:
        digit_indexes = {digit: code.find(digit) for digit in digits}
        filtered_values = {key: value for key, value in digit_indexes.items() if value != -1}

        max_digit = max(filtered_values, key=filtered_values.get)
        min_digit = min(filtered_values, key=filtered_values.get)

        first_digit = convert_word_to_digit(min_digit)
        last_digit = convert_word_to_digit(max_digit)

        concat_digits = f'{first_digit}{last_digit}'
        total += int(concat_digits)

    print(total)

if __name__ == '__main__':
    main()
