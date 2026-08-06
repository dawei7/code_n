## Description

You are given a string array `words`, and an array `groups`, both arrays having length `n`.

The **hamming distance** between two strings of equal length is the number of positions at which the corresponding characters are **different**.

You need to select the **longest** <span data-keyword="subsequence-array">subsequence</span> from an array of indices `[0, 1, ..., n - 1]`, such that for the subsequence denoted as `[i_0, i_1, ..., i_k-1]` having length `k`, the following holds:

<ul>
	<li>For **adjacent** indices in the subsequence, their corresponding groups are **unequal**, i.e., `groups[i_j] != groups[i_j+1]`, for each `j` where `0 < j + 1 < k`.</li>
	<li>`words[i_j]` and `words[i_j+1]` are **equal** in length, and the **hamming distance** between them is `1`, where `0 < j + 1 < k`, for all indices in the subsequence.</li>
</ul>

Return *a string array containing the words corresponding to the indices **(in order)** in the selected subsequence*. If there are multiple answers, return *any of them*.

**Note:** strings in `words` may be **unequal** in length.
