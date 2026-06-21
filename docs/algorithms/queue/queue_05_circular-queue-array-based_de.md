# Circular Queue (Array Based)

| | |
|---|---|
| **ID** | `queue_05` |
| **Kategorie** | queue |
| **Komplexität (erforderlich)** | $O(1)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) |

## Problemstellung

Entwerfen Sie Ihre Implementierung einer Circular Queue.
Eine Circular Queue ist eine lineare Datenstruktur, die dem FIFO-Prinzip folgt, bei der jedoch die letzte Position wieder mit der ersten Position verbunden ist, um einen Kreis zu bilden. Sie wird auch als "Ringpuffer" bezeichnet.
Dies eliminiert vollständig den grundlegenden Nachteil einer standardmäßigen Array-basierten Queue: Leere Plätze am Anfang des Arrays, die durch das Entfernen von Elementen (deQueue) entstehen, können nicht wiederverwendet werden.

Implementieren Sie die Klasse `MyCircularQueue`:
- `MyCircularQueue(k)` Initialisiert das Objekt mit der Größe der Queue `k`.
- `Front()` Gibt das vorderste Element zurück. Gibt -1 zurück, falls die Queue leer ist.
- `Rear()` Gibt das letzte Element zurück. Gibt -1 zurück, falls die Queue leer ist.
- `enQueue(value)` Fügt ein Element ein. Gibt True zurück, wenn der Vorgang erfolgreich war.
- `deQueue()` Löscht ein Element aus der Queue. Gibt True zurück, wenn der Vorgang erfolgreich war.
- `isEmpty()` Überprüft, ob die Queue leer ist.
- `isFull()` Überprüft, ob die Queue voll ist.

**Eingabe:** Eine Sequenz von Circular-Queue-Operationen.
**Ausgabe:** Booleans und Integers, abhängig von der Methode.

## Wann man sie verwendet

- Um die hardwarenahe Speicherarchitektur zu verstehen. Fast alle Hardware-Puffer (wie Tastatur-Eingabepuffer oder Streaming-Videospeicher) verwenden genau diese physische Struktur.

## Ansatz

Wir verwenden ein Array `arr` fester Größe mit der Kapazität K.
Wir verwalten zwei Pointer:
- `head`: Zeigt auf das älteste Element.
- `tail`: Zeigt auf das neueste Element (oder den nächsten freien Platz, je nach Implementierung).
Zusätzlich führen wir einen `size`-Zähler, um einfach zu verfolgen, ob die Queue leer oder voll ist.

**Die "Kreis"-Mathematik:**
Wann immer wir `head` oder `tail` inkrementieren, führen wir nicht einfach `+ 1` aus. Wir verwenden `(head + 1) % K`.
Der Modulo-Operator sorgt mathematisch dafür, dass der Pointer zurück auf den Index 0 springt, sobald er das Ende des Arrays `K` erreicht.

**Operationen:**
- `enQueue`: Wenn die Queue nicht voll ist, platzieren wir das Element am `tail`-Index. Wir bewegen `tail` mittels Modulo vorwärts und inkrementieren `size`.
- `deQueue`: Wenn die Queue nicht leer ist, müssen wir den Speicher nicht explizit löschen. Wir bewegen lediglich `head` mittels Modulo vorwärts und dekrementieren `size`. Der alte Speicher wird bei Bedarf einfach überschrieben!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for queue_05: Circular Queue (Array-based).

Implement a fixed-capacity circular queue using
"""


def solve(operations, capacity, n):
    """Fixed-capacity circular queue. Returns list of dequeued values."""
    if capacity <= 0:
        return []
    queue = [None] * capacity
    front = 0
    rear = -1
    size = 0
    dequeued = []
    for op in operations:
        name = op[0]
        if name == "enqueue":
            if size == capacity:
                continue  # overflow: silently skip
            rear = (rear + 1) % capacity
            queue[rear] = op[1]
            size += 1
        elif name == "dequeue":
            if size == 0:
                continue  # underflow: silently skip
            dequeued.append(queue[front])
            front = (front + 1) % capacity
            size -= 1
        elif name == "front":
            pass  # we don't return this
        elif name == "rear":
            pass
        elif name == "isEmpty":
            pass
        elif name == "isFull":
            pass
    return dequeued
```

</details>

## Ablaufbeispiel

`q = MyCircularQueue(3)`
`capacity = 3`, `queue = [0, 0, 0]`, `head = 0`, `tail = 0`, `size = 0`.

1. `enQueue(1)`: `queue[0]=1`. `tail = (0+1)%3 = 1`. `size=1`.
2. `enQueue(2)`: `queue[1]=2`. `tail = (1+1)%3 = 2`. `size=2`.
3. `enQueue(3)`: `queue[2]=3`. `tail = (2+1)%3 = 0`. `size=3`.
4. `enQueue(4)`: `isFull` ist True. Gibt `False` zurück.
5. `Rear()`: `(0 - 1 + 3) % 3 = 2`. `queue[2] = 3`. Gibt `3` zurück.
6. `deQueue()`: `head = (0+1)%3 = 1`. `size=2`. (Die `1` an Index 0 ist "gelöscht").
7. `enQueue(4)`: `queue[0]=4`. `tail = (0+1)%3 = 1`. `size=3`. (Es ist umgesprungen und hat Index 0 überschrieben!).
8. `Front()`: `queue[head] = queue[1] = 2`. Gibt `2` zurück.

Modelliert korrekt einen dynamischen Kreis! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(K)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(K)$ |
| **Schlechtester Fall** | $O(1)$ | $O(K)$ |

Jede einzelne Operation nutzt mathematisch sofortigen Array-Zugriff und Ganzzahl-Arithmetik. Die Zeitkomplexität ist strikt $O(1)$.
Die Platzkomplexität ist strikt auf $O(K)$ begrenzt, da wir das Array genau einmal vorab allokieren und den Speicher vollständig wiederverwenden, ohne Garbage Collection oder Reallokation.

## Varianten & Optimierungen

- **Keine Size-Variable:** Sie können dies ohne den `size`-Integer implementieren! Hierfür setzen Sie die Array-Größe auf `K + 1`. Die Queue ist leer, wenn `head == tail`. Die Queue ist voll, wenn `(tail + 1) % (K + 1) == head`. So werden hardwarenahe C-Ringpuffer implementiert, um konkurrierende Lese-/Schreib-Locks auf einer gemeinsamen `size`-Variable zu vermeiden.

## Anwendungen in der Praxis

- **Netzwerkkarten (NIC):** Hardware-Puffer, die eingehende TCP-Pakete halten, verwenden Ringpuffer. Wenn die CPU die Pakete nicht schnell genug per `deQueue` verarbeitet, springt der `enQueue`-Vorgang der NIC einfach zum Anfang zurück und überschreibt die ältesten Pakete, was zu einem "Paketverlust" führt.

## Verwandte Algorithmen in cOde(n)

- **[queue_01 - Implement Queue using Stacks](queue_01_implement-queue-using-stacks.md)** — Die höherwertige programmatische Abstraktion einer Queue.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*