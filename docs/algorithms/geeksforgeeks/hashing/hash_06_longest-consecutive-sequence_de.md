# Longest Consecutive Sequence

| | |
|---|---|
| **ID** | `hash_06` |
| **Kategorie** | Hashing |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) |

## Problemstellung

Gegeben ist ein unsortiertes Array von Integern `nums`. Geben Sie die Länge der längsten aufeinanderfolgenden Sequenz von Elementen zurück.
*Wichtige Einschränkung:* Sie müssen einen Algorithmus schreiben, der in $O(N)$ Zeit läuft.

**Eingabe:** Ein Integer-Array `nums`.
**Ausgabe:** Ein Integer, der die Länge der längsten aufeinanderfolgenden Sequenz repräsentiert.

## Wann man es verwendet

- Um zusammenhängende, aufeinanderfolgende Sequenzen zu finden, ohne sich auf eine $O(N \log N)$ Sortierung zu verlassen.
- Ein klassischer Test für das Verständnis, wie $O(1)$ Hash Set-Lookups die Zeitkomplexität grundlegend verändern können.

## Ansatz

**1. Die Sortierfalle:**
Der intuitive Ansatz besteht darin, das Array `[100, 4, 200, 1, 3, 2]` zu `[1, 2, 3, 4, 100, 200]` zu sortieren und dann eine einfache $O(N)$ for-Schleife zu verwenden, um die Sequenzen zu zählen.
Das Sortieren benötigt jedoch $O(N \log N)$ Zeit, was die strikte $O(N)$-Einschränkung des Problems verletzt!

**2. Das Hash Set:**
Wir fügen jede einzelne Zahl in ein Hash Set ein. Dies benötigt $O(N)$ Zeit und ermöglicht es uns, in $O(1)$ Zeit zu prüfen, ob eine bestimmte Zahl existiert.

**3. Die Erkenntnis zum Sequenzstart:**
Wenn wir einfach durch das Array iterieren und für jede Zahl `x+1, x+2, x+3` nachschlagen, könnten wir am Ende die Sequenz `1, 2, 3, 4` viermal separat zählen! (Beginnend bei 1, beginnend bei 2, usw.). Dies würde zu einer $O(N^2)$ Zeitkomplexität führen.
Wie stellen wir sicher, dass wir eine Sequenz nur EINMAL zählen?
**Wir beginnen NUR dann zu zählen, wenn die aktuelle Zahl der ANFANG einer Sequenz ist!**
Woher wissen wir, ob `x` der Anfang ist?
Ganz einfach: Wenn `x - 1` NICHT im Hash Set existiert!
Wenn `x - 1` existiert, befindet sich `x` in der Mitte einer Sequenz. Wir ignorieren es vollständig und lassen die Iteration von `x - 1` die Arbeit erledigen!

**4. Der Algorithmus:**
1. Erstellen Sie ein Hash Set aller Zahlen.
2. Iterieren Sie durch das `nums`-Array.
3. Für jede `num`:
   - Prüfen Sie, ob `num - 1` im Set ist.
   - Falls JA: Nichts tun.
   - Falls NEIN: Wir haben einen Sequenzanfang gefunden! Starten Sie eine `while`-Schleife und prüfen Sie, ob `num + 1`, `num + 2` usw. im Set existieren. Führen Sie einen laufenden Zähler `current_streak`.
4. Aktualisieren Sie `longest_streak = max(longest_streak, current_streak)`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for hash_06: Longest Consecutive Sequence.

Given an unsorted array, return the length of the longest
sequence of consecutive integers. Sort, then walk; O(n
log n). Real O(n) solution uses a set.
"""


def solve(arr, n):
    if n == 0:
        return 0
    s = sorted(set(arr))
    best = 1
    cur = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1] + 1:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 1
    return best
```

</details>

## Durchlauf

`nums = [100, 4, 200, 1, 3, 2]`.
`num_set = {1, 2, 3, 4, 100, 200}`.
`longest_streak = 0`.

1. `num = 100`:
   - Ist `99` im Set? NEIN. Anfang gefunden!
   - `while(101 in set)`? NEIN.
   - `current_streak = 1`. `longest_streak = 1`.
2. `num = 4`:
   - Ist `3` im Set? JA. Kein Anfang! Überspringen.
3. `num = 200`:
   - Ist `199` im Set? NEIN. Anfang gefunden!
   - `while(201 in set)`? NEIN.
   - `current_streak = 1`. `longest_streak = 1`.
4. `num = 1`:
   - Ist `0` im Set? NEIN. Anfang gefunden!
   - `while(2 in set)`? JA. `streak=2`, `curr=2`.
   - `while(3 in set)`? JA. `streak=3`, `curr=3`.
   - `while(4 in set)`? JA. `streak=4`, `curr=4`.
   - `while(5 in set)`? NEIN. `while`-Schleife beenden.
   - `longest_streak = max(1, 4) = 4`.
5. `num = 3`:
   - Ist `2` im Set? JA. Überspringen.
6. `num = 2`:
   - Ist `1` im Set? JA. Überspringen.

Ergebnis `4`. ✓ (Die Sequenz ist `1, 2, 3, 4`).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Man könnte bei einer `while`-Schleife innerhalb einer `for`-Schleife annehmen, dass es sich um $O(N^2)$ handelt.
Die `while`-Schleife wird jedoch NUR für Sequenzanfänge ausgeführt. Jede einzelne Zahl im gesamten Array wird während der gesamten Laufzeit des Algorithmus genau EINMAL innerhalb der `while`-Schleife besucht!
Daher ist die gesamte Zeit, die für das Durchlaufen der Sequenzen aufgewendet wird, durch $O(N)$ begrenzt. Zusammen mit der äußeren $O(N)$-Schleife ist die Zeitkomplexität strikt amortisiert $O(N)$.
Die Platzkomplexität beträgt $O(N)$, um das Hash Set zu speichern.

## Varianten & Optimierungen

- **Union-Find Disjoint Set:** Sie können dies auch in $O(N \cdot \alpha(N)$) Zeit ohne ein Hash Set lösen, indem Sie jede Zahl als Graph-Knoten behandeln und Union-Find (`graph_09`) ausführen, um `num` und `num+1` zu Komponenten zu verbinden. Die Antwort ist einfach die Größe der größten Zusammenhangskomponente!

## Anwendungen in der Praxis

- **Blockchain / Log-Kontinuität:** Überprüfung, ob ein massiver, unsortierter Dump von Blockhöhen oder Paket-Sequenz-IDs keine Lücken enthält, und Finden der längsten ungebrochenen Kette von gültigen, kontinuierlichen Daten.

## Verwandte Algorithmen in cOde(n)

- **[hash_01 - Two Sum](hash_01_two-sum.md)** — Verwendet genau denselben $O(N)$ Set/Map-Lookup-Trick, um das zu ersetzen, was intuitiv eine $O(N^2)$ Brute-Force-Schleife wäre.
- **[graph_09 - Union-Find](../graphs/graph_09_union-find.md)** — Der grafische Alternativansatz, um aufeinanderfolgende Elemente zu gruppieren.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*