[TOC]

## Solution

---

### Overview

We are asked to build a house with the shortest total travel distance to all buildings. To do so, we must be able to find the shortest distance between two cells: an empty land cell and a building. This process is then repeated for every empty land-building pair.
As such, an intuitive first step is to record the location of all buildings (1-valued cells) and empty land (0-valued cells) in separate vectors.

Then, for every empty land cell, traverse all buildings and add the Manhattan distance: $distance = |x1 - x2| + |y1 - y2|$, where `(x1, y1)` are the coordinates of empty land and `(x2, y2)` are the coordinates of a building.

But the problem here is that we have some blocked cells.
For example, in the below configuration the formula does not give the correct distance between P1 and P2. This is because there are **obstacles between the two points**.

![blocked paths](images/Slide1.PNG)

<br />

Since obstacles preclude us from using the formula, we will instead perform a level-wise Breadth-First Search (BFS) for each cell, where each level is 1 distance further away from the starting cell (traversing 4-directionally). As we expand our Breadth-First Search, we will not visit any cell that is blocked or any cell that has already been visited.

<br />

_Why did we choose to use BFS?_

> Our graph is not weighted. We can consider each edge to have the same weight of 1.
> Since the graph is unweighted, BFS can be used to find the shortest path between a starting cell and any other reachable cell.

> The actual distance calculation measures grid distance in terms of only horizontal and vertical movements. Since we can only move up, down, left, and right, we can apply BFS to calculate the actual distance.  At each iteration in the BFS, we will only consider expanding our search in the horizontal or vertical direction.

</br>

---

### Approach 1: BFS from Empty Land to All Buildings

**Intuition**

Our goal is to find the empty land cell with the shortest total distance to all buildings, so we must first find the shortest total distance to all buildings from each empty land cell.
As previously mentioned, this can be accomplished using BFS. For each empty cell (cell value equals 0) in the grid, start a BFS and sum all the distances to buildings (cell value equals 1) from this cell. We will also keep track of the number of buildings we have reached from this source cell (empty cell).
If we cannot reach all the buildings from the current empty cell, then it is not a valid empty cell. Furthermore, we can be certain that any cell visited during this BFS also cannot reach all of the buildings. So we will mark all cells visited during this BFS as obstacles to ensure that we do not start another BFS from this region.

**Algorithm**

1. For each empty cell ($\text{grid}[i][j]$ equals 0), start a BFS:
- In the BFS, traverse all 4-directionally adjacent cells that are not blocked or visited and keep track of the distance from the start cell. Each iteration adds 1 to the distance.
- Every time we reach a building, increment buildings reached counter `housesReached` by 1, and increase the total distance `distanceSum` by the current distance (i.e., the distance from the start cell to the building).
- If `housesReached` equals `totalHouses`, then return the total distance.
- Otherwise, the starting cell (and every cell visited during this BFS) cannot reach all of the buildings.  So set every visited empty land cell equal to 2 so that we do not start a new BFS from that cell and return $\text{INT}_{MAX}$.
2. Each time a total distance is returned from a BFS call, update the minimum distance (`minDistance`).
3. If it is possible to reach all buildings from any empty land cell, then return the minimum distance found. Otherwise, return `-1`.

![Slide 1](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide3.PNG)

![Slide 2](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide4.PNG)

![Slide 3](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide5.PNG)

![Slide 4](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide6.PNG)

![Slide 5](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide7.PNG)

![Slide 6](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide8.PNG)

![Slide 7](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide9.PNG)

![Slide 8](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide10.PNG)

![Slide 9](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide11.PNG)

![Slide 10](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide12.PNG)

![Slide 11](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide13.PNG)

![Slide 12](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide14.PNG)

![Slide 13](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide15.PNG)

![Slide 14](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide16.PNG)

![Slide 15](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide17.PNG)

![Slide 16](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide18.PNG)

![Slide 17](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide19.PNG)

![Slide 18](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide20.PNG)

![Slide 19](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide21.PNG)

![Slide 20](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide22.PNG)

![Slide 21](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide23.PNG)

![Slide 22](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide24.PNG)

![Slide 23](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide25.PNG)

![Slide 24](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide26.PNG)

![Slide 25](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide27.PNG)

![Slide 26](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide28.PNG)

![Slide 27](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide29.PNG)

![Slide 28](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide30.PNG)

![Slide 29](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide31.PNG)

![Slide 30](images/slideshow_317_shortest_distance_from_all_buildings_1_Slide32.PNG)

<br />

