# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass

class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        categories = 0

        for i in range(n):
            for j in range(i):
                if categoryHandler.haveSameCategory(i, j):
                    break
            else:
                categories += 1

        return categories
