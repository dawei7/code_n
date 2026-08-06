## Description

There are $n$ processes arranged as a rooted tree. For every index `i`, `pid[i]` is one process identifier and `ppid[i]` is the identifier of its parent.

Each process has exactly one parent except the root, whose parent identifier is `0`. A process may have any number of children. Killing a process also kills all of its descendants.

Given the identifier `kill`, return the identifiers of every process that will be killed. The answer may be returned in any order.
