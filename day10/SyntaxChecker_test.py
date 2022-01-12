import SyntaxResult as sr
import SyntaxChecker as sc
import unittest


class TestSyntaxChecker(unittest.TestCase):

    def test_case01(self):
        checkResult = sc.SyntaxChecker().check_syntax("")
        self.assertEqual(checkResult.is_valid, True)

    def test_case02(self):
        checkResult = sc.SyntaxChecker().check_syntax("()")
        self.assertEqual(checkResult.is_valid, True)

    def test_case03(self):
        checkResult = sc.SyntaxChecker().check_syntax("([])")
        self.assertEqual(checkResult.is_valid, True)

    def test_case04(self):
        checkResult = sc.SyntaxChecker().check_syntax("{()()()}")
        self.assertEqual(checkResult.is_valid, True)

    def test_case05(self):
        checkResult = sc.SyntaxChecker().check_syntax("<([{}])>")
        self.assertEqual(checkResult.is_valid, True)

    def test_case06(self):
        checkResult = sc.SyntaxChecker().check_syntax("[<>({}){}[([])<>]]")
        self.assertEqual(checkResult.is_valid, True)

    def test_case07(self):
        checkResult = sc.SyntaxChecker().check_syntax("(((((((((())))))))))")
        self.assertEqual(checkResult.is_valid, True)

    def test_case08(self):
        checkResult = sc.SyntaxChecker().check_syntax("(]")
        self.assertEqual(checkResult.is_valid, False)

    def test_case09(self):
        checkResult = sc.SyntaxChecker().check_syntax("{()()()>")
        self.assertEqual(checkResult.is_valid, False)

    def test_case10(self):
        checkResult = sc.SyntaxChecker().check_syntax("(((()))}")
        self.assertEqual(checkResult.is_valid, False)

    def test_case11(self):
        checkResult = sc.SyntaxChecker().check_syntax("<([]){()}[{}])")
        self.assertEqual(checkResult.is_valid, False)

    def test_case12(self):
        checkResult = sc.SyntaxChecker().check_syntax("()(")
        self.assertEqual(checkResult.is_valid, False)

    def test_case13(self):
        checkResult = sc.SyntaxChecker().check_syntax("[)")
        self.assertEqual(checkResult.is_valid, False)
        self.assertEqual(checkResult.invalid_character, ")")
        self.assertEqual(checkResult.invalid_character_points, 3)

    def test_case14(self):
        checkResult = sc.SyntaxChecker().check_syntax("(]")
        self.assertEqual(checkResult.is_valid, False)
        self.assertEqual(checkResult.invalid_character, "]")
        self.assertEqual(checkResult.invalid_character_points, 57)

    def test_case15(self):
        checkResult = sc.SyntaxChecker().check_syntax("[}")
        self.assertEqual(checkResult.is_valid, False)
        self.assertEqual(checkResult.invalid_character, "}")
        self.assertEqual(checkResult.invalid_character_points, 1197)

    def test_case16(self):
        checkResult = sc.SyntaxChecker().check_syntax("[>")
        self.assertEqual(checkResult.is_valid, False)
        self.assertEqual(checkResult.invalid_character, ">")
        self.assertEqual(checkResult.invalid_character_points, 25137)


if __name__ == '__main__':
    unittest.main()