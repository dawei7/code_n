## Description

You are given an integer `n` representing the size of a **0-indexed** memory array. All memory units are initially free.

You have a memory allocator with the following functionalities:

<ol>
	<li>**Allocate **a block of `size` consecutive free memory units and assign it the id `mID`.</li>
	<li>**Free** all memory units with the given id `mID`.</li>
</ol>

**Note** that:

<ul>
	<li>Multiple blocks can be allocated to the same `mID`.</li>
	<li>You should free all the memory units with `mID`, even if they were allocated in different blocks.</li>
</ul>

Implement the `Allocator` class:

<ul>
	<li>`Allocator(int n)` Initializes an `Allocator` object with a memory array of size `n`.</li>
	<li>`int allocate(int size, int mID)` Find the **leftmost** block of `size` **consecutive** free memory units and allocate it with the id `mID`. Return the block's first index. If such a block does not exist, return `-1`.</li>
	<li>`int freeMemory(int mID)` Free all memory units with the id `mID`. Return the number of memory units you have freed.</li>
</ul>
