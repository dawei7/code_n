## Description

You are **building** a string `s` of length `n` **one** character at a time, **prepending** each new character to the **front** of the string. The strings are labeled from `1` to `n`, where the string with length `i` is labeled `s_i`.

<ul>
	<li>For example, for `s = "abaca"`, `s_1 == "a"`, `s_2 == "ca"`, `s_3 == "aca"`, etc.</li>
</ul>

The **score** of `s_i` is the length of the **longest common prefix** between `s_i` and `s_n` (Note that `s == s_n`).

Given the final string `s`, return* the **sum** of the **score** of every *`s_i`.
