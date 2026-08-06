## Description

You are given an `m x n` 2D array `grid` of **positive** integers.

Your task is to traverse `grid` in a **zigzag** pattern while skipping every **alternate** cell.

Zigzag pattern traversal is defined as following the below actions:

<ul>
	<li>Start at the top-left cell `(0, 0)`.</li>
	<li>Move *right* within a row until the end of the row is reached.</li>
	<li>Drop down to the next row, then traverse *left* until the beginning of the row is reached.</li>
	<li>Continue **alternating** between right and left traversal until every row has been traversed.</li>
</ul>

**Note **that you **must skip** every *alternate* cell during the traversal.

Return an array of integers `result` containing, **in order**, the value of the cells visited during the zigzag traversal with skips.
