def number_followed_by_all_zeros(number):
    return number > 99 and str(number)[0] != '0' and int(str(number)[1::]) == 0


def is_pallindrome(number):
    return number > 99 and  str(number) == str(number)[::-1]


def is_awesome(number, awesome_phrases):
    return number > 99 and  number in awesome_phrases


def every_digit_is_the_same_number(number):
    return number > 99 and len(set(str(number))) == 1


def sequential_incrementing_digits(number):
    if number > 99:
        for i in range(1, len(str(number))):
            if int(str(number)[i - 1]) != int(str(number)[i]) - 1:
                if int(str(number)[i - 1]) == 9 and int(str(number)[i]) == 0:
                    continue
                return False
        return True
    else:
        return False


def sequential_decrementing_digits(number):
    if number > 99:
        for i in range(1, len(str(number))):
            if int(str(number)[i - 1]) != int(str(number)[i]) + 1:
                if int(str(number)[i - 1]) == 1 and int(str(number)[i]) == 0:
                    continue
                return False
        return True
    else:
        return False


def all_funcs_are_true(number, awesome_phrases):
    return (number_followed_by_all_zeros(number) or is_pallindrome(number) or is_awesome(number, awesome_phrases)
            or every_digit_is_the_same_number(number) or sequential_incrementing_digits(number)
            or sequential_decrementing_digits(number))


def is_interesting(number, awesome_phrases):
    if all_funcs_are_true(number, awesome_phrases):
        return 2
    elif all_funcs_are_true(number + 1, awesome_phrases) or all_funcs_are_true(number + 2, awesome_phrases):
        return 1
    else:
        return 0

print(is_interesting(11209, [1337, 256]))
