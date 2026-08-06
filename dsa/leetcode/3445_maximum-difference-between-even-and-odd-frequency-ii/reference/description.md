## Description

You are given a string `s` and an integer `k`. Your task is to find the **maximum** difference between the frequency of **two** characters, `freq[a] - freq[b]`, in a <span data-keyword="substring">substring</span> `subs` of `s`, such that:

<ul>
	<li>`subs` has a size of **at least** `k`.</li>
	<li>Character `a` has an *odd frequency* in `subs`.</li>
	<li>Character `b` has a **non-zero** *even frequency* in `subs`.</li>
</ul>

Return the **maximum** difference.

**Note** that `subs` can contain more than 2 **distinct** characters.
