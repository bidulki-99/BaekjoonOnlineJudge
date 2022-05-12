import sys
input = sys.stdin.readline

import heapq

V, E = map(int, input().split())
K = int(input())
graph = {}
for i in range(V):
    graph[i+1] = {}

for i in range(E):
    u, v, w = map(int, input().split())
    if v not in graph[u]:
        graph[u][v] = w
    else:
        graph[u][v] = min(w, graph[u][v])

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = []
    heapq.heappush(heap, [dist[start], start])

    while heap:
        cur_dist, cur_dest = heapq.heappop(heap)

        if dist[cur_dest] < cur_dist:
            continue

        for new_dest, new_dist in graph[cur_dest].items():
            temp = cur_dist + new_dist
            if temp < dist[new_dest]:
                dist[new_dest] = temp
                heapq.heappush(heap, [temp, new_dest])

    return dist

for key, val in sorted(dijkstra(graph, K).items()):
    if val == float('inf'):
        print('INF')
        continue
    print(val)
