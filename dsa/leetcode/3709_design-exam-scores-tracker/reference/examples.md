## Examples

**Example 1**

- Input: `operations = ["ExamTracker", "record", "totalScore", "record", "totalScore", "totalScore", "totalScore", "totalScore"]; arguments = [[], [1, 98], [1, 1], [5, 99], [1, 3], [1, 5], [3, 4], [2, 5]]`
- Output: `[null, null, 98, null, 98, 197, 0, 99]`
- Explanation:

| Operation | Effect or interval contents | Result |
|---|---|---:|
| `ExamTracker()` | Create an empty tracker. | `null` |
| `record(1, 98)` | Record Alice's score `98` at time `1`. | `null` |
| `totalScore(1, 1)` | The exam at time `1` is included. | `98` |
| `record(5, 99)` | Record score `99` at time `5`. | `null` |
| `totalScore(1, 3)` | Only the score `98` at time `1` lies in the interval. | `98` |
| `totalScore(1, 5)` | Both exams are included, so the total is `98 + 99`. | `197` |
| `totalScore(3, 4)` | No exam time lies between `3` and `4`. | `0` |
| `totalScore(2, 5)` | Only the score `99` at time `5` is included. | `99` |
