## Description

You want to distribute cookies among your children, giving each child at most one cookie.

Child `i` has greed factor `g[i]`, the minimum cookie size that makes that child content. Cookie `j` has size `s[j]`; it can be assigned to child `i` only when `s[j] >= g[i]`. Each cookie can be used once.

Choose the assignments that maximize the number of content children, and return that maximum count.
