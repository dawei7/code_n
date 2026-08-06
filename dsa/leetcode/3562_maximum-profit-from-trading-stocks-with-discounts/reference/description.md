## Description

You are given an integer `n`, representing the number of employees in a company. Each employee is assigned a unique ID from 1 to `n`, and employee 1 is the CEO, is the direct or indirect boss of every employee. You are given two **1-based **integer arrays, `present` and `future`, each of length `n`, where:

<ul>
	<li>`present[i]` represents the **current** price at which the `i^th` employee can buy a stock today.</li>
	<li>`future[i]` represents the **expected** price at which the `i^th` employee can sell the stock tomorrow.</li>
</ul>

The company's hierarchy is represented by a 2D integer array `hierarchy`, where `hierarchy[i] = [u_i, v_i]` means that employee `u_i` is the direct boss of employee `v_i`.

Additionally, you have an integer `budget` representing the total funds available for investment.

However, the company has a discount policy: if an employee's direct boss purchases their own stock, then the employee can buy their stock at **half** the original price (`floor(present[v] / 2)`).

Return the **maximum** profit that can be achieved without exceeding the given budget.

**Note:**

<ul>
	<li>You may buy each stock at most **once**.</li>
	<li>You **cannot** use any profit earned from future stock prices to fund additional investments and must buy only from `budget`.</li>
</ul>
