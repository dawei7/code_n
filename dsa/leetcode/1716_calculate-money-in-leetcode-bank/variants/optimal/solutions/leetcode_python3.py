class Solution:
    def totalMoney(self, n: int) -> int:
        complete_weeks, remaining_days = divmod(n, 7)
        complete_total = (
            28 * complete_weeks
            + 7 * complete_weeks * (complete_weeks - 1) // 2
        )
        partial_total = (
            remaining_days * (complete_weeks + 1)
            + remaining_days * (remaining_days - 1) // 2
        )
        return complete_total + partial_total