**Implementation**

```javascript
// Next four directions.
let dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

// BFS function to do bfs starting from (row, col).
let bfs = (grid, row, col, totalHouses) => {
    let rows = grid.length;
    let cols = grid[0].length;
    let distanceSum = 0;
    let housesReached = 0;

    // Use a queue to do a bfs, starting from cell located at (row, col).
    let queue = [[ row, col ]];

    // Keep track of visited cells.
    let vis = new Array(rows).fill(false).map(() => new Array(cols).fill(false));
    vis[row][col] = true;

    let steps = 0;

    while (queue.length && housesReached != totalHouses) {
        // Record the cells that we will explore in the next level
        let next_queue = [];
        for (let i = 0; i < queue.length; i++) {
            let curr = queue[i];
            row = curr[0];
            col = curr[1];

            // If this cell is a building, then add the distance from source to this cell
            // and we go past from this cell.
            if (grid[row][col] == 1) {
                distanceSum += steps;
                housesReached++;
                continue;
            }

            // This cell was empty cell, hence traverse the next cells which is not a blockage.
            dirs.forEach((dir) => {
                let nextRow = row + dir[0];
                let nextCol = col + dir[1];
                if (nextRow >= 0 && nextCol >= 0 && nextRow < rows && nextCol < cols) {
                    if (!vis[nextRow][nextCol] && grid[nextRow][nextCol] != 2) {
                        vis[nextRow][nextCol] = true;
                        next_queue.push([nextRow, nextCol]);
                    }
                }
            });
        }

        // Set the queue equal to the next level queue.
        queue = next_queue;
        // After traversing one level cells, increment the steps by 1 to reach to next level.
        steps++;
    }

    // If we did not reach all buildings, then any cell visited also cannot reach all buildings.
    // Set all cells visted to 2 so we do not check them again and return MAX_VALUE.
    if (housesReached != totalHouses) {
        for (let row = 0; row < rows; row++) {
            for (let col = 0; col < cols; col++) {
                if (grid[row][col] == 0 && vis[row][col]) {
                    grid[row][col] = 2;
                }
            }
        }
        return Number.MAX_VALUE;
    }

    // If we have reached all buildings then return the total distance calculated.
    return distanceSum;
};

let shortestDistance = function (grid) {
    let minDistance = Number.MAX_VALUE;
    let rows = grid.length;
    let cols = grid[0].length;
    let totalHouses = 0;

    for (let row = 0; row < rows; ++row) {
        for (let col = 0; col < cols; ++col) {
            if (grid[row][col] == 1) {
                totalHouses++;
            }
        }
    }

    // Find the min distance sum for each empty cell.
    for (let row = 0; row < rows; ++row) {
        for (let col = 0; col < cols; ++col) {
            if (grid[row][col] == 0) {
                minDistance = Math.min(minDistance, bfs(grid, row, col, totalHouses));
            }
        }
    }

    // If it is impossible to reach all buildings from any empty cell, then return -1.
    if (minDistance == Number.MAX_VALUE) {
        return -1;
    }
    return minDistance;
};
```

**Complexity Analysis**

Let $N$ and $M$ be the number of rows and columns in `grid` respectively.

-   Time Complexity: $O(N^2 \cdot M^2)$

    For each empty land, we will traverse to all other buildings.
    This will require $O($number of zeros $\cdot$ number of ones$)$ time and the number of zeros and ones in the matrix is of order $N \cdot M$.
    Consider that when half of the values in grid are 0 and half of the values are 1, the total elements in grid would be $(M \cdot N)$ so their counts are $(M \cdot N)/2$ and $(M \cdot N)/2$ respectively, thus giving time complexity $(M \cdot N)/2 \cdot (M \cdot N)/2$, that results in $O(N^2 \cdot M^2)$.

> In JavaScript implementation, for simplicity, we have used an array for the queue.
> Since popping elements from the front of an array is an $\mathcal{O}(n)$ operation, which is undesirable,
> instead of popping from the front of the `queue`, we will iterate over the `queue` and record cells to be explored in the next level in $\text{next}_{queue}$.
> Once the current `queue` has been traversed, we simply set `queue` equal to the $\text{next}_{queue}$.

-   Space Complexity: $O(N \cdot M)$

    We use an extra matrix to track the visited cells, and the queue will store each matrix element at most once during each BFS call.
    Hence, $O(N \cdot M)$ space is required.

<br/>

---

### Approach 2: BFS from Buildings to Empty Land

**Intuition**

