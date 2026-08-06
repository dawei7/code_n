## Description

`SeasonStats` contains one row for each team participating in a season, including its match results and goals scored and conceded. Derive two performance measures for every row: `points`, where each win contributes three and each draw contributes one, and `goal_difference`, equal to goals scored minus goals conceded.

Rank teams independently within each season. Greater points take precedence; when points tie, greater goal difference takes precedence; when both measures tie, the alphabetically earlier team name takes precedence. Return every team with its derived measures and one-based position. Order the complete result by `season_id` ascending, then position ascending, then `team_name` ascending.
