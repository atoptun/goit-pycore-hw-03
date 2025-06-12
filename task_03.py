import re
from pprint import pprint


pattern_not_digits = re.compile(r"\D")

def normalize_phone(num):
    """Normalize a Ukrainian phone number to the international format"""
    digits = re.sub(pattern_not_digits, "", num)
    digits = digits if digits.startswith("38") else f"38{digits}"
    return f"+{digits}"


raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:")
pprint(sanitized_numbers)

pattern_phone = re.compile(r"^\+\d{8,14}$")
assert all(pattern_phone.match(number) for number in sanitized_numbers)
