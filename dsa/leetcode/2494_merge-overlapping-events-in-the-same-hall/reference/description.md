## Description

The `HallEvents` table records the hall and inclusive start and end dates of scheduled events. Duplicate rows may be present.

Merge every set of overlapping events held in the same hall. Two events overlap when their inclusive date ranges share at least one day, so events ending and starting on the same date belong to one merged interval. Overlap is transitive: if one event connects two otherwise separate ranges, all three form a single interval. Events belonging to different halls never affect one another.

Return one row for each resulting merged interval. The rows may appear in any order.
