class Tree:
    class Node:
        def __init__(self, value=None, parent=None, left=None, right=None):
            self.value = value
            self.parent = parent
            self.left = left
            self.right = right

        def setValue(self, value):
            self.value = value

        def getValue(self):
            return self.value

        def setParent(self, parent):
            self.parent = parent

        def getParent(self):
            return self.parent

        def setLeft(self, left):
            self.left = left

        def getLeft(self):
            return self.left

        def setRight(self, right):
            self.right = right

        def getRight(self):
            return self.right

        def setParentChild(self, parent):
            self.parent = parent
            if parent is not None:
                if self.getValue() > parent.getValue():
                    parent.setRight(self)
                else:
                    parent.setLeft(self)

        def whichChild(self):
            parent = self.parent
            if parent is not None:
                if parent.getRight() == self:
                    return 1
                return 0
            return -1

    def __init__(self):
        self.root = Tree.Node()
        self.size = 0

    def getRoot(self):
        return self.root

    def insert(self, value):
        if self.getRoot().getValue() is None:
            self.getRoot().setValue(value)
            self.size += 1
            return None
        else:
            root = self.getRoot()
            result = self.searchNode(value, root)
            if result.getValue() == value:
                print("Duplicate found, not inserted")
                return None
            else:
                node = Tree.Node(value, result)
                if value > result.getValue():
                    result.setRight(node)
                else:
                    result.setLeft(node)
                self.size += 1
                return node

    def search(self, value):
        root = self.getRoot()
        result = self.searchNode(value, root)
        if result.getValue() == value:
            return result
        return None

    def searchNode(self, value, currentNode):
        if currentNode.getValue() == value:
            return currentNode

        if value > currentNode.getValue():
            if currentNode.getRight() is None:
                return currentNode
            return self.searchNode(value, currentNode.getRight())

        else:
            if currentNode.getLeft() is None:
                return currentNode
            return self.searchNode(value, currentNode.getLeft())

    def searchNodeAnalysis(self, value, currentNode, constantTime=0):
        if currentNode.getValue() == value:
            constantTime += 1
            return constantTime

        if value > currentNode.getValue():
            constantTime += 1
            if currentNode.getRight() is None:
                return constantTime
            return self.searchNodeAnalysis(value, currentNode.getRight(), constantTime)

        else:
            constantTime += 1
            if currentNode.getLeft() is None:
                return constantTime
            return self.searchNodeAnalysis(value, currentNode.getLeft(), constantTime)

    def __str__(self):
        return self.display()

    def display(self):
        content = self.inOrder(self.getRoot())
        result = ""
        for c in content:
            result += str(c) + " "
        return result

    def display2(self):
        content = self.bfs()
        result = ""
        for c in content:
            result += str(c) + " "
        return result

    def inOrder(self, node):
        if node is not None:
            yield from self.inOrder(node.getLeft())
            yield node.getValue()
            yield from self.inOrder(node.getRight())

    def bfs(self):
        queue = [self.getRoot()]
        while len(queue) != 0:
            node = queue[0]
            if node is not None:
                yield node.getValue()
                queue.append(node.getLeft())
                queue.append(node.getRight())
            queue.pop(0)


# import unittest


# class TestTreeTraversal(unittest.TestCase):
#     def testT(self):
#         a = Tree()
#         a.insert(10)
#         a.insert(5)
#         a.insert(15)
#         a.insert(4)
#         a.insert(6)
#         a.insert(14)
#         a.insert(16)

#         self.assertEqual(a.display2(), "10 5 15 4 6 14 16 ")


# print("best case when the tree is balanced")
# a = Tree()
# a.insert(10)
# a.insert(5)
# a.insert(15)
# a.insert(4)
# a.insert(6)
# a.insert(14)
# a.insert(16)
# a.insert(3)
# print(a.searchNodeAnalysis(16, a.getRoot()), a.size)


# print("worst case, when the treee is linear")
# a = Tree()
# a.insert(10)
# a.insert(9)
# a.insert(8)
# a.insert(7)
# a.insert(6)
# a.insert(5)
# a.insert(4)
# a.insert(3)

# print(a.searchNodeAnalysis(3, a.getRoot()), a.size)
