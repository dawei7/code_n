## Examples

**Example 1**

- **Input:** `Players = [[1, "Nadal"], [2, "Federer"], [3, "Novak"]], Championships = [[2018, 1, 1, 1, 1], [2019, 1, 1, 2, 2], [2020, 2, 1, 2, 2]]`

`Players` table:

| player_id | player_name |
|---:|---|
| 1 | Nadal |
| 2 | Federer |
| 3 | Novak |

`Championships` table:

| year | Wimbledon | Fr_open | US_open | Au_open |
|---:|---:|---:|---:|---:|
| 2018 | 1 | 1 | 1 | 1 |
| 2019 | 1 | 1 | 2 | 2 |
| 2020 | 2 | 1 | 2 | 2 |

- **Output:** `[[1, "Nadal", 7], [2, "Federer", 5]]`

| player_id | player_name | grand_slams_count |
|---:|---|---:|
| 1 | Nadal | 7 |
| 2 | Federer | 5 |

- **Explanation:**
  - Nadal (`1`): won 4 titles in 2018, 2 titles in 2019 (Wimbledon, Fr_open), 1 title in 2020 (Fr_open). Total $= 4 + 2 + 1 = 7$.
  - Federer (`2`): won 2 titles in 2019 (US_open, Au_open), 3 titles in 2020 (Wimbledon, US_open, Au_open). Total $= 2 + 3 = 5$.
  - Novak (`3`): won 0 titles, so excluded.

**Example 2**

- **Input:** `Players = [[7, "Serena"], [8, "Venus"]], Championships = [[2021, 7, 7, 7, 7]]`
- **Output:** `[[7, "Serena", 4]]`

- **Explanation:** Winning all four Grand Slam tournaments in a single calendar year contributes 4 to `grand_slams_count`.

**Example 3**

- **Input:** `Players = [[1, "A"], [2, "B"], [3, "C"], [4, "D"]], Championships = [[2024, 1, 2, 3, 4]]`
- **Output:** `[[1, "A", 1], [2, "B", 1], [3, "C", 1], [4, "D", 1]]`

- **Explanation:** Each tournament column contributes its respective champion independently.
