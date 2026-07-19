from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    """
    Constructs an m x n matrix by filling its cells in a spiral order
    using values from a given singly linked list. Unfilled cells default to -1.

    Args:
        m: The number of rows in the matrix.
        n: The number of columns in the matrix.
        head: The head of the singly linked list.

    Returns:
        A list of lists representing the m x n matrix.
    """
    # Initialize the m x n matrix with -1s
    matrix = [[-1] * n for _ in range(m)]

    # Define boundary pointers for the spiral traversal
    top, bottom = 0, m - 1
    left, right = 0, n - 1

    # Continue spiraling as long as boundaries are valid and there are list nodes
    while top <= bottom and left <= right:
        # Traverse right along the top row
        for j in range(left, right + 1):
            if head is None:
                return matrix  # Linked list exhausted, return current matrix
            matrix[top][j] = head.val
            head = head.next
        top += 1  # Move top boundary down

        # Traverse down along the rightmost column
        for i in range(top, bottom + 1):
            if head is None:
                return matrix
            matrix[i][right] = head.val
            head = head.next
        right -= 1  # Move right boundary left

        # Traverse left along the bottom row (only if there's still a row to traverse)
        if top <= bottom:
            for j in range(right, left - 1, -1):
                if head is None:
                    return matrix
                matrix[bottom][j] = head.val
                head = head.next
            bottom -= 1  # Move bottom boundary up

        # Traverse up along the leftmost column (only if there's still a column to traverse)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                if head is None:
                    return matrix
                matrix[i][left] = head.val
                head = head.next
            left += 1  # Move left boundary right

    return matrix
