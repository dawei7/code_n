## Description

You have the task of delivering some boxes from storage to their ports using only one ship. However, this ship has a **limit** on the **number of boxes** and the **total weight** that it can carry.

You are given an array `boxes`, where `boxes[i] = [ports_​​i​, weight_i]`, and three integers `portsCount`, `maxBoxes`, and `maxWeight`.

<ul>
	<li>`ports_​​i` is the port where you need to deliver the `i^th` box and `weights_i` is the weight of the `i^th` box.</li>
	<li>`portsCount` is the number of ports.</li>
	<li>`maxBoxes` and `maxWeight` are the respective box and weight limits of the ship.</li>
</ul>

The boxes need to be delivered **in the order they are given**. The ship will follow these steps:

<ul>
	<li>The ship will take some number of boxes from the `boxes` queue, not violating the `maxBoxes` and `maxWeight` constraints.</li>
	<li>For each loaded box **in order**, the ship will make a **trip** to the port the box needs to be delivered to and deliver it. If the ship is already at the correct port, no **trip** is needed, and the box can immediately be delivered.</li>
	<li>The ship then makes a return **trip** to storage to take more boxes from the queue.</li>
</ul>

The ship must end at storage after all the boxes have been delivered.

Return *the **minimum** number of **trips** the ship needs to make to deliver all boxes to their respective ports.*
