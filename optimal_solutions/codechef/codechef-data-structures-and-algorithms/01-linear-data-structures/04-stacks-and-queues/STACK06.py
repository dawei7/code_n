


def solve():
    MAX_SIZE = 101
    a = [0] * MAX_SIZE
    top = -1

    def push(ele):
        global top
        if top <= MAX_SIZE - 1:
            top += 1
            a[top] = ele
        else:
            print(f"Stack is full. Cannot push: {ele}")

    def pop():
        global top
        if top >= 0:
            ele = a[top]
            top -= 1
            return ele
        else:
            print("Stack is empty. Cannot pop.")
            return -1

    def is_empty():
        return top == -1

    def size():
        return top + 1

    def decimal_to_binary(decimal):
        while decimal > 0:
            remainder = decimal % 2
            push(remainder)
            decimal //= 2

        if is_empty():
            print("0")  # Special case for decimal = 0
            return

        while not is_empty():
            print(pop(), end="")
        print()

    if __name__ == "__main__":
        t = int(input())

        for _ in range(t):
            decimal = int(input())
            decimal_to_binary(decimal)


if __name__ == "__main__":
    solve()
