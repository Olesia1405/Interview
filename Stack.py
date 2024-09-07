class Stack:
    def __init__(self):
        self._stack = []

    def is_empty(self):
        return len(self._stack) == 0

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._stack[-1]

    def size(self):
        return len(self._stack)


def is_balanced(expression):
    stack = Stack()
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in matching_brackets.values():  # Если это открывающая скобка
            stack.push(char)
        elif char in matching_brackets.keys():  # Если это закрывающая скобка
            if stack.is_empty():
                return "Несбалансированно"
            top_element = stack.pop()
            if matching_brackets[char] != top_element:
                return "Несбалансированно"

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"



# Тестируем с различными входными данными
print(is_balanced("(((([{}]))))"))  # Сбалансированно
print(is_balanced("[([])((([[[]]])))]{()}"))  # Сбалансированно
print(is_balanced("{{[()]}}"))  # Сбалансированно
print(is_balanced("}{"))  # Несбалансированно
print(is_balanced("{{[(])]}}"))  # Несбалансированно
print(is_balanced("[[{()}]]"))  # Сбалансированно
print(is_balanced("[{]"))  # Несбалансированно
