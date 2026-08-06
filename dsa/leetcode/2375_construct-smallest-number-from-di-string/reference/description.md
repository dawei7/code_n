## Description

You are given a **0-indexed** string `pattern` of length `n` consisting of the characters `'I'` meaning **increasing** and `'D'` meaning **decreasing**.

A **0-indexed** string `num` of length `n + 1` is created using the following conditions:

<ul>
	<li>`num` consists of the digits `'1'` to `'9'`, where each digit is used **at most** once.</li>
	<li>If `pattern[i] == 'I'`, then `num[i] < num[i + 1]`.</li>
	<li>If `pattern[i] == 'D'`, then `num[i] > num[i + 1]`.</li>
</ul>

Return *the lexicographically **smallest** possible string *`num`* that meets the conditions.*
