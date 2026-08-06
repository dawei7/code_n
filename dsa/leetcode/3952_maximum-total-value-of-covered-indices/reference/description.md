## Description

You are given an integer array `nums` of length `n` and a binary string `s` of length `n`, where `s[i] == '1'` means index `i` initially contains a **token** and `s[i] == '0'` means it does not.

You may perform the following operation any number of times:

<ul>
	<li>Choose a token currently located at index `i`, where `i > 0`, such that this token has **not** been moved before.</li>
	<li>Move this token from index `i` to index `i - 1`.</li>
</ul>

An index is considered **covered** if it contains a token after all moves.

Return an integer denoting the **maximum total value** of `nums` at the covered indices after optimally performing the operations.
