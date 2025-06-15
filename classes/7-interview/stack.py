class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

def check_balance(string_with_parentheses):
        stack = Stack()
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in string_with_parentheses:
            if char in '([{':
                stack.push(char)
            elif char in ')]}':
                if stack.is_empty():
                    return "Несбалансированно"
                if stack.pop() != pairs[char]:
                    return "Несбалансированно"

        return "Сбалансированно" if stack.is_empty() else "Несбалансированно"

print(check_balance("(((([{}]))))"))  # Сбалансированно
print(check_balance("[([])((([[[]]])))]{()}"))  # Сбалансированно
print(check_balance("{{[()]}}"))  # Сбалансированно
print(check_balance("}{}"))  # Несбалансированно
print(check_balance("{{[(])]}}"))  # Несбалансированно
print(check_balance("[[{())}]"))