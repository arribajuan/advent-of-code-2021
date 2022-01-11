import SyntaxResult as sr

class SyntaxChecker:
    token_open = ["(", "[", "{", "<"]
    token_close = [")", "]", "}", ">"]

    def __init__(self):
        pass

    def __str__(self):
        result = "Syntax checker\n"
        result += f" - Opening tokens = {self.token_open}\n"
        result += f" - Opening tokens = {self.token_close}\n"
        return result

    @staticmethod
    def check_syntax(text_to_check):
        result = sr.SyntaxResult()

        return result

