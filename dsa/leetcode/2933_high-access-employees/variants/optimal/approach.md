## General

**Compare accesses only within one employee.** Group every timestamp by name
and convert `HHMM` to minutes after midnight. This conversion makes time
differences ordinary integer subtraction and deliberately gives no wraparound
between the end and beginning of the day.

**A qualifying triple becomes consecutive after sorting.** Sort each
employee's access minutes. If any three accesses fit within a period shorter
than one hour, take the earliest member of such a triple. The next two accesses
in sorted order occur no later than the other two chosen accesses, so those
three consecutive entries also span fewer than 60 minutes. Conversely, any
consecutive triple whose third time minus its first is below 60 directly proves
that the employee is high-access.

It is therefore enough to inspect `minutes[i + 2] - minutes[i]` for every
valid index after sorting. Use the strict comparison `< 60`: a difference of
exactly 60 minutes is explicitly excluded. Add the employee once as soon as a
qualifying triple is found. Sorting the final names is optional for the problem
but makes the app-local result deterministic.

## Complexity detail

Let $n=\lvert\texttt{access\_times}\rvert$. Grouping and scanning take
$O(n)$ time. Across all employees, sorting costs at most $O(n\log n)$ time.
The grouped minute lists and returned names use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Repeated window counting:** For every access, rescan that employee's full timeline to count the following hour; this is correct but can take $O(n^2)$ time.
- **Minute-frequency array:** A 1,440-slot array per employee permits a fixed-domain scan, but allocates substantially more space than the observed timestamps require.
- **Exactly 60 minutes:** A triple from `0800` through `0900` is not contained within one one-hour period because the inequality is strict.
- **Across midnight:** `2350` and `0005` are far apart within the same recorded day; the timeline must not wrap.
- **Repeated timestamps:** Multiple accesses at the same minute are separate records and can form a qualifying triple.
- **Any output order:** The contract permits arbitrary name order; sorting is only for deterministic presentation.
