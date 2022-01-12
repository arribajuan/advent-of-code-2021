class SyntaxResult:
    is_valid = False
    invalid_character = ""
    invalid_character_points = 0
    incomplete_syntax_string = ""
    incomplete_syntax_fix_string = ""
    incomplete_syntax_fix_points = 0
    text_to_check = ""

    def __init__(self):
        pass

    def __str__(self):
        result = "Syntax check result\n"
        result += f" - Is syntax valid? = {self.is_valid}\n"
        if not self.is_valid:
            result += f"   - Last invalid character = {self.invalid_character}\n"
            result += f"   - Last invalid character points = {self.invalid_character_points}\n"
            result += f"   - Incomplete syntax tokens remaining = {self.incomplete_syntax_string}\n"
            result += f"   - Incomplete syntax fix string = {self.incomplete_syntax_fix_string}\n"
            result += f"   - Incomplete syntax fix points = {self.incomplete_syntax_fix_points}\n"
        result += f" - Text checked = {self.text_to_check}\n"
        return result
