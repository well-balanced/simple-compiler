class ASTNode:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"ASTNode({self.type}, {self.value}, {self.left}, {self.right})"


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self):
        token = self.peek()
        self.pos += 1
        return token

    def parse_number(self):
        token = self.consume()
        return ASTNode("NUMBER", token[1])

    def parse_identifier(self):
        token = self.consume()
        return ASTNode("IDENTIFIER", token[1])

    def parse_term(self):
        token = self.peek()
        if token[0] == "NUMBER":
            return self.parse_number()
        elif token[0] == "IDENTIFIER":
            return self.parse_identifier()
        else:
            raise Exception(f"Unexpected token: {token[0]}")

    def parse_expression(self):
        left = self.parse_term()

        while self.peek() and self.peek()[0] == "OPERATOR":
            operator = self.consume()
            right = self.parse_term()
            left = ASTNode("BINARY_OP", operator[1], left, right)

        return left

    def parse_assignment(self):
        identifier = self.parse_identifier()
        token = self.consume()

        value = self.parse_expression()
        return ASTNode("ASSIGN", identifier, value)

    def parse(self):
        ast_tree = []
        while self.peek():
            ast_tree.append(self.parse_assignment())

        return ast_tree
