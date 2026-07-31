## Description

The `reactions` table records how users respond to pieces of content:

| Column | Type | Meaning |
|---|---|---|
| `user_id` | `int` | Identifier of the user who reacted |
| `content_id` | `int` | Identifier of the content receiving the reaction |
| `reaction` | `varchar` | The reaction type selected by the user |

The pair (`user_id`, `content_id`) is the primary key. Consequently, a user contributes at most one row for any one piece of content, and each row represents one reaction to one distinct content item.

Identify the **emotionally consistent users** according to all of these requirements:

1. Count every reaction made by each user.
2. Consider only users who reacted to at least five different content items.
3. A considered user is emotionally consistent when one reaction type accounts for at least 60% of that user's reactions.

For every qualifying user, report the reaction type meeting that threshold as `dominant_reaction` and its share of the user's reactions as `reaction_ratio`. Order the result by `reaction_ratio` in descending order, followed by `user_id` in ascending order.
