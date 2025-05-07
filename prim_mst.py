import sys


cities = ["Mersin", "Hatay", "Adana", "Antalya", "Osmaniye", "Maraş"]

city_index = {city: i for i, city in enumerate(cities)}

edges = [
    ("Mersin", "Adana", 70),
    ("Mersin", "Antalya", 480),
    ("Adana", "Osmaniye", 85),
    ("Osmaniye", "Hatay", 90),
    ("Adana", "Maraş", 160),
    ("Maraş", "Hatay", 110),
    ("Antalya", "Maraş", 610),
    ("Osmaniye", "Maraş", 106),
]

INF = float('inf')
n = len(cities)
graph = [[INF] * n for _ in range(n)]
for c1, c2, dist in edges:
    i, j = city_index[c1], city_index[c2]
    graph[i][j] = dist
    graph[j][i] = dist  

def prim_mst(graph):
    num_nodes = len(graph)
    selected = [False] * num_nodes
    selected[0] = True  
    mst_edges = []

    total_cost = 0

    print("Prim Algoritması - Minimum Spanning Tree Sonuçları:\n")
    for _ in range(num_nodes - 1):
        min_cost = INF
        a = b = -1
        for i in range(num_nodes):
            if selected[i]:
                for j in range(num_nodes):
                    if not selected[j] and graph[i][j] < min_cost:
                        min_cost = graph[i][j]
                        a, b = i, j
        if a != -1 and b != -1:
            print(f"{cities[a]} -- {cities[b]} : {graph[a][b]} km")
            mst_edges.append((cities[a], cities[b], graph[a][b]))
            total_cost += graph[a][b]
            selected[b] = True

    print(f"\nToplam MST maliyeti: {total_cost} km")
    return mst_edges, total_cost

if __name__ == "__main__":
    prim_mst(graph)
