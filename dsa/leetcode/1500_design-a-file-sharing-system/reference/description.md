## Description

A very large file is divided into $m$ chunks whose identifiers run from $1$ through $m$. Users may enter and leave a sharing system while owning different subsets of those chunks. Every joining user must receive the smallest positive user ID that is not currently assigned; an ID becomes available for reuse after its user leaves.

A user may request one chunk. The system must report, in ascending user-ID order, every current user who owns that chunk. A nonempty result means the transfer succeeds, so the requester also owns the chunk from that point onward. An empty result means no transfer occurs. Implement construction, joining, leaving, and requesting while keeping both user IDs and chunk ownership consistent through the entire operation stream.
