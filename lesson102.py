
class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

def breadth_first_search(start_node):

    # FIFO: First item we Insert will be the First on to take Out
    queue = [start_node]

    # We keep iterating (considering the neighbors) until the queue becomes empty
    while queue:

        # Remove and return the first item we have inserted into the list
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)

        # Let's consider the neighbors of the actual_node one by one
        for n in actual_node.adjacency_list:
            if not n.visitied:
                queue.append(n)




