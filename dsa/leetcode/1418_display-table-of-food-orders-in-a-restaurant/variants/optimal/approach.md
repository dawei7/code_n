## General

**The output is a pivot table**

Each input row is an individual order with a customer, a table number, and one food item. The display table changes that row-oriented data into:

- One output row per table that appears in the orders.
- One output column per distinct food item.
- A count at the intersection of a table and food item.

This is often called a pivot or cross-tabulation. Two global orderings are also required: food columns alphabetically and table rows numerically.

**Collect table orders and the global food vocabulary**

The code creates:

```python
tables = defaultdict(list)
items = set()
```

`tables` maps a numeric table number to a list containing one food name for every order placed at that table. Repeated names are deliberately retained because each occurrence represents one ordered item.

`items` is a set of all distinct food names. A set removes duplicates, which is correct for headers: each food needs one column regardless of how many times it was ordered.

The input loop unpacks every row as:

```python
for _, table, foodItem in orders:
```

The underscore receives the customer name. Customer identity does not appear in the display table and does not affect counts, so it is intentionally ignored.

**Convert table numbers before sorting**

The statement `tables[int(table)].append(foodItem)` converts the table string to an integer. This is crucial for later numeric ordering. Sorting strings would place `"10"` before `"2"` because character comparison sees `'1'` before `'2'`. Sorting integers correctly produces 2 before 10.

The same loop adds `foodItem` to `items`. After all orders are processed, the mapping has every order grouped by table, and the set has every column name needed anywhere in the result.

**Build the header once**

`sorted_items = sorted(items)` converts the set into the required alphabetical food order. Every data row must use this identical order so that a count stays under its correct header.

The first result row is:

```python
ans = [["Table"] + sorted_items]
```

The literal `"Table"` labels the first column. Concatenating the sorted food names produces exactly the prescribed header.

**Create rows in numeric table order**

`for table in sorted(tables)` visits the integer keys from smallest to largest. A table appears in `tables` only if at least one order belongs to it, so the algorithm creates exactly the required restaurant tables and no empty invented tables.

For one table:

```python
cnt = Counter(tables[table])
```

counts every food occurrence in that table's list. If Ceviche appears twice, its counter value is two. A food ordered elsewhere but not at this table has no explicit Counter entry; reading `cnt[item]` returns zero rather than raising an error.

The row is:

```python
row = [str(table)] + [str(cnt[item]) for item in sorted_items]
```

The numeric key is converted back to a string because every output cell must be a string. The list comprehension visits the global food headers in exactly their established order and converts each count to a string as well.

Appending each row after the header completes the table.

**Trace the sample's table 3**

The three table-3 orders add `"Ceviche"`, `"Fried Chicken"`, and `"Ceviche"` to `tables[3]`. Its Counter is conceptually:

```text
Ceviche: 2
Fried Chicken: 1
```

The global sorted food list is `["Beef Burrito", "Ceviche", "Fried Chicken", "Water"]`. Looking up those four names in order yields 0, 2, 1, and 0. Prefixing `"3"` produces:

```text
["3", "0", "2", "1", "0"]
```

The zero for Beef Burrito is just as important as the positive counts: rectangular output requires a cell for every global food column.

**Why grouping with lists remains correct**

The first pass could increment nested counters immediately, but storing lists and creating one Counter per table later is logically equivalent. Each input order contributes exactly one food occurrence to exactly one table list. Counter then maps multiplicity to quantity without losing any order.

The customer name is safely discarded because the display asks about quantities by table and food, not distinct customers. If the same customer orders the same item twice, there are two input rows and both must be counted.

**Why the complete result is correct**

Every distinct food enters `items`, so no required header is missing, and set uniqueness prevents duplicate columns. Sorting establishes alphabetical order.

Every order enters the list for its integer table, so Counter produces the exact number of occurrences for each table-food pair. Reading every sorted item fills present counts and absent zeros in matching column order. Sorting integer keys establishes numeric row order. Finally, string conversion matches the requested output representation. Therefore, both content and layout are correct.

## Complexity detail

Let $N$ be the number of orders, $F$ the number of distinct food items, and $T$ the number of distinct tables. Collecting the mapping and set takes expected $O(N)$ time. Sorting food names costs $O(F\log F)$, and sorting table keys costs $O(T\log T)$.

Across all tables, building Counters scans exactly $N$ stored food occurrences. Constructing each rectangular row looks up all $F$ foods, costing $O(TF)$. Total time is:

$$
O(N + F\log F + T\log T + TF).
$$

The table lists store $N$ food references, the global set stores $F$ names, and the returned matrix contains roughly $(T+1)(F+1)$ cells. The manifest summarizes storage as $O(N+TF)$, with smaller $F$ and $T$ structures absorbed.

## Alternatives and edge cases

- **Nested counters during ingestion:** Use `counts[table][food] += 1` in the first pass. This avoids storing repeated food lists and can reduce intermediate memory while preserving the same output construction.
- **Sort all orders first:** Sorting by table and food can group occurrences, but it adds $O(N\log N)$ work when hash-based collection needs only expected linear ingestion.
- **Use table strings as keys:** This produces incorrect lexicographic row order for values such as 2 and 10 unless a numeric sort key is supplied.
- **One table:** The result contains one header and one data row; food columns still sort alphabetically.
- **One food type:** Every table row has one count column, including only tables that placed orders.
- **Food absent at a table:** Counter returns zero for the missing key, which is emitted as `"0"`.
- **Repeated identical orders:** Each input row is an order occurrence and correctly increments the count.
- **Spaces and capitalization in food names:** Python's default string ordering supplies the required lexicographical ordering for the exact names; names are not normalized.
- **Customer names:** They are irrelevant to aggregation and are intentionally ignored rather than treated as distinct-order filters.
- **Output types:** Table numbers and counts must be strings in the returned matrix, so both are explicitly converted.
