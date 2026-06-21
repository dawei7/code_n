# Next Greater Element (Monotonic Stack)

| | |
|---|---|
| **ID** | `stack_02` |
| **Kategorie** | stack |
| **Komplexität (erforderlich)** | $O(N)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Next Greater Element I & II](https://leetcode.com/problems/next-greater-element-i/) |

## Problemstellung

Gegeben ist ein Array von Integern `nums`. Finde für jedes Element im Array das **Next Greater Element** (das nächstgrößere Element).
Das Next Greater Element eines Elements `x` ist das *erste* Element rechts von `x`, das strikt größer als `x` ist.
Falls kein solches Element existiert, gib für diese Position `-1` aus.

**Eingabe:** Ein Integer-Array `nums`.
**Ausgabe:** Ein Integer-Array gleicher Länge, das die nächstgrößeren Elemente enthält.

**Beispiel:**
`nums = [4, 5, 2, 25]`
Ausgabe: `[5, 25, 25, -1]`.
*(Das nächste Element von 4 ist 5. Das nächste von 5 ist 25. Das nächste von 2 ist 25. 25 hat kein nächstgrößeres Element).*

## Wann man es verwendet

- Um verschachtelte $O(N^2)$-Schleifen zu eliminieren, wenn man nach dem "nächsten größeren/kleineren Wert rechts/links" sucht.
- Dies führt den **Monotonic Stack** ein, ein kritisches Konzept, das das Rückgrat für fortgeschrittene Array-Geometrie-Probleme wie *Trapping Rain Water* und *Largest Rectangle in Histogram* bildet.

## Ansatz

Eine naive Lösung benötigt $O(N^2)$, indem für jedes einzelne Element die rechte Seite des Arrays durchsucht wird.
Wir können dies auf $O(N)$ reduzieren, indem wir einen **Monotonic Decreasing Stack** verwenden.

Ein Monotonic Stack ist ein Stack, dessen Elemente immer in einer bestimmten Reihenfolge sortiert sind (z. B. strikt abnehmend von unten nach oben).
Anstatt die Werte direkt zu speichern, speichern wir deren **Indizes**.

**Die Logik:**
Iteriere von links nach rechts durch das Array.
Für jedes Element `curr = nums[i]`:
- Solange der Stack NICHT leer ist UND `curr` strikt größer ist als das Element am Index, der oben auf dem Stack liegt (`nums[stack.top()]`):
  - Wir haben das Next Greater Element für das Element an `stack.top()` gefunden!
  - Entferne (pop) den obersten Index vom Stack.
  - Setze das Ergebnis für diesen entfernten Index auf `curr`.
- Lege (push) den aktuellen Index `i` auf den Stack, damit er auf sein eigenes Next Greater Element warten kann.

Elemente, die am Ende noch im Stack verbleiben, haben kein größeres Element gefunden und erhalten daher standardmäßig `-1`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for stack_02: Next Greater Element.

Monotonic stack: walk left to right, maintaining a stack of
indices whose next-greater hasn't been found yet. When arr[i]
is greater than the top, pop and record i as the answer for
the popped index. O(n).
"""


def solve(arr, n):
    result = [-1] * n
    stack = []  # indices
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    return result
```

</details>

## Durchlauf

`nums = [4, 5, 2, 25]`
`result = [-1, -1, -1, -1]`. `stack = []`.

1. `i=0, curr=4`. Stack leer. Push `0`. `stack=[0]`.
2. `i=1, curr=5`. 
   - `5 > nums[stack[-1]]` (was `nums[0] = 4` entspricht). Ja!
   - Pop `0`. `result[0] = 5`.
   - Push `1`. `stack=[1]`.
   - `result = [5, -1, -1, -1]`.
3. `i=2, curr=2`.
   - `2 > nums[stack[-1]]` (was `nums[1] = 5` entspricht). Nein.
   - Push `2`. `stack=[1, 2]`. (Beachte, dass die Werte `[5, 2]` monoton abnehmend sind).
4. `i=3, curr=25`.
   - `25 > nums[stack[-1]]` (was `nums[2] = 2` entspricht). Ja!
   - Pop `2`. `result[2] = 25`.
   - `25 > nums[stack[-1]]` (was `nums[1] = 5` entspricht). Ja!
   - Pop `1`. `result[1] = 25`.
   - Push `3`. `stack=[3]`.
   - `result = [5, 25, 25, -1]`.

Schleife endet. Das Ergebnis ist `[5, 25, 25, -1]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Jedes Element wird genau einmal auf den Stack gelegt und höchstens einmal vom Stack entfernt. Daher läuft die `while`-Schleife über die gesamte Programmausführung hinweg höchstens N-mal. Die Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität beträgt $O(N)$, um das Ergebnis-Array und den Stack zu speichern.

## Varianten & Optimierungen

- **Zirkuläres Array (NGE II):** Wenn das Array zirkulär ist (das NGE für das letzte Element könnte das erste Element sein), iteriert man einfach **zweimal** durch das Array (d. h. `for i in range(2 * n): curr = nums[i % n]`) und verwendet exakt dieselbe Stack-Logik!
- **Next Smaller Element:** Ändere die Bedingung zu `curr < nums[stack[-1]]`, um einen monoton *steigenden* Stack zu erhalten.
- **Previous Greater Element:** Iteriere stattdessen rückwärts von rechts nach links.

## Anwendungen in der Praxis

- **Aktienmarkttrends:** Berechnung, wie viele Tage man warten muss, bis der Aktienkurs den heutigen Kurs übersteigt.

## Verwandte Algorithmen in cOde(n)

- **[stack_03 - Stock Span Problem](stack_03_stock-span-problem.md)** — Die direkte Anwendung der Rückwärtssuche unter Verwendung derselben monotonen Logik.
- **[stack_04 - Largest Rectangle in Histogram](stack_04_largest-rectangle-in-histogram.md)** — Kombiniert *Next Smaller Element* und *Previous Smaller Element*, um Breiten in $O(N)$ zu berechnen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*