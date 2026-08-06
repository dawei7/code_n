## Description

You are given an integer array `pizzas` of size `n`, where `pizzas[i]` represents the weight of the `i^th` pizza. Every day, you eat **exactly** 4 pizzas. Due to your incredible metabolism, when you eat pizzas of weights `W`, `X`, `Y`, and `Z`, where `W <= X <= Y <= Z`, you gain the weight of only 1 pizza!

<ul>
	<li>On **<span style="box-sizing: border-box; margin: 0px; padding: 0px;">odd-numbered</span>** days **(1-indexed)**, you gain a weight of `Z`.</li>
	<li>On **even-numbered** days, you gain a weight of `Y`.</li>
</ul>

Find the **maximum** total weight you can gain by eating **all** pizzas optimally.

**Note**: It is guaranteed that `n` is a multiple of 4, and each pizza can be eaten only once.
