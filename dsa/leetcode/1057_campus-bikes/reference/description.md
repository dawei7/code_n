## Description

A campus is represented on the X-Y plane. There are $W$ workers and $B$ bikes, with $W \le B$. The arrays `workers` and `bikes` give their respective coordinates, and every supplied worker and bike position is unique.

Assign one bike to every worker through a repeated global selection process. Among all workers and bikes that are still available, choose the pair with the smallest **Manhattan distance**. When several pairs share that distance, select the pair with the smallest worker index; if a tie remains, select the smallest bike index. Remove the selected worker and bike from availability and continue until every worker has an assignment.

For points $p_1=(x_1,y_1)$ and $p_2=(x_2,y_2)$, the Manhattan distance is

$$
\operatorname{Manhattan}(p_1,p_2)=\lvert x_1-x_2\rvert+\lvert y_1-y_2\rvert.
$$

Return a worker-indexed array containing the 0-indexed bike assigned to each worker.
