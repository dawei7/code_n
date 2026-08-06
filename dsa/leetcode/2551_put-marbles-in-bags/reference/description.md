## Description

You have `k` bags. You are given a **0-indexed** integer array `weights` where `weights[i]` is the weight of the `i^th` marble. You are also given the integer `k.`

Divide the marbles into the `k` bags according to the following rules:

<ul>
	<li>No bag is empty.</li>
	<li>If the `i^th` marble and `j^th` marble are in a bag, then all marbles with an index between the `i^th` and `j^th` indices should also be in that same bag.</li>
	<li>If a bag consists of all the marbles with an index from `i` to `j` inclusively, then the cost of the bag is `weights[i] + weights[j]`.</li>
</ul>

The **score** after distributing the marbles is the sum of the costs of all the `k` bags.

Return *the **difference** between the **maximum** and **minimum** scores among marble distributions*.
