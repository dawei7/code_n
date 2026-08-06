## Description

You have two soups, **A** and **B**, each starting with `n` mL. On every turn, one of the following four serving operations is chosen *at random*, each with probability `0.25` **independent** of all previous turns:

<ul>
	<li>pour 100 mL from type A and 0 mL from type B</li>
	<li>pour 75 mL from type A and 25 mL from type B</li>
	<li>pour 50 mL from type A and 50 mL from type B</li>
	<li>pour 25 mL from type A and 75 mL from type B</li>
</ul>

**Note:**

<ul>
	<li>There is no operation that pours 0 mL from A and 100 mL from B.</li>
	<li>The amounts from A and B are poured *simultaneously* during the turn.</li>
	<li>If an operation asks you to pour **more than** you have left of a soup, pour all that remains of that soup.</li>
</ul>

The process stops immediately after any turn in which *one of the soups* is used up.

Return the probability that A is used up *before* B, plus half the probability that both soups are used up in the** same turn**. Answers within `10^-5` of the actual answer will be accepted.
