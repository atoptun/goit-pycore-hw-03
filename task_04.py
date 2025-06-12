from datetime import datetime, timedelta
from pprint import pprint

def get_upcoming_birthdays(users):
    """Returns a list of users who need to be congratulated during the week."""
    today = datetime.today().date()
    result = []
    for user in users:
        bd = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        try:
            bd = bd.replace(year=today.year)
        except ValueError: 
            bd = bd.replace(year=today.year, day=28)

        if 0 <= (bd - today).days <= 6:
            if (wd := bd.weekday()) > 4:
                bd += timedelta(7 - wd)
            result.append({**user, "congratulation_date": bd.strftime("%Y.%m.%d")})
    
    return result


users = [
    {"name": "John Doe 1", "birthday": "1985.06.10"},
    {"name": "John Doe 2", "birthday": "1985.06.11"},
    {"name": "John Doe 3", "birthday": "1984.02.29"},
    {"name": "Jane Smith 1", "birthday": "1990.06.14"},
    {"name": "Jane Smith 2", "birthday": "1990.06.17"},
    {"name": "Jane Smith 3", "birthday": "1990.01.27"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:")
pprint(upcoming_birthdays, sort_dicts=False)
