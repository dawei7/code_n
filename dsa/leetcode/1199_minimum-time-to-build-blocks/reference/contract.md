## Function Contract

**Inputs**

- `blocks`: A nonempty integer list in which each value is the time one worker needs to build that block.
- `split`: The fixed time required for one worker to become two workers.

Each block must be assigned to exactly one worker. A worker who builds a block leaves afterward, while workers on different branches may build or split at the same time. Total elapsed time is therefore governed by the slowest parallel branch rather than by the sum of all workers' actions.

Let $n$ be `blocks.length`.

**Return value**

Return the smallest possible time by which all $n$ blocks have been built, starting with one worker.
