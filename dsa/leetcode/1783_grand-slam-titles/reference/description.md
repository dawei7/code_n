## Description

The `Players` table identifies tennis players by a unique `player_id` and records each player's name. The `Championships` table has one row per year. Its four tournament columns—`Wimbledon`, `Fr_open`, `US_open`, and `Au_open`—each store the `player_id` of that year's winner.

Report how many Grand Slam tournaments each player won across all years and all four tournament columns. A player who won several tournaments in one year receives credit for every title. Exclude players who never won a tournament, and return each remaining player's identifier, name, and total as `grand_slams_count`. The result rows may be in any order.
