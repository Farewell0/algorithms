# 广度优先搜索算法    找出到X的最短路径

from collections import deque

# 想要搜索的目标
def person_is_target(name):
    return name[-1] == "m"          # 随便定的一个条件

def search(name, graph):
    search_queue = deque()          # 创建一个队列
    search_queue += graph[name]
    searched = []                   # 用于记录已经检查过的人的list
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_target(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def main():
    graph = {
            "you":["alice", "bob", "claire"],
            "bob":["anuj", "peggy"],
            "alice":["peggy"],
            "claire":["thom", "jonny"],
            "anuj":[],
            "peggy":[],
            "thom":[],
            "jonny":[]
        }             # 使用散列表的映射创建一个图
    print(search("you", graph))


if __name__ == "__main__":
    main()