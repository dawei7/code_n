## Description

Two people each provide the time slots during which they are available. A slot is written as `[start, end]` and represents the inclusive time range from `start` through `end`.

Within either person's schedule, distinct availability slots never intersect. For any two slots `[start1, end1]` and `[start2, end2]` belonging to the same person, either `start1 > end2` or `start2 > end1`.

Given both schedules and a required positive `duration`, find the earliest time slot that both people can use for exactly that duration. If no common availability is long enough, return an empty list.
