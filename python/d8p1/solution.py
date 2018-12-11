from functools import reduce

class Node:
    def __init__(self):
        self.children = []
        self.metadata = []

def read_tree(data, index=0):
    children_num = data[index]
    metadata_num = data[index+1]

    index += 2
    tree = Node()

    for _ in range(children_num):
        index, node = read_tree(data, index)
        tree.children.append(node)
   
    for _ in range(metadata_num):
        tree.metadata.append(data[index])
        index += 1
    
    return index, tree


def traverse(tree):
    nodes = [tree]
    for node in tree.children:
        nodes.extend(traverse(node))
    return nodes


def solve(filename):
    with open(filename) as fp:
        data = list(map(int, fp.readline().split(' ')))

    _, tree = read_tree(data)
    return sum(map(lambda x: sum(x.metadata), traverse(tree)))    

assert solve('easy_input') == 138
print(solve('input'))