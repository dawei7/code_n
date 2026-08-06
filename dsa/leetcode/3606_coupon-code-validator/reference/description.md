## Description

You are given three arrays of length `n` that describe the properties of `n` coupons: `code`, `businessLine`, and `isActive`. The `i^th `coupon has:

<ul>
	<li>`code[i]`: a **string** representing the coupon identifier.</li>
	<li>`businessLine[i]`: a **string** denoting the business category of the coupon.</li>
	<li>`isActive[i]`: a **boolean** indicating whether the coupon is currently active.</li>
</ul>

A coupon is considered **valid** if all of the following conditions hold:

<ol>
	<li>`code[i]` is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (`_`).</li>
	<li>`businessLine[i]` is one of the following four categories: `"electronics"`, `"grocery"`, `"pharmacy"`, `"restaurant"`.</li>
	<li>`isActive[i]` is **true**.</li>
</ol>

Return an array of the **codes** of all valid coupons, **sorted** first by their **businessLine** in the order: `"electronics"`, `"grocery"`, `"pharmacy", "restaurant"`, and then by **code** in lexicographical (ascending) order within each category.
