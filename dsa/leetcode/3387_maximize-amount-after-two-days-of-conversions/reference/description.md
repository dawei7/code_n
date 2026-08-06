## Description

You are given a string `initialCurrency`, and you start with `1.0` of `initialCurrency`.

You are also given four arrays with currency pairs (strings) and rates (real numbers):

<ul>
	<li>`pairs1[i] = [startCurrency_i, targetCurrency_i]` denotes that you can convert from `startCurrency_i` to `targetCurrency_i` at a rate of `rates1[i]` on **day 1**.</li>
	<li>`pairs2[i] = [startCurrency_i, targetCurrency_i]` denotes that you can convert from `startCurrency_i` to `targetCurrency_i` at a rate of `rates2[i]` on **day 2**.</li>
	<li>Also, each `targetCurrency` can be converted back to its corresponding `startCurrency` at a rate of `1 / rate`.</li>
</ul>

You can perform **any** number of conversions, **including zero**, using `rates1` on day 1, **followed** by any number of additional conversions, **including zero**, using `rates2` on day 2.

Return the **maximum** amount of `initialCurrency` you can have after performing any number of conversions on both days **in order**.

**Note: **Conversion rates are valid, and there will be no contradictions in the rates for either day. The rates for the days are independent of each other.
