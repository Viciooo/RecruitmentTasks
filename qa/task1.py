import string
import unittest


def tested_function(s: string):
    start = 0
    result = 0

    while start - result != len(s):
        i = start
        memo = []
        while i < len(s) and s[i] not in memo:
            memo.append(s[i])
            i += 1
        result = max(i - start, result)
        start += 1

    return result


class TestLongestSubstringFunction(unittest.TestCase):
    def test_empty_string_should_give_0(self):
        self.assertEqual(0, tested_function(''))

    def test_single_char_should_give_1(self):
        self.assertEqual(1, tested_function('a'))

    def test_set_best_on_second_try(self):
        self.assertEqual(4, tested_function('abcbadab'))

    def test_whole_string_should_be_best_substring(self):
        self.assertEqual(6, tested_function('abcdef'))
