# Turm von Hanoi

| | |
|---|---|
| **ID** | `recursion_04` |
| **Kategorie** | Rekursion |
| **Komplexität (erforderlich)** | $O(2^N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Turm von Hanoi](https://de.wikipedia.org/wiki/Turm_von_Hanoi) |

## Problemstellung

Sie haben drei Stäbe (`Source`, `Destination` und `Auxiliary`) und `N` Scheiben unterschiedlicher Größe.
Zu Beginn sind alle `N` Scheiben auf dem `Source`-Stab in absteigender Reihenfolge ihrer Größe gestapelt (die größte unten, die kleinste oben).
Das Ziel ist es, den gesamten Stapel auf den `Destination`-Stab zu bewegen, wobei folgende Regeln einzuhalten sind:
1. Es darf immer nur eine Scheibe gleichzeitig bewegt werden.
2. Ein Zug besteht darin, die oberste Scheibe von einem der Stapel zu nehmen und sie auf einen anderen Stapel zu legen.
3. Keine Scheibe darf auf eine kleinere Scheibe gelegt werden.

Geben Sie die schrittweisen Anweisungen zur Lösung des Puzzles aus.

**Eingabe:** Eine Ganzzahl `N`, die die Anzahl der Scheiben repräsentiert.
**Ausgabe:** Eine Reihe von Strings, die die Züge darstellen (z. B. "Move disk 1 from A to C").

## Wann man es verwendet

- Um die Mächtigkeit der "Leap of Faith"-Rekursion zu verstehen (darauf zu vertrauen, dass der rekursive Aufruf ein kleineres Teilproblem korrekt löst, ohne jeden Schritt mental nachzuvollziehen).
- Eine klassische akademische Übung für die vollständige Induktion.

## Ansatz

**1. Die "Leap of Faith"-Erkenntnis:**
Angenommen, wir möchten N Scheiben von `Source` nach `Destination` bewegen.
Die absolut größte Scheibe (Scheibe N) befindet sich ganz unten. Um sie zum `Destination`-Stab zu bewegen, MÜSSEN wir zuerst die N-1 Scheiben darüber vollständig aus dem Weg räumen!
Wo legen wir diese N-1 Scheiben ab? Wir können sie nicht auf den `Destination`-Stab legen, da Scheibe N dann dort nicht platziert werden könnte! Wir müssen die N-1 Scheiben auf den `Auxiliary`-Stab bewegen.

Wenn wir annehmen, dass unsere rekursive Funktion auf magische Weise weiß, wie man N-1 Scheiben perfekt bewegt:
1. Wir weisen die rekursive Funktion an, die obersten N-1 Scheiben von `Source` nach `Auxiliary` zu bewegen.
2. Nun liegt Scheibe N vollständig frei. Der `Destination`-Stab ist komplett leer. Wir bewegen einfach Scheibe N von `Source` nach `Destination`!
3. Schließlich weisen wir die rekursive Funktion an, die N-1 Scheiben vom `Auxiliary`-Stab auf den `Destination`-Stab zu bewegen (der nun Scheibe N sicher am Boden hält).

**2. Die Struktur der rekursiven Funktion:**
Wir benötigen eine Funktion `hanoi(n, source, destination, auxiliary)`.
- **Induktionsanfang (Basis):** Wenn `n == 1`, gibt es nur eine Scheibe. Bewegen Sie diese einfach direkt von `source` nach `destination` und kehren Sie zurück.
- **Rekursionsschritt 1:** Bewegen Sie N-1 Scheiben von `source` nach `auxiliary`. (Während dieses Schrittes fungiert der `destination`-Stab als temporärer Helfer).
- **Der physische Zug:** Geben Sie "Move disk N from source to destination" aus.
- **Rekursionsschritt 2:** Bewegen Sie N-1 Scheiben von `auxiliary` nach `destination`. (Während dieses Schrittes fungiert der `source`-Stab als temporärer Helfer).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for recursion_04: Tower of Hanoi.

Move n disks from source to destination using an auxiliary
peg. The optimal recurrence is: move n-1 disks from source
to auxiliary, move the largest disk, move n-1 disks from
auxiliary to destination. Returns the sequence of moves as
a list of (from, to) tuples.
"""


def solve(n, source, destination, auxiliary):
    moves = []

    def helper(count, src, dst, aux):
        if count == 0:
            return
        helper(count - 1, src, aux, dst)
        moves.append((src, dst))
        helper(count - 1, aux, dst, src)

    helper(n, source, destination, auxiliary)
    return moves
```

</details>

## Durchlauf

`N = 3`. Stäbe: Source=`A`, Dest=`C`, Aux=`B`.
Start: `recurse(3, A, C, B)`.

1. **`recurse(3, A, C, B)`**:
   - Schritt 1: Aufruf `recurse(2, A, B, C)`.
2. **`recurse(2, A, B, C)`**:
   - Schritt 1: Aufruf `recurse(1, A, C, B)`.
3. **`recurse(1, A, C, B)`**:
   - Induktionsanfang! Ausgabe: `Move disk 1 from A to C`. Rückkehr.
4. Zurück in `recurse(2)`:
   - Schritt 2: Ausgabe: `Move disk 2 from A to B`.
   - Schritt 3: Aufruf `recurse(1, C, B, A)`.
5. **`recurse(1, C, B, A)`**:
   - Induktionsanfang! Ausgabe: `Move disk 1 from C to B`. Rückkehr.
6. Zurück in `recurse(3)`:
   - Schritt 2: Ausgabe: `Move disk 3 from A to C`.
   - Schritt 3: Aufruf `recurse(2, B, C, A)`.
7. **`recurse(2, B, C, A)`**:
   - Schritt 1: Aufruf `recurse(1, B, A, C)`.
8. **`recurse(1, B, A, C)`**:
   - Induktionsanfang! Ausgabe: `Move disk 1 from B to A`. Rückkehr.
9. Zurück in `recurse(2)`:
   - Schritt 2: Ausgabe: `Move disk 2 from B to C`.
   - Schritt 3: Aufruf `recurse(1, A, C, B)`.
10. **`recurse(1, A, C, B)`**:
    - Induktionsanfang! Ausgabe: `Move disk 1 from A to C`. Rückkehr.

Puzzle gelöst! Gesamtzüge = 7. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(2^N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(2^N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(2^N)$ | $O(N)$ |

Sei T(N) die Anzahl der Züge zur Lösung für N Scheiben.
T(N) = 2 \cdot T(N-1) + 1.
Diese Rekursionsgleichung löst sich exakt zu T(N) = 2^N - 1 auf.
Da wir physisch 2^N - 1 Anweisungen ausgeben müssen, ist die Zeitkomplexität strikt $O(2^N)$.
Die maximale Tiefe des rekursiven Aufruf-Stacks ist N, daher ist die Platzkomplexität $O(N)$ (abgesehen vom Konsolenausgabestrom).
*(Die Legende besagt, dass Priester in einem hinduistischen Tempel derzeit eine 64-Scheiben-Version dieses Puzzles lösen. Bei einer Scheibe pro Sekunde werden 2^{64}-1 Züge etwa 585 Milliarden Jahre dauern, woraufhin das Universum enden wird).*

## Varianten & Optimierungen

- **Iterativer Ansatz:** Das Puzzle kann vollständig ohne Rekursion unter Verwendung einer erstaunlich einfachen deterministischen mathematischen Regel gelöst werden. Wenn N gerade ist, führen Sie den ersten Zug zwischen `A` und `B` aus. Wenn N ungerade ist, führen Sie den ersten Zug zwischen `A` und `C` aus. Führen Sie dann kontinuierlich eine Schleife aus: Führen Sie den einzig gültigen Zug zwischen `A` und `B`, dann `A` und `C`, dann `B` und `C` aus.
- **Gray-Code-Matrix:** Die Sequenz der Scheibenzüge, die zur perfekten Lösung des Turms von Hanoi erforderlich ist, spiegelt exakt die Bit-Flips wider, die zur Generierung einer N-Bit Gray-Code-Sequenz benötigt werden!

## Anwendungen in der Praxis

- **Psychologische Tests:** Der Turm von Hanoi ist ein Standardtest der Verhaltenspsychologie, der verwendet wird, um die exekutiven Funktionen des Frontallappens, die Planungsfähigkeiten und das Arbeitsgedächtnis bei Menschen und Primaten zu bewerten.

## Verwandte Algorithmen in cOde(n)

- **[recursion_01 - Power Sum](recursion_01_power-sum.md)** — Eine weitere grundlegende binäre Rekursionsbaumstruktur.
- **[graphs_01 - DFS](../graphs/graph_01_dfs.md)** — Die rekursive Traversierung des Turms von Hanoi zeichnet tatsächlich exakt eine Tiefensuche (Depth-First Search) über einen fraktalen Graphen nach, der als Sierpinski-Dreieck bekannt ist!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*