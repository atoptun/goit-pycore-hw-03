from datetime import datetime, timedelta

def get_days_from_today(date: str) -> int | None:
    """Returns the number of days between a date and the current day."""
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - date
        return delta.days
    except ValueError:
        return None
    

assert get_days_from_today(datetime.today().strftime("%Y-%m-%d")) == 0
assert get_days_from_today((datetime.today() - timedelta(days=3)).strftime("%Y-%m-%d")) == 3
assert get_days_from_today((datetime.today() + timedelta(days=3)).strftime("%Y-%m-%d")) == -3
assert get_days_from_today("2023-15-01") == None
