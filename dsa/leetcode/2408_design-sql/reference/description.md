### 1. Description

You are given two string arrays, `names` and `columns`, both of size `n`. The $$i^{\text{th}}$$ table is represented by the name $\text{names}[i]$ and contains $\text{columns}[i]$ number of columns.

You need to implement a class that supports the following **operations**:

- **Insert** a row in a specific table with an id assigned using an *auto-increment* method, where the id of the first inserted row is 1, and the id of each *new *row inserted into the same table is **one greater** than the id of the **last inserted** row, even if the last row was *removed*.

- **Remove** a row from a specific table. Removing a row **does not** affect the id of the next inserted row.

- **Select** a specific cell from any table and return its value.

- **Export** all rows from any table in csv format.

Implement the `SQL` class:

- `SQL(String[] names, int[] columns)`

		- Creates the `n` tables.

- `bool ins(String name, String[] row)`

		- Inserts `row` into the table `name` and returns `true`.

- If `row.length` **does not** match the expected number of columns, or `name` is **not** a valid table, returns `false` without any insertion.

- `void rmv(String name, int rowId)`

		- Removes the row `rowId` from the table `name`.

- If `name` is **not** a valid table or there is no row with id `rowId`, no removal is performed.

- `String sel(String name, int rowId, int columnId)`

		- Returns the value of the cell at the specified `rowId` and `columnId` in the table `name`.

- If `name` is **not** a valid table, or the cell `(rowId, columnId)` is **invalid**, returns `"<null>"`.

- `String[] exp(String name)`

		- Returns the rows present in the table `name`.

- If name is **not** a valid table, returns an empty array. Each row is represented as a string, with each cell value (**including** the row's id) separated by a `","`.

### 2. Function Contract

**Inputs**

- $SQL(names: \text{List}[str], columns: \text{List}[int])$: Initializes database tables with matching names and column counts.
- $ins(name: str, row: \text{List}[str]) -> bool$: Inserts `row` into table `name` if valid; returns `True` if inserted, `False` otherwise.
- `rmv(name: str, rowId: int) -> None`: Removes row `rowId` from table `name`.
- `sel(name: str, rowId: int, columnId: int) -> str`: Returns string value at 1-indexed `columnId` of row `rowId` in table `name`, or `"<null>"` if missing/invalid.
- $exp(name: str) -> \text{List}[str]$: Returns list of CSV-formatted strings `"id,val1,val2,..."` for surviving rows in table `name`, or `[]` if unknown.

**Return value**

Each operation returns its specified type (`None`, `bool`, `str`, or $\text{List}[str]$).

### 3. Examples

#### Example 1

- **Input:** 

```
["SQL","ins","sel","ins","exp","rmv","sel","exp"]
[[["one","two","three"],[2,3,1]],["two",["first","second","third"]],["two",1,3],["two",["fourth","fifth","sixth"]],["two"],["two",1],["two",2,2],["two"]]
```

- **Output:** 

```
[null,true,"third",true,["1,first,second,third","2,fourth,fifth,sixth"],null,"fifth",["2,fourth,fifth,sixth"]]
```

- **Explanation:** ```
// Creates three tables.
SQL sql = new SQL(["one", "two", "three"], [2, 3, 1]);

// Adds a row to the table "two" with id 1. Returns True.
sql.ins("two", ["first", "second", "third"]);

// Returns the value "third" from the third column
// in the row with id 1 of the table "two".
sql.sel("two", 1, 3);

// Adds another row to the table "two" with id 2. Returns True.
sql.ins("two", ["fourth", "fifth", "sixth"]);

// Exports the rows of the table "two".
// Currently, the table has 2 rows with ids 1 and 2.
sql.exp("two");

// Removes the first row of the table "two". Note that the second row
// will still have the id 2.
sql.rmv("two", 1);

// Returns the value "fifth" from the second column
// in the row with id 2 of the table "two".
sql.sel("two", 2, 2);

// Exports the rows of the table "two".
// Currently, the table has 1 row with id 2.
sql.exp("two");
```

#### Example 2

- **Input:** 

```
["SQL","ins","sel","rmv","sel","ins","ins"]
[[["one","two","three"],[2,3,1]],["two",["first","second","third"]],["two",1,3],["two",1],["two",1,2],["two",["fourth","fifth"]],["two",["fourth","fifth","sixth"]]]
```

- **Output:** 

```
[null,true,"third",null,"<null>",false,true]
```

- **Explanation:** ```
// Creates three tables.
SQL sQL = new SQL(["one", "two", "three"], [2, 3, 1]);

// Adds a row to the table "two" with id 1. Returns True.
sQL.ins("two", ["first", "second", "third"]);

// Returns the value "third" from the third column
// in the row with id 1 of the table "two".
sQL.sel("two", 1, 3);

// Removes the first row of the table "two".
sQL.rmv("two", 1);

// Returns "<null>" as the cell with id 1
// has been removed from table "two".
sQL.sel("two", 1, 2);

// Returns False as number of columns are not correct.
sQL.ins("two", ["fourth", "fifth"]);

// Adds a row to the table "two" with id 2. Returns True.
sQL.ins("two", ["fourth", "fifth", "sixth"]);
```

### 4. Constraints

- $n = \text{names.length} = \text{columns.length}$

- $1 \le n \le 10^{4}$

- $1 \le \text{names}[i].length, \text{row}[i].length, \text{name.length} \le 10$

- $\text{names}[i]$, $\text{row}[i]$, and `name` consist only of lowercase English letters.

- $1 \le \text{columns}[i] \le 10$

- $1 \le \text{row.length} \le 10$

- All $\text{names}[i]$ are **distinct**.

- At most `2000` calls will be made to `ins` and `rmv`.

- At most $10^{4}$ calls will be made to `sel`.

- At most `500` calls will be made to `exp`.

### 5. Follow-up

Which approach would you choose if the table might become sparse due to many deletions, and why? Consider the impact on memory usage and performance.
