# 狄克斯特拉算法    找到加权图中前往X的最短路径(权不能是负的)

# 找出开销最低的节点
def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and cost not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def search(graph, costs, parents):
    processed = []          # 记录处理过的节点
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

def main():
    graph = {
            "start": {"a":6, "b":2},
            "a": {"fin": 1},
            "b": {"a":3, "fin":5},
            "fin": {}
        }               # 创建一个加权图
    infinity = float("inf")     # 代表无穷大
    costs = {
        "a": 6,
        "b": 2,
        "fin": infinity
    }                   # 储存每个节点的开销（从起点出发到该节点的时间）
    parents = {
        "a": "start",
        "b": "start",
        "fin": None
    }                   # 存储父节点的散列表
    # search(graph, costs, parents)
    print(costs)
    print(parents)

if __name__ == "__main__":
    main()

