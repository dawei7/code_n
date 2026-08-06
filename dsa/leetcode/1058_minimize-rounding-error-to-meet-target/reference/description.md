## Description

Given decimal prices $[p_1,p_2,\ldots,p_N]$ and an integer `target`, round every $p_i$ independently to either $\lfloor p_i\rfloor$ or $\lceil p_i\rceil$. The selected rounded values must sum exactly to `target`.

When this sum cannot be achieved, return `"-1"`. Otherwise, minimize the total rounding error

$$
\sum_{i=1}^{N}\left\lvert R_i(p_i)-p_i\right\rvert,
$$

where each $R_i$ is the chosen floor or ceiling operation. Return the minimum error as a string with exactly three digits after the decimal point.
