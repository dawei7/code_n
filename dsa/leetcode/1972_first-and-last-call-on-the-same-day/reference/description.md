## Description

The `Calls` table records phone calls with a caller, a recipient, and a
timestamp. For every user and calendar day on which that user participated in
at least one call, consider the other person in the user's chronologically
first call and the other person in the user's chronologically last call.

Report each user who has at least one day where those two people are the same.
A call counts for both participants regardless of which one is stored as the
caller. Return each qualifying user ID once, in any order.
