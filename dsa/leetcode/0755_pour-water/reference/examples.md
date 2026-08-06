## Examples

**Example 1**

- Input: `heights = [2,1,1,2,1,2,2], volume = 4, k = 3`
- Output: `[2,2,2,3,2,2,2]`
- Explanation: A droplet may travel only through positions at the same or a lower current level. The five source diagrams distinguish the original terrain from settled water and place infinitely high walls outside indices `0` and `6`; the tables below preserve that information at every stage.

Before any water is poured:

| Component \ Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Terrain | 2 | 1 | 1 | 2 | 1 | 2 | 2 |
| Settled water | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Total level | 2 | 1 | 1 | 2 | 1 | 2 | 2 |

The first droplet begins at `k = 3`. Moving left eventually lowers it, so it settles at index `2`; continuing farther left from that level would not make it fall again.

| Component \ Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Terrain | 2 | 1 | 1 | 2 | 1 | 2 | 2 |
| Settled water | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| Total level | 2 | 1 | 2 | 2 | 1 | 2 | 2 |

The second droplet also moves left and settles at index `1`. Left remains preferred even though moving right could make this droplet fall sooner.

| Component \ Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Terrain | 2 | 1 | 1 | 2 | 1 | 2 | 2 |
| Settled water | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| Total level | 2 | 2 | 2 | 2 | 1 | 2 | 2 |

For the third droplet, moving left would no longer produce a lower level. It therefore tries the right side and settles at index `4`.

| Component \ Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Terrain | 2 | 1 | 1 | 2 | 1 | 2 | 2 |
| Settled water | 0 | 1 | 1 | 0 | 1 | 0 | 0 |
| Total level | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

For the fourth droplet, neither the left nor the right direction would eventually lower it, so it stays at `k = 3`.

| Component \ Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Terrain | 2 | 1 | 1 | 2 | 1 | 2 | 2 |
| Settled water | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
| Total level | 2 | 2 | 2 | 3 | 2 | 2 | 2 |

**Example 2**

- Input: `heights = [1,2,3,4], volume = 2, k = 2`
- Output: `[2,3,3,4]`
- Explanation: The last droplet settles at index `1`; moving farther left from there would not eventually take it to a lower level.

**Example 3**

- Input: `heights = [3,1,3], volume = 5, k = 1`
- Output: `[4,4,4]`
