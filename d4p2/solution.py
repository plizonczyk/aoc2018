from collections import defaultdict
from datetime import datetime

lines = []
with open('input') as fp:
    lines = fp.readlines()

timestamped_events = [(datetime.strptime(line[1:17], '%Y-%m-%d %H:%M'), line[19:].strip()) for line in lines]
timestamped_events.sort()

sleep_times = defaultdict(list)
for event_time, event in timestamped_events:
    if event.startswith('Guard'):
        guard_id = event.split(' ')[1].strip('#')
    elif event == 'falls asleep':
        sleeps_since = event_time.minute
    else:
        sleep_times[guard_id].append((sleeps_since, event_time.minute))

guard_sleep_patterns = dict()
for guard_id, times in sleep_times.items():
    guard_sleep_patterns[guard_id] = defaultdict(int)
    for start_time, end_time in times:
        for i in range(start_time, end_time):
            guard_sleep_patterns[guard_id][i] += 1

most_frequent_sleeping_minutes = {k: max(v.items(), key=lambda x: x[1]) for k, v in guard_sleep_patterns.items()}
result = max(most_frequent_sleeping_minutes.items(), key=lambda x: x[1][1])
print(int(result[0]) * result[1][0])