In the previous approach, to get the minimum distance we started a BFS from each empty land (cell value equal to 0) to all the buildings (cell value equal to 1), but another way to look at the problem is starting from a building and finding all reachable empty lands.

If we can reach a building from an empty land, then we can also traverse the other way (i.e., reach empty land from a building).

When there are fewer buildings than empty lands, then this approach will require less time than the previous approach and vice versa. While, on average, this approach is not an improvement on the previous approach, it will serve as a mental stepping stone to better understand the third approach.

Previously, we were calculating the total minimum distance sum of one empty cell in one BFS traversal, hence we were only returning the distance sum from the BFS function for each cell.
But if we start BFS from a building instead of an empty cell, we will be generating partial distance (i.e., distance from only one building to the current cell and not the sum distance from all the buildings to this empty cell), hence we need some extra space to store the sum of the partial distances from each building cell.

We will need to store 2 values at each cell position of empty cells: total distance sum from all buildings to this empty land and number of buildings that can reach this empty land.

**Algorithm**

1. For each building cell ($\text{grid}[i][j]$ equals 1), start a BFS:
- For each empty cell we reach, increase the cell's sum of distances by the steps taken to reach the cell.
- For each empty cell we reach, also increment the cell's building counter by 1.
2. After traversing all buildings, get the minimum distance from all empty cells which have `housesReached` equal to `totalHouses`.
3. If it is possible for all buildings to reach a specific empty land cell, then return the minimum distance found. Otherwise, return `-1`.

![Slide 1](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide34.PNG)

![Slide 2](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide35.PNG)

![Slide 3](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide36.PNG)

![Slide 4](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide37.PNG)

![Slide 5](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide38.PNG)

![Slide 6](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide39.PNG)

![Slide 7](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide40.PNG)

![Slide 8](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide41.PNG)

![Slide 9](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide42.PNG)

![Slide 10](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide43.PNG)

![Slide 11](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide44.PNG)

![Slide 12](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide45.PNG)

![Slide 13](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide46.PNG)

![Slide 14](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide47.PNG)

![Slide 15](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide48.PNG)

![Slide 16](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide49.PNG)

![Slide 17](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide50.PNG)

![Slide 18](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide51.PNG)

![Slide 19](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide52.PNG)

![Slide 20](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide53.PNG)

![Slide 21](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide54.PNG)

![Slide 22](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide55.PNG)

![Slide 23](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide56.PNG)

![Slide 24](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide57.PNG)

![Slide 25](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide58.PNG)

![Slide 26](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide59.PNG)

![Slide 27](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide60.PNG)

![Slide 28](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide61.PNG)

![Slide 29](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide62.PNG)

![Slide 30](images/slideshow_317_shortest_distance_from_all_buildings_2_Slide63.PNG)

<br />

**Implementation**

```javascript
let dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

let bfs = function (grid, distances, row, col) {
    let rows = grid.length;
    let cols = grid[0].length;

    // Use a queue to do a BFS, starting from cell at (row, col).
    let queue = [[ row, col ]];

    // Keep track of visited cells
    let vis = new Array(rows).fill(false).map(() => new Array(cols).fill(false));
    vis[row][col] = true;

    let steps = 0;

    while (queue.length) {
        // Record the cells that we will explore in the next level
        let next_queue = [];

        for (let i = 0; i < queue.length; i++) {
            let curr = queue[i];

            row = curr[0];
            col = curr[1];

            // If we reached an empty cell, then add the distance
            // and increment the count of buildings reached at this cell.
            if (grid[row][col] == 0) {
                distances[row][col][0] += steps;
                distances[row][col][1]++;
            }

            // Traverse the next cells which is not a blockage.
            dirs.forEach((dir) => {
                let nextRow = row + dir[0];
                let nextCol = col + dir[1];

                if (nextRow >= 0 && nextCol >= 0 && nextRow < rows && nextCol < cols) {
                    if (!vis[nextRow][nextCol] && grid[nextRow][nextCol] == 0) {
                        vis[nextRow][nextCol] = true;
                        next_queue.push([nextRow, nextCol]);
                    }
                }
            });
        }

        // Set the queue equal to the next level queue.
        queue = next_queue;
        // After traversing one level cells, increment the steps by 1 to reach to next level.
        steps++;
    }
};

let shortestDistance = function (grid) {
    let minDistance = Number.MAX_VALUE;
    let rows = grid.length;
    let cols = grid[0].length;
    let totalHouses = 0;

    // Store { total_dist, buildings_count } for each cell.
    let distances = new Array(rows).fill(0).map(() => new Array(cols).fill(0).map(() => new Array(2).fill(0)));

    // Count buildings and start BFS from each building.
    for (let row = 0; row < rows; ++row) {
        for (let col = 0; col < cols; ++col) {
            if (grid[row][col] == 1) {
                totalHouses++;
                bfs(grid, distances, row, col);
            }
        }
    }

    // Check all empty lands with buildings count equal to total buildings and find the min ans.
    for (let row = 0; row < rows; ++row) {
        for (let col = 0; col < cols; ++col) {
            if (distances[row][col][1] == totalHouses) {
                minDistance = Math.min(minDistance, distances[row][col][0]);
            }
        }
    }

    // If we haven't found a valid cell return -1.
    if (minDistance == Number.MAX_VALUE) {
        return -1;
    }
    return minDistance;
};
```

