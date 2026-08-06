## Description

You are given the customer visit log of a shop represented by a **0-indexed** string `customers` consisting only of characters `'N'` and `'Y'`:

<ul>
	<li>if the `i^th` character is `'Y'`, it means that customers come at the `i^th` hour</li>
	<li>whereas `'N'` indicates that no customers come at the `i^th` hour.</li>
</ul>

If the shop closes at the `j^th` hour (`0 <= j <= n`), the **penalty** is calculated as follows:

<ul>
	<li>For every hour when the shop is open and no customers come, the penalty increases by `1`.</li>
	<li>For every hour when the shop is closed and customers come, the penalty increases by `1`.</li>
</ul>

Return* the **earliest** hour at which the shop must be closed to incur a **minimum** penalty.*

**Note** that if a shop closes at the `j^th` hour, it means the shop is closed at the hour `j`.
