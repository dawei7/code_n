import heapq

def solve(heights, queries):
    n = len(heights)
    q = len(queries)
    results = [-1] * q

    # Store deferred queries by their rightmost starting index. While scanning
    # left to right, active queries can only be answered by later buildings.
    deferred_queries = [[] for _ in range(n)]

    for query_idx, (a, b) in enumerate(queries):
        if a > b:
            a, b = b, a

        # If a == b or heights[b] > heights[a], they can meet at b
        if a == b or heights[a] < heights[b]:
            results[query_idx] = b
        else:
            # Otherwise, they need the first index > b with height > heights[a].
            deferred_queries[b].append((heights[a], query_idx))

    min_heap = []

    for i, height in enumerate(heights):
        # Resolve queries that started earlier; queries at this same index are
        # pushed after the check so this building cannot answer itself.
        while min_heap and heights[i] > min_heap[0][0]:
            _, query_idx = heapq.heappop(min_heap)
            results[query_idx] = i

        for required_height, query_idx in deferred_queries[i]:
            heapq.heappush(min_heap, (required_height, query_idx))

    return results
