## Description

Two roads meet at one intersection. Road A carries north-to-south traffic in direction `1` and south-to-north traffic in direction `2`. Road B carries west-to-east traffic in direction `3` and east-to-west traffic in direction `4`.

Each road has a traffic light before the intersection. A green light permits cars in either direction on that road to cross; a red light requires both directions to wait. The two roads may never have green lights simultaneously: whenever Road A is green, Road B is red, and vice versa. Road A starts green and Road B starts red.

Cars may continue crossing in both directions of the green road until the other road receives the green light. Cars traveling on different roads must never cross at the same time.

Design a deadlock-free controller for this intersection. For every arriving car, invoke the supplied callbacks so that the correct road is green before the car crosses. Calling `turnGreen` when the arriving car's road is already green is a wrong answer.
