import sys

brackets = [
    (12500, 0),
    (50000, 20),
    (150000, 40),
    (sys.maxsize, 45)
]


def taxman(income: int):
    tax = 0

    last_bracket = 0
    for bracket, tax_rate in brackets:
        tax += max(min(income - last_bracket, bracket - last_bracket), 0) * (tax_rate / 100)
        last_bracket = bracket

    return tax
