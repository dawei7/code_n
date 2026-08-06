## Description

A spreadsheet is a grid with 26 columns (labeled from `'A'` to `'Z'`) and a given number of `rows`. Each cell in the spreadsheet can hold an integer value between 0 and 10^5.

Implement the `Spreadsheet` class:

<ul>
	<li>`Spreadsheet(int rows)` Initializes a spreadsheet with 26 columns (labeled `'A'` to `'Z'`) and the specified number of rows. All cells are initially set to 0.</li>
	<li>`void setCell(String cell, int value)` Sets the value of the specified `cell`. The cell reference is provided in the format `"AX"` (e.g., `"A1"`, `"B10"`), where the letter represents the column (from `'A'` to `'Z'`) and the number represents a **1-indexed** row.</li>
	<li>`void resetCell(String cell)` Resets the specified cell to 0.</li>
	<li>`int getValue(String formula)` Evaluates a formula of the form `"=X+Y"`, where `X` and `Y` are **either** cell references or non-negative integers, and returns the computed sum.</li>
</ul>

**Note:** If `getValue` references a cell that has not been explicitly set using `setCell`, its value is considered 0.
