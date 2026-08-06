## Description

An **image smoother** is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/smoother-grid.jpg" style="width: 493px; height: 493px;" />
Given an `m x n` integer matrix `img` representing the grayscale of an image, return *the image after applying the smoother on each cell of it*.
