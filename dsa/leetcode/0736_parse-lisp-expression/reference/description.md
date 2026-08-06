## Description

You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

<ul>
	<li>An expression is either an integer, let expression, add expression, mult expression, or an assigned variable. Expressions always evaluate to a single integer.</li>
	<li>(An integer could be positive or negative.)</li>
	<li>A let expression takes the form `"(let v_1 e_1 v_2 e_2 ... v_n e_n expr)"`, where let is always the string `"let"`, then there are one or more pairs of alternating variables and expressions, meaning that the first variable `v_1` is assigned the value of the expression `e_1`, the second variable `v_2` is assigned the value of the expression `e_2`, and so on sequentially; and then the value of this let expression is the value of the expression `expr`.</li>
	<li>An add expression takes the form `"(add e_1 e_2)"` where add is always the string `"add"`, there are always two expressions `e_1`, `e_2` and the result is the addition of the evaluation of `e_1` and the evaluation of `e_2`.</li>
	<li>A mult expression takes the form `"(mult e_1 e_2)"` where mult is always the string `"mult"`, there are always two expressions `e_1`, `e_2` and the result is the multiplication of the evaluation of e1 and the evaluation of e2.</li>
	<li>For this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally, for your convenience, the names `"add"`, `"let"`, and `"mult"` are protected and will never be used as variable names.</li>
	<li>Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on the scope.</li>
</ul>
