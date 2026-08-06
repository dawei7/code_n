## Description

You are given a 2D integer array `items`, where `items[i] = [factor_i, price_i]` represents the `i^th` item. You are also given an integer `budget`.

There are unlimited copies of each item available for purchase. You may buy any number of copies of any items such that the total cost of the purchased copies is at most `budget`.

After buying items, you may receive free copies according to the following rules:

<ul>
	<li>Each purchased copy of item `i` can give you **at most one** free copy of another item `j`.</li>
	<li>The free item must satisfy `i != j` and `factor_i` divides `factor_j`.</li>
	<li>For each ordered pair `(i, j)`, you can receive a free copy of item `j` from purchases of item `i` **at most once**, regardless of how many copies of item `i` you buy.</li>
	<li>The same item `j` can be received multiple times for free if it is received from purchases of different item types.</li>
</ul>

Return the **maximum total number of item copies** you can obtain, including both purchased copies and free copies, while spending at most `budget` on purchased items.
