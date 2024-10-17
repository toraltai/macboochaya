from datetime import datetime, timedelta


def is_date_within_2_weeks(input_date_str):
    input_date = datetime.strptime(input_date_str, '%Y-%m-%d')
    current_date = datetime.now()
    three_weeks_ago = current_date - timedelta(weeks=2)
    result = three_weeks_ago.date() <= input_date.date() <= current_date.date()

    return result