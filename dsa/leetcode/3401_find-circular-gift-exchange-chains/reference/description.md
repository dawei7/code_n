## Description

The `SecretSanta` table records directed gift exchanges between employees. Each row identifies the employee giving the gift, the employee receiving it, and the gift's value. A circular chain is a continuous loop in which every participating employee gives to exactly one other employee and receives from exactly one other employee.

Find each distinct chain statistic: the number of exchanges in the loop and the sum of their gift values. Assign `chain_id` values after sorting first by chain length and then by total gift value, both in descending order. The verified platform result represents equal `(chain_length, total_gift_value)` pairs once, even if separate employee loops share those same two statistics.
