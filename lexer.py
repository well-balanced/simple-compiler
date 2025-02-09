import re


class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.token_specifications = [
            ("NUMBER", r"\d+"),
            ("IDENTIFIER", r"[a-zA-Z_]+"),
            ("ASSIGN", r"="),
            ("OPERATOR", r"[\+\-\*\/\%]"),
            ("WHITESPACE", r"\s+"),
        ]

    def tokenize(self):
        pos = 0

        while pos < len(self.code):
            match = None
            for token_type, pattern in self.token_specifications:
                regex = re.compile(pattern)
                match = regex.match(self.code, pos)

                if match:
                    value = match.group()
                    if token_type != "WHITESPACE":
                        self.tokens.append((token_type, value))
                    pos += len(value)
                    break
            if not match:
                raise Exception(f"Unexpected character: {self.code[pos]}")

        return self.tokens
