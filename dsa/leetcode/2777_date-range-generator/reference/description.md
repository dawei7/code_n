## Description

Given a start date `start`, an end date `end`, and a positive integer `step`, create a generator that yields calendar dates beginning at `start` and continuing toward `end`. Consecutive yielded dates must be exactly `step` days apart.

The range is inclusive: yield `end` when it lies on the progression formed from `start`. If a step passes beyond `end`, stop without yielding that later date. Every yielded value must be a string in `YYYY-MM-DD` format.
