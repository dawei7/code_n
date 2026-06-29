


def solve():
    def findSubsets(inputNumbers):
        result = []

        def generate(idx, current):
            if idx == len(inputNumbers):
                result.append(current.copy())
                return

            # Exclude
            generate(idx + 1, current)

            # Include
            current.append(inputNumbers[idx])
            generate(idx + 1, current)
            current.pop()

        generate(0, [])
        return result


if __name__ == "__main__":
    solve()
