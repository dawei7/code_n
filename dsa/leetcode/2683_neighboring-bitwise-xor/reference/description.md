## Description

A **0-indexed** array `derived` with length `n` is derived by computing the **bitwise XOR** (⊕) of adjacent values in a **binary array** `original` of length `n`.

Specifically, for each index `i` in the range `[0, n - 1]`:

<ul>
	<li>If `i = n - 1`, then `derived[i] = original[i] ⊕ original[0]`.</li>
	<li>Otherwise, `derived[i] = original[i] ⊕ original[i + 1]`.</li>
</ul>

Given an array `derived`, your task is to determine whether there exists a **valid binary array** `original` that could have formed `derived`.

Return ***true** if such an array exists or **false** otherwise.*

<ul>
	<li>A binary array is an array containing only **0's** and **1's**</li>
</ul>
