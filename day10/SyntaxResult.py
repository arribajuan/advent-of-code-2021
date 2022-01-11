class SyntaxResult:
    is_valid = False
    text_to_check = ""

    def __init__(self):
        pass

    def __str__(self):
        result = "Syntax check result\n"
        result += f" - Is syntax valid? = {self.is_valid}\n"
        result += f" - Text checked = {self.text_to_check}\n"
        return result
