## Description

Determine whether the integer array `nums` is consecutive. If $x$ is its minimum value and $n$ is its length, being consecutive means that the array contains every integer in the inclusive range $[x,x+n-1]$.

The input order does not matter, but every required value must occur. Because the array itself has exactly $n$ positions and the target range has exactly $n$ distinct integers, a duplicated value necessarily leaves another value missing and makes the result false. Return a boolean expressing whether the complete range is present.
