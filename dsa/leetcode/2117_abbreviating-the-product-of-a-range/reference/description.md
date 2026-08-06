## Description

You are given two positive integers `left` and `right` with `left <= right`. Calculate the **product** of all integers in the **inclusive** range `[left, right]`.

Since the product may be very large, you will **abbreviate** it following these steps:

<ol>
	<li>Count all **trailing** zeros in the product and **remove** them. Let us denote this count as `C`.

	<ul>
		<li>For example, there are `3` trailing zeros in `1000`, and there are `0` trailing zeros in `546`.</li>
	</ul>
	</li>
	<li>Denote the remaining number of digits in the product as `d`. If `d > 10`, then express the product as `<pre>...<suf>` where `<pre>` denotes the **first** `5` digits of the product, and `<suf>` denotes the **last** `5` digits of the product **after** removing all trailing zeros. If `d <= 10`, we keep it unchanged.
	<ul>
		<li>For example, we express `1234567654321` as `12345...54321`, but `1234567` is represented as `1234567`.</li>
	</ul>
	</li>
	<li>Finally, represent the product as a **string** `"<pre>...<suf>eC"`.
	<ul>
		<li>For example, `12345678987600000` will be represented as `"12345...89876e5"`.</li>
	</ul>
	</li>
</ol>

Return *a string denoting the **abbreviated product** of all integers in the **inclusive** range* `[left, right]`.