**Complexity Analysis**

Let $N$ and $M$ be the number of rows and columns in `grid` respectively.

-   Time Complexity: $O(N^2 \cdot M^2)$

    For each building, we will traverse across all reachable land.
    This will require $O($number of zeros $\cdot$ number of ones$)$ time and the number of zeros and ones in the matrix is of order $N \cdot M$.
    Consider that when half of the values in grid are 0 and half of the values are 1, total elements in grid will be $(M \cdot N)$ so their counts are $(M \cdot N)/2$ and $(M \cdot N)/2$ respectively, thus giving time complexity $(M \cdot N)/2 \cdot (M \cdot N)/2$, which results in $O(N^2 \cdot M^2)$.

> In JavaScript implementation, for simplicity, we have used an array for the queue.
> However, popping elements from the front of an array is an $\mathcal{O}(n)$ operation, which is undesirable.
> So, instead of popping from the front of the `queue`, we will iterate over the `queue` and record cells to be explored in the next level in $\text{next}_{queue}$.
> Once the current `queue` has been traversed, we simply set `queue` equal to the $\text{next}_{queue}$.

-   Space Complexity: $O(N \cdot M)$

    We use an extra matrix to track the visited cells and another one to store distance sum along with the building counter for each empty cell, and the queue will store each matrix element at most once during each BFS call.
    Hence, $O(N \cdot M)$ space is required.

<br/>

---

### Approach 3: BFS from Buildings to Empty Land (Optimized)

**Intuition**

Instead of making a new matrix each time to track the visited cells, we can use the input grid matrix for this purpose.
During the first BFS we can change the visited empty land values from `0` to `-1`. Then during the next BFS we will only visit empty lands with a value of `-1`s (meaning they can reach the first building), then change `-1` to `-2` and then perform the next BFS only on `-2`s, and so on...

This approach allows us to avoid visiting any cell that cannot reach all buildings.

_Can we also use this decrement in empty land value to denote that the cell has been visited?_

> Imagine we are currently at cell `(2, 3)` with value `-1` and we change its value to `-2`.
> In the queue the next element is `(2, 4)`, its value is also `-1` and we change its value to `-2`. While exploring paths from `(2, 4)`, we see that the cell `(2, 3)` is adjacent, and has the value `-2`. However, currently, we are checking for `-1` valued cells only. Hence, `(2, 3)` will not be inserted again in the queue, so this decrease in value can be used as a visited cell check because when a cell has been visited, then its value will be 1 less and it will not satisfy the condition to be inserted in the queue.

If there was an empty land cell that was not reachable in the previous iteration, then its value has not been decreased, hence we will not insert that cell in the queue when we start a BFS from another building cell.
Therefore, this approach prunes many iterations and saves some time since we are not creating a new matrix to track visited cells for each BFS call.

![Slide 1](images/slideshow_317_shortest_distance_from_all_buildings_3_Slide65.PNG)

![Slide 2](images/slideshow_317_shortest_distance_from_all_buildings_3_Slide66.PNG)

![Slide 3](images/slideshow_317_shortest_distance_from_all_buildings_3_Slide67.PNG)

<br />

**Algorithm**

1. For each $\text{grid}[i][j]$ that is equal to 1, start a BFS. During the BFS:
- All 4-directionally adjacent grid cells with values equal to `emptyLandValue` are valid.
- Visit them one by one and store the distances of these cells from the source in a `total` matrix.
- Decrease the value of visited cells by 1.
2. After each BFS traversal, decrement `emptyLandValue` by 1.
3. Before we start a BFS call for a building, we set `minDist` equal to $\text{INT}_{MAX}$.
4. Then we will traverse all of the empty land cells with values equal to `emptyLandValue`
5. After the last BFS traversal, if the minimum distance equals $\text{INT}_{MAX}$, then there has not been any cell that can be reached by all the buildings, so return `-1`.
6. Otherwise, return the minimum distance `minDist`.

