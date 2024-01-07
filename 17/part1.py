from collections import defaultdict
import time
from heapq import heappush, heappop
import math

heat_loss_map: list[list[int]] = []

with open('input.txt') as f:
    for line in f:
        heat_loss_map.append(list(int(c) for c in line.strip()))


def within_bounds(y, x):
    return y >= 0 and y < len(heat_loss_map) and x >= 0 and x < len(heat_loss_map[y])


ALL_DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))


def get_reachable_nodes(current_node, max_straight):
    (y, x), came_from_direction, straight_count = current_node
    for dy, dx in ALL_DIRECTIONS:
        if (-dy, -dx) == came_from_direction:
            # you cannot turn back
            continue
        direction_straight_count = straight_count if (
            dy, dx) == came_from_direction else 0
        weight = 0
        for i in range(max_straight - direction_straight_count):
            ny, nx = y + (i+1) * dy, x + (i+1) * dx
            if not within_bounds(ny, nx):
                continue
            weight += heat_loss_map[ny][nx]
            yield (((ny, nx), (dy, dx), direction_straight_count + i + 1), weight)


Graph = dict[int, tuple[int, list[int]]]


def make_graph(start=(0, 0), target=(len(heat_loss_map) - 1, len(heat_loss_map[-1]) - 1), max_straight=3):
    def heuristic(y, x):
        return abs(target[0] - y) + abs(target[1] - x)
    nodes = {(start,): 1, (target,): 0}
    node_seq = 2
    graph: Graph = {0: (0, [])}
    q = [(1, (start, None, 0))]
    while q:
        current_node_id, current_node = q.pop()
        for node, weight in get_reachable_nodes(current_node, max_straight):
            if node[0] == target:
                node_id = 0
            elif node not in nodes:
                node_id = node_seq
                nodes[node] = node_id
                node_seq += 1
                q.append((node_id, node))
            else:
                node_id = nodes[node]

            if current_node_id in graph:
                graph_node = graph[current_node_id]
            else:
                graph_node = (heuristic(*node[0]), [])
                graph[current_node_id] = graph_node
            _, neighbors = graph_node
            neighbors.append((node_id, weight))
    return graph, nodes


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return list(reversed(total_path))


def a_star(graph: Graph, start: int = 1, target: int = 0):
    start_h, _ = graph[start]
    open_set = [(start_h, start)]
    came_from = {}
    g_score = defaultdict(lambda: math.inf)
    g_score[start] = 0
    f_score = defaultdict(lambda: math.inf)
    f_score[start] = start_h
    while open_set:
        _, current_id = heappop(open_set)
        if current_id == target:
            return g_score[target], reconstruct_path(came_from, current_id)
        _, neighbors = graph[current_id]
        for neighbor, weight in neighbors:
            tentative_g_score = g_score[current_id] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_id
                g_score[neighbor] = tentative_g_score
                try:
                    neighbor_f_score = tentative_g_score + graph[neighbor][0]
                except KeyError:
                    print(current_id, neighbor)
                    raise
                f_score[neighbor] = neighbor_f_score
                if not any(n == neighbor for _, n in open_set):  # TODO can we optimize this
                    heappush(open_set, (neighbor_f_score, neighbor))
    raise ValueError('target cannot be reached')


perf = time.perf_counter()

graph, nodes = make_graph()

duration = time.perf_counter() - perf

print(f'nodes={len(graph)}, edges={sum(len(e)
      for _, e in graph.values())}, construction took', duration)

perf = time.perf_counter()
min_cost, path = a_star(graph)
print('Finding minimum cost path took', time.perf_counter() - perf)
print(min_cost)
