def solve(n: int, queries: list[list[int]]) -> list[int]:
    # Initialize the array with 0s, representing uncolored elements.
    colors = [0] * n
    
    # Initialize the count of adjacent pairs with the same positive color.
    current_adjacent_pairs = 0
    
    # List to store the result after each query.
    results = []

    # Process each query
    for index, new_color in queries:
        old_color = colors[index]

        # Step 1: Decrement count for adjacencies involving the old_color at 'index'.
        # We only decrement if the old_color was positive (not 0) and formed a pair.

        # Check left neighbor (index - 1)
        if index > 0:
            # If the left neighbor had the same old_color (and old_color was positive),
            # this pair is about to be broken.
            if colors[index - 1] == old_color and old_color != 0:
                current_adjacent_pairs -= 1
        
        # Check right neighbor (index + 1)
        if index < n - 1:
            # If the right neighbor had the same old_color (and old_color was positive),
            # this pair is about to be broken.
            if colors[index + 1] == old_color and old_color != 0:
                current_adjacent_pairs -= 1

        # Step 2: Update the color of the element at 'index'.
        colors[index] = new_color

        # Step 3: Increment count for adjacencies involving the new_color at 'index'.
        # We only increment if the new_color is positive (not 0) and forms a new pair.

        # Check left neighbor (index - 1)
        if index > 0:
            # If the left neighbor now has the same new_color (and new_color is positive),
            # a new pair is formed.
            if colors[index - 1] == new_color and new_color != 0:
                current_adjacent_pairs += 1
        
        # Check right neighbor (index + 1)
        if index < n - 1:
            # If the right neighbor now has the same new_color (and new_color is positive),
            # a new pair is formed.
            if colors[index + 1] == new_color and new_color != 0:
                current_adjacent_pairs += 1
        
        # Add the current count of adjacent pairs to the results list.
        results.append(current_adjacent_pairs)

    return results
