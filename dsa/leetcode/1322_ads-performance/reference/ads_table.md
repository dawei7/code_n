## Ads Table

| Column Name | Type |
|---|---|
| `ad_id` | `int` |
| `user_id` | `int` |
| `action` | `enum` |

The pair (`ad_id`, `user_id`) is the primary key, so a user contributes at most one row to a particular advertisement. Each row identifies an advertisement, a user, and that user's action for the advertisement. `action` is one of `Clicked`, `Viewed`, or `Ignored`.
