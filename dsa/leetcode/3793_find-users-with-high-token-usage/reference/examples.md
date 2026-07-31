## Examples

**Example 1**

- Input: `prompts table (9 rows)`
- Output: `users 3 and 1 with their prompt counts and average tokens`
- Explanation: The input table is:

| `user_id` | `prompt` | `tokens` |
|---:|---|---:|
| 1 | `Write a blog outline` | 120 |
| 1 | `Generate SQL query` | 80 |
| 1 | `Summarize an article` | 200 |
| 2 | `Create resume bullet` | 60 |
| 2 | `Improve LinkedIn bio` | 70 |
| 3 | `Explain neural networks` | 300 |
| 3 | `Generate interview Q&A` | 250 |
| 3 | `Write cover letter` | 180 |
| 3 | `Optimize Python code` | 220 |

The result is:

| `user_id` | `prompt_count` | `avg_tokens` |
|---:|---:|---:|
| 3 | 4 | 237.5 |
| 1 | 3 | 133.33 |

- **User 1:** This user submitted three prompts. Their average is `(120 + 80 + 200) / 3 = 133.33`, and the 200-token prompt exceeds that average, so the user is included.
- **User 2:** This user submitted only two prompts, below the required minimum, so the user is excluded.
- **User 3:** This user submitted four prompts with average `(300 + 250 + 180 + 220) / 4 = 237.5`. Both the 300-token and 250-token prompts exceed the average, so the user is included.

User 3 precedes user 1 because `237.5` is the larger average. The secondary ascending `user_id` key would decide their order if those averages were equal.
