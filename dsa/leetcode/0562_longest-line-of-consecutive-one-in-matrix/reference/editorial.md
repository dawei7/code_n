
## Solution

---
### Approach 1: Brute Force

**Algorithm**

The brute force approach is really simple. We directly traverse along every valid line in the given matrix: i.e. Horizontal, Vertical, Diagonal aline above and below the middle diagonal, Anti-diagonal line above and below the middle anti-diagonal. Each time during the traversal, we keep on incrementing the $count$ if we encounter continuous 1's. We reset the $count$ for any discontinuity encountered. While doing this, we also keep a track of the maximum $count$ found so far.

```java
class Solution {
  public int longestLine(int[][] M) {
    if (M.length == 0) return 0;
    int ones = 0;
    // horizontal
    for (int i = 0; i < M.length; i++) {
      int count = 0;
      for (int j = 0; j < M[0].length; j++) {
        if (M[i][j] == 1) {
          count++;
          ones = Math.max(ones, count);
        } else count = 0;
      }
    }
    // vertical
    for (int i = 0; i < M[0].length; i++) {
      int count = 0;
      for (int j = 0; j < M.length; j++) {
        if (M[j][i] == 1) {
          count++;
          ones = Math.max(ones, count);
        } else count = 0;
      }
    }
    // upper diagonal
    for (int i = 0; i < M[0].length || i < M.length; i++) {
      int count = 0;
      for (int x = 0, y = i; x < M.length && y < M[0].length; x++, y++) {
        if (M[x][y] == 1) {
          count++;
          ones = Math.max(ones, count);
        } else count = 0;
      }
    }
    // lower diagonal
    for (int i = 0; i < M[0].length || i < M.length; i++) {
      int count = 0;
      for (int x = i, y = 0; x < M.length && y < M[0].length; x++, y++) {
        if (M[x][y] == 1) {
          count++;
          ones = Math.max(ones, count);
        } else count = 0;
      }
    }
    // upper anti-diagonal
    for (int i = 0; i < M[0].length || i < M.length; i++) {
      int count = 0;
      for (int x = 0, y = M[0].length - i - 1; x < M.length && y >= 0; x++, y--) {
        if (M[x][y] == 1) {
          count++;
          ones = Math.max(ones, count);
        } else count = 0;
      }
    }
    // lower anti-diagonal
    for (int i = 0; i < M[0].length || i < M.length; i++) {
      int count = 0;
      for (int x = i, y = M[0].length - 1; x < M.length && y >= 0; x++, y--) {
        // System.out.println(x+" "+y);
        if (M[x][y] == 1) {
          count++;
          ones = Math.max(ones, count);
        } else count = 0;
      }
    }
    return ones;
  }
}
```

**Complexity Analysis**

Let $m$ be the length of the matrix and $n$ be the width of the matrix. As a result, $mn$ would be the total number of cells in the matrix.

* Time complexity : $O(mn)$. We traverse along the entire matrix 4 times.
* Space complexity : $O(1)$. Constant space is used.

---
### Approach 2: Using 3D Dynamic Programming

**Algorithm**

Instead of traversing over the same matrix multiple times, we can keep a track of the 1' along all the lines possible while traversing the matrix once only. In order to do so, we make use of a $4mn$ sized $dp$ array. Here, $\text{dp}[0]$, $\text{dp}[1]$, $\text{dp}[2]$ ,$\text{dp}[3]$ are used to store the maximum number of continuous 1's found so far along the Horizontal, Vertical, Diagonal and Anti-diagonal lines respectively. e.g. $\text{dp}[i][j][0]$ is used to store the number of continuous 1's found so far(till we reach the element $M[i][j]$), along the horizontal lines only.

Thus, we traverse the matrix $M$ in a row-wise fashion only but, keep updating the entries for every $dp$ appropriately.

The following image shows the filled $dp$ values for this matrix:
```
 0 1 1 0

 0 1 1 0

 0 0 1 1

```

![Longest_Line](images/562_Longest_Line.PNG)

While filling up the $dp$, we can keep a track of the length of the longest consecutive line of 1's.

Watch this animation for complete process:

![Slide 1](images/slideshow_562_Longest_Line_562_Longest_LineSlide1.PNG)

![Slide 2](images/slideshow_562_Longest_Line_562_Longest_LineSlide2.PNG)

