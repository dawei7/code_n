## Description

You are given a string `road` containing only `x` and `.`. Each `x` represents a pothole, while each `.` represents a smooth section of road. You also have an integer `budget` available for repairs.

One repair operation may fix $k$ consecutive potholes for a price of $k+1$. You may perform multiple operations, provided their total price does not exceed `budget`. Return the maximum number of potholes that can be fixed. Repaired positions must come from consecutive potholes within the same uninterrupted `x` block; an operation cannot cross a smooth section.
