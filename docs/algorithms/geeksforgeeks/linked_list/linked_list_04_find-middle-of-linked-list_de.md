# Find Middle of Linked List

| | |
|---|---|
| **ID** | `linked_list_04` |
| **Category** | linked_list |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 1/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) |

## Problem statement

Gegeben ist der `head` einer einfach verketteten Liste (Singly Linked List). Geben Sie den mittleren Knoten der Liste zurück.
Falls es zwei mittlere Knoten gibt (d. h. die Länge ist gerade), geben Sie den **zweiten** mittleren Knoten zurück.

**Input:** Ein `head` Knoten einer einfach verketteten Liste.
**Output:** Ein Knoten der einfach verketteten Liste, der die Mitte repräsentiert.

**Beispiel 1 (Ungerade):**
`head = [1, 2, 3, 4, 5]`
Output: `Node(3)`.

**Beispiel 2 (Gerade):**
`head = [1, 2, 3, 4, 5, 6]`
Output: `Node(4)`. (Die beiden mittleren Knoten sind 3 und 4, wir geben den zweiten zurück).

## Anwendung

- Als Hilfsroutine, um eine Linked List sauber in zwei Hälften zu teilen, beispielsweise für Divide-and-Conquer-Algorithmen (wie Merge Sort für Linked Lists) oder zur Überprüfung auf Palindrome.
- Festigt das Paradigma der **Fast and Slow Pointers**.

## Ansatz

Ein naiver Ansatz benötigt zwei Durchläufe:
1. Traversieren der gesamten Liste, um die Gesamtzahl der Knoten N zu bestimmen.
2. Erneutes Traversieren und Stoppen bei N / 2.
Dies erfordert $O(1.5 N)$ Iterationen.

Wir können dies in exakt einem Durchlauf (0.5 N Iterationen) erreichen, indem wir **Fast and Slow Pointers** verwenden.

1. Initialisiere zwei Pointer: `slow` und `fast`, die beide auf `head` zeigen.
2. Bewege `slow` um 1 Schritt und `fast` um 2 Schritte.
3. Da sich `fast` doppelt so schnell bewegt, befindet sich `slow` mathematisch gesehen exakt am Mittelpunkt, sobald `fast` das Ende der Liste erreicht!

*Behandlung von Randfällen:*
Wenn die Liste `[1, 2]` ist:
- Initial: `slow=1`, `fast=1`.
- Schritt 1: `slow=2`, `fast=None`.
- Die Schleife terminiert. `slow` steht auf `2` (dem zweiten mittleren Knoten). Perfekt!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for linked_list_04: Find Middle of Linked List.

Slow and fast pointers: slow moves 1 step, fast moves 2. When
fast hits the end, slow is at the middle. Return (new_values,
new_next, new_head) with the list unchanged structurally
(only the head is set to the middle index).
"""


def solve(values, next, head, n):
    if n == 0 or head == -1:
        return list(values), list(next), -1
    slow = head
    fast = head
    while fast != -1 and next[fast] != -1:
        slow = next[slow]
        fast = next[next[fast]]
    return list(values), list(next), slow
```

</details>

## Ablauf

*(Ungerade Länge)*
`List: 1 -> 2 -> 3 -> 4 -> 5`
- Start: `S=1, F=1`.
- Iteration 1: `S=2, F=3`.
- Iteration 2: `S=3, F=5`.
- Iteration 3: `F.next` ist `None`. Schleife terminiert.
Rückgabe `S` (`Node(3)`). ✓

*(Gerade Länge)*
`List: 1 -> 2 -> 3 -> 4`
- Start: `S=1, F=1`.
- Iteration 1: `S=2, F=3`.
- Iteration 2: `S=3, F=None`.
- Iteration 3: `F` ist `None`. Schleife terminiert.
Rückgabe `S` (`Node(3)`). ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Der Fast Pointer traversiert N Knoten, was N/2 Iterationen entspricht. Die Zeitkomplexität ist strikt $O(N)$.
Unabhängig von der Listengröße werden nur zwei Pointer instanziiert. Die Platzkomplexität ist $O(1)$.

## Varianten & Optimierungen

- **Erster mittlerer Knoten:** Wenn das Problem den *ersten* mittleren Knoten bei einer Liste gerader Länge verlangt (z. B. Rückgabe von `3` statt `4` bei `[1, 2, 3, 4, 5, 6]`), initialisiert man den Fast Pointer einfach einen Schritt weiter vorne! `slow = head, fast = head.next`.
- **Palindrome Linked List:** Verwenden Sie diesen Algorithmus, um die Mitte zu finden. Nutzen Sie anschließend `linked_list_01`, um die zweite Hälfte der Liste in-place umzukehren. Verwenden Sie schließlich zwei Pointer (einen am Anfang, einen in der Mitte), um die Liste zu durchlaufen und zu prüfen, ob die Werte übereinstimmen. So lässt sich die Palindrom-Eigenschaft in $O(N)$ Zeit und $O(1)$ Platz prüfen!

## Anwendungen in der Praxis

- **Netzwerk-Routing:** In Gossip-Protokollen erfordert das rekursive Halbieren der Übertragungsdistanz eine effiziente Identifizierung topologischer Mittelpunkte, ohne den gesamten Netzwerkzustand abbilden zu müssen.

## Verwandte Algorithmen in cOde(n)

- **[linked_list_02 - Detect Cycle](ll_02_detect-cycle-in-linked-list.md)** — Der andere zentrale Anwendungsfall für Fast/Slow Pointers.

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*