class FenwickTree:
    def __init__(self, size):
        # The tree array is 1-indexed, so size+1 elements are needed.
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, index, delta):
        # index is 1-based
        while index <= self.size:
            self.tree[index] += delta
            # Move to the next index to update (parent in the implicit tree structure)
            index += index & (-index)

    def query(self, index):
        # index is 1-based
        s = 0
        while index > 0:
            s += self.tree[index]
            # Move to the previous index to query (parent in the implicit tree structure)
            index -= index & (-index)
        return s

def solve(nums: list[int]) -> int:
    n = len(nums)
    
    # Pair each number with its original 0-based index.
    # Sorting this list will order by value, then by original index (due to stable sort).
    # This ensures that if multiple elements have the same smallest value,
    # we process the one that appeared earliest in the original array,
    # which minimizes cost.
    indexed_nums = sorted([(num, i) for i, num in enumerate(nums)])
    
    # Initialize Fenwick Tree to track the presence of elements.
    # The tree will store 1 at index (original_index + 1) if the element
    # at original_index is present, and 0 otherwise.
    # The size needs to be n for 1-based indexing up to n.
    ft = FenwickTree(n)
    
    # Initially, all elements are present.
    # Populate the Fenwick Tree such that ft.query(k) returns k,
    # meaning there are k elements present up to original index k-1.
    for i in range(1, n + 1):
        ft.update(i, 1)
        
    total_cost = 0
    
    # Process elements in increasing order of their values.
    # If values are equal, process by increasing original index (due to stable sort).
    for _, original_index in indexed_nums:
        # The current 1-based position of this element in the *remaining* array
        # is given by querying the Fenwick Tree up to its (original_index + 1).
        # This counts how many elements are still present at or before its original position.
        # This count is exactly its current 1-based index.
        current_position = ft.query(original_index + 1)
        
        total_cost += current_position
        
        # Mark this element as removed by updating its count in the Fenwick Tree to -1.
        # This ensures that future queries for elements with original_index > this one
        # will correctly reflect the reduced count of preceding elements.
        ft.update(original_index + 1, -1)
        
    return total_cost
