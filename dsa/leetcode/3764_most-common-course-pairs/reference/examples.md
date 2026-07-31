## Examples

**Example 1**

- Input: `course_completions` table (19 rows)

| `user_id` | `course_id` | `course_name` | `completion_date` | `course_rating` |
|---:|---:|---|---|---:|
| 1 | 101 | `Python Basics` | `2024-01-05` | 5 |
| 1 | 102 | `SQL Fundamentals` | `2024-02-10` | 4 |
| 1 | 103 | `JavaScript` | `2024-03-15` | 5 |
| 1 | 104 | `React Basics` | `2024-04-20` | 4 |
| 1 | 105 | `Node.js` | `2024-05-25` | 5 |
| 1 | 106 | `Docker` | `2024-06-30` | 4 |
| 2 | 101 | `Python Basics` | `2024-01-08` | 4 |
| 2 | 104 | `React Basics` | `2024-02-14` | 5 |
| 2 | 105 | `Node.js` | `2024-03-20` | 4 |
| 2 | 106 | `Docker` | `2024-04-25` | 5 |
| 2 | 107 | `AWS Fundamentals` | `2024-05-30` | 4 |
| 3 | 101 | `Python Basics` | `2024-01-10` | 3 |
| 3 | 102 | `SQL Fundamentals` | `2024-02-12` | 3 |
| 3 | 103 | `JavaScript` | `2024-03-18` | 3 |
| 3 | 104 | `React Basics` | `2024-04-22` | 2 |
| 3 | 105 | `Node.js` | `2024-05-28` | 3 |
| 4 | 101 | `Python Basics` | `2024-01-12` | 5 |
| 4 | 108 | `Data Science` | `2024-02-16` | 5 |
| 4 | 109 | `Machine Learning` | `2024-03-22` | 5 |

- Output: seven ordered course-transition rows

| `first_course` | `second_course` | `transition_count` |
|---|---|---:|
| `Node.js` | `Docker` | 2 |
| `React Basics` | `Node.js` | 2 |
| `Docker` | `AWS Fundamentals` | 1 |
| `JavaScript` | `React Basics` | 1 |
| `Python Basics` | `React Basics` | 1 |
| `Python Basics` | `SQL Fundamentals` | 1 |
| `SQL Fundamentals` | `JavaScript` | 1 |

- Explanation:

  - **User 1:** Six completed courses with an average rating of 4.5 satisfy both top-performer requirements.
  - **User 2:** Five completed courses with an average rating of 4.4 also satisfy both requirements.
  - **User 3:** Five courses meet the count boundary, but the 2.8 average is too low, so this user is excluded.
  - **User 4:** Every rating is 5, but only three courses were completed, so this user is excluded.
  - **Course pairs among the top performers:**
    - User 1 follows `Python Basics → SQL Fundamentals → JavaScript → React Basics → Node.js → Docker`.
    - User 2 follows `Python Basics → React Basics → Node.js → Docker → AWS Fundamentals`.
    - `Node.js → Docker` and `React Basics → Node.js` each occur twice, making them the most frequent transitions.

The result first orders those two frequency-2 rows by `first_course`; all remaining frequency-1 rows likewise use `first_course` and then `second_course` in ascending order.
