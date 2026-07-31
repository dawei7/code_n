## General

**Store availability and the first unresolved boundary.** Maintain a Boolean array whose entry for video $i$ records whether it has arrived. Also store `prefix`, the length of the longest uploaded prefix known so far. Initially every flag is false and `prefix` is 0.

When `upload(video)` is called, mark that video. Then, while the next position after `prefix` is marked, advance the boundary. An upload beyond a gap merely records future availability. When the missing video eventually arrives, the same loop crosses it and every consecutively available video beyond it.

The boundary never moves backward and stops exactly at the first missing video. Thus every value through `prefix` is uploaded, while `prefix + 1` is absent unless the prefix already covers all $n$ videos. This invariant makes `longest()` a direct return of the stored boundary.

## Complexity detail

Constructing the Boolean array takes $O(n)$ time. Each upload marks one entry, and although one call may advance across many positions, `prefix` advances at most $n$ times over the object's lifetime. Across $q$ method calls, the total time is $O(n+q)$; `longest()` itself is $O(1)$. The availability array uses $O(n)$ space.

## Alternatives and edge cases

- **Rescan from video 1 on every query:** Storing uploaded videos in a set is simple, but recomputing the prefix for every `longest()` call can cost $O(nq)$ total time.
- **Min-heap of missing videos:** Removing arbitrary uploaded identifiers needs extra bookkeeping or lazy deletion; the smallest missing identifier still determines the answer.
- **Union-find:** Uploaded adjacent identifiers can be joined into intervals, but this adds machinery when one monotone boundary is sufficient.
- **Videos arrive in order:** The boundary advances by one after every upload.
- **Videos arrive in reverse order:** The prefix remains 0 until video 1 arrives, then it can jump directly to $n$.
- **Gap closure:** One upload may connect the prefix to a long run of videos that were recorded earlier.
- **Repeated queries:** Calling `longest()` without another upload must return the same value and perform no scan.
- **Single video:** The answer changes from 0 to 1 when video 1 is uploaded.
