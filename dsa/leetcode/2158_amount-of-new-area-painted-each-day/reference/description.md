## Description

Represent a long, narrow painting by a number line. On day $i$, the pair
`paint[i] = [start_i, end_i]` requests painting the half-open interval
$[\textit{start}_i,\textit{end}_i)$. Its area is therefore
$\textit{end}_i-\textit{start}_i$.

Previously painted area must not be painted again because overlapping coats
would make the result uneven. For every day, report only the amount of its
requested interval that has never appeared in any earlier day's interval.
Return these daily amounts in their original chronological order.
