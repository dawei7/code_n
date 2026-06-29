


def solve():
    def sortedInsert(stack, element):
        if not stack or stack[-1] < element:
            stack.append(element)
            return
        top = stack.pop()
        sortedInsert(stack, element)
        stack.append(top)


    def sortStack(stack):
        if not stack:
            return
        top = stack.pop()
        sortStack(stack)
        sortedInsert(stack, top)


if __name__ == "__main__":
    solve()
