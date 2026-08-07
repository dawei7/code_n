### 1. Description

Alice frequently takes exams and wants to track her scores and calculate the total scores over specific time periods.

Implement the `ExamTracker` class:

- `ExamTracker()`: Initializes the `ExamTracker` object.

- `void record(int time, int score)`: Alice takes a new exam at time `time` and achieves the score `score`.

- `long long totalScore(int startTime, int endTime)`: Returns an integer that represents the **total** score of all exams taken by Alice between `startTime` and `endTime` (inclusive). If there are no recorded exams taken by Alice within the specified time interval, return 0.

It is guaranteed that the function calls are made in chronological order. That is,

- Calls to `record()` will be made with **strictly increasing** `time`.

- Alice will never ask for total scores that require information from the future. That is, if the latest `record()` is called with $time = t$, then `totalScore()` will always be called with $startTime \le endTime \le t$.

### 2. Function Contract

**Inputs**

- `operations`: A chronological list beginning with `"ExamTracker"`, followed by `"record"` and `"totalScore"` operation names.
- `arguments`: A parallel list whose entry contains no values for construction, `[time, score]` for `record`, or `[startTime, endTime]` for `totalScore`.

The canonical class API constructs one `ExamTracker` object and applies the listed calls to it. Let $q$ be the total number of post-construction calls and $r$ the number of `record` calls.

**Return value**

Return one result per operation: `null` for construction and `record`, and the inclusive interval sum for `totalScore`. A query with no recorded time in its interval contributes `0`.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:**

["ExamTracker", "record", "totalScore", "record", "totalScore", "totalScore", "totalScore", "totalScore"]

[[], [1, 98], [1, 1], [5, 99], [1, 3], [1, 5], [3, 4], [2, 5]]

**Output:**

[null, null, 98, null, 98, 197, 0, 99]

**Explanation**

ExamTracker examTracker = new ExamTracker();

examTracker.record(1, 98); // Alice takes a new exam at time 1, scoring 98.

examTracker.totalScore(1, 1); // Between time 1 and time 1, Alice took 1 exam at time 1, scoring 98. The total score is 98.

examTracker.record(5, 99); // Alice takes a new exam at time 5, scoring 99.

examTracker.totalScore(1, 3); // Between time 1 and time 3, Alice took 1 exam at time 1, scoring 98. The total score is 98.

examTracker.totalScore(1, 5); // Between time 1 and time 5, Alice took 2 exams at time 1 and 5, scoring 98 and 99. The total score is $98 + 99 = 197$.

examTracker.totalScore(3, 4); // Alice did not take any exam between time 3 and time 4. Therefore, the answer is 0.

examTracker.totalScore(2, 5); // Between time 2 and time 5, Alice took 1 exam at time 5, scoring 99. The total score is 99.</div>

### 4. Constraints

- $1 \le time \le 10^{9}$

- $1 \le score \le 10^{9}$

- $1 \le startTime \le endTime \le t$, where `t` is the value of `time` from the most recent call of `record()`.

- Calls of `record()` will be made with **strictly increasing** `time`.

- After `ExamTracker()`, the first function call will always be `record()`.

- At most $10^{5}$ calls will be made in total to `record()` and `totalScore()`.