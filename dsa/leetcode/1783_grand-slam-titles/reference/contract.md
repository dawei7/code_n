## Function Contract

**Database Schemas**

**`Players`**

| Column | Type | Meaning |
|---|---|---|
| `player_id` | int | Unique player identifier. |
| `player_name` | varchar | Display name of the player. |

**`Championships`**

| Column | Type | Meaning |
|---|---|---|
| `year` | int | Year of the championships. |
| `Wimbledon` | int | Player ID of the Wimbledon winner. |
| `Fr_open` | int | Player ID of the French Open winner. |
| `US_open` | int | Player ID of the US Open winner. |
| `Au_open` | int | Player ID of the Australian Open winner. |

**Return value**

Return columns `player_id`, `player_name`, and `grand_slams_count`. Include only players who won at least one Grand Slam tournament. `grand_slams_count` is the total number of titles won across all four tournament columns and years. Row order is unrestricted.
