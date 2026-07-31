## Description

You are given two integer arrays, `startTime` and `endTime`, of equal length $n$. Employee $i$ is available throughout the closed interval from `startTime[i]` through `endTime[i]`. Two employees can interact when their intervals share at least one time point; touching at an endpoint therefore counts as overlap.

A team is valid when at least one employee belonging to that team can interact with every other team member. The remaining members do not need to interact with one another, and the team does not need to share one time point common to everyone. Return the greatest possible number of employees in a valid team.
