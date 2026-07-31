## General

The numeric `id` does not define “previous,” so first attach `ROW_NUMBER() OVER ()` to the table's presented scan order. This yields a consecutive `sequence_number` without reordering by `id`.

Seed a recursive CTE with sequence number one. For each following number, join the current source row to the previously filled row. If the current drink is non-null, retain it; otherwise `COALESCE(current_row.drink, previous_row.drink)` carries forward the already resolved drink.

Because the first drink is guaranteed non-null, the recursive state always contains a valid value to propagate. Inductively, after producing sequence position $i$, its drink equals the closest non-null source drink at or before $i$: the current non-null value replaces the state, while a null inherits the correct state from $i-1$. Ordering the final rows by `sequence_number` restores exactly the assigned input sequence.

## Complexity detail

Let $R$ be the number of `CoffeeShop` rows. Assigning and ordering sequence numbers and joining successive sequence positions requires $O(R\log R)$ logical work under the intended indexed/materialized execution plan, with $O(R)$ intermediate space. Actual SQL cost depends on the database optimizer, materialization strategy, and internal indexes.

## Alternatives and edge cases

- **User-defined variable:** A MySQL session variable can carry the previous drink in one scan, but expression-evaluation order and variable assignment make that formulation less portable and harder to reason about.
- **Correlated previous-row search:** Looking backward separately for every null row can require $O(R^2)$ work.
- **Order by `id`:** Numeric identifier order is unrelated to the presented row sequence and changes the meaning of “previous.”
- **Consecutive nulls:** The recursion inherits the already filled value, so runs of any length receive the same preceding drink.
- **Non-null row:** A new drink replaces the carried state immediately.
- **First row:** The contract's non-null guarantee provides the recursion's base value.
