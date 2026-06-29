import heapq


def solve():
    def get_neighbors(size, row, col):
        # Yield valid neighboring cells within the grid boundaries
        for delta_row, delta_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_row, new_col = row + delta_row, col + delta_col
            if 0 <= new_row < size and 0 <= new_col < size:
                yield (new_row, new_col)

    def find_min_max_path(matrix, size):
        min_heap = []
        heapq.heappush(min_heap, (matrix[0][0], 0, 0))  # Push starting cell (value, row, col)
        matrix[0][0] = -1  # Mark starting cell as visited
        max_height = -1

        while min_heap:
            max_height, row, col = heapq.heappop(min_heap)

            # If we reach the bottom-right cell, break the loop
            if (row, col) == (size - 1, size - 1):
                break

            # Process each neighbor of the current cell
            for neighbor_row, neighbor_col in get_neighbors(size, row, col):
                if matrix[neighbor_row][neighbor_col] != -1:  # Check if the cell is unvisited
                    # Push the cell with the updated maximum height for the path so far
                    heapq.heappush(min_heap, (max(max_height, matrix[neighbor_row][neighbor_col]), neighbor_row, neighbor_col))
                    matrix[neighbor_row][neighbor_col] = -1  # Mark cell as visited

        return max_height

    # Read number of test cases
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        matrix = [list(map(int, input().split())) for _ in range(n)]
        print(find_min_max_path(matrix, n))


if __name__ == "__main__":
    solve()
