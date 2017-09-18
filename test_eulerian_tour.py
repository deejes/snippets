from find_eulerian_tour import find_eulerian_tour

a1 = [(1, 2), (2, 3),(4,1), (3, 4)]
a2 = [(1,2),(3,4)]
a3 = ['a',(4,5)]
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert find_eulerian_tour(a1) == [1,2,3,4,1]
    assert find_eulerian_tour(a2) == False
    assert find_eulerian_tour(a3) == False
