## Description

You are given an integer array `nums`. Repeatedly inspect the current array for adjacent elements with equal values. Whenever one or more equal adjacent pairs exist, select the **leftmost** such pair and replace its two values with their sum.

Each replacement shortens the array by one. Because a merge can create a new equal pair with a neighboring value, continue applying the same leftmost rule to the updated array until no adjacent values are equal.

Return the final array after the process can no longer perform a merge.

