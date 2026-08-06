## Description

Create an in-memory database containing several named tables. Each table has a fixed number of user columns and assigns row IDs independently, beginning at 1. A successful insertion receives the next ID for its table. IDs are never reused: deleting the latest row does not change the ID that a later insertion receives.

Support inserting a correctly sized row, removing a row, selecting a one-indexed column from a row, and exporting a table's surviving rows as comma-separated strings that begin with their IDs. Invalid table names and malformed inserts must follow their specified failure results without changing state. Missing rows or invalid cells select as `"<null>"`, while exporting an unknown table produces an empty list.
