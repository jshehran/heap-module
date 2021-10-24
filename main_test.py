from main import merge
import unittest

class MergeHeapTestCase(unittest.TestCase):
    """merge_heap unit tests"""

    def test_merge_no_input(self):
        actual = list(merge())
        expected = []
        self.assertEqual(expected, actual)

    def test_merge_empty_iterable(self):
        input1 = []
        actual = list(merge(input1))
        expected = []
        self.assertEqual(expected, actual)

    def test_merge_one_nonempty_iterable(self):
        input_nonempty = range(8)
        actual = list(merge(input_nonempty))
        expected=list(input_nonempty)
        self.assertEqual(expected, actual)

    def test_merge_iterables_of_different_size(self):
        input_range1 = range(100)
        input_range2 = range(-10, 1000)
        input_range3 = range(8, 30000)
        actual = list(merge(input_range1, input_range2, input_range3))
        expected=sorted(list(input_range1) + list(input_range2) + list(input_range3))
        self.assertEqual(expected, actual)

    def test_from_example_test_data(self):
        # Given three input iterables
        input1 = [1, 5, 9]
        input2 = [2, 5]
        input3 = [1, 6, 10, 11]
        actual = list(merge(input1, input2, input3))
        expected = [1, 1, 2, 5, 5, 6, 9, 10, 11]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()