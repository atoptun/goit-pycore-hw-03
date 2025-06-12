import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """Returns a list of random unique integers"""
    if min < 1 or max > 1000 or min >= max or quantity <= 0 or quantity > max - min:
        return []
    numbers = []
    while len(numbers) < quantity:
        number = random.randint(min, max)
        if number not in numbers:
            numbers.append(number)
        
    numbers.sort()
    return numbers


numbers = get_numbers_ticket(1, 49, 6)
print(numbers)
assert len(numbers) == 6 and min(numbers) >= 1 and max(numbers) <= 49

numbers = get_numbers_ticket(1, 36, 5)
print(numbers)
assert len(numbers) == 5 and min(numbers) >= 1 and max(numbers) <= 36

assert len(get_numbers_ticket(0, 1000, 5)) == 0
assert len(get_numbers_ticket(1, 2000, 5)) == 0
assert len(get_numbers_ticket(1, 10, 15)) == 0
assert len(get_numbers_ticket(1, 10, 0)) == 0







