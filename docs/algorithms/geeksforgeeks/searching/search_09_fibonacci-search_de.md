# Fibonacci Search

| | |
|---|---|
| **ID** | `search_09` |
| **Kategorie** | searching |
| **Komplexität (erforderlich)** | $O(\log N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 1/10 |
| **Wikipedia** | [Fibonacci search technique](https://en.wikipedia.org/wiki/Fibonacci_search_technique) |

## Problemstellung

Gegeben ist ein sortiertes Array `arr` und ein `target`-Wert.
Finde den Index des `target` im Array. Falls das `target` nicht vorhanden ist, gib `-1` zurück.
Optimiere die Suche für Umgebungen, in denen **Divisionsoperatoren** (`/` oder `//`) und **Bitwise Shifts** (`>>`) nicht unterstützt werden oder extrem rechenintensiv sind, und du AUSSCHLIESSLICH Addition und Subtraktion verwenden darfst.

**Eingabe:** Ein sortiertes Array `arr` und ein `target`-Wert.
**Ausgabe:** Eine Ganzzahl, die den Index repräsentiert.

## Wann man es verwendet

- Rein hardware- bzw. systemnahe Optimierungstechnik.
- Einsatz auf extrem alten Mikroprozessoren oder spezialisierten eingebetteten Systemen (wie ASICs), bei denen Divisions-Logikgatter physisch nicht auf dem Silizium-Chip existieren.
- Optimiert zudem die CPU-Cache-Performance, da das Array in ungleiche Abschnitte (~= 61\% und 39\%) unterteilt wird, was gelegentlich besser mit physischen Speicherseiten (Memory Pages) korreliert als eine exakte 50%-Teilung.

## Ansatz

**1. Das Divisionsproblem:**
Die Binäre Suche verwendet `mid = (left + right) / 2`.
Dies erfordert eine Division. Wie können wir ein Array ohne Division teilen?

**2. Die Fibonacci-Folge:**
Erinnere dich an die Folge: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34...`
Eine grundlegende Eigenschaft der Folge ist F_k = F_{k-1} + F_{k-2}.
Wenn ein Array die Länge 13 hat, können wir es mathematisch perfekt in zwei Abschnitte der Länge 8 und 5 unterteilen!
Wenn wir den Abschnitt der Größe 5 eliminieren, bleibt ein Array der Größe 8 übrig. Aber 8 ist ebenfalls eine Fibonacci-Zahl! Wir können es erneut in 5 und 3 unterteilen!
Wir können das Array rekursiv NUR durch Subtraktion verkleinern: F_{k-1} = F_k - F_{k-2}!

**3. Der Algorithmus:**
1. Generiere Fibonacci-Zahlen, bis wir F_k finden, das \ge N (die Länge des Arrays) ist.
2. Setze einen `offset = -1`. Dies repräsentiert den Start unseres aktuell aktiven Array-Abschnitts.
3. Unser "Mittelpunkt" (Probe) wird einfach berechnet als: `i = min(offset + F_{k-2}, N-1)`. Wir schneiden einen Abschnitt der Größe F_{k-2} von links ab.
4. Vergleiche `arr[i]` mit dem `target`:
   - **Treffer:** Gib `i` zurück.
   - **Target ist kleiner:** Das `target` befindet sich im linken Abschnitt (Größe F_{k-2}). Wir verschieben unsere Fibonacci-Zahlen um ZWEI nach unten: F_k = F_{k-2}.
   - **Target ist größer:** Das `target` befindet sich im rechten Abschnitt (Größe F_{k-1}). Wir verschieben unsere Fibonacci-Zahlen um EINS nach unten: F_k = F_{k-1}. Entscheidend ist, dass wir unseren `offset` auf `i` aktualisieren, wodurch effektiv der gesamte linke Abschnitt abgeschnitten wird!
5. Wiederhole den Vorgang, bis F_k auf 1 fällt.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for search_09: Fibonacci Search.

Sorted array; uses Fibonacci numbers to split the range.
Always shrinks by at least one Fibonacci number, so the loop
runs in O(log n) time. The split is by index, not value.
"""


def solve(data, target, n):
    if n == 0:
        return -1
    # Initialise the smallest Fibonacci >= n.
    fib2, fib1 = 0, 1
    fib = fib1 + fib2
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    offset = -1
    while fib > 1:
        i = min(offset + fib2, n - 1)
        if data[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif data[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    if fib1 and offset + 1 < n and data[offset + 1] == target:
        return offset + 1
    return -1
```

</details>

## Durchlauf

`arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`. `target = 60`. Länge 10.

1. Generiere Fibonacci: `0, 1, 1, 2, 3, 5, 8, 13`.
   - F_k = 13, F_{k-1} = 8, F_{k-2} = 5.
   - `offset = -1`.
2. **Schleife 1:**
   - `i = min(-1 + 5, 9) = 4`. `arr[4] = 50`.
   - `50 < 60`. Das `target` ist in der rechten Hälfte!
   - `offset = 4`.
   - Verschiebe um 1 nach unten: F_k = 8, F_{k-1} = 5, F_{k-2} = 3.
3. **Schleife 2:**
   - `i = min(4 + 3, 9) = 7`. `arr[7] = 80`.
   - `80 > 60`. Das `target` ist in der linken Hälfte!
   - `offset = 4` (unverändert).
   - Verschiebe um 2 nach unten: F_k = 3, F_{k-1} = 2, F_{k-2} = 1.
4. **Schleife 3:**
   - `i = min(4 + 1, 9) = 5`. `arr[5] = 60`.
   - `60 == 60`! Treffer gefunden!

Ergebnis: `5`. ✓
*(Beachte, wie wir erfolgreich eine Divide-and-Conquer-Suche durchgeführt haben, ohne einen einzigen `/`-, `%`-, `*`- oder `>>`-Operator auszuführen!)*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(1)$ |

Die Fibonacci-Zahlen wachsen exponentiell. Speziell gilt F_k ~= 1.618^k.
Da die Größe des aktiven Arrays bei jedem Schritt strikt um den Goldenen Schnitt schrumpft, ist die Anzahl der erforderlichen Iterationen strikt durch $O(\log N)$ begrenzt.
Die Platzkomplexität ist $O(1)$, da wir nur drei Ganzzahlen verfolgen, um den aktiven Fibonacci-Zustand zu erhalten.

## Varianten & Optimierungen

- **Golden-Section Search (`search_05` Hinweis):** Der Fibonacci-Suchalgorithmus angewendet auf mathematische unimodale Funktionen anstelle von Arrays, verwendet, um das absolute Minimum/Maximum einer Kurve ohne Analysis zu finden.

## Anwendungen in der Praxis

- **Mainframes der späten 1950er Jahre:** Die IBM 650 (der erste in Serie produzierte Computer) hatte eine quälend langsame Trommelspeicher-Architektur, bei der eine Division um Größenordnungen länger dauerte als eine Addition. Die Fibonacci-Suche wurde speziell erfunden, um das Sortieren und Suchen auf diesen Maschinen zu optimieren.

## Verwandte Algorithmen in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — Das divisionsbasierte algorithmische Gegenstück.
- **[dynamic_01 - Fibonacci Numbers](../dynamic/dp_01_fibonacci.md)** — Der dynamische Programmieralgorithmus, der zur Generierung der Zahlen verwendet wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*