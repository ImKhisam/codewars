def number_followed_by_all_zeros(number):
    return str(number)[0] != '0' and int(str(number)[1::]) == 0


def is_pallindrome(number):
    return str(number) == str(number)[::-1]


def is_awesome(number, awesome_phrases):
    return number in awesome_phrases


def every_digit_is_the_same_number(number):
    return len(set(str(number))) == 1


def sequential_incrementing_digits(number):
    pass


def all_funcs_are_true(number, awesome_phrases):
    return number_followed_by_all_zeros(number) and is_pallindrome(number) and is_awesome(number, awesome_phrases)


def is_interesting(number, awesome_phrases):
    pass


print(sequential_incrementing_digits(516789))

