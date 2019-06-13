import sys

brackets = [
    (12500, 0),
    (50000, 20),
    (150000, 40),
    (sys.maxsize, 45)
]


def taxman(income: int, tax_brackets=brackets):
    tax = 0

    last_bracket = 0
    for bracket, tax_rate in tax_brackets:
        tax += tax_for_brakcet(income, last_bracket, bracket, tax_rate)
        last_bracket = bracket

        if income < bracket:
            break

    return tax


def tax_for_brakcet(income, last_bracket, bracket, tax_rate):
    effective_income = income - last_bracket
    tax_bracket = bracket - last_bracket

    taxable_income = max(min(effective_income, tax_bracket), 0)
    return taxable_income * (tax_rate / 100)
