# Boundary Traversal of Binary Tree

| | |
|---|---|
| **ID** | `tree_19` |
| **Category** | trees |
| **Complexity (required)** | $O(N)$ Time, $O(H)$ Space |
| **Difficulty** | 6/10 |
| **Interview relevance** | 5/10 |
| **GeeksForGeeks Equivalent** | [Boundary Traversal of binary tree](https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/) |

## Problem statement

Gegeben ist ein Binary Tree. Geben Sie die Boundary-Knoten des Binary Tree gegen den Uhrzeigersinn aus, beginnend bei der Root.
Die Boundary umfasst:
1. Die Left Boundary (ohne Blattknoten).
2. Alle Blattknoten (von links nach rechts).
3. Die Right Boundary (ohne Blattknoten, in umgekehrter Reihenfolge).

**Input:** Ein `root`-Knoten eines Binary Tree.
**Output:** Ein Array von Integern, das die Boundary gegen den Uhrzeigersinn repräsentiert.

## When to use it

- Um Ihre Fähigkeit zu testen, ein komplexes Problem in kleinere, modulare und hochspezifische Tree-Traversal-Funktionen zu zerlegen.

## Approach

Dieses Problem wirkt zunächst überwältigend, wird aber trivial, wenn man es in 4 distinkte, aufeinanderfolgende Schritte unterteilt.

**1. Die Root:**
Fügen Sie die Root zum Ergebnis-Array hinzu (es sei denn, die Root ist selbst ein Blattknoten; in diesem Fall wollen wir sie nicht doppelt hinzufügen!).

**2. Die Left Boundary (Top-Down):**
Erstellen Sie eine Funktion, die bei `root.left` beginnt.
Wir fügen den Knoten zum Ergebnis hinzu. Wir bewegen uns zu `node.left`.
Was passiert, wenn `node.left` null ist? Die Boundary endet hier nicht! Sie verläuft im Zickzack! Wir bewegen uns stattdessen zu `node.right`.
Wir setzen dies fort, bis wir einen Blattknoten erreichen. Wir fügen den Blattknoten NICHT hinzu (Blätter werden in Schritt 3 behandelt).

**3. Die Blätter (Left-to-Right):**
Erstellen Sie eine Standard Pre-Order DFS-Funktion (`tree_01`).
Wenn der Knoten ein Blatt ist (`!node.left and !node.right`), fügen Sie ihn zum Ergebnis hinzu!
Andernfalls durchsuchen Sie rekursiv `node.left` und `node.right`. Dies garantiert mathematisch, dass die Blätter perfekt von links nach rechts hinzugefügt werden.

**4. Die Right Boundary (Bottom-Up):**
Erstellen Sie eine Funktion, die bei `root.right` beginnt.
Wir bewegen uns zu `node.right`. Wenn dieser null ist, gehen wir im Zickzack zu `node.left`.
Wir fahren fort, bis wir ein Blatt erreichen (dieses nicht hinzufügen).
ABER ACHTUNG! Die Boundary muss gegen den Uhrzeigersinn verlaufen! Wir bewegen uns die Right Boundary HINUNTER, müssen sie aber AUFWÄRTS ausgeben!
Wie kehren wir sie um? Wir verwenden ein temporäres Array (oder den rekursiven Call Stack), um die Knoten beim Abstieg zu sammeln, und hängen sie dann in umgekehrter Reihenfolge an unser Haupt-Ergebnis-Array an!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for tree_19: Boundary Traversal.

