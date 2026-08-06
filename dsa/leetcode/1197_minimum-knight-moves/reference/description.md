## Description

An infinite chessboard is indexed by integer coordinates in every direction. A knight begins at `[0,0]` and may make any standard knight move: two squares along one cardinal direction followed by one square along the perpendicular axis.

The source illustration's information is reproduced accessibly below. These are all eight possible coordinate changes from any square:

| Change in x | Change in y |
|---:|---:|
| `+2` | `+1` |
| `+2` | `-1` |
| `-2` | `+1` |
| `-2` | `-1` |
| `+1` | `+2` |
| `+1` | `-2` |
| `-1` | `+2` |
| `-1` | `-2` |

Given the destination `[x,y]`, determine the minimum number of moves needed to reach it. A route to every valid target is guaranteed to exist.
