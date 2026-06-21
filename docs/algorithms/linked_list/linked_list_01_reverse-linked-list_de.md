# Reverse Linked List

| | |
|---|---|
| **ID** | `linked_list_01` |
| **Kategorie** | linked_list |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 10/10 |
| **LeetCode-Äquivalent** | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) |

## Problemstellung

Gegeben ist der `head` einer einfach verketteten Liste (singly linked list). Kehren Sie die Liste um und geben Sie den neuen `head` zurück.

**Eingabe:** Ein Node `head` einer einfach verketteten Liste.
**Ausgabe:** Ein Node einer einfach verketteten Liste, der den neuen `head` repräsentiert.

**Beispiel 1:**
`head = [1, 2, 3, 4, 5]`
Ausgabe: `[5, 4, 3, 2, 1]`.

## Wann man es verwendet

- Dies ist die absolut grundlegendste Operation für eine Linked List. Fast jeder fortgeschrittene Algorithmus für Linked Lists (wie das Prüfen auf Palindrome oder das Umkehren von Teilsegmenten) basiert vollständig auf Ihrer Fähigkeit, Pointer sicher in-place umzukehren.

## Ansatz

**Iterativer Ansatz (Drei-Pointer-Methode):**
Um eine einfach verkettete Liste umzukehren, müssen wir den `next`-Pointer jedes einzelnen Node so ändern, dass er auf den vorherigen Node zeigt.
Da es sich um eine einfach verkettete Liste handelt, weiß ein Node nicht, wer sein Vorgänger ist. Wir müssen daher manuell einen `prev`-Pointer verwalten!
Wenn wir `curr.next = prev` setzen, trennen wir sofort die Verbindung zum Rest der Liste! Um zu verhindern, dass der Rest der Liste verloren geht, müssen wir `curr.next` temporär in einem `next_node`-Pointer speichern, *bevor* wir ihn überschreiben.

1. Initialisiere `prev = None` und `curr = head`.
2. Solange `curr` nicht `None` ist:
   - Speichere den nächsten Node: `next_node = curr.next`.
   - Kehre den Pointer um: `curr.next = prev`.
   - Verschiebe `prev` nach vorne: `prev = curr`.
   - Verschiebe `curr` nach vorne: `curr = next_node`.
3. Wenn die Schleife endet, ist `curr` gleich `None` und `prev` zeigt auf den letzten verarbeiteten Node, welcher der neue `head` ist!

**Rekursiver Ansatz:**
Wir können rekursiv bis zum Ende der Liste traversieren. Der letzte Node wird zum neuen `head`. Während die Rekursion aufgelöst wird, weisen wir für einen gegebenen `node` dessen Nachfolger an, auf ihn zurückzuzeigen: `node.next.next = node`, und trennen dann den Vorwärtspointer `node.next = None`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for linked_list_01: Reverse Linked List.

Iterative in-place reversal. Walk the list with prev, cur,
nxt pointers; on each step, flip cur.next to prev, then
advance. O(n) time, O(1) space. Return the new parallel
``(values, next)`` representation.
"""


def solve(values, next, head, n):
    if n == 0 or head == -1:
        return values, next, -1
    new_next = list(next)
    prev = -1
    cur = head
    new_head = -1
    while cur != -1:
        nxt_node = new_next[cur]
        new_next[cur] = prev
        new_head = cur
        prev = cur
        cur = nxt_node
    return list(values), new_next, new_head
```

</details>

## Ablauf

*(Iterativ)*
`List: 1 -> 2 -> 3 -> None`.
`prev = None`, `curr = Node(1)`.

**Iteration 1:**
- `next_node = Node(2)`.
- `curr.next = prev` (Node 1 zeigt auf `None`).
- `prev = Node(1)`.
- `curr = Node(2)`.
*(Liste ist jetzt: 1 -> None, und 2 -> 3 -> None)*

**Iteration 2:**
- `next_node = Node(3)`.
- `curr.next = prev` (Node 2 zeigt auf Node 1).
- `prev = Node(2)`.
- `curr = Node(3)`.
*(Liste ist jetzt: 2 -> 1 -> None, und 3 -> None)*

**Iteration 3:**
- `next_node = None`.
- `curr.next = prev` (Node 3 zeigt auf Node 2).
- `prev = Node(3)`.
- `curr = None`.
*(Liste ist jetzt: 3 -> 2 -> 1 -> None)*

Schleife endet (`curr` ist None). Gib `prev` (Node 3) zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Der iterative Ansatz durchläuft die Liste genau einmal, was $O(N)$ Zeit in Anspruch nimmt, und verwendet drei zusätzliche Pointer, was $O(1)$ Platz benötigt.
Der rekursive Ansatz benötigt $O(N)$ Zeit, verbraucht aber aufgrund des rekursiven Aufruf-Stacks $O(N)$ Platz. In Vorstellungsgesprächen wird der iterative Ansatz fast immer bevorzugt.

## Varianten & Optimierungen

- **Teilsegment umkehren (Reverse Linked List II):** Kehren Sie nur die Nodes von Position `m` bis `n` um. Sie traversieren bis zur Position `m`, verwenden die exakt gleiche iterative Umkehrlogik für `n - m` Schritte und fügen dann den "Kopf" und das "Ende" des umgekehrten Segments sorgfältig wieder in die Hauptliste ein.
- **Umkehren in K-Blöcken:** Siehe `linked_list_05`.

## Anwendungen in der Praxis

- **Undo-Operationen:** Umkehren einer chronologischen Sequenz von Zustandsänderungen, die in einer einfach verketteten Liste gespeichert sind, um Operationen rückgängig zu machen.

## Verwandte Algorithmen in cOde(n)

- **[linked_list_05 - Reverse in Groups of K](ll_05_reverse-in-groups-of-k.md)** — Der ultimative Test für Ihre Meisterschaft in der Pointer-Manipulation.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*