## Description

You are given an array of strings `ideas` that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

<ol>
	<li>Choose 2 **distinct** names from `ideas`, call them `idea_A` and `idea_B`.</li>
	<li>Swap the first letters of `idea_A` and `idea_B` with each other.</li>
	<li>If **both** of the new names are not found in the original `ideas`, then the name `idea_A idea_B` (the **concatenation** of `idea_A` and `idea_B`, separated by a space) is a valid company name.</li>
	<li>Otherwise, it is not a valid name.</li>
</ol>

Return *the number of **distinct** valid names for the company*.
