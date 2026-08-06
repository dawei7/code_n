## Description

You are given an integer array `nums` and a list of queries. Each query is `[x, y]`. Its special sum starts at index `x` and includes `nums[x]`, `nums[x + y]`, `nums[x + 2 * y]`, and so on while the selected index remains inside the array.

Return the special sum for every query in its original order, with each result reduced modulo $10^9+7$. Queries do not modify `nums`, and repeated starting positions or step sizes must each produce their own output.
