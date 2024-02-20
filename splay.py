from bst import Tree

# -1 -> root
#  0 -> left
#  1 -> right


class SplayTree(Tree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        node = super().insert(value)
        if node is not None:
            while node.whichChild() != -1:
                pos = node.whichChild()
                if pos == 1:
                    self.zag(node)

                if pos == 0:
                    self.zig(node)
            # setting up the correct root
            self.root = node
        return node

    def zig(self, y):
        x = y.getParent()
        b = y.getRight()

        y.setParentChild(x.getParent())
        if b is not None:
            b.setParentChild(x)
        else:
            x.setLeft(None)
        x.setParentChild(y)

    def zag(self, y):
        x = y.getParent()
        b = y.getLeft()

        y.setParentChild(x.getParent())
        if b is not None:
            b.setParentChild(x)
        else:
            x.setRight(None)
        x.setParentChild(y)


a = SplayTree()
a.insert(15)
a.insert(10)
a.insert(17)
print(a.getRoot().getValue())
print(a.display())
