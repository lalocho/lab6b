import time
from queue import Queue
from GraphAM import GraphAM
from GraphAL import GraphAL,DisjointSetForest

# prints a minimal spanning tree for a directed graph
def topological_sort(graph):
    start_time = time.clock()
    all_in_degrees = []
    sort_result = []
     # q = Queue()
    for i in range(GraphAL.get_num_vertices(graph)):
        all_in_degrees.append(GraphAL.get_vertex_in_degree(graph, i))
    # print(all_in_degrees)
    q = Queue()
    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.put(i)

    while not q.empty():
        u = q.get()
        sort_result.append(u)
        for adj_vertex in range(len(graph.adj_list)):
            all_in_degrees[adj_vertex] -= 1
            if all_in_degrees[adj_vertex] == 0:
                q.put(adj_vertex)
    print(time.clock() - start_time, "seconds")
    if len(sort_result) != graph.get_num_vertices():
        return None
    print(sort_result)

def is_cycle(num_vertices,mst):
    if len(mst)< 2:
        return True
    visited = DisjointSetForest(num_vertices)



    for i in range(len(mst)):

        visited.union(mst[i][0],mst[i][1])
        print(visited.get_num_of_sets())
    if visited.get_num_of_sets() != 1:
        return True
    return False

# creates minimum spanning tree of an input graph
def kruskalls(graph):
    start_time = time.clock()
    # edges = sorted(graph.adj_list, key=lambda x: x.weight, reverse=False)

    if graph.adj_list is None:
        return None
    edges = list()
    for i in range(len(graph.adj_list)):
        tmp = graph.adj_list[i]
        while tmp is not None:
            edges.append([i,tmp.item,tmp.weight])
            tmp = tmp.next
    # print(edges)
    edges.sort(key=lambda tup: tup[2])
    print(edges)
    mst = []
    visited = [False] * graph.get_num_vertices()
    for edge in edges:
        print(visited)
        print(mst)

        # print(edge[0])
        # print(edge[1])
        if not visited[edge[0]] and not visited[edge[1]] :
            mst.append(edge)
            visited[edge[0]] = True
            visited[edge[1]] = True
        elif visited[edge[0]] and not visited[edge[1]]:
            mst.append(edge)
            visited[edge[1]] = True
        elif not visited[edge[0]] and visited[edge[1]]:
            visited[edge[0]] = True
            mst.append(edge)
        if  not is_cycle(graph.get_num_vertices(),mst):
            print("finta madre")
            print(mst)
            print(time.clock() - start_time, "seconds")
            return
    print(time.clock() - start_time, "seconds")




def main():
    graph = GraphAL(initial_num_vertices=6, is_directed=True)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)

    graph.add_edge(2, 3)
    graph.add_edge(4, 5)
    graph.add_edge(5, 2)

    graph.add_edge(5, 3)

    graph2 = GraphAL(initial_num_vertices=6, is_directed=True)
    graph2.add_edge(0, 1, 1)
    graph2.add_edge(0, 4, 21)
    graph2.add_edge(1, 2, 3)

    graph2.add_edge(2, 3, 13)
    graph2.add_edge(4, 5, 4)
    graph2.add_edge(5, 2, 15)

    graph2.add_edge(5, 3, 6)

    graph2.add_edge(1, 3, 7)
    graph2.add_edge(1, 4, 9)
    graph2.add_edge(1, 5, 10)
    graph2.add_edge(0, 3, 14)

    topological_sort(graph)
    kruskalls(graph2)

main()
