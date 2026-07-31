## General

Let $m$ be the number of rows in `EmployeeShifts`.

**Turn intervals into ordered events**

Each shift contributes a start event with delta `+1` and an end event with delta `-1`. Partition events by `employee_id`, then order them by time. At an equal time, place end events before start events. This tie rule implements the strict overlap definition: a shift that ends exactly when another begins is no longer active and must not form a pair.

**Count active shifts before each start**

Use a window sum of `delta` from the beginning of an employee's event sequence through the row immediately before the current event. At a start event, this sum is the number of that employee's earlier shifts whose ends have not yet occurred. Every such active shift overlaps the new one, so the value is exactly the number of new overlapping pairs introduced at that start.

Sum `active_before` over start events for each employee. Filter out zero sums and order the remaining groups by `employee_id`.

Every pair has one later-starting shift because start times are unique per employee. When that later shift begins, its earlier partner is counted precisely if the earlier end is strictly later. Thus each overlapping pair contributes once, touching pairs contribute zero times, and no pair can be duplicated.

## Complexity detail

The event relation has $2m$ rows. Partitioned event ordering dominates the linear event construction, window scan, and grouping, giving $O(m \log m)$ time in the general case. The event and window state can retain $O(m)$ rows.

## Alternatives and edge cases

- **Self-join all shift pairs:** Comparing every earlier/later pair is direct and correct but can take $O(m^2)$ time for one employee.
- **Use non-strict endpoint comparison:** Treating `end_time = start_time` as overlap incorrectly counts adjacent shifts.
- **Process starts before ends at a tie:** This has the same endpoint bug; end events must be applied first.
- An employee with one shift produces no output row.
- Fully nested shifts contribute every possible pair.
- A long shift can overlap several mutually disjoint shorter shifts, and each pair is counted separately.
- Employees are partitioned independently even when their clock times match.
- The unique `(employee_id, start_time)` key gives every same-employee pair an unambiguous earlier start.
- Output order is numeric `employee_id` ascending, and employees with zero overlaps are omitted.
