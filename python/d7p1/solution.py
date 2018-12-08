from collections import defaultdict
from functools import reduce


def find_available(graph):
    return sorted(list(set(graph.keys()) - reduce(lambda x, y: x | y, graph.values())))


def solve(filename):
    graph = defaultdict(set)
    with open(filename) as fp:
        for line in fp.readlines():
            graph[line[5]].add(line[36])
            if not line[36] in graph:
                graph[line[36]] = set()

    result = ''
    while graph:
        available = find_available(graph)
        del graph[available[0]]
        result += available[0]

    print(result)
    return result

assert solve('easy_input') == 'CABDFE'
solve('input')