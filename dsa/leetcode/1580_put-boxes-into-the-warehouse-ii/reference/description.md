## Description

You are given unit-width boxes with heights listed in `boxes` and a warehouse whose rooms are arranged from left to right with ceiling heights listed in `warehouse`. At most one box may occupy a room, and boxes cannot be stacked.

You may reorder the boxes and push each box into the warehouse from either the left entrance or the right entrance. A box cannot pass through a room whose height is smaller than the box; that room stops the box and any boxes queued behind it from that direction.

Choose the insertion order and entrance for every placed box. Return the maximum number of boxes that can be stored in the warehouse under these movement and height restrictions.
