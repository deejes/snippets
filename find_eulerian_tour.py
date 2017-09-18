# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

a1 = [(1, 2), (2, 3),(4,1), (3, 4)]


def find_eulerian_tour(graph):
    # your code here
    for x in graph:
        if type(x) != tuple:
            return False
    result = []
    link = graph.pop(0)
    result.append(link[0])
    while graph:
        state = False
        for x in graph:
            if x[0] == link[1]:
                link = graph.pop(graph.index(x))
                result.append(x[0])
                state = True
        if not graph:
            result.append(link[1])
        if not state:
            # there is no eulerian path
            return False
    return result

print find_eulerian_tour(a1)
