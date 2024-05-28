import datetime

def shift_time(days: int, seconds: int):
    base_time = datetime.datetime(2023, 1, 1, 12, 30, 0)
    shifted_time = base_time + datetime.timedelta(days=days, seconds=seconds)
    shifted_day = shifted_time.day
    shifted_second = shifted_time.second
    return shifted_day, shifted_second

days = int(input())
seconds = int(input())
print(shift_time(days, seconds))