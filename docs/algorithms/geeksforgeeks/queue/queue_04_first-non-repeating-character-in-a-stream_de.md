# Erstes nicht-wiederholtes Zeichen in einem Stream

| | |
|---|---|
| **ID** | `queue_04` |
| **Kategorie** | queue |
| **Komplexität (erforderlich)** | $O(1)$ amortisiert pro Zeichen |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) (Stream-Variante) |

## Problemstellung

Gegeben ist ein ankommender Stream von Zeichen. Finden Sie zu jedem beliebigen Zeitpunkt das **erste nicht-wiederholte Zeichen** im Stream.
Wenn neue Zeichen eintreffen, könnte das bisherige "erste nicht-wiederholte Zeichen" erneut auftreten, was bedeutet, dass es ungültig wird. In diesem Fall müssen Sie sofort das *nächstälteste* nicht-wiederholte Zeichen ausgeben.

**Eingabe:** Ein String `s`, der den Datenstrom repräsentiert.
**Ausgabe:** Ein String derselben Länge, bei dem das i-te Zeichen das erste nicht-wiederholte Zeichen ist, das vom Index `0` bis `i` gesehen wurde. Wenn alle bisher gesehenen Zeichen wiederholt wurden, geben Sie `#` aus.

**Beispiel:**
Stream: `"a a b c"`
1. `"a"`: Das erste eindeutige Zeichen ist `a`. Ausgabe: `a`
2. `"a"`: `a` wurde wiederholt! Alle Zeichen wiederholen sich. Ausgabe: `#`
3. `"b"`: `b` ist neu und eindeutig. Ausgabe: `b`
4. `"c"`: `c` ist neu, aber `b` ist älter und immer noch eindeutig. Ausgabe: `b`
Finaler Ausgabe-String: `"a#bb"`.

## Anwendung

- Lösung von Echtzeit-Stream-Verarbeitungsproblemen, bei denen die historische chronologische Reihenfolge wichtig ist.
- Ein klassisches Problem in Vorstellungsgesprächen, das die duale Verwendung von Hash Maps (für den Zustand) und Queues (für die Chronologie) vermittelt.

## Ansatz

Wir müssen zwei Dinge gleichzeitig verfolgen:
1. **Chronologie:** Welches gültige Zeichen kam *zuerst* an? Eine **Queue** ist hierfür perfekt geeignet.
2. **Häufigkeit:** Ist dieses Zeichen schon einmal angekommen? Eine **Hash Map (oder ein Array)** ist hierfür perfekt geeignet.

**Die Logik:**
Für jedes eingehende Zeichen `char`:
1. Erhöhen Sie dessen Zähler in der Hash Map.
2. Wenn der Zähler genau `1` ist (es ist völlig neu), fügen Sie es hinten in die Queue ein (enqueue).
3. Nun müssen wir das Zeichen überprüfen, das sich aktuell an der **Vorderseite** der Queue befindet (der älteste Kandidat).
   - Suchen Sie den Zähler des vordersten Zeichens in der Hash Map nach.
   - Wenn der Zähler `> 1` ist, bedeutet dies, dass es seit dem ursprünglichen Einfügen in die Queue erneut aufgetreten ist! Es ist "tot". Entfernen Sie es aus der Queue (dequeue) und verwerfen Sie es.
   - Wiederholen Sie diese `while`-Schleife, bis die Queue leer ist ODER das vorderste Zeichen einen Zähler von genau `1` aufweist.
4. Wenn die Queue leer ist, geben Sie `#` aus. Andernfalls geben Sie das Zeichen an der Vorderseite der Queue aus.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for queue_04: First Non-Repeating Character in a Stream.

Given a stream of characters (a string), for each
"""


def solve(stream, n):
    """First non-repeating char in each prefix of stream."""
    from collections import deque, Counter
    if n == 0:
        return ""
    q = deque()
    freq = Counter()
    result = []
    for ch in stream:
        freq[ch] += 1
        q.append(ch)
        # Pop from the front of the queue while the head has
        # appeared more than once.
        while q and freq[q[0]] > 1:
            q.popleft()
        if q:
            result.append(q[0])
        else:
            result.append("_")
    return "".join(result)
```

</details>

## Durchlauf

`stream = "aabc"`

1. **`char = 'a'`**:
   - `freq['a'] = 1`.
   - Queue push `'a'`. `q = ['a']`.
   - `q[0]` ist `'a'`. `freq['a'] == 1`. Schleife ignoriert.
   - Ergebnis: `a`.
2. **`char = 'a'`**:
   - `freq['a'] = 2`.
   - `q[0]` ist `'a'`. `freq['a'] > 1`! Entfernen! `q = []`.
   - Queue ist leer.
   - Ergebnis: `#`.
3. **`char = 'b'`**:
   - `freq['b'] = 1`.
   - Queue push `'b'`. `q = ['b']`.
   - `q[0]` ist `'b'`. `freq['b'] == 1`. Schleife ignoriert.
   - Ergebnis: `b`.
4. **`char = 'c'`**:
   - `freq['c'] = 1`.
   - Queue push `'c'`. `q = ['b', 'c']`.
   - `q[0]` ist `'b'`. `freq['b'] == 1`. Schleife ignoriert.
   - Ergebnis: `b`.

Ausgabe: `"a#bb"`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ amortisiert | $O(1)$ / $O(U)$ |
| **Durchschnittlicher Fall** | $O(1)$ amortisiert | $O(1)$ / $O(U)$ |
| **Schlechtester Fall** | $O(1)$ amortisiert | $O(1)$ / $O(U)$ |

Das Aktualisieren der Hash Map benötigt $O(1)$. Das Einfügen in die Queue benötigt $O(1)$.
Obwohl es eine `while`-Schleife gibt, wird jedes Zeichen über die gesamte Lebensdauer des Streams höchstens *einmal* in die Queue eingefügt und höchstens *einmal* entfernt. Daher ergibt die innere `while`-Schleife eine amortisierte Zeitkomplexität von $O(1)$.
Platzkomplexität: Da es nur 26 englische Kleinbuchstaben (oder 256 ASCII-Zeichen) gibt, werden die Queue und die Hash Map niemals $O(U)$ überschreiten, wobei U die Größe des eindeutigen Alphabets ist. Daher ist der zusätzliche Platzbedarf strikt $O(1)$, unabhängig davon, wie groß der Stream N wird!

## Varianten & Optimierungen

- **Doubly Linked List + Hash Map (LRU Cache-Variante):** Wenn Sie eine strikte $O(1)$ Worst-Case-Zeit pro Zeichen benötigen (ohne amortisierte Schleifen), können Sie eine Doubly Linked List verwenden. Die Hash Map speichert direkte Pointer auf die DLL-Nodes. Wenn ein Zeichen wiederholt wird, löschen Sie dessen Node in $O(1)$ aus der Mitte der DLL. Der Kopf der DLL ist immer die Antwort.

## Anwendungen in der Praxis

- **Netzwerk-Routing:** Echtzeit-Deduplizierung von Netzwerkpaketen, um die erste eindeutige Sequenz-ID zu identifizieren, die verworfen wurde und eine erneute Übertragung erfordert.

## Verwandte Algorithmen in cOde(n)

- **[linked_list_06 - LRU Cache](../linked_list/ll_06_lru-cache.md)** — Die fortgeschrittene strukturelle Variante dieses Problems unter Verwendung von DLLs.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Wettbewerbsprogrammierungs-Referenzseiten verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*