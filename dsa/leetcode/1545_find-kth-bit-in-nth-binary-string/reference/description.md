## Description

Given two positive integers `n` and `k`, the binary string `S_n` is formed as follows:

<ul>
	<li>`S_1 = "0"`</li>
	<li>`S_i = S_i - 1 + "1" + reverse(invert(S_i - 1))` for `i > 1`</li>
</ul>

Where `+` denotes the concatenation operation, `reverse(x)` returns the reversed string `x`, and `invert(x)` inverts all the bits in `x` (`0` changes to `1` and `1` changes to `0`).

For example, the first four strings in the above sequence are:

<ul>
	<li>`S_1 = "0"`</li>
	<li>`S_2 = "0**1**1"`</li>
	<li>`S_3 = "011**1**001"`</li>
	<li>`S_4 = "0111001**1**0110001"`</li>
</ul>

Return *the* `k^th` *bit* *in* `S_n`. It is guaranteed that `k` is valid for the given `n`.
