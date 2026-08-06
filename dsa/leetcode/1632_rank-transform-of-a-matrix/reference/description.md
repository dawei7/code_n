## Description

Given an `m x n` `matrix`, return *a new matrix *`answer`* where *`answer[row][col]`* is the ****rank** of *`matrix[row][col]`.

The **rank** is an **integer** that represents how large an element is compared to other elements. It is calculated using the following rules:

<ul>
	<li>The rank is an integer starting from `1`.</li>
	<li>If two elements `p` and `q` are in the **same row or column**, then:
	<ul>
		<li>If `p < q` then `rank(p) < rank(q)`</li>
		<li>If `p == q` then `rank(p) == rank(q)`</li>
		<li>If `p > q` then `rank(p) > rank(q)`</li>
	</ul>
	</li>
	<li>The **rank** should be as **small** as possible.</li>
</ul>

The test cases are generated so that `answer` is unique under the given rules.
