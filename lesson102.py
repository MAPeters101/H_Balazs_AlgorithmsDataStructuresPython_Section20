
class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def breadth_first_search(start_node):

    # FIFO: First item we Insert will be the First on to take Out
    queue = [start_node]
    start_node.visited = True

    # We keep iterating (considering the neighbors) until the queue becomes empty
    while queue:

        # Remove and return the first item we have inserted into the list
        actual_node = queue.pop(0)
        print(actual_node.name)

        # Let's consider the neighbors of the actual_node one by one
        for n in actual_node.adjacency_list:
            if not n.visited:
                n.visited = True
                queue.append(n)


if __name__ == '__main__':

    # We can create the nodes or vertices
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # We have to handle the neighbors
    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    # Run the BFS
    breadth_first_search(node1)
    print('-'*80)

    # We can create the nodes or vertices
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")

    # We have to handle the neighbors
    node1.adjacency_list.append(node2)
    node2.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node3.adjacency_list.append(node4)

    # Run the BFS
    breadth_first_search(node1)
    print('-'*80)


