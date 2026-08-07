## Description

You are given a string `initialCurrency`, and you start with `1.0` of `initialCurrency`.

You are also given four arrays with currency pairs (strings) and rates (real numbers):

	- `pairs1[i] = [startCurrency_i, targetCurrency_i]` denotes that you can convert from `startCurrency_i` to `targetCurrency_i` at a rate of `rates1[i]` on **day 1**.

	- `pairs2[i] = [startCurrency_i, targetCurrency_i]` denotes that you can convert from `startCurrency_i` to `targetCurrency_i` at a rate of `rates2[i]` on **day 2**.

	- Also, each `targetCurrency` can be converted back to its corresponding `startCurrency` at a rate of `1 / rate`.

You can perform **any** number of conversions, **including zero**, using `rates1` on day 1, **followed** by any number of additional conversions, **including zero**, using `rates2` on day 2.

Return the **maximum** amount of `initialCurrency` you can have after performing any number of conversions on both days **in order**.

**Note: **Conversion rates are valid, and there will be no contradictions in the rates for either day. The rates for the days are independent of each other.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0]</span>

**Output:** <span class="example-io">720.00000</span>

**Explanation:**

To get the maximum amount of **EUR**, starting with 1.0 **EUR**:

	- On Day 1:

		<li>Convert **EUR **to **USD** to get 2.0 **USD**.

		- Convert **USD** to **JPY** to get 6.0 **JPY**.

	</li>
	- On Day 2:

		<li>Convert **JPY** to **USD** to get 24.0 **USD**.

		- Convert **USD** to **CHF** to get 120.0 **CHF**.

		- Finally, convert **CHF** to **EUR** to get 720.0 **EUR**.

	</li>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">initialCurrency = "NGN", pairs1 = </span>[["NGN","EUR"]]<span class="example-io">, rates1 = </span>[9.0]<span class="example-io">, pairs2 = </span>[["NGN","EUR"]]<span class="example-io">, rates2 = </span>[6.0]

**Output:** 1.50000

**Explanation:**

Converting **NGN** to **EUR** on day 1 and **EUR** to **NGN** using the inverse rate on day 2 gives the maximum amount.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"]], rates2 = [10.0]</span>

**Output:** <span class="example-io">1.00000</span>

**Explanation:**

In this example, there is no need to make any conversions on either day.

</div>

**Constraints:**

	- `1 <= initialCurrency.length <= 3`

	- `initialCurrency` consists only of uppercase English letters.

	- `1 <= n == pairs1.length <= 10`

	- `1 <= m == pairs2.length <= 10`

	- `pairs1[i] == [startCurrency_i, targetCurrency_i]`<!-- notionvc: c31b5bb8-4df6-4987-9bcd-6dff8a5f7cd4 -->

	- `pairs2[i] == [startCurrency_i, targetCurrency_i]`<!--{C}%3C!%2D%2D%20notionvc%3A%20c31b5bb8-4df6-4987-9bcd-6dff8a5f7cd4%20%2D%2D%3E-->

	- `1 <= startCurrency_i.length, targetCurrency_i.length <= 3`

	- `startCurrency_i` and `targetCurrency_i` consist only of uppercase English letters.

	- `rates1.length == n`

	- `rates2.length == m`

	- `1.0 <= rates1[i], rates2[i] <= 10.0`

	- The input is generated such that there are no contradictions or cycles in the conversion graphs for either day.

	- The input is generated such that the output is **at most** `5 * 10^10`.
