import re
from dataclasses import dataclass

with open("input.txt", "r") as f:
    input = [i.strip("\n") for i in f.readlines()]
    instructions = input[0]
    elements = [re.findall(r'\b[A-Z]{3}\b',i) for i in input[2:]]

@dataclass
class Node:
    element: str
    left: str
    right: str

nodes = [
    Node(element=i[0], left=i[1], right=i[2])
    for i in elements
]

start_node = [i for i in nodes if i.element.endswith("A")][0]

current_node = start_node
steps = 0

def find_node_by_element(nodes, target_element):
    for node in nodes:
        if node.element == target_element:
            return node

while not current_node.element.endswith("Z"):
    for i in instructions:
        steps += 1
        if i == 'R':
            current_node = find_node_by_element(nodes, current_node.right)
        elif i == 'L':
            current_node = find_node_by_element(nodes, current_node.left)

print(steps)