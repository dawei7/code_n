## Description

Alice takes exams over time and wants a tracker that can record each result and total the scores earned during a requested time interval.

Implement the `ExamTracker` class with these operations:

- `ExamTracker()` creates an empty tracker.
- `record(time, score)` records an exam taken at `time` with the given `score`.
- `totalScore(startTime, endTime)` returns the sum of the scores recorded at times in the inclusive interval from `startTime` through `endTime`. Return `0` when that interval contains no recorded exam.

Calls arrive chronologically. In particular, successive `record` operations use strictly increasing times, and a query never asks beyond the latest recorded time. If the most recent record occurred at time `t`, every query satisfies `startTime <= endTime <= t`.
