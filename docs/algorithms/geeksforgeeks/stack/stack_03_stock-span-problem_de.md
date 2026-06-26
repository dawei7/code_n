# Stock Span Problem

| | |
|---|---|
| **ID** | `stack_03` |
| **Kategorie** | stack |
| **Komplexität (erforderlich)** | $O(N)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) |

## Problemstellung

Das Stock Span Problem ist ein finanzmathematisches Problem, bei dem eine Reihe von N täglichen Aktienkursen gegeben ist.
Wir müssen die **Span** (Spanne) des Aktienkurses für alle N Tage berechnen.
Die Spanne des Aktienkurses an einem gegebenen Tag i ist definiert als die maximale Anzahl aufeinanderfolgender Tage unmittelbar vor dem gegebenen Tag, an denen der Aktienkurs am aktuellen Tag größer oder gleich dem Kurs an den vorangegangenen Tagen war.
(Die Spanne eines Tages schließt den Tag selbst immer mit ein, daher ist die minimale Spanne 1).

**Eingabe:** Ein Integer-Array `prices`, das die täglichen Aktienkurse repräsentiert.
**Ausgabe:** Ein Integer-Array `spans` derselben Länge.

**Beispiel:**
`prices = [100, 80, 60, 70, 60, 75, 85]`
Ausgabe: `[1, 1, 1, 2, 1, 4, 6]`.
*(An Tag 5 (Kurs 75) ist der Kurs höher als an den Tagen mit den Kursen 60, 70, 60. Daher ist die Spanne 4).*

## Anwendungsbereiche

- Wenn Sie einen eingehenden Datenstrom verarbeiten und historische Anfragen basierend auf monotonen Trends beantworten müssen, ohne die gesamte Historie aktiv vorzuhalten.

## Ansatz

Dies ist eine direkte Anwendung des **Monotonic Stack**, speziell zur Ermittlung des **Previous Greater Element** (das vorherige größere Element).
Wenn wir den Index des letzten Tages in der Vergangenheit kennen, an dem der Kurs strikt *höher* war als der heutige Kurs, dann ist unsere "Spanne" einfach die Differenz zwischen dem heutigen Index und dem Index dieses vorherigen höheren Tages!

Wir führen einen **Monotonically Decreasing Stack** (monoton fallenden Stack) von Indizes.
Für den aktuellen Tag `i` mit `prices[i]` gilt:
- Solange der Stack nicht leer ist und `prices[stack.top()] <= prices[i]`:
  - Der vorherige Kurs ist kleiner oder gleich dem heutigen Kurs. Der heutige Kurs übertrifft ihn vollständig! Wir können ihn sicher für immer vom Stack `pop`en, da jeder zukünftige Tag, der zurückblickt, auf den höheren Kurs von *heute* treffen wird, bevor er jemals den kleineren, entfernten Kurs erreicht.
- Nachdem alle kleineren Kurse entfernt wurden, enthält das oberste Element des Stacks nun den Index des **Previous Greater Element**.
- Wenn der Stack leer ist, bedeutet dies, dass der heutige Kurs der höchste ist, den wir bisher gesehen haben! Die Spanne ist `i + 1` (alle Tage seit Beginn).
- Andernfalls ist die Spanne `i - stack.top()`.
- Abschließend `push`en wir den heutigen Index `i` auf den Stack.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for stack_03: Stock Span Problem.

For each day i, the span is the number of consecutive days
just before i with a price <= arr[i] (plus today). Monotonic
stack: walk left to right, popping while the top's price is
<= today's. The span is i - (top index after popping), or
i + 1 if the stack is empty. O(n).
"""


def solve(arr, n):
    spans = [0] * n
    stack = []  # indices
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            spans[i] = i - stack[-1]
        else:
            spans[i] = i + 1
        stack.append(i)
    return spans
```

</details>

## Durchlauf

`prices = [100, 80, 60, 70]`

1. `i=0, price=100`. Stack leer. `spans[0] = 0 + 1 = 1`. Push `0`. `stack=[0]`.
2. `i=1, price=80`. 
   - `80 <= prices[0] (100)`? Falsch.
   - Stack nicht leer. `spans[1] = i - stack[-1] = 1 - 0 = 1`.
   - Push `1`. `stack=[0, 1]`. (Werte `[100, 80]`).
3. `i=2, price=60`.
   - `60 <= prices[1] (80)`? Falsch.
   - Stack nicht leer. `spans[2] = i - stack[-1] = 2 - 1 = 1`.
   - Push `2`. `stack=[0, 1, 2]`. (Werte `[100, 80, 60]`).
4. `i=3, price=70`.
   - `70 <= prices[2] (60)`? Wahr! Pop `2`. `stack=[0, 1]`.
   - `70 <= prices[1] (80)`? Falsch.
   - Stack nicht leer. `spans[3] = i - stack[-1] = 3 - 1 = 2`.
   - Push `3`. `stack=[0, 1, 3]`. (Werte `[100, 80, 70]`).

Ausgabe: `[1, 1, 1, 2]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Obwohl sich eine `while`-Schleife innerhalb der `for`-Schleife befindet, wird jeder Index von 0 bis N-1 genau einmal auf den Stack gepusht und höchstens einmal gepopt. Die Gesamtzahl der Stack-Operationen ist linear proportional zu N. Daher ist die Zeitkomplexität streng amortisiert $O(N)$.
Die Platzkomplexität beträgt $O(N)$ für den Stack und das Ausgabe-Array.

## Varianten & Optimierungen

- **Online Stream Processing:** Wenn die Kurse einzeln über eine API eintreffen (z. B. `next(price)`), können Sie den Stack innerhalb eines Klassenstatus kapseln. Anstatt Indizes zu speichern, speichert der Stack Paare von `(price, span)`. Wenn Sie kleinere Kurse entfernen, addieren Sie einfach deren Spannen: `current_span += popped_span`. Dies entkoppelt die Logik vollständig von absoluten Indizes!

## Praxisanwendungen

- **UI-Dashboards:** Dynamisches Rendern von historischen Unterstützungs- und Widerstandsgrenzen in Live-Kryptowährungs-Charts, ohne bei jedem neuen Tick die gesamte Historie des Tages neu scannen zu müssen.

## Verwandte Algorithmen in cOde(n)

- **[stack_02 - Next Greater Element](stack_02_next-greater-element.md)** — Der grundlegende Algorithmus zur Vermittlung des Monotonic Stack-Musters.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*