![Slide 1](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide69.PNG)

![Slide 2](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide70.PNG)

![Slide 3](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide71.PNG)

![Slide 4](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide72.PNG)

![Slide 5](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide73.PNG)

![Slide 6](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide74.PNG)

![Slide 7](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide75.PNG)

![Slide 8](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide76.PNG)

![Slide 9](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide77.PNG)

![Slide 10](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide78.PNG)

![Slide 11](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide79.PNG)

![Slide 12](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide80.PNG)

![Slide 13](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide81.PNG)

![Slide 14](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide82.PNG)

![Slide 15](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide83.PNG)

![Slide 16](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide84.PNG)

![Slide 17](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide85.PNG)

![Slide 18](images/slideshow_317_shortest_distance_from_all_buildings_4_Slide86.PNG)

<br />

**Implementation**

```javascript
// Next four directions.
let dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

// Queue Implementation using Linked List.
class Node {
    constructor(row, col) {
        this.row = row;
        this.col = col;
        this.prev = null;
        this.next = null;
    }
}

class QueueClass {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    length() {
        return this.length;
    }

    push(row, col) {
        const newNode = new Node(row, col);

        if (this.head == null) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }

        this.length++;
    }

    pop() {
        if (this.head == null) return null;

        // Get the popped node.
        const popped = this.head;

        // Save newHead to a variable (could be null).
        const newHead = this.head.next;

        // If newHead is not null.
        if (newHead) {
            newHead.prev = null;
            this.head.next = null;
        }

        else {
            // Change tail in case newHead is null.
            this.tail = null;
        }

        // Assign new tail (could be null).
        this.head = newHead;

        // Decrement length.
        this.length--;
        return popped;
    }

    empty() {
        return this.length == 0;
    }
}

let shortestDistance = function (grid) {
    let minDistance = Number.MAX_VALUE;
    let rows = grid.length;
    let cols = grid[0].length;

    // Total Mtrix to store total distance sum for each empty cell.
    let total = new Array(rows).fill(0).map(() => new Array(cols).fill(0));

    let emptyLandValue = 0;
    let minDist = Number.MAX_VALUE;

    for (let row = 0; row < rows; ++row) {
        for (let col = 0; col < cols; ++col) {

            // Start a BFS from each building.
            if (grid[row][col] == 1) {
                minDist = Number.MAX_VALUE;

                // Use a queue to perform a BFS, starting from the cell located at (row, col).
                let q = new QueueClass();
                q.push(row, col);

                let steps = 0;

                while (!q.empty()) {
                    steps++;

                    for (let level = q.length; level > 0; --level) {
                        let curr = q.pop();

                        dirs.forEach((dir) => {
                            let nextRow = curr.row + dir[0];
                            let nextCol = curr.col + dir[1];

                            // For each cell with the value equal to empty land value
                            // add distance and decrement the cell value by 1.
                            if (nextRow >= 0 && nextRow < rows &&
                                nextCol >= 0 && nextCol < cols &&
                                grid[nextRow][nextCol] == emptyLandValue) {
                                grid[nextRow][nextCol]--;
                                total[nextRow][nextCol] += steps;

                                q.push(nextRow, nextCol);
                                minDist = Math.min(minDist, total[nextRow][nextCol]);
                            }
                        });
                    }
                }

                // Decrement empty land value to be searched in next iteration.
                emptyLandValue--;
            }
        }
    }

    return minDist == Number.MAX_VALUE ? -1 : minDist;
};
```

**Complexity Analysis**

Let $N$ and $M$ be the number of rows and columns in `grid` respectively.

-   Time Complexity: $O(N^2 \cdot M^2)$

    For each building, we will traverse across all reachable land.
    This will require $O($number of zeros $\cdot$ number of ones$)$ time and the number of zeros and ones in the matrix is of order $N \cdot M$.
    Consider that when half of the values in grid are 0 and half of the values are 1, total elements in grid would be $(M \cdot N)$ so their counts are $(M \cdot N)/2$ and $(M \cdot N)/2$ respectively, thus giving time complexity $(M \cdot N)/2 \cdot (M \cdot N)/2$, that results in $O(N^2 \cdot M^2)$.

-   Space Complexity: $O(N \cdot M)$

    We use an extra matrix to store distance sums, and the queue will store each matrix element at most once during each BFS call.
    Hence, $O(N \cdot M)$ space is required.

<br/>

---