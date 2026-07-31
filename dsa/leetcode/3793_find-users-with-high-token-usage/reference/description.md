## Description

The `prompts` table records prompts sent by users to an AI system and the token consumption of each request:

| Column | Type | Meaning |
|---|---|---|
| `user_id` | `int` | Identifier of the submitting user |
| `prompt` | `varchar` | Prompt text |
| `tokens` | `int` | Tokens consumed by the prompt |

The pair (`user_id`, `prompt`) is the table's primary key, so no user has two rows with the same prompt text.

Analyze usage separately for each user. Report the number of submitted prompts and the average number of tokens per prompt, rounded to two decimal places. Retain a user only when they submitted at least three prompts and at least one of their prompts used strictly more tokens than their own average.

Order the result by average token usage from highest to lowest, then by `user_id` from lowest to highest.