Walk the boundary of a binary tree anti-clockwise:
left edge top-to-bottom, then leaves left-to-right, then
right edge bottom-to-top.
"""


def solve(children, root, n):
    """Boundary traversal: left edge + leaves + right edge (reversed)."""
    if root == -1:
        return []
    out = [root]

    def is_leaf(u):
        return children[u][0] == -1 and children[u][1] == -1

    def left_boundary(u):
        cur = children[u][0]
        while cur != -1:
            if not is_leaf(cur):
                out.append(cur)
            cur = children[cur][0] if children[cur][0] != -1 else children[cur][1]

    def leaves(u):
        if u == -1:
            return
        if is_leaf(u):
            out.append(u)
        else:
            leaves(children[u][0])
            leaves(children[u][1])

    def right_boundary(u):
        stack = []
        cur = children[u][1]
        while cur != -1:
            if not is_leaf(cur):
                stack.append(cur)
            cur = children[cur][1] if children[cur][1] != -1 else children[cur][0]
        while stack:
            out.append(stack.pop())

    if not is_leaf(root):
        left_boundary(root)
        leaves(root)
        right_boundary(root)
    # If root is a leaf, leaves() would only emit root; we
    # already added it. The contract: include the root exactly once.
    return out
```

</details>

## Walk-through

Tree:
```text
        1
      /   \
     2     3
    / \   / 
   4   5 6   
      / \
     7   8
```

1. **Root:** Füge `1` hinzu. `res = [1]`.
2. **Left Boundary:** Starte bei `2`.
   - `2` ist kein Blatt. Füge `2` hinzu. `res = [1, 2]`.
   - Gehe links zu `4`.
   - `4` ist ein Blatt. Stopp!
3. **Blätter:** Starte DFS von der Root `1`.
   - Erreicht `4` (Blatt). Füge `4` hinzu. `res = [1, 2, 4]`.
   - Erreicht `7` (Blatt). Füge `7` hinzu. `res = [1, 2, 4, 7]`.
   - Erreicht `8` (Blatt). Füge `8` hinzu. `res = [1, 2, 4, 7, 8]`.
   - Erreicht `6` (Blatt). Füge `6` hinzu. `res = [1, 2, 4, 7, 8, 6]`.
4. **Right Boundary:** Starte bei `3`.
   - `3` ist kein Blatt. Füge `3` zu `tmp = [3]` hinzu.
   - `3` hat kein rechtes Kind! Zickzack links zu `6`.
   - `6` ist ein Blatt. Stopp!
   - Kehre `tmp` um: `[3]`.
   - An `res` anhängen: `res = [1, 2, 4, 7, 8, 6, 3]`.

Ergebnis: `[1, 2, 4, 7, 8, 6, 3]`. ✓

## Complexity

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(H)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(H)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Die Left Boundary benötigt $O(H)$ Zeit. Die Right Boundary benötigt $O(H)$ Zeit. Das Sammeln der Blätter durchläuft den gesamten Baum und benötigt $O(N)$ Zeit.
Die gesamte Zeitkomplexität beträgt exakt $O(N)$.
Die Platzkomplexität ist durch den rekursiven Call Stack für das Sammeln der Blätter und das temporäre Array für die Right Boundary begrenzt. Der maximale Platzbedarf ist proportional zur Höhe des Baumes $O(H)$, was sich im schlechtesten Fall zu $O(N)$ verschlechtert.

## Variants & optimizations

- **Anti-Clockwise Matrix Spiral (`array_03`):** Das exakte konzeptionelle Äquivalent dieses Problems angewendet auf ein 2D-Array! Sie schälen die oberen, rechten, unteren und linken Ränder in einer while-Schleife ab.

## Real-world applications

- **Convex Hull Rendering:** In der Grafik ermöglicht die Berechnung der "Boundary"-Knoten bei einem massiven hierarchischen Layout von Formen dem System, die äußere Silhouette sofort zu zeichnen, ohne die Tausenden von inneren Formen verarbeiten zu müssen.

## Related algorithms in cOde(n)

- **[tree_18 - Right Side View](tree_18_right-side-view.md)** — Ein visuell ähnliches Problem, aber die "View" ist strikt vertikal, während die "Boundary" den strukturellen Kanten folgt, selbst wenn diese nach innen zickzacken.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Competitive Programming verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Source repository: <https://github.com/dawei7/code_n>.*