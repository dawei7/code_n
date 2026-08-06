## Description

You are given three integers `n`, `pos`, and `k`.

There are `n` people standing in a line indexed from 0 to `n - 1`. Each person **independently** chooses a direction:

<ul>
	<li>`'L'`: **visible** only to people on their **right**</li>
	<li>`'R'`: **visible** only to people on their **left**</li>
</ul>
A person at index `pos` sees others as follows:

<ul>
	<li>A person `i < pos` is visible if and only if they choose `'L'`.</li>
	<li>A person `i > pos` is visible if and only if they choose `'R'`.</li>
</ul>

Return the number of possible direction assignments such that the person at index `pos` sees **exactly** `k` people.

Since the answer may be large, return it **modulo** `10^9 + 7`.
