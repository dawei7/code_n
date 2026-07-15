from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        book_count = len(books)
        minimum_height = [0] + [10**18] * book_count

        for end in range(1, book_count + 1):
            width = 0
            shelf_height = 0
            for start in range(end - 1, -1, -1):
                thickness, height = books[start]
                width += thickness
                if width > shelfWidth:
                    break
                shelf_height = max(shelf_height, height)
                minimum_height[end] = min(
                    minimum_height[end], minimum_height[start] + shelf_height
                )
        return minimum_height[book_count]
