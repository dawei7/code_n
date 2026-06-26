# Ägyptischer Bruch

| | |
|---|---|
| **ID** | `greedy_11` |
| **Kategorie** | greedy |
| **Komplexität (erforderlich)** | $O(log(denominator)$) Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **GeeksForGeeks Äquivalent** | [Greedy Algorithm for Egyptian Fraction](https://www.geeksforgeeks.org/greedy-algorithm-egyptian-fraction/) |

## Problemstellung

Jeder positive Bruch \frac{N}{D} (wobei N < D) kann als Summe eindeutiger Stammbrüche dargestellt werden. Ein Stammbruch ist ein Bruch, dessen Zähler 1 ist und dessen Nenner eine positive ganze Zahl ist.
Zum Beispiel: \frac{2}{3} = \frac{1}{2} + \frac{1}{6}.
Gegeben sind N und D, finde eine Darstellung als Ägyptischer Bruch. (Hinweis: Es kann mehrere gültige Darstellungen geben; jede gültige Sequenz von Stammbrüchen ist akzeptabel).

**Eingabe:** Zwei Ganzzahlen, `numerator` und `denominator`.
**Ausgabe:** Eine Liste von Ganzzahlen, die die Nenner der Stammbrüche repräsentieren.

## Wann man es verwendet

- Mathematische Wissensfragen / spezifische Rätsel in Vorstellungsgesprächen.
- Verwendet einen reinen Greedy-Algorithmus, der von Fibonacci entwickelt wurde.

## Ansatz

**Die Greedy-Entscheidung (Fibonacci-Algorithmus):**
In jedem Schritt möchten wir den *größtmöglichen Stammbruch* von unserem aktuellen Bruch subtrahieren.
Wie finden wir den größten Stammbruch \frac{1}{X}, der strikt \le \frac{N}{D} ist?
Wir nehmen einfach den Aufrundungswert (Ceiling) von \frac{D}{N}!
X = \lceil \frac{D}{N} \rceil.

Sobald wir X gefunden haben, subtrahieren wir \frac{1}{X} von \frac{N}{D}.
\frac{N}{D} - \frac{1}{X} = \frac{N \cdot X - D}{D \cdot X}.
Dieser neue Bruch wird zu unserem neuen \frac{N}{D}. Wir wiederholen den Prozess, bis der Zähler N gleich 1 (oder 0) wird.

**Warum es funktioniert:**
Fibonacci hat mathematisch bewiesen, dass der Zähler N im Rest bei jedem Schritt strikt abnimmt. Daher terminiert der Algorithmus garantiert in einer endlichen Anzahl von Schritten und liefert genau eindeutige Stammbrüche.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for greedy_11: Egyptian Fraction.

Every positive rational number ``p/q`` can be written as the sum
of distinct unit fractions (1/d). The greedy algorithm picks the
smallest unit fraction not smaller than the remainder, which is
``1 / ceil(q / p)``. Stop when the remainder hits zero; cap the
loop at q+1 steps so a degenerate input can't run forever.
"""


def solve(p, q):
    if p <= 0 or q <= 0:
        return []
    result = []
    for _ in range(q + 1):
        if p == 0:
            break
        d = (q + p - 1) // p  # ceil(q / p)
        result.append(d)
        p = p * d - q
        q = q * d
        # Reduce to keep numbers small.
        from math import gcd
        g = gcd(p, q) or 1
        p //= g
        q //= g
    return result
```

</details>

## Durchlauf

`n = 6`, `d = 14`. (Bruch \frac{6}{14}).

1. `x = ceil(14 / 6) = ceil(2.33) = 3`.
   - Hänge `3` an. (Unser erster Stammbruch ist \frac{1}{3}).
   - Rest: \frac{6}{14} - \frac{1}{3} = \frac{18 - 14}{42} = \frac{4}{42}.
   - Vereinfache \frac{4}{42} -> \frac{2}{21}.
   - Neuer Zustand: `n = 2`, `d = 21`.
2. `x = ceil(21 / 2) = ceil(10.5) = 11`.
   - Hänge `11` an. (Unser nächster Stammbruch ist \frac{1}{11}).
   - Rest: \frac{2}{21} - \frac{1}{11} = \frac{22 - 21}{231} = \frac{1}{231}.
   - Vereinfachung: Bereits \frac{1}{231}.
   - Neuer Zustand: `n = 1`, `d = 231`.
3. `x = ceil(231 / 1) = 231`.
   - Hänge `231` an.
   - Rest: \frac{1}{231} - \frac{1}{231} = 0.
   - Neuer Zustand: `n = 0`, Schleife terminiert.

Ergebnis: `[3, 11, 231]`.
Überprüfung: \frac{1}{3} + \frac{1}{11} + \frac{1}{231} = \frac{77 + 21 + 1}{231} = \frac{99}{231} = \frac{9 x 11}{21 x 11} = \frac{9}{21} = \frac{3}{7} = \frac{6}{14}. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Die Anzahl der Terme (und damit die Schleifeniterationen) ist im Allgemeinen durch $O(\log N)$ oder $O(N)$ begrenzt, abhängig von den spezifischen arithmetischen Eigenschaften des Zählers. Jede Iteration benötigt $O(log(\min(n,d)$)) Zeit, um den ggT (GCD) zur Vereinfachung zu berechnen.
Die Platzkomplexität beträgt $O(1)$ für die Speicherung lokaler Variablen, abgesehen vom Ausgabe-Array.

## Varianten & Optimierungen

- **Sylvester-Folge:** Wenn man diesen Algorithmus auf \frac{N}{D} = \frac{N}{N+1} anwendet, erzeugt er die Sylvester-Folge, bei der die Nenner doppelt exponentiell wachsen! Wenn man den Bruch nicht in jedem Schritt mit `math.gcd` vereinfacht, werden die Variablen `n` und `d` schnell die 64-Bit-Ganzzahlgrenzen überschreiten.

## Anwendungen in der Praxis

- **Altägyptische Mathematik:** Der Papyrus Rhind (1650 v. Chr.) zeigt, dass den alten Ägyptern eine Notation für allgemeine Brüche (wie 3/4) fehlte. Sie hatten NUR Symbole für Stammbrüche (wie 1/2, 1/3, 1/4). Um 3/4 zu schreiben, waren sie buchstäblich gezwungen, diesen Algorithmus zu verwenden und es als "1/2 und 1/4" zu schreiben.

## Verwandte Algorithmen in cOde(n)

- **[math_01 - GCD (Euklidischer Algorithmus)](../math/math_01_gcd.md)** — Der Euklidische Algorithmus, der im Hintergrund von `math.gcd()` läuft und erforderlich ist, um Ganzzahlüberläufe zu verhindern.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*