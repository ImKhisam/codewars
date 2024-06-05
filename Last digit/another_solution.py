def last_digit(a, b):
    return ((a % 10) ** ((b - 1) % 4 + 1)) % 10 if b else 1