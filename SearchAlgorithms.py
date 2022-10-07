from os import TMP_MAX
from tracemalloc import start
from Space import *
from Constants import *


def is_Exist(val: Node, arr: list[Node]):
    for i in range(0, len(arr)):
        if arr[i].value == val.value:
            return True
    return False


""" def BFS(g: Graph, sc: pygame.Surface):
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

    raise NotImplementedError('Not implemented') """


def BFS(g: Graph, sc: pygame.Surface):
    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    start_pos = g.start.value
    goal_pos = g.goal.value
    if len(open_set) == 0:
        return
    while len(open_set) != 0:
        current_Node = open_set.pop()
        g.grid_cells[current_Node].set_color(yellow)
        g.draw(sc)
        closed_set.append(current_Node)
        if g.is_goal(g.grid_cells[current_Node]):
            i = goal_pos
            while i == start_pos:
                temp = father[i]
                i = temp
                father.remove(temp)
                g.grid_cells[neighbors.value].set_color(grey)
                g.draw(sc)
            return
        g.grid_cells[current_Node].set_color(blue)
        g.draw(sc)
        neighbors: Node
        for neighbors in g.get_neighbors(g.grid_cells[current_Node]):
            if neighbors.value not in closed_set:
                if neighbors.value not in open_set:
                    if neighbors.value != g.goal.value:
                        g.grid_cells[neighbors.value].set_color(red)
                        g.draw(sc)
                    open_set.insert(0, neighbors.value)
                    father[neighbors.value] = current_Node
            #pygame.draw.line(sc, grey, i, temp)


""" def DFS(g: Graph, sc: pygame.Surface):
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

    raise NotImplementedError('Not implemented') """


def DFS(g: Graph, sc: pygame.Surface):
    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    start_pos = g.start.value
    goal_pos = g.goal.value
    if len(open_set) == 0:
        return
    while len(open_set) != 0:
        current_Node = open_set.pop()
        g.grid_cells[current_Node].set_color(yellow)
        g.draw(sc)

        if current_Node not in closed_set:
            closed_set.append(current_Node)
            if g.is_goal(g.grid_cells[current_Node]):
                return
            g.grid_cells[current_Node].set_color(blue)
            g.draw(sc)
            neighbors: Node
            for neighbors in g.get_neighbors(g.grid_cells[current_Node]):
                if neighbors.value not in closed_set:
                    if neighbors.value not in open_set:
                        if neighbors.value != g.goal.value:
                            g.grid_cells[neighbors.value].set_color(red)
                            g.draw(sc)
                        open_set.append(neighbors.value)
                        father[neighbors.value] = current_Node


def UCS(g: Graph, sc: pygame.Surface):
    print('Implement UCS algorithm')
    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0
    start_pos = g.start.value
    goal_pos = g.goal.value
    # TODO: Implement UCS algorithm using open_set, closed_set, and father
    while open_set:
        open_set = dict(sorted(open_set.items(), key=lambda x: x[1]))
        first_key = next(iter(open_set))
        current_Node = first_key
        current_Node: Node .set_color(yellow)
        weight = open_set[first_key]
        open_set.pop(first_key)
        if current_Node not in closed_set:
            closed_set.append(current_Node)
            if g.is_goal(g.grid_cells[current_Node]):
                return
            for i in g.get_neighbors(g.grid_cells[current_Node]):
                new_cost = cost[current_Node] + g.get.cost(current_Node, i)
                if i.value not in closed_set or new_cost < cost[current_Node]:
                    cost[i.value] = new_cost
                    open_set[i.value] = new_cost
                    father[i.value] = current_Node

    raise NotImplementedError('Not implemented')


def heuristic(a: Node, b: Node):
    return abs(a.x-b.x) + abs(a.y-b.y)


def AStar(g: Graph, sc: pygame.Surface):
    print('Implement A* algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0
    start_pos = g.start.value
    goal_pos = g.goal.value
    # TODO: Implement UCS algorithm using open_set, closed_set, and father
    while open_set:
        open_set = dict(sorted(open_set.items(), key=lambda x: x[1]))
        first_key = next(iter(open_set))
        current_Node = first_key
        current_Node: Node .set_color(yellow)
        weight = open_set[first_key]
        open_set.pop(first_key)
        if current_Node not in closed_set:
            closed_set.append(current_Node)
            if g.is_goal(g.grid_cells[current_Node]):
                return
            for i in g.get_neighbors(g.grid_cells[current_Node]):
                new_cost = cost[current_Node] + g.get.cost(current_Node, i)
                if i.value not in closed_set or new_cost < cost[current_Node]:
                    cost[i.value] = new_cost
                    open_set[i.value] = new_cost + heuristic(i,g.goal)
                    father[i.value] = current_Node
    raise NotImplementedError('Not implemented')
