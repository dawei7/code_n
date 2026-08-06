## Description

One white blood cell must eliminate every bacterial strain in `timeReq`. Eliminating strain $i$ occupies one cell for `timeReq[i]` time units. Once that task finishes, the cell is exhausted and cannot split or eliminate another strain. Strains may be assigned in any order, but one strain cannot be attacked by multiple cells.

Before accepting an elimination task, a cell may instead spend `splitTime` time units dividing into two cells. The two descendants then act simultaneously and may independently split again or eliminate one strain each. All activity on separate branches happens in parallel.

Choose the splitting schedule and strain assignments that minimize the time at which every strain has been eliminated. Return that minimum completion time, measured from the moment the initial single cell starts.
