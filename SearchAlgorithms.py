from os import TMP_MAX
from tracemalloc import start
from Space import *
from Constants import *


def is_Exist(val: Node, arr: list[Node]):
    for i in range(0, len(arr)):
        if arr[i].value == val.value:
            return True
    return False


def set_Color_Path(g: Graph, path, sc: pygame.surface):
    g.goal.set_color(grey)
    g.draw(sc)
    prev = g.goal.value
    while prev != g.start.value:
        pygame.draw.line(sc, green, (g.grid_cells[prev].x, g.grid_cells[prev].y), (
            g.grid_cells[path[prev]].x, g.grid_cells[path[prev]].y), 2)
        pygame.display.flip()
        prev = path[prev]
        g.grid_cells[prev].set_color(grey)
        g.draw(sc)


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
        # Thay đổi màu cho nút đang xét
            current_Node.set_color(yellow)
            g.draw(sc)
        # kiểm tra xem tìm thấy node cần tìm chưa
            if g.is_goal(current_Node):
                set_Color_Path(g, father, sc)
                return
        # xóa nút đã kiểm tra
            open_set.remove(current_Node)
        # thêm các nút đã kiểm tra vào closed_set
            closed_set.append(current_Node)
        # Thay đổi màu cho nút đã được kiểm tra
            current_Node.set_color(blue)
            g.draw(sc)
        # thêm các nút được thăm tới vào open_set
            neighbors: list[Node] = g.get_neighbors(current_Node)
            while len(neighbors) != 0:
                if not is_Exist(neighbors[0], closed_set):
                    if not is_Exist(neighbors[0], open_set):
                        if neighbors[0].value != g.goal.value:
                            neighbors[0].set_color(red)
                            g.draw(sc)
                        open_set.append(neighbors[0])
                        father[neighbors[0].value] = current_Node.value

                neighbors.remove(neighbors[0])

    raise NotImplementedError('Not implemented')


""" def BFS(g: Graph, sc: pygame.Surface):
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
            #pygame.draw.line(sc, grey, i, temp) """


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
                set_Color_Path(g, father, sc)
                return
        # xóa nút đã kiểm tra
            open_set.remove(current_Node)
        # thêm các nút đã kiểm tra vào closed_set
            closed_set.append(current_Node)
        # Thay đổi màu cho nút đã được kiểm tra
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
                        father[neighbors[0].value] = current_Node.value
                neighbors.remove(neighbors[0])
            open_set[0:0] = temp

    raise NotImplementedError('Not implemented')


""" def DFS(g: Graph, sc: pygame.Surface):
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
 """


def Min_Cost(g: Graph, open_set: list[Node], cost):
    min = 99999
    result = open_set[0]
    for node in open_set:
        if min > cost[node.value]:
            min = cost[node.value]
            result = node
    print(min)
    return result


def Min_Cost_Heuristic(g: Graph, open_set: list[Node], cost):
    min = 99999
    result = open_set[0]
    for node in open_set:
        if min > cost[node.value] + g.heuristic(node):
            min = cost[node.value] + g.heuristic(node)
            result = node
    return result


def distanceNode(node1: Node, node2: Node):
    return sqrt(pow(node1.x - node2.x, 2) + pow(node1.y - node2.y, 2))


def UCS(g: Graph, sc: pygame.Surface):
    print('Implement UCS algorithm')

    open_set: list[Node] = [g.start]
    closed_set: list[int] = []

    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    if len(open_set) == 0:
        return
    for i in range(0, len(open_set)):
        while len(open_set) != 0:
            current_Node: Node = Min_Cost(g, open_set, cost)
            if current_Node.value != g.start.value:
                current_Node.set_color(yellow)
                g.draw(sc)

            # kiểm tra xem tìm thấy node cần tìm chưa
            if g.is_goal(current_Node):
                set_Color_Path(g, father, sc)
                return

            # xóa nút đã kiểm tra
            open_set.remove(current_Node)
            # thêm các nút đã kiểm tra vào closed_set
            closed_set.append(current_Node)
            # Thay đổi màu cho nút đã được kiểm tra
            current_Node.set_color(blue)
            g.draw(sc)

            # kiểm tra các biên và update cost
            neighbors: list[Node] = g.get_neighbors(current_Node)
            while len(neighbors) != 0:
                if not is_Exist(neighbors[0], closed_set):
                    if not is_Exist(neighbors[0], open_set):
                        if neighbors[0].value != g.goal.value:
                            neighbors[0].set_color(red)
                            g.draw(sc)
                        cost[neighbors[0].value] = cost[current_Node.value] + \
                            distanceNode(current_Node, neighbors[0])
                        open_set.append(neighbors[0])
                        father[neighbors[0].value] = current_Node.value

                neighbors.remove(neighbors[0])

    raise NotImplementedError('Not implemented')


def AStar(g: Graph, sc: pygame.Surface):
    print('Implement A* algorithm')

    open_set: list[Node] = [g.start]
    closed_set: list[int] = []

    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    if len(open_set) == 0:
        return
    for i in range(0, len(open_set)):
        while len(open_set) != 0:
            current_Node: Node = Min_Cost_Heuristic(
                g, open_set, cost)
            if current_Node.value != g.start.value:
                current_Node.set_color(yellow)
                g.draw(sc)

            # kiểm tra xem tìm thấy node cần tìm chưa
            if g.is_goal(current_Node):
                set_Color_Path(g, father, sc)
                return

            # xóa nút đã kiểm tra
            open_set.remove(current_Node)
            # thêm các nút đã kiểm tra vào closed_set
            closed_set.append(current_Node)
            # Thay đổi màu cho nút đã được kiểm tra
            current_Node.set_color(blue)
            g.draw(sc)

            # kiểm tra các biên và update cost
            neighbors: list[Node] = g.get_neighbors(current_Node)
            while len(neighbors) != 0:
                if not is_Exist(neighbors[0], closed_set):
                    if not is_Exist(neighbors[0], open_set):
                        if neighbors[0].value != g.goal.value:
                            neighbors[0].set_color(red)
                            g.draw(sc)
                        cost[neighbors[0].value] = cost[current_Node.value] + \
                            distanceNode(current_Node, neighbors[0])
                        open_set.append(neighbors[0])
                        father[neighbors[0].value] = current_Node.value

                neighbors.remove(neighbors[0])
    raise NotImplementedError('Not implemented')
