import unittest

import SyntaxChecker as sc


class TestSyntaxChecker(unittest.TestCase):

    def test_syntax_check_01(self):
        result = sc.SyntaxChecker().check_syntax("")
        self.assertEqual(result.is_valid, True)

    def test_syntax_check_02(self):
        result = sc.SyntaxChecker().check_syntax("()")
        self.assertEqual(result.is_valid, True)

    def test_syntax_check_03(self):
        result = sc.SyntaxChecker().check_syntax("([])")
        self.assertEqual(result.is_valid, True)

    def test_syntax_check_04(self):
        result = sc.SyntaxChecker().check_syntax("{()()()}")
        self.assertEqual(result.is_valid, True)

    def test_syntax_check_05(self):
        result = sc.SyntaxChecker().check_syntax("<([{}])>")
        self.assertEqual(result.is_valid, True)

    def test_syntax_check_06(self):
        result = sc.SyntaxChecker().check_syntax("[<>({}){}[([])<>]]")
        self.assertEqual(result.is_valid, True)

    def test_syntax_check_07(self):
        result = sc.SyntaxChecker().check_syntax("(((((((((())))))))))")
        self.assertEqual(result.is_valid, True)

    def test_syntax_check_08(self):
        result = sc.SyntaxChecker().check_syntax("(]")
        self.assertEqual(result.is_valid, False)

    def test_syntax_check_09(self):
        result = sc.SyntaxChecker().check_syntax("{()()()>")
        self.assertEqual(result.is_valid, False)

    def test_syntax_check_10(self):
        result = sc.SyntaxChecker().check_syntax("(((()))}")
        self.assertEqual(result.is_valid, False)

    def test_syntax_check_11(self):
        result = sc.SyntaxChecker().check_syntax("<([]){()}[{}])")
        self.assertEqual(result.is_valid, False)

    def test_syntax_check_12(self):
        result = sc.SyntaxChecker().check_syntax("()(")
        self.assertEqual(result.is_valid, False)

    def test_invalid_character_points_01(self):
        result = sc.SyntaxChecker().check_syntax("[)")
        self.assertEqual(result.is_valid, False)
        self.assertEqual(result.invalid_character, ")")
        self.assertEqual(result.invalid_character_points, 3)

    def test_invalid_character_points_02(self):
        result = sc.SyntaxChecker().check_syntax("(]")
        self.assertEqual(result.is_valid, False)
        self.assertEqual(result.invalid_character, "]")
        self.assertEqual(result.invalid_character_points, 57)

    def test_invalid_character_points_03(self):
        result = sc.SyntaxChecker().check_syntax("[}")
        self.assertEqual(result.is_valid, False)
        self.assertEqual(result.invalid_character, "}")
        self.assertEqual(result.invalid_character_points, 1197)

    def test_invalid_character_points_04(self):
        result = sc.SyntaxChecker().check_syntax("[>")
        self.assertEqual(result.is_valid, False)
        self.assertEqual(result.invalid_character, ">")
        self.assertEqual(result.invalid_character_points, 25137)

    def test_syntax_completion_01(self):
        result = sc.SyntaxChecker().check_syntax("[({(<(())[]>[[{[]{<()<>>")
        self.assertEqual(result.is_valid, False)
        self.assertEqual(result.incomplete_syntax_string, "[({([[{{")
        self.assertEqual(result.incomplete_syntax_fix_string, "}}]])})]")
        self.assertEqual(result.incomplete_syntax_fix_points, 288957)

    def test_syntax_completion_02(self):
        result = sc.SyntaxChecker().check_syntax("[(()[<>])]({[<{<<[]>>(")
        self.assertEqual(result.is_valid, False)
        self.assertEqual(result.incomplete_syntax_string, "({[<{(")
        self.assertEqual(result.incomplete_syntax_fix_string, ")}>]})")
        self.assertEqual(result.incomplete_syntax_fix_points, 5566)

    def test_syntax_completion_03(self):
        result = sc.SyntaxChecker().check_syntax("(((({<>}<{<{<>}{[]{[]{}")
        self.assertEqual(result.is_valid, False)
        self.assertEqual(result.incomplete_syntax_string, "((((<{<{{")
        self.assertEqual(result.incomplete_syntax_fix_string, "}}>}>))))")
        self.assertEqual(result.incomplete_syntax_fix_points, 1480781)

    def test_syntax_completion_04(self):
        result = sc.SyntaxChecker().check_syntax("{<[[]]>}<{[{[{[]{()[[[]")
        self.assertEqual(result.is_valid, False)
        self.assertEqual(result.incomplete_syntax_string, "<{[{[{{[[")
        self.assertEqual(result.incomplete_syntax_fix_string, "]]}}]}]}>")
        self.assertEqual(result.incomplete_syntax_fix_points, 995444)

    def test_syntax_completion_05(self):
        result = sc.SyntaxChecker().check_syntax("<{([{{}}[<[[[<>{}]]]>[]]")
        self.assertEqual(result.is_valid, False)
        self.assertEqual(result.incomplete_syntax_string, "<{([")
        self.assertEqual(result.incomplete_syntax_fix_string, "])}>")
        self.assertEqual(result.incomplete_syntax_fix_points, 294)

    def test_syntax_completion_string_01(self):
        result = sc.SyntaxChecker().complete_invalid_syntax_string("[({([[{{")
        self.assertEqual(result, "}}]])})]")

    def test_syntax_completion_string_02(self):
        result = sc.SyntaxChecker().complete_invalid_syntax_string("({[<{(")
        self.assertEqual(result, ")}>]})")

    def test_syntax_completion_string_03(self):
        result = sc.SyntaxChecker().complete_invalid_syntax_string("((((<{<{{")
        self.assertEqual(result, "}}>}>))))")

    def test_syntax_completion_string_04(self):
        result = sc.SyntaxChecker().complete_invalid_syntax_string("<{[{[{{[[")
        self.assertEqual(result, "]]}}]}]}>")

    def test_syntax_completion_string_05(self):
        result = sc.SyntaxChecker().complete_invalid_syntax_string("<{([")
        self.assertEqual(result, "])}>")

    def test_syntax_completion_points_01(self):
        result = sc.SyntaxChecker().calculate_invalid_syntax_points("}}]])})]")
        self.assertEqual(result, 288957)

    def test_syntax_completion_points_02(self):
        result = sc.SyntaxChecker().calculate_invalid_syntax_points(")}>]})")
        self.assertEqual(result, 5566)

    def test_syntax_completion_points_03(self):
        result = sc.SyntaxChecker().calculate_invalid_syntax_points("}}>}>))))")
        self.assertEqual(result, 1480781)

    def test_syntax_completion_points_04(self):
        result = sc.SyntaxChecker().calculate_invalid_syntax_points("]]}}]}]}>")
        self.assertEqual(result, 995444)

    def test_syntax_completion_points_05(self):
        result = sc.SyntaxChecker().calculate_invalid_syntax_points("])}>")
        self.assertEqual(result, 294)


if __name__ == '__main__':
    unittest.main()
