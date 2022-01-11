import SyntaxResult as sr

class SyntaxChecker:
    token_open: list[str] = ["(", "[", "{", "<"]
    token_close: list[str] = [")", "]", "}", ">"]
    token_queue: list[str] = []

    def __init__(self):
        pass

    def __str__(self):
        result = "Syntax checker\n"
        result += f" - Opening tokens = {self.token_open}\n"
        result += f" - Closing tokens = {self.token_close}\n"
        return result

    def check_syntax(self, text_to_check):
        print(f"")
        print(f"Checking syntax for {text_to_check}")

        result = sr.SyntaxResult()
        result.text_to_check = text_to_check
        result.is_valid = True

        for c in text_to_check:
            if c in self.token_open:
                self.token_queue.append(c)
                print(f" - {c} Open token - queue: {self.token_queue}")
            elif c in self.token_close:
                last_token = self.token_queue.pop()
                if last_token in self.token_open:
                    # We have an open token, let's see if it matches
                    if self.token_open.index(last_token) == self.token_close.index(c):
                        print(f" - {c} Close token - does it match {last_token} ? Yes")
                    else:
                        print(f" - {c} Close token - does it match {last_token} ? No ... this is invalid")
                        result.is_valid = False
                        return result
                else:
                    # We have a close token again, this is not valid
                    print(f" - {c} Close token - does it match {last_token}? No ... this is invalid")
                    result.is_valid = False
                    return result

        if len(self.token_queue) > 0:
            print(f" - Token queue is not empty ({len(self.token_queue)} items remaining) ... this is invalid")
            result.is_valid = False

        return result




