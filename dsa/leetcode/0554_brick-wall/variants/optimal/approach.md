## General
**Convert brick boundaries into horizontal positions**

Within each row, accumulate brick widths from the left. Every partial sum before the final brick is an internal edge where a vertical line can pass without crossing that row's brick.

**Count how many rows share each edge**

Use a hash table from cumulative position to its frequency across rows. A row contributes at most once to a position because all brick widths are positive.

**Choose the most frequent internal edge**

If a position is an edge in `e` rows, the line avoids bricks in those rows and crosses one brick in each of the remaining $r - e$ rows. Maximizing `e` therefore minimizes the crossings. If no internal edge exists, every legal line crosses all rows.

**Why excluding the final sum matters**

The cumulative sum after a row's last brick is the wall's right outer boundary. Counting it would make every row appear avoidable and incorrectly return zero for any wall, even though lines along the outer sides are forbidden.

## Complexity detail
Let `B` be the total number of bricks. Every brick except each row's last is included in one cumulative update and hash operation, so time is $O(B)$. At most $O(B)$ distinct internal positions are stored.

## Alternatives and edge cases
- **Test every edge against every row:** is correct but repeatedly locates the containing brick and can take $O(B^2)$ time.
- **Sort all edge positions:** the most common run can be found after sorting in $O(B \log B)$ time and $O(B)$ space.
- **One brick per row:** supplies no internal edges, so every row is crossed.
- **Single row with several bricks:** a line can follow any internal edge and cross zero bricks.
- **Perfectly aligned rows:** a shared internal edge across every row yields zero crossings.
- **Different brick partitions:** only cumulative positions matter, not brick indices.
- **Outer boundaries:** neither position zero nor the full wall width is a legal candidate.
