import unittest
from tree import Tree


class TestLonelyNodes(unittest.TestCase):

    def test_empty_tree_should_give_1(self):
        tree = Tree()
        self.assertEqual(1, tree)

    def test_should_give_5(self):
        tree1 = Tree()
        tree1.build_from_array(
            [5, 3, 7, 2, 5, 1, 0, None, None, None, None, None, None, 2, 8, None, None, None, None, None, None, None,
             None,
             None, None, None, None, None, None, None, 5])

        self.assertEqual(5, tree1.leaves())


class TestLargestNumberOfEdgesInPath(unittest.TestCase):

    def test_empty_tree_should_give_0(self):
        tree1 = Tree()

        self.assertEqual(0, tree1.largest_edges_num_in_path())

    def test_should_give_4(self):
        tree1 = Tree()
        tree1.build_from_array(
            [5, 3, 7, 2, 5, 1, 0, None, None, None, None, None, None, 2, 8, None, None, None, None, None, None, None,
             None,
             None, None, None, None, None, None, None, 5])

        self.assertEqual(4, tree1.largest_edges_num_in_path())


class TestEquals(unittest.TestCase):

    def test_empty_trees_should_equal(self):
        tree1 = Tree()
        tree2 = Tree()
        self.assertTrue(tree1 == tree2)

    def test_equal_trees_should_give_true(self):
        tree1 = Tree()
        tree1.build_from_array(
            [5, 3, 7, 2, 5, 1, 0, None, None, None, None, None, None, 2, 8, None, None, None, None, None, None, None,
             None,
             None, None, None, None, None, None, None, 5])

        tree2 = Tree()
        tree2.build_from_array(
            [5, 3, 7, 2, 5, 1, 0, None, None, None, None, None, None, 2, 8, None, None, None, None, None, None, None,
             None,
             None, None, None, None, None, None, None, 5])

        self.assertTrue(tree1 == tree2)

    def test_same_values_but_different_tree_should_give_false(self):
        tree1 = Tree()
        tree1.build_from_array(
            [5, 3, 7, 2, 5, 1, 0, 2, 8, 5])

        tree2 = Tree()
        tree2.build_from_array(
            [5, 3, 7, 2, 5, 1, 0, None, None, None, None, None, None, 2, 8, None, None, None, None, None, None, None,
             None,
             None, None, None, None, None, None, None, 5])

        self.assertFalse(tree1 == tree2)

    def test_same_length_different_values_should_give_false(self):
        tree1 = Tree()
        tree1.build_from_array(
            [5, 3, 7, 2, 5, 1, 0, None, None, 1, 2, None, None, 2, 8, None, None, 2, None, None, None, None,
             None,
             None, None, 3, None, None, 1, None, 5])

        tree2 = Tree()
        tree2.build_from_array(
            [5, 3, 7, 2, 5, 1, 0, None, None, None, None, None, None, 2, 8, None, None, None, None, None, None, None,
             None,
             None, None, None, None, None, None, None, 5])

        self.assertFalse(tree1 == tree2)

    def test_tree_compared_to_other_object_should_give_false(self):
        tree1 = Tree()
        self.assertFalse(tree1 == [])


if __name__ == '__main__':
    unittest.main()
