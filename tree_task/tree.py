from typing import List

tmp_array = []
tmp = None


class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "[" + str(self.value) + "]"


class Tree:
    def __init__(self):
        self.root = None
        self.height = self.__get_height(self.root)

    def build_from_array(self, array: List[int]):
        n = len(array)
        i = 0
        self.root = self.build(array, self.root, i, n)
        self.height = self.__get_height(self.root)

    def build(self, array: List[int], node: TreeNode, i: int, n: int):
        if i < n and array[i] is not None:
            node = TreeNode(array[i])
            node.left = self.build(array, node.left,
                                   2 * i + 1, n)
            node.right = self.build(array, node.right,
                                    2 * i + 2, n)
        return node

    def inOrder(self, node: TreeNode or None = None, just_started: bool = True):
        global tmp_array
        if just_started and node is None:
            tmp_array = []
            self.inOrder(self.root, False)

        if node is not None:
            self.inOrder(node.left, False)
            tmp_array.append(node.value)
            self.inOrder(node.right, False)
        return tmp_array

    def __get_height(self, node: TreeNode or None):
        if node is None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def print2DUtil(self, node: TreeNode, space: int, spaces_in_print: int):
        if node is None:
            return

        space += spaces_in_print

        self.print2DUtil(node.right, space, spaces_in_print)
        print()
        for i in range(spaces_in_print, space):
            print(end=" ")

        print(node)

        self.print2DUtil(node.left, space, spaces_in_print)

    def print(self, spaces: int = 5):
        self.print2DUtil(self.root, 0, spaces)
        print("\n*******************************************\n")

    def leaves(self, node: TreeNode or None = None, just_started: bool = True):
        global tmp
        if just_started and node is None:
            tmp = 0
            self.leaves(self.root, False)

        if node is not None:
            if node.left is None and node.right is None:
                tmp += 1
            else:
                self.leaves(node.left, False)
                self.leaves(node.right, False)

        return tmp

    def largest_edges_num_in_path(self):
        return max(self.height - 1, 0)

    def __eq_trees(self, node_a: TreeNode, node_b: TreeNode):
        if node_a is None and node_b is None:
            return True

        if node_a is not None and node_b is not None:
            return ((node_a.value == node_b.value) and self.__eq_trees(node_a.left, node_b.left) and
                    self.__eq_trees(node_a.right, node_b.right))

        return False

    def __eq__(self, other):
        return isinstance(other, Tree) and self.__eq_trees(self.root, other.root)