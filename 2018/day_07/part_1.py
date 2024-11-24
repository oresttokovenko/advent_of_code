# part 1

from pathlib import Path
from collections.abc import Sequence

p = Path('input.txt').read_text().rstrip().split('\n')
p = [tuple(filter(str.isupper, i.lstrip('S'))) for i in p]
print(p)

def topological_sort(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next_node in graph[start]:
        if next_node not in visited:
            topological_sort(graph, next_node, visited)
    return visited
    
if __name__ == "__main__":
    ...
    result = topological_sort(graph=p, start='X')
    print(result)
