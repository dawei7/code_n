## General

The requested row is defined by an equality condition on `student_id`, while the output schema is a subset of the input columns. A boolean comparison against `101` produces a mask identifying the target row. Passing that mask and the ordered column list `['name', 'age']` to `.loc` performs row filtering and column projection together.

The identifier is unique, so the mask selects exactly one record. `.loc` retains that record's original values and emits only the two named columns in the supplied order, which matches the required result.

## Complexity detail

Let $n$ be the number of student rows. Constructing the equality mask examines every identifier, so the method takes $O(n)$ time and $O(n)$ auxiliary space for the boolean mask. The selected output contains one fixed-size row.

## Alternatives and edge cases

- **Boolean filtering followed by projection:** Filtering with bracket syntax and then selecting `name` and `age` has the same $O(n)$ time and space bounds, but `.loc` combines both dimensions in one expression.
- **Sort before filtering:** Sorting by `student_id` and then applying the filter remains correct but adds unnecessary $O(n \log n)$ work and may change row order in tasks without unique matches.
- **Column order:** The output must list `name` before `age` and omit `student_id`.
- **Target position:** Student `101` may occur anywhere in the input; position-based indexing is invalid.
- **Repeated names:** Names need not be unique, so selection must use `student_id`.
