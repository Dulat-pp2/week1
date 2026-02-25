from datetime import datetime, timedelta

#1
today = datetime.now()
five_days_ago = today - timedelta(days=5)

print(five_days_ago)

#2
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(today)
print(yesterday)
print(tomorrow)

#3
now = datetime.now()
no_micro = now.replace(microsecond=0)

print(no_micro)

#4
d1 = input()
d2 = input()

t1 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
t2 = datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")

diff = abs((t2 - t1).total_seconds())

print(int(diff))