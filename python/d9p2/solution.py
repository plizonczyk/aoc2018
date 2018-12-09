from collections import defaultdict

class Node:
    def __init__(self, marble, cw=None, ccw=None):
        self.marble = marble
        self.cw = cw
        self.ccw = ccw

    def insert(self, node):  # between 1CW and 2CW
        node.cw = self.cw.cw
        node.ccw = self.cw
        node.ccw.cw = node
        node.cw.ccw = node
    
    def pop(self):  # 7 CCW
        to_remove = self.ccw.ccw.ccw.ccw.ccw.ccw.ccw
        to_remove.ccw.cw = to_remove.cw
        to_remove.cw.ccw = to_remove.ccw
        return to_remove.marble, to_remove.cw

    def __repr__(self):
        return 'CCW: {}, ({}), {}: CW'.format(self.ccw.marble, self.marble, self.cw.marble)


def solve(players, last):
    current_player = 0
    current_marble = 1
    circled_marble = Node(marble=0)
    circled_marble.cw = circled_marble.ccw = circled_marble
    scores = defaultdict(int)

    while current_marble <= last:
        if current_marble % 10000 == 0:
            print('{} of {} ({:.2f}%)'.format(current_marble, last, current_marble*100/last))
        current_player = current_player + 1 if current_player < players else 1
        if current_marble % 23:
            new_node = Node(current_marble)
            circled_marble.insert(new_node)
            circled_marble = new_node
        else:
            popped_marble, circled_marble = circled_marble.pop()
            scores[current_player] += popped_marble + current_marble

        current_marble += 1

    winner = max(scores.values())
    print(winner)
    return winner


assert solve(players=9, last=25) == 32
assert solve(players=10, last=1618) == 8317
assert solve(players=13, last=7999) == 146373
assert solve(players=17, last=1104) == 2764
assert solve(players=21, last=6111) == 54718
assert solve(players=30, last=5807) == 37305
solve(players=447, last=7151000)