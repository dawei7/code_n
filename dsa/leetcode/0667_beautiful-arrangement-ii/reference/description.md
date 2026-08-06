## Description

Given two integers `n` and `k`, construct a list `answer` that contains `n` different positive integers ranging from `1` to `n` and obeys the following requirement:

<ul>
	<li>Suppose this list is `answer = [a_1, a_2, a_3, ... , a_n]`, then the list `[|a_1 - a_2|, |a_2 - a_3|, |a_3 - a_4|, ... , |a_n-1 - a_n|]` has exactly `k` distinct integers.</li>
</ul>

Return *the list* `answer`. If there multiple valid answers, return **any of them**.
