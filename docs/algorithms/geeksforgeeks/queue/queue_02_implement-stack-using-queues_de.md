# Implement Stack using Queues

| | |
|---|---|
| **ID** | `queue_02` |
| **Kategorie** | queue |
| **Komplexität (erforderlich)** | $O(N)$ Push, $O(1)$ Pop |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) |

## Problemstellung

Implementieren Sie einen Last-In-First-Out (LIFO) Stack unter Verwendung von nur zwei Queues. Der implementierte Stack sollte alle Funktionen eines normalen Stacks unterstützen (`push`, `top`, `pop` und `empty`).

Sie dürfen nur Standardoperationen einer Queue verwenden, das heißt, nur `push to back`, `peek/pop from front`, `size` und `is empty` sind zulässig.

**Eingabe:** Eine Sequenz von Stack-Operationen.
**Ausgabe:** Die Ergebnisse der `top`- und `pop`-Operationen.

**Beispiel:**
```text
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top();   // return 2
myStack.pop();   // return 2
myStack.empty(); // return False
```

## Wann man es verwendet

- Eine Übung für Vorstellungsgespräche, um das Verständnis für die Rotation von Datenstrukturen zu testen.
- In produktiver Software nicht praktisch nützlich (im Gegensatz zum Aufbau von Queues aus Stacks, was Anwendungsfälle in der funktionalen Programmierung hat).

## Ansatz

Eine Queue ist **FIFO** (First-In, First-Out).
Ein Stack ist **LIFO** (Last-In, First-Out).

Damit sich eine Queue wie ein Stack verhält, muss das zuletzt hinzugefügte Element auf magische Weise an den *Anfang* der Queue gelangen, damit es als Erstes entfernt werden kann.
Im Gegensatz zu Stacks, die die Reihenfolge beim Umfüllen ineinander perfekt umkehren, bleibt die Reihenfolge beim Umfüllen einer Queue in eine andere Queue exakt gleich!

**Der 1-Queue-Rotationstrick:**
Wenn wir ein neues Element `x` in eine Queue einfügen, landet es ganz hinten.
Wenn wir es am Anfang haben wollen, können wir einfach die aktuelle Größe der Queue `s` messen, `x` hinten anfügen und dann das vordere Element `s` mal **entfernen und wieder hinten anfügen**!
Dies rotiert die gesamte Queue wie ein Fließband und zieht das neu hinzugefügte Element ganz nach vorne.

Dies macht zwei Queues komplett überflüssig! Wir können es mit nur einer einzigen Queue aufbauen.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for queue_02: Implement Stack using Queues.

Implement a LIFO stack using only FIFO queues
"""


def solve(operations, n):
    """Implement LIFO stack using one FIFO queue."""
    from collections import deque
    q = deque()
    results = []
    for op in operations:
        name = op[0]
        if name == "push":
            q.append(op[1])
            # Rotate: dequeue and re-enqueue (len(q) - 1) times
            # so the new element ends up at the front.
            for _ in range(len(q) - 1):
                q.append(q.popleft())
        elif name == "pop":
            if q:
                q.popleft()
        elif name == "top":
            if q:
                results.append(q[0])
        elif name == "empty":
            pass
    return results
```

</details>

## Ablauf

1. `push(1)`: 
   - `s = 0`.
   - `1` anhängen. Queue: `[1]`.
   - `0` mal rotieren. Queue: `[1]`.
2. `push(2)`:
   - `s = 1`.
   - `2` anhängen. Queue: `[1, 2]`.
   - `1` mal rotieren. `1` entfernen, `1` anhängen. Queue: `[2, 1]`.
3. `push(3)`:
   - `s = 2`.
   - `3` anhängen. Queue: `[2, 1, 3]`.
   - `2` mal rotieren:
     - `2` entfernen, `2` anhängen. Queue: `[1, 3, 2]`.
     - `1` entfernen, `1` anhängen. Queue: `[3, 2, 1]`.
4. `pop()`:
   - Vorderstes Element entfernen. Gibt `3` zurück. Queue: `[2, 1]`.
5. `pop()`:
   - Vorderstes Element entfernen. Gibt `2` zurück. Queue: `[1]`.

Alle Elemente kamen in der exakten Reihenfolge `3, 2, 1` heraus. LIFO! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ Push | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ Push | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ Push | $O(N)$ |

- **Push:** Streng $O(N)$. Jedes Mal, wenn wir ein Element hinzufügen, müssen wir physisch alle $N$ bereits vorhandenen Elemente rotieren.
- **Pop / Top:** Streng $O(1)$. Da die Schwerstarbeit während des `push` erledigt wird, liegt das neueste Element immer geduldig am Anfang der Queue.
Die Platzkomplexität beträgt $O(N)$ für die Queue.

## Varianten & Optimierungen

- **Zwei Queues ($O(N)$ Pop):** Die "offizielle" naive Lösung besteht darin, `q1` und `q2` zu verwenden. Um `push` auszuführen, fügt man einfach in $O(1)$ zu `q1` hinzu. Um `pop` auszuführen, entfernt man $N-1$ Elemente aus `q1` und fügt sie in `q2` ein, entfernt das letzte verbleibende Element in `q1` und gibt es zurück, und tauscht dann die Referenzen von `q1` und `q2`. Dies macht `push` zu $O(1)$ und `pop` zu $O(N)$.
- **Warum ist 1-Queue besser?** Weil der 1-Queue-Ansatz die exakt gleiche Zeitkomplexität aufweist, aber buchstäblich die Hälfte der Speicherallokation benötigt und die Verwaltung von zwei Pointern vermeidet.

## Anwendungen in der Praxis

- **Fließband-Scheduling:** Strukturierung von Round-Robin-CPU-Schedulern, um die Priorität eines eingehenden Threads dynamisch zu erhöhen, indem der Ausführungs-Ringpuffer manuell vorgespult wird.

## Verwandte Algorithmen in cOde(n)

- **[queue_01 - Implement Queue using Stacks](queue_01_implement-queue-using-stacks.md)** — Das inverse Problem, welches auf brillante Weise eine amortisierte $O(1)$-Zeit für alle Operationen erreicht.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*