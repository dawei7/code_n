## Description

A **boolean expression** is an expression that evaluates to either `true` or `false`. It can be in one of the following shapes:

<ul>
	<li>`'t'` that evaluates to `true`.</li>
	<li>`'f'` that evaluates to `false`.</li>
	<li>`'!(subExpr)'` that evaluates to **the logical NOT** of the inner expression `subExpr`.</li>
	<li>`'&(subExpr_1, subExpr_2, ..., subExpr_n)'` that evaluates to **the logical AND** of the inner expressions `subExpr_1, subExpr_2, ..., subExpr_n` where `n >= 1`.</li>
	<li>`'|(subExpr_1, subExpr_2, ..., subExpr_n)'` that evaluates to **the logical OR** of the inner expressions `subExpr_1, subExpr_2, ..., subExpr_n` where `n >= 1`.</li>
</ul>

Given a string `expression` that represents a **boolean expression**, return *the evaluation of that expression*.

It is **guaranteed** that the given expression is valid and follows the given rules.
