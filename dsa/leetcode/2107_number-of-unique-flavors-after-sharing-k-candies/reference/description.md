## Description

You have a 0-indexed array `candies`, where each integer identifies one candy's flavor. To share with your little sister, you must select exactly `k` consecutive candies and give her that entire contiguous block. The candies before and after the selected block are the ones you keep.

Different choices of the shared block can remove different occurrences of repeated flavors. Choose its starting position so that the candies left with you contain as many unique flavors as possible, and return that maximum count. When `k = 0`, the shared block is empty and you keep every candy; when `k` equals the array length, you keep none.
