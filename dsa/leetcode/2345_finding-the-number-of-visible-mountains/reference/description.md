## Description

Each pair `peaks[i] = [x_i, y_i]` describes a right-angled isosceles mountain whose peak is $(x_i, y_i)$, whose base lies on the $x$-axis, and whose ascending and descending slopes are $1$ and $-1$. Thus its base endpoints are $x_i - y_i$ and $x_i + y_i$.

A mountain is visible only when its peak lies neither inside nor on the border of any other mountain. Completely overlapping mountains hide one another, so duplicate peaks are all invisible. Return the number of mountains whose peaks remain visible under these rules.
