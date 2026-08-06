## Description

You are given two string arrays, `names` and `columns`, both of size `n`. The `i^th` table is represented by the name `names[i]` and contains `columns[i]` number of columns.

You need to implement a class that supports the following **operations**:

<ul>
	<li>**Insert** a row in a specific table with an id assigned using an *auto-increment* method, where the id of the first inserted row is 1, and the id of each *new *row inserted into the same table is **one greater** than the id of the **last inserted** row, even if the last row was *removed*.</li>
	<li>**Remove** a row from a specific table. Removing a row **does not** affect the id of the next inserted row.</li>
	<li>**Select** a specific cell from any table and return its value.</li>
	<li>**Export** all rows from any table in csv format.</li>
</ul>

Implement the `SQL` class:

<ul>
	<li>`SQL(String[] names, int[] columns)`

	<ul>
		<li>Creates the `n` tables.</li>
	</ul>
	</li>
	<li>`bool ins(String name, String[] row)`
	<ul>
		<li>Inserts `row` into the table `name` and returns `true`.</li>
		<li>If `row.length` **does not** match the expected number of columns, or `name` is **not** a valid table, returns `false` without any insertion.</li>
	</ul>
	</li>
	<li>`void rmv(String name, int rowId)`
	<ul>
		<li>Removes the row `rowId` from the table `name`.</li>
		<li>If `name` is **not** a valid table or there is no row with id `rowId`, no removal is performed.</li>
	</ul>
	</li>
	<li>`String sel(String name, int rowId, int columnId)`
	<ul>
		<li>Returns the value of the cell at the specified `rowId` and `columnId` in the table `name`.</li>
		<li>If `name` is **not** a valid table, or the cell `(rowId, columnId)` is **invalid**, returns `"<null>"`.</li>
	</ul>
	</li>
	<li>`String[] exp(String name)`
	<ul>
		<li>Returns the rows present in the table `name`.</li>
		<li>If name is **not** a valid table, returns an empty array. Each row is represented as a string, with each cell value (**including** the row's id) separated by a `","`.</li>
	</ul>
	</li>
</ul>
