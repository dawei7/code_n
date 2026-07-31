## General

**Assign levels from the root.** The first recursive common table expression starts at the row whose `manager_id` is `NULL` and assigns level 1. Each recursive step joins a manager already reached to their direct reports and adds one to the level. Because every employee has one manager path to the CEO, this visits each row at its unique hierarchy depth.

**Materialize each reporting subtree.** The second recursive CTE begins with one self-pair `(manager_id, member_id)` for every employee. Recursion extends each pair from its current member to that member's direct reports. Its completed rows are therefore exactly the ancestor-or-self relationships in the organization, and each row carries the member's salary.

Group that closure by its originating manager. Counting members and subtracting one excludes the manager from `team_size`; summing their salaries includes the manager and yields `budget`. Joining these aggregates to the level rows ensures that leaves remain present: their closure contains only their self-pair, so their team size is zero and their budget is their own salary.

Finally order by level ascending, the aggregate budget descending, and employee name ascending. The level CTE proves each employee's depth, while the closure construction proves that the corresponding aggregate includes every direct and indirect report exactly once.

## Complexity detail

Let $n$ be the employee count and $a$ the number of ancestor-or-self pairs in the hierarchy. The two recursive traversals and grouping process $O(a+n)$ rows, while ordering the $n$ result rows costs $O(n\log n)$. With an index on `manager_id`, or the database engine's equivalent recursive-join optimization, total time is $O(a+n\log n)$. A chain has $a=n(n+1)/2$, whereas a star has $a=2n-1$.

The recursive closure contains $a$ rows, and the level and result working sets contain $O(n)$ rows, so auxiliary database space is $O(a+n)$.

## Alternatives and edge cases

- **Correlated recursive query per employee:** Rebuilding or rescanning the descendant relation separately for every result row repeats closure work and can become cubic on a chain.
- **Fixed-depth self-joins:** A query with a predetermined number of joins silently misses employees below that depth.
- **Direct reports only:** Grouping solely on `manager_id` omits indirect reports from both `team_size` and `budget`.
- **Path strings:** Encoding ancestry as delimited text can work, but prefix or substring matching is more fragile and usually forces repeated scans.
- **CEO row:** The CEO is level 1, controls every other employee, and must appear in the result.
- **Leaf employee:** The self-pair produces team size zero and a budget equal to the leaf's salary.
- **Budget inclusion:** A manager's own salary is included even though the manager is excluded from their team size.
- **Arbitrary identifiers and row order:** Recursion follows manager keys, not identifier order or physical table order.
- **Ordering ties:** Equal level and budget values are resolved by employee name ascending, not employee ID.
- **Department:** The column describes employees but does not partition the hierarchy or its salary budgets.
