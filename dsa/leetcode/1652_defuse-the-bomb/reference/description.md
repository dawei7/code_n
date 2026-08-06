## Description

You have a bomb to defuse, and your time is running out! Your informer will provide you with a **circular** array `code` of length of `n` and a key `k`.

To decrypt the code, you must replace every number. All the numbers are replaced **simultaneously**.

<ul>
	<li>If `k > 0`, replace the `i^th` number with the sum of the **next** `k` numbers.</li>
	<li>If `k < 0`, replace the `i^th` number with the sum of the **previous** -`k` numbers.</li>
	<li>If `k == 0`, replace the `i^th` number with `0`.</li>
</ul>

As `code` is circular, the next element of `code[n-1]` is `code[0]`, and the previous element of `code[0]` is `code[n-1]`.

Given the **circular** array `code` and an integer key `k`, return *the decrypted code to defuse the bomb*!
