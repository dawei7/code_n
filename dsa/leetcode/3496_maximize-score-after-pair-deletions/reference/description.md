## Description

Begin with the integer array `nums`. While it contains more than two elements, an operation must delete exactly two current boundary elements: either the first two, the last two, or the first and last. Add both deleted values to the accumulated score, including negative values when they are selected.

Operations stop as soon as at most two elements remain; those survivors do not contribute to the score. Choose the deletion sequence that makes the total score as large as possible and return that maximum. The original order of all elements that remain after any operation is preserved.
