class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1

        eight_dollar_children = min(money // 7, children)
        money -= eight_dollar_children * 7

        if eight_dollar_children == children and money > 0:
            eight_dollar_children -= 1
        elif eight_dollar_children == children - 1 and money == 3:
            eight_dollar_children -= 1

        return eight_dollar_children
