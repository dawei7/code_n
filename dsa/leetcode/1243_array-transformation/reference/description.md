## Description

Begin with an integer array `arr`. Each day produces a new array from the complete array of the previous day, so every decision in one day is simultaneous.

For each interior element:

- increment it by one when it is strictly smaller than both its left and right neighbors;
- decrement it by one when it is strictly larger than both neighbors; and
- otherwise leave it unchanged.

The first and last elements never change. Continue producing daily arrays until a day makes no change, then return that stable array.
