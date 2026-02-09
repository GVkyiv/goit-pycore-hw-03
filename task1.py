from datetime import datetime, date

def get_days_from_today(date_str: str) -> int:
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        return (date.today() - given_date).days
    except ValueError:
        raise ValueError("Неправильный формат. Нужно YYYY-MM-DD, например 2020-10-09")

user_input = input("Введи дату (YYYY-MM-DD): ")

try:
    print(get_days_from_today(user_input))
except ValueError as e:
    print(e)

