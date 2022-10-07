from tracemalloc import start
from Space import *
from Constants import *


def is_Exist(val: Node, arr: list[Node]):
    for i in range(0, len(arr)):
        if arr[i].value == val.value:
            return True
    return False


def BFS(g: Graph, sc: pygame.Surface):
    print('Implement BFS algorithm')

    open_set: list[Node] = [g.start]
    closed_set: list[Node] = []
    father = [-1]*g.get_len()

    # TODO: Implement BFS algorithm using open_set, closed_set, and father
    if len(open_set) == 0:
        return
    for i in range(0, len(open_set)):
        while len(open_set) != 0:
            current_Node: Node = open_set[i]
            current_Node.set_color(yellow)
            g.draw(sc)
        # kiểm tra xem tìm thấy node cần tìm chưa
            if g.is_goal(current_Node):
                return
        # xóa nút đã kiểm tra
            open_set.remove(current_Node)
        # thêm các nút đã kiểm tra vào closed_set
            closed_set.append(current_Node)

            current_Node.set_color(blue)
            g.draw(sc)
        # thêm cái nút được thăm tới vào open_set
            neighbors: list[Node] = g.get_neighbors(current_Node)
            while len(neighbors) != 0:
                if not is_Exist(neighbors[0], closed_set):
                    if not is_Exist(neighbors[0], open_set):
                        if neighbors[0].value != g.goal.value:
                            neighbors[0].set_color(red)
                            g.draw(sc)
                        open_set.append(neighbors[0])
                neighbors.remove(neighbors[0])

    raise NotImplementedError('Not implemented')


def DFS(g: Graph, sc: pygame.Surface):
    print('Implement DFS algorithm')

    open_set: list[Node] = [g.start]
    closed_set: list[Node] = []
    father = [-1]*g.get_len()

    # TODO: Implement DFS algorithm using open_set, closed_set, and father
    if len(open_set) == 0:
        return
    for i in range(0, len(open_set)):
        while len(open_set) != 0:
            current_Node: Node = open_set[i]
            current_Node.set_color(yellow)
            g.draw(sc)

        # kiểm tra xem tìm thấy node cần tìm chưa
            if g.is_goal(current_Node):
                return
        # xóa nút đã kiểm tra
            open_set.remove(current_Node)
        # thêm các nút đã kiểm tra vào closed_set
            closed_set.append(current_Node)

            current_Node.set_color(blue)
            g.draw(sc)

        # thêm cái nút được thăm tới vào open_set
            neighbors: list[Node] = g.get_neighbors(current_Node)
            temp: list[Node] = []
            while len(neighbors) != 0:
                if not is_Exist(neighbors[0], closed_set):
                    if not is_Exist(neighbors[0], open_set):
                        if neighbors[0].value != g.goal.value:
                            neighbors[0].set_color(red)
                            g.draw(sc)
                        temp.append(neighbors[0])
                neighbors.remove(neighbors[0])
            open_set[0:0] = temp
            
    raise NotImplementedError('Not implemented')


def UCS(g: Graph, sc: pygame.Surface):
    print('Implement UCS algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    # TODO: Implement UCS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')


def AStar(g: Graph, sc: pygame.Surface):
    print('Implement A* algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    # TODO: Implement A* algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')
