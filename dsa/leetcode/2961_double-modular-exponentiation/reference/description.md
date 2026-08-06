## Description

You are given a **0-indexed** 2D array `variables` where `variables[i] = [a_i, b_i, c_i, m_i]`, and an integer `target`.

An index `i` is **good** if the following formula holds:

<ul>
	<li>`0 <= i < variables.length`</li>
	<li>`((a_i^b_i % 10)^c_i) % m_i == target`</li>
</ul>

Return *an array consisting of **good** indices in **any order***.
