## Description

A campus is represented as a two-dimensional grid containing $n$ workers and $m$ bikes, where $n \le m$. Arrays `workers` and `bikes` give the grid coordinate of each indexed worker and bike, and every listed location is unique.

Assign one distinct bike to every worker. A bike cannot serve more than one worker, while surplus bikes may remain unused. The cost of an assignment is the sum of the Manhattan distances between all workers and their assigned bikes.

For points $p_1=(x_1,y_1)$ and $p_2=(x_2,y_2)$, their Manhattan distance is

$$
\operatorname{Manhattan}(p_1,p_2)=\lvert x_1-x_2\rvert+\lvert y_1-y_2\rvert.
$$

Return the minimum possible total cost over every valid one-to-one assignment.
