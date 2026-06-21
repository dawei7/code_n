# Merge Two Sorted Linked Lists

| | |
|---|---|
| **ID** | `linked_list_03` |
| **Kategorie** | linked_list |
| **Komplexität (erforderlich)** | $O(N + M)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) |

## Problemstellung

Gegeben sind die Köpfe (`heads`) zweier sortierter Linked Lists `list1` und `list2`.
Führen Sie die beiden Listen zu einer einzigen sortierten Liste zusammen. Die Liste sollte durch das Verknüpfen der Knoten der ersten beiden Listen entstehen (erstellen Sie keine neuen Knoten, sondern passen Sie lediglich die bestehenden Pointer an).
Geben Sie den Kopf der zusammengeführten Linked List zurück.

**Input:** Zwei einfach verkettete Listen-Knoten `list1` und `list2`.
**Output:** Ein einfach verketteter Listen-Knoten, der den Kopf der zusammengeführten Liste repräsentiert.

**Beispiel:**
`list1 = [1, 2, 4]`, `list2 = [1, 3, 4]`
Output: `[1, 1, 2, 3, 4, 4]`.

## Wann man es verwendet

- Um das "Dummy Head"-Paradigma zu verstehen, welches wohl das wichtigste Entwurfsmuster ist, um Abstürze durch Randfälle bei der Manipulation von Linked Lists zu vermeiden.
- Es ist die zentrale Subroutine, die für die Implementierung von Merge Sort auf einer Linked List erforderlich ist.

## Ansatz

Wir müssen beide Listen gleichzeitig durchlaufen. In jedem Schritt vergleichen wir die aktuellen Knoten beider Listen, wählen den kleineren aus, hängen ihn an unsere zusammengeführte Liste an und rücken den Pointer der Liste vor, aus der wir den Knoten gewählt haben.

**Das "Dummy Node"-Muster:**
Beim Aufbau einer neuen Linked List ist der schwierigste Teil der Umgang mit dem allerersten Knoten (dem `head`). Wenn die Liste anfangs leer ist, müssen wir eine spezielle `if not head: head = node`-Logik schreiben.
Um dies vollständig zu vermeiden, erstellen wir einen künstlichen `dummy`-Knoten (z. B. `Node(-1)`).
Wir verwenden einen `tail`-Pointer, der bei `dummy` beginnt.
Wir können nun blind Knoten mit `tail.next = picked_node` anhängen, ohne uns jemals um `None`-Exceptions sorgen zu müssen!
Ganz am Ende geben wir einfach `dummy.next` zurück, um die tatsächliche Liste zu erhalten, wobei der künstliche `dummy`-Knoten vollständig ignoriert wird.

1. Initialisiere `dummy = Node(-1)` und `tail = dummy`.
2. Solange `list1` und `list2` beide nicht `None` sind:
   - Wenn `list1.val <= list2.val`:
     - `tail.next = list1`
     - `list1 = list1.next`
   - Sonst:
     - `tail.next = list2`
     - `list2 = list2.next`
   - `tail = tail.next`
3. Wenn eine Liste vor der anderen erschöpft ist, sind die verbleibenden Elemente in der anderen Liste bereits sortiert! Wir können einfach den gesamten verbleibenden Teil in einer $O(1)$-Operation anhängen: `tail.next = list1 if list1 else list2`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for linked_list_03: Merge Two Sorted Lists.

Two-pointer walk. On each step, attach the smaller of the two
heads to the merged tail and advance that head. Append the
remaining tail of the non-empty list. Return the merged
``(values, next)`` representation.
"""


def solve(values1, next1, head1, values2, next2, head2, n1, n2):
    if n1 == 0:
        merged = list(values2)
    elif n2 == 0:
        merged = list(values1)
    else:
        merged = []
        i, j = head1, head2
        while i != -1 and j != -1:
            if values1[i] <= values2[j]:
                merged.append(values1[i])
                i = next1[i]
            else:
                merged.append(values2[j])
                j = next2[j]
        while i != -1:
            merged.append(values1[i])
            i = next1[i]
        while j != -1:
            merged.append(values2[j])
            j = next2[j]
    n = len(merged)
    merged_nxt = [k + 1 for k in range(n - 1)] + [-1]
    return merged, merged_nxt
```

</details>

## Durchlauf

`L1: 1 -> 3`, `L2: 2 -> 4`.
`dummy = Node(-1)`, `tail = dummy`.

1. `L1 (1) < L2 (2)`.
   - `tail.next = Node(1)`. `tail` bewegt sich zu `Node(1)`.
   - `L1` bewegt sich zu `Node(3)`.
2. `L1 (3) > L2 (2)`.
   - `tail.next = Node(2)`. `tail` bewegt sich zu `Node(2)`.
   - `L2` bewegt sich zu `Node(4)`.
3. `L1 (3) < L2 (4)`.
   - `tail.next = Node(3)`. `tail` bewegt sich zu `Node(3)`.
   - `L1` bewegt sich zu `None`.
4. Die Schleife terminiert, da `L1` gleich `None` ist.
5. Anhängen der Reste: `L1` ist `None`, also `tail.next = L2 (Node(4))`.

Zusammengeführte Liste: `-1 -> 1 -> 2 -> 3 -> 4`.
Rückgabe von `dummy.next`: `1 -> 2 -> 3 -> 4`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N + M)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N + M)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N + M)$ | $O(1)$ |

Wir durchlaufen jeden Knoten in beiden Listen genau einmal. Die Zeitkomplexität ist strikt $O(N + M)$.
Da wir lediglich bestehende Pointer neu verknüpfen und keine neuen Knoten erstellen (außer dem einzelnen $O(1)$ `dummy`-Knoten), ist die Platzkomplexität strikt $O(1)$.

## Varianten & Optimierungen

- **Merge K Sorted Lists:** Sie erhalten K sortierte Linked Lists. Sie können dies lösen, indem Sie diese paarweise zusammenführen (Divide and Conquer, $O(N log K)$) oder indem Sie alle K Köpfe in eine Min-Heap einfügen. Der Min-Heap-Ansatz liefert Ihnen sofort den absolut kleinsten Knoten unter allen K Listen. Sie entnehmen den kleinsten, hängen ihn an Ihren `dummy`-`tail` an und fügen den `next`-Knoten dieses Knotens wieder in den Heap ein! Dies läuft ebenfalls in $O(N log K)$, ist aber oft einfacher zu implementieren.

## Anwendungen in der Praxis

- **External Merge Sort:** Wenn Datensätze sortiert werden müssen, die zu groß für den Arbeitsspeicher sind (wie 100-GB-Datenbanken), werden Teilmengen sortiert und auf der Festplatte gespeichert. Ein Pointer wird dem Anfang jedes Datei-Chunks zugewiesen, und diese werden genau wie hier zusammengeführt, um das endgültig sortierte Ergebnis zu erzeugen, ohne die RAM-Beschränkungen zu überschreiten.

## Verwandte Algorithmen in cOde(n)

- **[heap_04 - Merge K Sorted Lists](../heap/heap_04_merge-k-sorted-lists.md)** — Die Verallgemeinerung für mehrere Listen unter Verwendung von Priority Queues.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*