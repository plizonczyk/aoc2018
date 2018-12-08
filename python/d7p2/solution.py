from collections import defaultdict
from functools import reduce


def find_available(graph):
    return sorted(list(set(graph.keys()) - reduce(lambda x, y: x | y, graph.values())))

def read_graph(filename):
    graph = defaultdict(set)
    with open(filename) as fp:
        for line in fp.readlines():
            graph[line[5]].add(line[36])
            if not line[36] in graph:
                graph[line[36]] = set()
    return graph

def find_tasks_and_times(graph, workers):
    available = find_available(graph)
    for task in workers:
        if task in available:
            available.remove(task)

    return [(task, ord(task) - ord('A')) for task in available]

def solve(filename, num_workers, step_base):
    time = 0
    workers = dict()  # task name: time to finish
    graph = read_graph(filename)
    result = ''

    while graph or workers:
        tasks = find_tasks_and_times(graph, workers)
        while len(workers) < num_workers and tasks:
            task, task_time = tasks.pop(0)
            workers[task] = task_time + step_base

        finished, time_lapsed = min(workers.items(), key=lambda x: x[1])

        time += time_lapsed
        del workers[finished]
        del graph[finished]
        result += finished
        for worker in workers.keys():
            workers[worker] -= time_lapsed

    print(result, time)
    return result, time

assert solve('easy_input', num_workers=2, step_base=1) == ('CABFDE', 15)
solve('input', num_workers=5, step_base=61)