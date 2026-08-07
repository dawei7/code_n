### 1. Description

Design the basic function of **Excel** and implement the function of the sum formula.

Implement the `Excel` class:

- `Excel(int height, char width)` Initializes the object with the `height` and the `width` of the sheet. The sheet is an integer matrix `mat` of size `height x width` with the row index in the range `[1, height]` and the column index in the range `['A', width]`. All the values should be **zero** initially.

- `void set(int row, char column, int val)` Changes the value at $\text{mat}[row][column]$ to be `val`.

- `int get(int row, char column)` Returns the value at $\text{mat}[row][column]$.

- `int sum(int row, char column, List<String> numbers)` Sets the value at $\text{mat}[row][column]$ to be the sum of cells represented by `numbers` and returns the value at $\text{mat}[row][column]$. This sum formula **should exist** until this cell is overlapped by another value or another sum formula. $\text{numbers}[i]$ could be on the format:

		<li>`"ColRow"` that represents a single cell.

			<li>For example, `"F7"` represents the cell $\text{mat}[7]['F']$.

		</li>
- `"ColRow1:ColRow2"` that represents a range of cells. The range will always be a rectangle where `"ColRow1"` represent the position of the top-left cell, and `"ColRow2"` represents the position of the bottom-right cell.

			<li>For example, `"B3:F7"` represents the cells $\text{mat}[i][j]$ for $3 \le i \le 7$ and $'B' \le j \le 'F'$.

		</li>

	</li>

### 2. Function Contract

**Inputs**

- `operations`: A sequence beginning with construction of `Excel`, followed by `set`, `get`, or `sum` calls.
- `arguments`: The matching constructor dimensions, cell coordinates and values, or formula-reference lists.

**Source-native interface**

`Excel(height, width)` creates a `height x width` integer sheet. Valid row indices are in `[1, height]`, valid columns are in `['A', width]`, and every cell initially contains `0`.

`set(row, column, val)` replaces the target cell's current literal or formula with the integer `val`.

`get(row, column)` returns the target cell's current integer value.

`sum(row, column, numbers)` replaces the target cell with a sum formula, returns its current value, and keeps that formula active until the target is overwritten. Each entry in `numbers` is either a single-cell reference such as `F7` or a rectangular range such as `B3:F7`; range endpoints are the top-left and bottom-right cells, and both endpoints are included.

**Return value**

The app-local operation trace returns `null` for construction and `set`, and returns the requested integer for every `get` and `sum` call.

### 3. Note

You could assume that there will not be any circular sum reference.

- For example, $\text{mat}[1]['A'] = sum(1, "B")$ and $\text{mat}[1]['B'] = sum(1, "A")$.

### 4. Examples

#### Example 1

```
**Input**
["Excel", "set", "sum", "set", "get"]
[[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]
**Output**
[null, null, 4, null, 6]

**Explanation**
Excel excel = new Excel(3, "C");
 // construct a 3*3 2D array with all zero.
 //   A B C
 // 1 0 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.set(1, "A", 2);
 // set mat[1]["A"] to be 2.
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.sum(3, "C", ["A1", "A1:B2"]); // return 4
 // set mat[3]["C"] to be the sum of value at mat[1]["A"] and the values sum of the rectangle range whose top-left cell is mat[1]["A"] and bottom-right cell is mat[2]["B"].
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 4
excel.set(2, "B", 2);
 // set mat[2]["B"] to be 2. Note mat[3]["C"] should also be changed.
 //   A B C
 // 1 2 0 0
 // 2 0 2 0
 // 3 0 0 6
excel.get(3, "C"); // return 6
```

### 5. Constraints

- $1 \le height \le 26$

- $'A' \le width \le 'Z'$

- $1 \le row \le height$

- $'A' \le column \le width$

- $-100 \le val \le 100$

- $1 \le \text{numbers.length} \le 5$

- $\text{numbers}[i]$ has the format `"ColRow"` or `"ColRow1:ColRow2"`.

- At most `100` calls will be made to `set`, `get`, and `sum`.