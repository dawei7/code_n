from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = 0

        for middle, middle_rating in enumerate(rating):
            left_smaller = left_greater = 0
            right_smaller = right_greater = 0
            for candidate in rating[:middle]:
                if candidate < middle_rating:
                    left_smaller += 1
                else:
                    left_greater += 1
            for candidate in rating[middle + 1:]:
                if candidate < middle_rating:
                    right_smaller += 1
                else:
                    right_greater += 1
            teams += left_smaller * right_greater
            teams += left_greater * right_smaller

        return teams
