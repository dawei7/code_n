## Description

Under the grammar given below, strings can represent a set of lowercase words. Let `R(expr)` denote the set of words the expression represents.

The grammar can best be understood through simple examples:

<ul>
	<li>Single letters represent a singleton set containing that word.
	<ul>
		<li>`R("a") = {"a"}`</li>
		<li>`R("w") = {"w"}`</li>
	</ul>
	</li>
	<li>When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
	<ul>
		<li>`R("{a,b,c}") = {"a","b","c"}`</li>
		<li>`R("{{a,b},{b,c}}") = {"a","b","c"}` (notice the final set only contains each word at most once)</li>
	</ul>
	</li>
	<li>When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
	<ul>
		<li>`R("{a,b}{c,d}") = {"ac","ad","bc","bd"}`</li>
		<li>`R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}`</li>
	</ul>
	</li>
</ul>

Formally, the three rules for our grammar:

<ul>
	<li>For every lowercase letter `x`, we have `R(x) = {x}`.</li>
	<li>For expressions `e_1, e_2, ... , e_k` with `k >= 2`, we have `R({e_1, e_2, ...}) = R(e_1) ∪ R(e_2) ∪ ...`</li>
	<li>For expressions `e_1` and `e_2`, we have `R(e_1 + e_2) = {a + b for (a, b) in R(e_1) × R(e_2)}`, where `+` denotes concatenation, and `×` denotes the cartesian product.</li>
</ul>

Given an expression representing a set of words under the given grammar, return *the sorted list of words that the expression represents*.
