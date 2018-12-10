from queue import Queue
from Graphs.GraphAM import GraphAM
from Graphs.GraphAL import GraphAL


def breath_first_search(graph, start_node):
    visited_order = []
    visited = [False] * graph.get_num_vertices()
    path = [-1] * graph.get_num_vertices()

    q = Queue()
    q.put(start_node)
    visited[start_node] = True
    visited_order.append(start_node)

    while not q.empty():
        u = q.get()
        for adj_vertex in graph.get_vertices_reachable_from(u):
            if not visited[adj_vertex]:
                visited[adj_vertex] = True
                visited_order.append(adj_vertex)
                path[adj_vertex] = u
                q.put(adj_vertex)

    return path, visited_order


def depth_first_search(graph, start_node):
    visited_order = []
    visited = [False] * graph.get_num_vertices()
    path = [-1] * graph.get_num_vertices()

    stack = []  # A list can be used as a stack

    stack.append(start_node)

    while len(stack) > 0:
        u = stack.pop()

        if not visited[u]:
            visited[u] = True
            visited_order.append(u)

            for adj_vertex in graph.get_vertices_reachable_from(u):
                if not visited[adj_vertex]:
                    path[adj_vertex] = u
                    stack.append(adj_vertex)

    return path, visited_order


graph = GraphAL(initial_num_vertices=11, is_directed=True)
graph = GraphAM(initial_num_vertices=11, is_directed=True)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)

graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)

graph.add_edge(4, 7)
graph.add_edge(5, 8)
graph.add_edge(6, 9)

graph.add_edge(7, 10)
graph.add_edge(8, 10)
graph.add_edge(9, 10)


#   /--> 1 -> 4 -> 7 -\
#  /                   \
# 0 -> 2 -> 5 -> 8------> 10
#  \                  /
#  \--> 3 -> 6 -> 9--/

path, visited_order = depth_first_search(graph, 0)
print("DFS: ", visited_order)

path, visited_order = breath_first_search(graph, 0)
print("BFS: ", visited_order)
