# Design SQL

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2408 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-sql/) |

## Problem Description

### Goal

Create an in-memory database containing several named tables. Each table has a fixed number of user columns and assigns row IDs independently, beginning at 1. A successful insertion receives the next ID for its table. IDs are never reused: deleting the latest row does not change the ID that a later insertion receives.

Support inserting a correctly sized row, removing a row, selecting a one-indexed column from a row, and exporting a table's surviving rows as comma-separated strings that begin with their IDs. Invalid table names and malformed inserts must follow their specified failure results without changing state. Missing rows or invalid cells select as `"<null>"`, while exporting an unknown table produces an empty list.

### Function Contract

**Inputs**

- `operations`: A sequence beginning with `"SQL"` and followed by method names `"ins"`, `"rmv"`, `"sel"`, or `"exp"`.
- `arguments`: The argument list paired with every operation. Construction receives distinct table `names` and their `columns`; later entries contain the arguments for that method.

Let $n$ be the number of tables, $q$ the number of later operations, $S$ the number of user cells currently stored, and $E$ the total number of cells materialized by all exports.

Table names and cell values contain lowercase English letters. There are at most $10^4$ tables and selects, 2,000 insertions and removals, and 500 exports. Each table and inserted row has between 1 and 10 user columns.

**Return value**

Return one result per operation: `null` for construction and removals, booleans for insertions, strings for selections, and lists of CSV row strings for exports.

### Examples

**Example 1**

- Input: `operations = ["SQL","ins","sel","ins","exp","rmv","sel","exp"]`, `arguments = [[["one","two","three"],[2,3,1]],["two",["first","second","third"]],["two",1,3],["two",["fourth","fifth","sixth"]],["two"],["two",1],["two",2,2],["two"]]`
- Output: `[null,true,"third",true,["1,first,second,third","2,fourth,fifth,sixth"],null,"fifth",["2,fourth,fifth,sixth"]]`

**Example 2**

- Input: `operations = ["SQL","ins","sel","rmv","sel","ins","ins"]`, `arguments = [[["one","two","three"],[2,3,1]],["two",["first","second","third"]],["two",1,3],["two",1],["two",1,2],["two",["fourth","fifth"]],["two",["fourth","fifth","sixth"]]]`
- Output: `[null,true,"third",null,"<null>",false,true]`

**Example 3**

- Input: `operations = ["SQL","ins","rmv","ins","exp"]`, `arguments = [[["data"],[1]],["data",["alpha"]],["data",1],["data",["beta"]],["data"]]`
- Output: `[null,true,null,true,["2,beta"]]`