![Slide 3](images/slideshow_562_Longest_Line_562_Longest_LineSlide3.PNG)

![Slide 4](images/slideshow_562_Longest_Line_562_Longest_LineSlide4.PNG)

![Slide 5](images/slideshow_562_Longest_Line_562_Longest_LineSlide5.PNG)

![Slide 6](images/slideshow_562_Longest_Line_562_Longest_LineSlide6.PNG)

![Slide 7](images/slideshow_562_Longest_Line_562_Longest_LineSlide7.PNG)

![Slide 8](images/slideshow_562_Longest_Line_562_Longest_LineSlide8.PNG)

![Slide 9](images/slideshow_562_Longest_Line_562_Longest_LineSlide9.PNG)

![Slide 10](images/slideshow_562_Longest_Line_562_Longest_LineSlide10.PNG)

![Slide 11](images/slideshow_562_Longest_Line_562_Longest_LineSlide11.PNG)

![Slide 12](images/slideshow_562_Longest_Line_562_Longest_LineSlide12.PNG)

![Slide 13](images/slideshow_562_Longest_Line_562_Longest_LineSlide13.PNG)

![Slide 14](images/slideshow_562_Longest_Line_562_Longest_LineSlide14.PNG)

```java
class Solution {
  public int longestLine(int[][] M) {
    if (M.length == 0) return 0;
    int ones = 0;
    int[][][] dp = new int[M.length][M[0].length][4];
    for (int i = 0; i < M.length; i++) {
      for (int j = 0; j < M[0].length; j++) {
        if (M[i][j] == 1) {
          dp[i][j][0] = j > 0 ? dp[i][j - 1][0] + 1 : 1;
          dp[i][j][1] = i > 0 ? dp[i - 1][j][1] + 1 : 1;
          dp[i][j][2] = (i > 0 && j > 0) ? dp[i - 1][j - 1][2] + 1 : 1;
          dp[i][j][3] = (i > 0 && j < M[0].length - 1) ? dp[i - 1][j + 1][3] + 1 : 1;
          ones =
              Math.max(
                  ones,
                  Math.max(Math.max(dp[i][j][0], dp[i][j][1]), Math.max(dp[i][j][2], dp[i][j][3])));
        }
      }
    }
    return ones;
  }
}
```

**Complexity Analysis**

* Time complexity : $O(mn)$. We traverse the entire matrix once only.

* Space complexity : $O(mn)$. $dp$ array of size $4mn$ is used, where $m$ and $n$ are the number of rows ans coloumns of the matrix.

---

### Approach 3: Using 2D Dynamic Programming

**Algorithm**

In the previous approach, we can observe that the current $dp$ entry is dependent only on the entries of the just previous corresponding $dp$ row. Thus, instead of maintaining a 2-D $dp$ matrix for each kind of line of 1's possible, we can use a 1-d array for each one of them, and update the corresponding entries in the same row during each row's traversal. Taking this into account, the previous 3-D $dp$ matrix shrinks to a 2-D $dp$ matrix now. The rest of the procedure remains same as the previous approach.

```java
class Solution {
  public int longestLine(int[][] M) {
    if (M.length == 0) return 0;
    int ones = 0;
    int[][] dp = new int[M[0].length][4];
    for (int i = 0; i < M.length; i++) {
      int old = 0;
      for (int j = 0; j < M[0].length; j++) {
        if (M[i][j] == 1) {
          dp[j][0] = j > 0 ? dp[j - 1][0] + 1 : 1;
          dp[j][1] = i > 0 ? dp[j][1] + 1 : 1;
          int prev = dp[j][2];
          dp[j][2] = (i > 0 && j > 0) ? old + 1 : 1;
          old = prev;
          dp[j][3] = (i > 0 && j < M[0].length - 1) ? dp[j + 1][3] + 1 : 1;
          ones =
              Math.max(ones, Math.max(Math.max(dp[j][0], dp[j][1]), Math.max(dp[j][2], dp[j][3])));
        } else {
          old = dp[j][2];
          dp[j][0] = dp[j][1] = dp[j][2] = dp[j][3] = 0;
        }
      }
    }
    return ones;
  }
}
```

**Complexity Analysis**

* Time complexity : $O(mn)$. The entire matrix is traversed once only.

* Space complexity : $O(n)$. $dp$ array of size $4n$ is used, where $n$ is the number of columns of the matrix.