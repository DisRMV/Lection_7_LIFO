from collections import deque


class Stack:

    def __init__(self, stack=deque()):
        self.stack = deque(stack)

    def isEmpty(self):
        return bool(not self.stack)

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def check_brackets(self, some_str, brackets='()[]{}'):
        if len(some_str) % 2 != 0:
            return 'Несбалансированно'
        opening, closing = brackets[::2], brackets[1::2]
        for i in some_str:
            if i in opening:
                self.stack.append(opening.index(i))
            elif i in closing:
                if self.stack[-1] == closing.index(i):
                    self.stack.pop()
                else:
                    return 'Несбалансированно'
        return 'Сбалансированно'


if __name__ == '__main__':
    some_stack = Stack()
    print(some_stack.isEmpty())
    some_stack.push('123')
    some_stack.push('str')
    some_stack.push([])
    print(some_stack.stack)
    print(some_stack.pop())
    print(some_stack.stack)
    print(some_stack.peek())
    print(some_stack.size())
    text = '[([])((([[[]]])))]{()}'
    print(some_stack.check_brackets(text))
