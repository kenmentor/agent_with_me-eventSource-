class Node:
    def __init__ (self,id,value,children_node):
        self.id = id 
        self.value = value 
        self.children_node = children_node
class Graph:
    pass 
graph = Node("a",3,
[
    Node("a",3,
[Node("b",4,
[Node("c",4,
[]
),Node("d",4,
[Node("f",40,
[Node("id",34,[Node("id2",30,[])])])])]
)]),Node("b",4,
[Node("c",4,
[]
),Node("d",4,
[Node("f",40,
[Node("g",34,[Node("h",30,[Node("a",3,
[Node("i",4,
[Node("j",4,
[]
),Node("k",4,
[Node("f",40,
[Node("sk",34,[Node("g",30,[Node("a",3,
[Node("b",4,
[Node("c",4,
[]
),Node("d",4,
[Node("f",40,
[Node("f",34,[Node("id3",30,[Node("a",3,
[Node("b",4,
[Node("c",4,
[]
),Node("d",4,
[Node("f",40,
[Node("3",34,[Node("dd",30,[]),Node("a",3,
[Node("b",4,
[Node("c",4,
[]
),Node("d",4,
[Node("f",40,
[Node("id",34,[Node("id1",30,[])])])])]
)])])])])]
)])])])])])]
)])])])])])]
)])])])])])]
)])


running = True 
stack = [graph]
cost = 0 
goal = "id1"
while running:
    current = stack.pop(-1)
    cost+= 1
    print(current.id)
    for node in current.children_node:
        stack.append(node)
    if current.id == goal or len(stack)== 0 :
        print(cost)
        break 
    