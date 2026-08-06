## Description

The \`TeamStats\` table stores one row per Premier League team, identified by the unique column \`team_id\`. Each row also contains the team's name and its numbers of matches, wins, draws, and losses.

Produce a league table with \`team_name\`, \`points\`, \`position\`, and \`tier\`. Award three points per win, one per draw, and none per loss. Rank teams by descending points using competition positions, so equal totals share a position and later positions may have gaps.

Split positions into three point-based tiers: Tier 1 covers the top 33% of teams, Tier 2 the middle 33%, and Tier 3 the bottom 34%. Round each boundary upward; when a tied position reaches across a boundary, keep every team at that position in the higher tier. Return rows by descending points and then ascending \`team_name\`.
