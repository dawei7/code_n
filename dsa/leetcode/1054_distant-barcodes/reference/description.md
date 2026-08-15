### 1. Description

In a warehouse, there is a row of barcodes, where the $$i^{\text{th}}$$ barcode is $\text{barcodes}[i]$.

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

### 2. Function Contract

**Inputs**

- `barcodes`: Input parameter (`List[int]`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** $barcodes = [1,1,1,2,2,2]$
- **Output:** `[2,1,2,1,2,1]`

#### Example 2

- **Input:** $barcodes = [1,1,1,1,2,2,3,3]$
- **Output:** `[1,3,1,3,1,2,1,2]`

### 4. Constraints

- $1 \le \text{barcodes.length} \le 10000$

- $1 \le \text{barcodes}[i] \le 10000$
