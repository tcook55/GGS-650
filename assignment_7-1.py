class Node:
    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
# Compare the new value with the parent node
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

# Print tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()

# Insert nodes into binary tree
root = Node(10)
root.insert(4)
root.insert(19)
root.insert(8)
root.insert(7)
root.insert(2)

root.PrintTree()
