# Zyklus in einer Linked List erkennen

| | |
|---|---|
| **ID** | `linked_list_02` |
| **Kategorie** | linked_list |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Linked List Cycle I & II](https://leetcode.com/problems/linked-list-cycle/) |

## Problemstellung

Gegeben ist `head`, der Anfang einer Linked List. Bestimmen Sie, ob die Linked List einen Zyklus enthält.
Ein Zyklus existiert, wenn es einen Knoten in der Liste gibt, der durch kontinuierliches Folgen des `next`-Pointers erneut erreicht werden kann.
Geben Sie `True` zurück, falls ein Zyklus existiert, andernfalls `False`.
*(Zusatzaufgabe: Falls ein Zyklus existiert, geben Sie den EXAKTEN Knoten zurück, an dem der Zyklus beginnt).*

**Eingabe:** Ein Node `head` einer einfach verketteten Liste.
**Ausgabe:** Ein Boolean (oder ein Node für die Zusatzaufgabe).

**Beispiel:**
`head = [3, 2, 0, -4]`, wobei `-4` zurück auf `2` zeigt.
Ausgabe: `True` (Zyklus beginnt bei Knoten `2`).

## Wann wird es verwendet?

- Zur Erkennung von Endlosschleifen bei pointer-basierten Traversierungen.
- Dies ist die klassische Einführung in **Floyds Zyklenerkennungsalgorithmus** (auch bekannt als Tortoise and Hare Algorithmus).

## Ansatz

Eine naive Lösung speichert jeden besuchten Knoten in einem Hash Set. Wenn Sie jemals auf einen Knoten stoßen, der bereits im Set enthalten ist, existiert ein Zyklus! Dies benötigt $O(N)$ Zeit und $O(N)$ Platz.
Wir können dies mit $O(1)$ Platz unter Verwendung von **Two Pointers** lösen: einem Slow-Pointer (Schildkröte) und einem Fast-Pointer (Hase).

**Zyklus erkennen:**
1. Beide Pointer starten am `head`.
2. Der Slow-Pointer bewegt sich 1 Schritt pro Iteration (`slow = slow.next`).
3. Der Fast-Pointer bewegt sich 2 Schritte pro Iteration (`fast = fast.next.next`).
4. Wenn KEIN Zyklus vorhanden ist, erreicht der Fast-Pointer irgendwann das Ende der Liste (`None`).
5. Wenn ein Zyklus vorhanden ist, wird der Fast-Pointer den Slow-Pointer innerhalb der Schleife überrunden. Es ist mathematisch garantiert, dass sie irgendwann auf exakt denselben Knoten zeigen!

**Start des Zyklus finden (Der mathematische Trick):**
Wenn sie sich treffen, wissen wir, dass ein Zyklus existiert. Aber wo beginnt er?
Sei L die Distanz vom `head` zum Zyklusstart.
Sei C die Länge des Zyklus.
Wenn sie sich treffen, hat der Slow-Pointer L + x Schritte zurückgelegt (wobei x die Distanz innerhalb des Zyklus ist).
Der Fast-Pointer hat L + x + nC Schritte zurückgelegt.
Da der Fast-Pointer doppelt so schnell ist: 2(L + x) = L + x + nC.
Nach L aufgelöst: L = nC - x.
Das bedeutet, die Distanz vom `head` zum Zyklusstart (L) ist mathematisch identisch mit der Distanz vom Treffpunkt zum Zyklusstart!
**Algorithmus:** Lassen Sie den `slow`-Pointer am Treffpunkt. Setzen Sie den `fast`-Pointer zurück auf den `head`. Bewegen Sie nun BEIDE Pointer 1 Schritt pro Iteration. Der exakte Knoten, an dem sie erneut kollidieren, ist der Start des Zyklus!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for linked_list_02: Detect Cycle.

Floyd's tortoise and hare: walk with slow and fast pointers
that advance 1 and 2 steps at a time respectively. If they
ever meet, there's a cycle; if fast reaches the end, there
isn't. O(n) time, O(1) space.
"""


def solve(next, head, n):
    if n == 0 or head == -1:
        return False
    slow = head
    fast = head
    while fast != -1 and next[fast] != -1:
        slow = next[slow]
        fast = next[next[fast]]
        if slow == fast:
            return True
    return False
```

</details>

## Durchlauf

Liste: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> (zurück zu 3)`

**Phase 1 (Erkennen):**
- Start: `S=1, F=1`.
- Schritt 1: `S=2, F=3`.
- Schritt 2: `S=3, F=5`.
- Schritt 3: `S=4, F=3`. (F springt von 6 auf 3).
- Schritt 4: `S=5, F=5`.
Kollision bei `5`! Zyklus existiert.

**Phase 2 (Start finden):**
- Reset Fast: `S=5, F=1`.
- 1 Schritt: `S=6, F=2`.
- 1 Schritt: `S=3, F=3`.
Kollision bei `3`! Der Zyklus beginnt bei Knoten `3`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Der Fast-Pointer wird den Slow-Pointer in maximal N Schritten einholen. Die Zeitkomplexität ist strikt $O(N)$.
Es werden nur zwei Pointer verwendet. Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Die doppelte Zahl finden ($O(1)$ Platz):** Gegeben ist ein Array von Integern, deren Werte zwischen 1 und N liegen. Finden Sie die einzige doppelte Zahl, ohne das Array zu verändern. Sie können die Array-Werte als "next-Pointer" betrachten (`next_node = arr[current_node]`). Da mehrere Zahlen auf den doppelten Wert zeigen, bildet sich ein Zyklus! Sie können exakt diesen Linked-List-Algorithmus verwenden, um den Start des Zyklus zu finden, welcher die doppelte Zahl ist!

## Anwendungen in der Praxis

- **Deadlock-Erkennung:** Betriebssysteme überwachen Ressourcenallokationsgraphen. Wenn ein gerichteter Zyklus mittels Pointer-Traversierung erkannt wird, ist ein Deadlock aufgetreten.

## Verwandte Algorithmen in cOde(n)

- **[linked_list_04 - Find Middle of Linked List](ll_04_find-middle-of-linked-list.md)** — Die andere grundlegende Anwendung der Slow/Fast-Pointer-Technik.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*