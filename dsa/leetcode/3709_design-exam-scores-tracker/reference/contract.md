## Function Contract

**Inputs**

- `operations`: A chronological list beginning with `"ExamTracker"`, followed by `"record"` and `"totalScore"` operation names.
- `arguments`: A parallel list whose entry contains no values for construction, `[time, score]` for `record`, or `[startTime, endTime]` for `totalScore`.

The canonical class API constructs one `ExamTracker` object and applies the listed calls to it. Let $q$ be the total number of post-construction calls and $r$ the number of `record` calls.

**Return value**

Return one result per operation: `null` for construction and `record`, and the inclusive interval sum for `totalScore`. A query with no recorded time in its interval contributes `0`.
