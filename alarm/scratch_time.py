from datetime import datetime,timedelta

wake_time = datetime.strptime('20:58', '%H:%M')
wake_time = (wake_time - timedelta(minutes=30)).time()

now = datetime.now()
current_time = now.time()

# Set wake_date to today or tomorrow, depending on current time
wake_tomorrow = wake_time < current_time
wake_date = now.date() + wake_tomorrow * timedelta(days=1)

wake_datetime = datetime.combine(wake_date,wake_time)

print(wake_datetime)