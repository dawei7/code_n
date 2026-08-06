## Function Contract

**Class operations**

- `LogSystem()`: Create an empty log storage system.
- `put(id, timestamp)`: Store the log identified by `id` at `timestamp`.
- `retrieve(start, end, granularity)`: Return all stored IDs whose timestamps fall within the inclusive range at the requested precision.

Both query boundaries use the same `Year:Month:Day:Hour:Minute:Second` format as stored timestamps. When `granularity` is, for example, `Day`, compare the year, month, and day fields and ignore hour, minute, and second. Apply the same rule to every other supported precision.

The result of each retrieval is a collection of every matching ID; no ordering among those IDs is required. In the app-local operation trace, construction and `put` produce `null`, while each `retrieve` produces its ID list in the corresponding result position.
