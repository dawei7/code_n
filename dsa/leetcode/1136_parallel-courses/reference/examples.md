## Examples

**Example 1**

- **Input:** `n = 3, relations = [[1,3],[2,3]]`
- **Output:** `2`
- **Explanation:** Courses `1` and `2` have no prerequisites, so both can be taken in the first semester. Their shared dependent course `3` can then be taken in the second semester.

The source graph is reproduced independently below. Every arrow points from a prerequisite to its dependent course.

```mermaid
---
config:
  flowchart:
    nodeSpacing: 55
    rankSpacing: 50
---
graph TB
    accTitle: Two prerequisite courses converge on course 3
    accDescr: Directed arrows run from course 1 to course 3 and from course 2 to course 3. Courses 1 and 2 form the first semester; course 3 forms the second.
    C1((1)) --> C3((3))
    C2((2)) --> C3
```

**Example 2**

- **Input:** `n = 3, relations = [[1,2],[2,3],[3,1]]`
- **Output:** `-1`
- **Explanation:** The three relationships form a directed cycle. Each course waits for another course in that same cycle, so none can be taken first.

The source graph is reproduced independently as the complete prerequisite cycle:

```mermaid
---
config:
  flowchart:
    nodeSpacing: 55
    rankSpacing: 50
---
graph LR
    accTitle: Three-course prerequisite cycle
    accDescr: Course 1 is required before course 2, course 2 before course 3, and course 3 before course 1, leaving no eligible starting course.
    C1((1)) --> C2((2))
    C2 --> C3((3))
    C3 --> C1
```
