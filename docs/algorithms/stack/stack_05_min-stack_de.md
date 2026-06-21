# Min Stack

| | |
|---|---|
| **ID** | `stack_05` |
| **Kategorie** | stack |
| **Komplexität (erforderlich)** | $O(1)$ für alle Operationen |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Min Stack](https://leetcode.com/problems/min-stack/) |

## Problemstellung

Entwerfen Sie einen Stack, der `push`, `pop`, `top` sowie das Abrufen des kleinsten Elements in konstanter Zeit unterstützt.

Implementieren Sie die Klasse `MinStack`:
- `MinStack()` initialisiert das Stack-Objekt.
- `void push(int val)` legt das Element `val` auf den Stack.
- `void pop()` entfernt das oberste Element des Stacks.
- `int top()` gibt das oberste Element des Stacks zurück.
- `int getMin()` ruft das kleinste Element im Stack ab.

Sie müssen eine Lösung mit einer Zeitkomplexität von $O(1)$ für jede Funktion implementieren.

**Eingabe:** Eine Sequenz von Stack-Operationen.
**Ausgabe:** Die Ergebnisse der `top`- und `getMin`-Operationen.

**Beispiel:**
```text
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

## Wann man es verwendet

- Um eine fortlaufende Historie aggregierter Zustände (wie `min` oder `max`) parallel zu den Rohdaten zu verwalten, wobei ein $O(1)$-Rollback beim Entfernen von Daten garantiert wird.

## Ansatz

Ein Standard-Stack bietet $O(1)$ für `push`, `pop` und `top`. Das Finden des kleinsten Elements erfordert jedoch einen $O(N)$-Scan.
Wenn wir eine einzelne Integer-Variable `current_min` verwenden, um das Minimum zu verfolgen, funktioniert dies perfekt für `push`-Operationen. ABER, wenn wir das Element `pop`en, das zufällig das `current_min` ist, haben wir absolut keine Information darüber, welches das *zweitkleinste* Element war! Wir müssten den gesamten Stack erneut durchsuchen.

**Die Lösung: Zwei Stacks (oder Tupel)**
Wir können zwei parallele Stacks führen:
1. `main_stack`: Speichert die tatsächlichen Werte.
2. `min_stack`: Speichert das Minimum *genau in dem Moment*, in dem das entsprechende Element auf den `main_stack` gelegt wurde.

Wann immer wir einen neuen Wert `x` pushen, ist das neue Minimum einfach `min(x, min_stack.top())`. Wir pushen dieses neue Minimum auf den `min_stack`.
Wenn wir vom `main_stack` poppen, poppen wir gleichzeitig vom `min_stack`. Dies setzt die Zeit sofort zurück und stellt den `min_stack` auf den Zustand des Minimums wieder her, der vor dem Pushen von `x` existierte!

Alternativ können Sie einfach einen Stack verwenden, der ein Tupel speichert: `(val, current_min_at_this_level)`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for stack_05: Min Stack.

Two parallel stacks: one for values, one for the running minimum.
push, pop, top, get_min are all O(1).
"""


def solve(ops, n):
    stack = []
    mins = []
    out = []
    for op in ops:
        cmd = op[0]
        if cmd == "push":
            v = op[1]
            stack.append(v)
            if not mins or v <= mins[-1]:
                mins.append(v)
        elif cmd == "pop":
            if not stack:
                out.append(-1)
            else:
                v = stack.pop()
                if mins and v == mins[-1]:
                    mins.pop()
                out.append(v)
        elif cmd == "get_min":
            out.append(mins[-1] if mins else -1)
    return out
```

</details>

## Durchlauf

1. `push(-2)`: Stack leer. Pushe `(-2, -2)`.
2. `push(0)`: `min(0, -2) = -2`. Pushe `(0, -2)`. Stack: `[(-2, -2), (0, -2)]`.
3. `push(-3)`: `min(-3, -2) = -3`. Pushe `(-3, -3)`. Stack: `[(-2, -2), (0, -2), (-3, -3)]`.
4. `getMin()`: Betrachte das oberste Tupel `(-3, -3)`. Gib `1st index` zurück -> `-3`.
5. `pop()`: Poppe `(-3, -3)`. Stack: `[(-2, -2), (0, -2)]`.
6. `top()`: Betrachte das oberste Tupel `(0, -2)`. Gib `0th index` zurück -> `0`.
7. `getMin()`: Betrachte das oberste Tupel `(0, -2)`. Gib `1st index` zurück -> `-2`.

Alle Operationen benötigten $O(1)$! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(N)$ |
| **Schlechtester Fall** | $O(1)$ | $O(N)$ |

Jede einzelne Operation greift strikt auf das Ende des Arrays zu, was eine Zeitkomplexität von $O(1)$ erfordert.
Die Platzkomplexität beträgt $O(N)$, da wir für jedes der N gepushten Elemente zwei Werte (oder zwei parallele Stacks) speichern.

## Varianten & Optimierungen

- **Platzoptimierung (Differenzspeicherung):** Man kann technisch $O(1)$ zusätzlichen Platz erreichen (abgesehen von den obligatorischen $O(N)$ zum Speichern der Werte). Anstatt Tupel zu speichern, speichert man eine kodierte Differenz: `val - current_min`. Wenn die Differenz negativ ist, bedeutet dies, dass ein neues Minimum gefunden wurde und die Variable `current_min` aktualisiert wird. Beim Poppen einer negativen Differenz kann man mathematisch das vorherige Minimum rekonstruieren! Dieser Trick ist elegant, wird aber in Vorstellungsgesprächen selten erwartet.

## Anwendungen in der Praxis

- **Undo/Redo-Zustände:** Texteditoren verfolgen die Historie des Dokumentzustands mithilfe von Stacks. Wenn eine bestimmte Metrik (wie die Zeichenanzahl oder ein Dokument-Hash) für jeden vergangenen Zustand sofort abrufbar sein muss, stellt das Anhängen der Metrik an das Zustandstupel $O(1)$-Rollbacks sicher.

## Verwandte Algorithmen in cOde(n)

- **[queue_01 - Implement Queue using Stacks](../queue/queue_01_implement-queue-using-stacks.md)** — Ein weiteres grundlegendes Problem beim Entwurf von Datenstrukturen unter Verwendung von Stacks.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*