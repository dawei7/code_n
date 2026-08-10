## General

**Shelves divide the ordered books into contiguous groups**

Book order cannot change. Therefore, every shelf contains one contiguous block of the input, and a complete arrangement is a partition of the sequence into contiguous blocks whose total thicknesses do not exceed `shelfWidth`.

The cost of one block is the maximum book height in it, because the shelf must be tall enough for its tallest member. This turns the problem into a prefix dynamic program: try every valid position where the final shelf could begin.

**Define the prefix state**

`f[i]` is the minimum total height needed for the first `i` books. `f[0] = 0` represents placing no books.

When processing book `i` in one-based DP language, the code begins with that book alone on a new shelf. Its width and height are `w` and `h` from the loop tuple, and:

`f[i] = f[i - 1] + h`.

This is always valid because every individual thickness is at most the shelf width. It also gives an initial upper bound that later candidates can improve.

**Extend the last shelf backward**

The inner loop moves `j` from `i - 1` down to one. On each step it adds book `j - 1` to the left side of the current final shelf. Variable `w` becomes the total thickness of books from index `j - 1` through `i - 1`, and `h` becomes their maximum height.

If `w > shelfWidth`, this block is invalid. Moving `j` farther left can only add positive thickness, so every earlier start is also invalid and the loop can break.

Otherwise, the books before this shelf are exactly the first `j - 1` books, whose optimal height is `f[j - 1]`. The candidate total is:

`f[j - 1] + h`.

Taking the minimum over the current value and every valid final-shelf start computes the best arrangement for the first `i` books.

**Why optimal prefix solutions combine correctly**

Consider an optimal arrangement of the first `i` books and let its last shelf begin at book `j` in one-based terms. That shelf is a valid contiguous block, and everything before it is an arrangement of the first `j - 1` books.

If the preceding part were taller than `f[j - 1]`, replacing it with the optimal prefix arrangement would preserve order and shelf validity while lowering the total, contradicting optimality. Therefore, the optimal full arrangement appears among the candidates checked for `f[i]`.

Conversely, every candidate combines an already valid optimal prefix with one width-valid final shelf, so it constructs a legal arrangement. The minimum of all legal candidates is thus exactly optimal.

The DP proceeds from smaller prefixes to larger ones, so every referenced `f[j - 1]` is already final when used. Returning `f[n]` solves the complete sequence.

The running maximum `h` is what makes evaluating a candidate constant-time after extending it. Recomputing the tallest book from scratch for every possible block would add another loop and could raise the work to cubic time. Likewise, accumulating `w` avoids repeatedly summing the same thickness ranges.

## Complexity detail

There are $n$ outer iterations. In the worst case, every book is thin enough that the inner loop examines all earlier books, producing $1+2+\cdots+n = O(n^2)$ work.

The DP array contains $n+1$ integers, so auxiliary space is $O(n)$. Width, height, indices, and candidate calculations use constant additional storage. The input is not modified.

The early width break can make practical execution much faster when shelves fill after only a few books, but it does not change the quadratic worst case.

## Alternatives and edge cases

- **Top-down memoization:** Define the same prefix or suffix states recursively and try all shelf endings. It has the same $O(n^2)$ time but adds recursion overhead.
- **Greedy fill each shelf:** Putting as many books as possible on the current shelf can be suboptimal because moving a tall book to another shelf may reduce the sum of shelf maxima.
- **Reordering by height:** Invalid because the input order must be preserved; shelves correspond to contiguous blocks.
- **One book:** The default candidate places it alone, so the answer is its height.
- **All books fit on one shelf:** The inner expansion eventually considers the whole prefix, and `f[n]` becomes the maximum height of all books.
- **Each book uses full width:** No two books fit together, so the default candidates sum every height.
- **Equal heights:** Grouping them can save height whenever width permits because one shelf maximum covers all of them.
- **A very tall book:** Its height dominates any shelf containing it, which may make grouping neighboring short books with it beneficial.
- **Width exactly equal to the limit:** The block remains valid because the break occurs only for `w > shelfWidth`.
- **Positive thickness:** Once width exceeds the limit, extending farther left can never restore validity, justifying the break.
- **Multiple optimal partitions:** The DP stores only their minimum height, which is all the contract requests.
