from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    queue_search = deque()
    queue_search += [name]
    searched = set()
    while queue_search:
        person = queue_search.popleft()
        if person in searched:
            continue
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        queue_search += graph[person]
        searched.add(person)
    return False


search("you")
