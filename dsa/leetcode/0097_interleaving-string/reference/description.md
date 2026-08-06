## Description

Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an **interleaving** of `s1` and `s2`.

An **interleaving** of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` <span data-keyword="substring-nonempty">substrings</span> respectively, such that:

<ul>
	<li>`s = s_1 + s_2 + ... + s_n`</li>
	<li>`t = t_1 + t_2 + ... + t_m`</li>
	<li>`|n - m| <= 1`</li>
	<li>The **interleaving** is `s_1 + t_1 + s_2 + t_2 + s_3 + t_3 + ...` or `t_1 + s_1 + t_2 + s_2 + t_3 + s_3 + ...`</li>
</ul>

**Note:** `a + b` is the concatenation of strings `a` and `b`.
