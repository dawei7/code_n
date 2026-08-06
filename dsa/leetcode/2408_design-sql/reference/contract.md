## Function Contract

**Inputs**

- `SQL(names: List[str], columns: List[int])`: Initializes database tables with matching names and column counts.
- `ins(name: str, row: List[str]) -> bool`: Inserts `row` into table `name` if valid; returns `True` if inserted, `False` otherwise.
- `rmv(name: str, rowId: int) -> None`: Removes row `rowId` from table `name`.
- `sel(name: str, rowId: int, columnId: int) -> str`: Returns string value at 1-indexed `columnId` of row `rowId` in table `name`, or `"<null>"` if missing/invalid.
- `exp(name: str) -> List[str]`: Returns list of CSV-formatted strings `"id,val1,val2,..."` for surviving rows in table `name`, or `[]` if unknown.

**Return value**

Each operation returns its specified type (`None`, `bool`, `str`, or `List[str]`).
