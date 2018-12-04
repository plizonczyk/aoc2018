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

most_sleepy_guard = max([(guard_id, sum([t[1]-t[0] for t in times])) for guard_id, times in sleep_times.items()], key=lambda x: x[1])[0]

sleep_pattern = defaultdict(int)
for start_time, end_time in sleep_times[most_sleepy_guard]:
    for i in range(start_time, end_time):
        sleep_pattern[i] += 1

print(int(most_sleepy_guard) * max(sleep_pattern.items(), key=lambda x: x[1])[0])