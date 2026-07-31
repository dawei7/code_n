class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        seen_rows = set()
        seen_columns = set()
        total = 0

        for query_type, index, value in reversed(queries):
            if query_type == 0:
                if index in seen_rows:
                    continue
                seen_rows.add(index)
                total += value * (n - len(seen_columns))
            else:
                if index in seen_columns:
                    continue
                seen_columns.add(index)
                total += value * (n - len(seen_rows))

        return total
