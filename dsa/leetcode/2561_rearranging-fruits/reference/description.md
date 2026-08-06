## Description

You have two fruit baskets containing `n` fruits each. You are given two **0-indexed** integer arrays `basket1` and `basket2` representing the cost of fruit in each basket. You want to make both baskets **equal**. To do so, you can use the following operation as many times as you want:

<ul>
	<li>Choose two indices `i` and `j`, and swap the `i^<font size="1">th</font>` fruit of `basket1` with the `j^<font size="1">th</font>` fruit of `basket2`.</li>
	<li>The cost of the swap is `min(basket1[i], basket2[j])`.</li>
</ul>

Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

Return *the minimum cost to make both the baskets equal or *`-1`* if impossible.*
