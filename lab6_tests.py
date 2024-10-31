import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input1 = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input1, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input2 = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input2, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input3 = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input3, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input4 = []
        expected = None
        actual = lab6.index_smallest_from(input4, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input5 = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input5)
        self.assertEqual(expected, input5)


    def test_selection_sort_2(self):
        input6 = []
        expected = []
        lab6.selection_sort(input6)
        self.assertEqual(expected, input6)


    def test_selection_sort_3(self):
        input7 = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input7)
        self.assertEqual(expected, input7)


    def test_selection_sort_4(self):
        input8 = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input8)
        self.assertEqual(expected, input8)


    # Part 1
    def test_books(self):
        books = []
        lab6.selection_sort_books(books)
        assert books == []

    def test_books2(self):
        books = [
            data.Book(["J.K. Rowling"], "Harry Potter"),
            data.Book(["Camille Abetong"], "Apple Berry"),
            data.Book(["Diego Rodriguez"], "Juicy Juggle")
        ]
        lab6.selection_sort_books(books)
        assert books == [
            data.Book(["Camille Abetong"], "Apple Berry"),
            data.Book(["J.K. Rowling"], "Harry Potter"),
            data.Book(["Diego Rodriguez"], "Juicy Juggle")
        ]
    # Part 2
    def test_swap(self):
        # Test case 1: Basic mixed case
        input_str = "Camille Abetong"
        expected = "cAMILLE aBETONG"
        assert lab6.swap_case(input_str) == expected

    def test_swap2(self):
        input_str = "DiEgO"
        expected = "dIeGo"
        assert lab6.swap_case(input_str) == expected

    # Part 3
    def test_translate(self):
        input_str = "abcdcba"
        expected = "ebcdcbe"
        assert lab6.str_translate(input_str, 'a', 'e') == expected

    def test_translate2(self):
        input_str = "camille abetong"
        expected = "camille abetong"
        assert lab6.str_translate(input_str, 'x', 'y') == expected

    # Part 4
    def test_histogram(self):
        input_str = "camille diego camille diego camille camille camille diego"
        expected = {"camille": 5, "diego": 3}
        assert lab6.histogram(input_str) == expected

    def test_histogram2(self):
        input_str = "hi love hi hi love love love love love yay"
        expected = {"hi": 3, "love": 6, "yay": 1}
        assert lab6.histogram(input_str) == expected




if __name__ == '__main__':
    unittest.main()
