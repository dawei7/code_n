# Implement Queue using Stacks

| | |
|---|---|
| **ID** | `queue_01` |
| **Kategorie** | queue |
| **Komplexität (erforderlich)** | Amortisiert $O(1)$ Push/Pop |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) |

## Problemstellung

Implementieren Sie eine First-In-First-Out (FIFO) Queue unter Verwendung von nur zwei Stacks. Die implementierte Queue sollte alle Funktionen einer normalen Queue unterstützen (`push`, `peek`, `pop` und `empty`).

Sie dürfen nur Standardoperationen eines Stacks verwenden, das heißt, nur `push to top`, `peek/pop from top`, `size` und `is empty` sind zulässig.

**Eingabe:** Eine Sequenz von Queue-Operationen.
**Ausgabe:** Die Ergebnisse der `peek`- und `pop`-Operationen.

**Beispiel:**
```text
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek();  // return 1
myQueue.pop();   // return 1, queue is [2]
myQueue.empty(); // return false
```

## Wann man es verwendet

- Eine grundlegende Aufwärmübung für Vorstellungsgespräche, um das Verständnis für die Invertierung von Datenstrukturen zu testen.
- Praktische Anwendung in funktionalen Programmiersprachen (wie Haskell), in denen rein unveränderliche Linked Lists exakt wie LIFO-Stacks funktionieren, was zwei Stacks erfordert, um eine veränderliche FIFO-Queue zu simulieren.

## Ansatz

Ein Stack ist **LIFO** (Last-In, First-Out).
Eine Queue ist **FIFO** (First-In, First-Out).

Um LIFO in FIFO umzuwandeln, müssen wir die Reihenfolge der Elemente umkehren.
Wenn man alle Elemente aus einem Stack entfernt (`pop`) und sie direkt in einen anderen Stack einfügt (`push`), kehrt sich die Reihenfolge perfekt um!

Wir verwenden zwei Stacks:
1. `push_stack`: Hier fügen wir blind alle eingehenden Elemente hinzu. Dies ist extrem schnell mit $O(1)$.
2. `pop_stack`: Wir entfernen Elemente ausschließlich von hier. Da sie vom `push_stack` umgefüllt wurden, sind sie in umgekehrter Reihenfolge, was bedeutet, dass das älteste Element wunderbar ganz oben liegt, genau wie bei einer Queue!

**Die goldene Regel:**
- **Push:** Immer auf den `push_stack` pushen.
- **Pop / Peek:** Prüfen, ob der `pop_stack` leer ist.
  - Wenn er leer ist, müssen wir *alle* aktuellen Elemente vom `push_stack` einzeln in den `pop_stack` umfüllen. Dies kehrt ihre Reihenfolge physisch um.
  - Wenn er NICHT leer ist, geben wir einfach das oberste Element des `pop_stack` zurück. Wir schieben Elemente **nicht** hin und her. Wir füllen nur um, wenn der `pop_stack` vollständig geleert wurde.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for queue_01: Implement Queue using Stacks.

Implement a FIFO queue using only two LIFO stacks.
"""


def solve(operations, n):
    """Implement FIFO queue with two LIFO stacks."""
    inbox = []
    outbox = []
    results = []
    for op in operations:
        name = op[0]
        if name == "push":
            inbox.append(op[1])
        elif name == "pop":
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            if outbox:
                outbox.pop()
        elif name == "peek":
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            if outbox:
                results.append(outbox[-1])
        elif name == "empty":
            pass
    return results
```

</details>

## Ablauf

1. `push(1)`: `push_stack = [1]`, `pop_stack = []`.
2. `push(2)`: `push_stack = [1, 2]`, `pop_stack = []`.
3. `push(3)`: `push_stack = [1, 2, 3]`, `pop_stack = []`.
4. `pop()`: 
   - `pop_stack` ist leer. Transfer!
   - Pop 3, push 3. Pop 2, push 2. Pop 1, push 1.
   - `push_stack = []`, `pop_stack = [3, 2, 1]`.
   - Pop vom `pop_stack`: Gibt `1` zurück. `pop_stack = [3, 2]`.
5. `push(4)`: `push_stack = [4]`, `pop_stack = [3, 2]`. *(Beachten Sie, dass wir nicht transferieren!)*
6. `pop()`:
   - `pop_stack` ist NICHT leer. Nicht transferieren.
   - Pop vom `pop_stack`: Gibt `2` zurück. `pop_stack = [3]`.
7. `pop()`:
   - Pop vom `pop_stack`: Gibt `3` zurück. `pop_stack = []`.
8. `pop()`:
   - `pop_stack` ist leer. Transfer!
   - `push_stack = []`, `pop_stack = [4]`.
   - Pop vom `pop_stack`: Gibt `4` zurück. `pop_stack = []`.

Alle Elemente kamen in der exakten Reihenfolge `1, 2, 3, 4` heraus. FIFO! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(N)$ |
| **Durchschnittlicher Fall** | Amortisiert $O(1)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ (einzelne Operation) | $O(N)$ |

- **Push:** Streng $O(1)$.
- **Pop/Peek:** Amortisiert $O(1)$. Obwohl ein einzelner `pop` einen Transfer von N Elementen auslösen kann, was $O(N)$ Zeit in Anspruch nimmt, wird dieses Element während seines gesamten Lebenszyklus *genau einmal* transferiert. Daher ist über N Operationen die gesamte Zeit für Transfers $O(N)$, was im Durchschnitt $O(1)$ pro Operation ergibt.
Die Platzkomplexität beträgt $O(N)$, um die Elemente zu speichern.

## Varianten & Optimierungen

- **Streng $O(1)$ Pop, $O(N)$ Push:** Sie können das Design umkehren. Wann immer Sie `push` aufrufen, füllen Sie alles vom `queue_stack` in einen `auxiliary_stack` um, fügen das neue Element unten in den `queue_stack` ein und füllen dann alles zurück. Dies macht `pop` streng $O(1)$, aber `push` streng $O(N)$. Das amortisierte Design ist weitaus überlegen.

## Anwendungen in der Praxis

- **Queues in der funktionalen Programmierung:** Rein funktionale Sprachen wie Clojure verwenden exakt diese "Zwei-Listen"-Struktur, um persistente, unveränderliche Queues effizient zu implementieren.

## Verwandte Algorithmen in cOde(n)

- **[queue_02 - Implement Stack using Queues](queue_02_implement-stack-using-queues.md)** — Das inverse Problem.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*