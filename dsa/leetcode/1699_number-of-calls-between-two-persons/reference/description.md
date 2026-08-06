## Description

The `Calls` table records one phone call per row with a caller `from_id`, a different recipient `to_id`, and the call's `duration`. The table has no primary key and may contain duplicate rows. Direction identifies who initiated a row, but the requested report treats calls in both directions as interactions between the same pair of people.

Produce one row for each unordered pair that appears in the table. Name the smaller identifier `person1` and the larger identifier `person2`, so `person1 < person2`. Report the number of call rows between them as `call_count` and the sum of their durations as `total_duration`. Return the pair rows in any order.
