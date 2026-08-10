## General

For two different teams $i$ and $j$, `grid[i][j] == 1` means $i$ is stronger than $j$. A champion has no stronger opponent. Under the tournament guarantees, that is equivalent to being stronger than every other team.

The exact source examines each matrix row. For candidate `i`, it evaluates

`all(x == 1 for j, x in enumerate(row) if i != j)`.

The generator skips diagonal entry `grid[i][i]`, which is always zero and describes no comparison. Every remaining row entry must be one. The first row satisfying that condition is returned.

**Why an all-one off-diagonal row identifies the champion**

If candidate $i$ has a one against every $j\ne i$, then $i$ is stronger than every other team. In particular, none of those teams is stronger than $i$, because the input guarantees opposite comparison results for each pair. Hence $i$ is a champion.

Conversely, suppose $i$ is the champion. For every other team $j$, exactly one of $i$ or $j$ is stronger. Since no $j$ may be stronger than the champion, $i$ must be stronger than $j$, so `grid[i][j]` is one. The champion's row therefore passes the test.

This proves the predicate is necessary and sufficient.

**Why returning the first match is safe**

Two different rows cannot both contain ones against every opponent. If teams $a$ and $b$ both passed, the first row would require `grid[a][b] == 1`, while the second would require `grid[b][a] == 1`. The contract says these two entries differ, making that impossible.

The transitive-order guarantee also ensures a strongest team exists. Therefore the loop will encounter exactly one passing row for legal input. Although Python would implicitly return `None` if no row passed, that path is unreachable under the reference contract.

**How `all` evaluates**

`all` starts conceptually true and consumes generated comparisons until one is false. A candidate may therefore be rejected early after its first loss. In the worst case, however, many rows can have their zero near the end, and the champion's entire row must be checked.

The source does not use the candidate-elimination algorithm described by the Optimal manifest summary. It directly verifies rows in the matrix.

For `[[0,0,1],[1,0,1],[0,0,0]]`:

- row $0$ fails because it loses to team $1$;
- row $1$ has ones against teams $0$ and $2$, so it passes and returns $1$;
- later rows need not be examined.

**Role of transitivity**

The row predicate itself only needs pairwise comparison completeness and uniqueness. Transitivity explains why the tournament represents a consistent strength ordering and guarantees a maximum team. Without it, a rock-paper-scissors cycle could leave every row with a loss and the function would return no integer.

## Complexity detail

There are $n$ rows and up to $n-1$ off-diagonal entries checked per row. Worst-case running time is $O(n^2)$, not the $O(n)$ stated in the manifest. Short-circuiting `all` may reduce work on particular inputs but does not improve the worst-case bound.

The generator is lazy and stores no copied row or candidate list. Aside from loop and generator state, auxiliary space is $O(1)$. The $n\times n$ input matrix is not counted as auxiliary storage.

An $O(n)$ candidate-elimination method exists, but it is not the checked-in implementation being explained.

## Alternatives and edge cases

- **Candidate elimination:** Compare a current candidate with each next team and replace the loser, then optionally verify. Under the strong tournament guarantees this can run in $O(n)$ time and $O(1)$ space.
- **Column indegree count:** Count losses for every team from the matrix in $O(n^2)$ time and $O(n)$ space; the champion has zero losses.
- **Do not include the diagonal:** `grid[i][i]` is zero by definition. Testing it would reject every candidate.
- **Two apparent champions:** Impossible because their mutual pair cannot point in both directions.
- **Cycle without transitivity:** Every team might lose to someone, and the source would fall through with `None`. Legal inputs exclude this.
- **Early short-circuit:** `all` stops at the first zero, improving common-case constants but not worst-case asymptotics.
- **Single champion guarantee:** It follows from the complete transitive tournament even though the method has no explicit `-1` branch.
- **Manifest mismatch:** The summary's elimination language and $O(n)$ time do not describe this source. Faithful analysis is $O(n^2)$ for row verification.
- **Why a loss is decisive:** Once row $i$ contains zero against some different team $j$, the pairwise guarantee means $j$ is stronger than $i$. No comparisons with other teams can restore $i$ as champion.
- **Row order:** Returning the first passing row does not prefer a smaller label over another valid champion; uniqueness proves no second passing row exists.
- **Matrix storage:** The input already occupies $O(n^2)$ space, but the method allocates no additional structure proportional to it.
- **Worst-case short-circuit example:** If each rejected row's first zero appears near its last checked column, almost every off-diagonal entry is inspected before the champion is found.
