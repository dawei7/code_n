## Description

There are `k` workers who want to move `n` boxes from the right (old) warehouse to the left (new) warehouse. You are given the two integers `n` and `k`, and a 2D integer array `time` of size `k x 4` where `time[i] = [right_i, pick_i, left_i, put_i]`.

The warehouses are separated by a river and connected by a bridge. Initially, all `k` workers are waiting on the left side of the bridge. To move the boxes, the `i^th` worker can do the following:

<ul>
	<li>Cross the bridge to the right side in `right_i` minutes.</li>
	<li>Pick a box from the right warehouse in `pick_i` minutes.</li>
	<li>Cross the bridge to the left side in `left_i` minutes.</li>
	<li>Put the box into the left warehouse in `put_i` minutes.</li>
</ul>

The `i^th` worker is **less efficient** than the j`^th` worker if either condition is met:

<ul>
	<li>`left_i + right_i > left_j + right_j`</li>
	<li>`left_i + right_i == left_j + right_j` and `i > j`</li>
</ul>

The following rules regulate the movement of the workers through the bridge:

<ul>
	<li>Only one worker can use the bridge at a time.</li>
	<li>When the bridge is unused prioritize the **least efficient** worker (who have picked up the box) on the right side to cross. If not, prioritize the **least efficient** worker on the left side to cross.</li>
	<li>If enough workers have already been dispatched from the left side to pick up all the remaining boxes, **no more** workers will be sent from the left side.</li>
</ul>

Return the **elapsed minutes** at which the last box reaches the **left side of the bridge**.
