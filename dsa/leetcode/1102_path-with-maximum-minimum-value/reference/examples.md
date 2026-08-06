## Examples

Bold values in the following grids recreate the path or threshold-connected cells highlighted by the source images, using accessible tables instead of copied provider artwork.

**Example 1**

- **Input:** `grid = [[5,4,5],[1,2,6],[7,4,6]]`
- **Output:** `4`

| **5** | **4** | **5** |
|---:|---:|---:|
| 1 | 2 | **6** |
| 7 | 4 | **6** |

- **Explanation:** The highlighted path has values `5 → 4 → 5 → 6 → 6`, whose minimum is 4; no path can achieve a larger score.

**Example 2**

- **Input:** `grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]`
- **Output:** `2`

| **2** | **2** | 1 | **2** | **2** | **2** |
|---:|---:|---:|---:|---:|---:|
| 1 | **2** | **2** | **2** | 1 | **2** |

The highlighted cells contain a corner-to-corner path whose minimum value is 2.

**Example 3**

- **Input:** `grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]`
- **Output:** `3`

| **3** | **4** | **6** | **3** | **4** |
|---:|---:|---:|---:|---:|
| 0 | 2 | 1 | 1 | **7** |
| **8** | **8** | **3** | 2 | **7** |
| **3** | 2 | **4** | **9** | **8** |
| **4** | 1 | 2 | 0 | 0 |
| **4** | **6** | **5** | **4** | **3** |

The highlighted cells connect the two corners while keeping every visited value at least 3.
