# Rabin-Karp-Algorithmus

| | |
|---|---|
| **ID** | `string_06` |
| **Kategorie** | strings |
| **Komplexität (erforderlich)** | $O(N + M)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Rabin-Karp algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm) |

## Problemstellung

Gegeben ist ein `text`-String der Länge N und ein `pattern`-String der Länge M.
Finde alle Startindizes, an denen das `pattern` als zusammenhängender Teilstring innerhalb des `text` vorkommt.
Dies muss in einer durchschnittlichen Zeit von $O(N + M)$ unter Verwendung von String-Hashing gelöst werden.

**Eingabe:** Zwei Strings `text` und `pattern`.
**Ausgabe:** Ein Array von Integern, die die Startindizes der Übereinstimmungen repräsentieren.

## Wann man ihn verwendet

- Bei der String-Suche (ähnlich wie KMP), wenn man gezielt MEHRERE verschiedene Patterns gleichzeitig suchen muss! (KMP erfordert die Vorausberechnung eines LPS-Arrays für jedes einzelne Pattern. Rabin-Karp berechnet lediglich einen einzelnen Integer-Hash für jedes Pattern!).
- Zur Erkennung von Plagiaten in umfangreichen Dokumenten durch das Hashing von Wortsequenzen.

## Ansatz

**1. Die Schwäche des naiven Vergleichs:**
Wenn `text = "AAAAAAAAAB"` und `pattern = "AAAB"`, prüft der naive Ansatz `"AAAB"` gegen Index 0, scheitert am letzten Buchstaben, verschiebt um 1, prüft `"AAAB"` gegen Index 1, scheitert am letzten Buchstaben... Dies führt zu $O(N \times M)$ Vergleichen! Das zeichenweise Vergleichen von Strings ist teuer.

**2. Die Idee des Hashings:**
Der Vergleich von Integern ist blitzschnell $O(1)$. Was wäre, wenn wir das `pattern` in einen Integer (einen Hash) umwandeln?
Wir wandeln auch das erste Fenster des `text` (Länge M) in einen Integer-Hash um.
Wenn die Hashes ÜBEREINSTIMMEN, prüfen wir sicherheitshalber die Strings zeichenweise, um sicherzustellen, dass es keine Hash-Kollision ist.
Wenn die Hashes NICHT übereinstimmen, können die Strings mathematisch nicht identisch sein! Wir verschieben das Fenster sofort!

**3. Der Rolling Hash (Der Trick):**
Moment, wenn wir für jedes Fenster im Text einen neuen Hash berechnen, benötigt das Hashing eines Strings der Länge M eine Zeit von $O(M)$. N Fenster x $O(M)$ Hashing = $O(N \times M)$ Zeit! Das macht den gesamten Vorteil zunichte!
Wir müssen einen **Rolling Hash** verwenden.
Stellen Sie sich den String als eine Zahl zur Basis 256 vor. `"ABC"` -> A \cdot 256^2 + B \cdot 256^1 + C \cdot 256^0.
Wenn wir unser Fenster von `"ABC"` auf `"BCD"` verschieben, berechnen wir nicht alles von Grund auf neu!
Wir nehmen einfach den alten Hash, subtrahieren den Wert von `"A"` (der Buchstabe, der aus dem Fenster fällt), multiplizieren das Ganze mit 256, um alles nach links zu verschieben, und addieren `"D"` (den neuen Buchstaben, der in das Fenster eintritt)!
Dies benötigt exakt $O(1)$ konstante Zeit!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_06: Rabin-Karp.

Rolling-hash substring search.
"""


def solve(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    BASE = 256
    MOD = (1 << 61) - 1
    p_hash = 0
    t_hash = 0
    h = 1
    for i in range(m):
        p_hash = (p_hash * BASE + ord(pattern[i])) % MOD
        t_hash = (t_hash * BASE + ord(text[i])) % MOD
        if i < m - 1:
            h = (h * BASE) % MOD
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t_hash = ((t_hash - ord(text[i]) * h) * BASE + ord(text[i + m])) % MOD
            if t_hash < 0:
                t_hash += MOD
    return -1
```

</details>

## Durchlauf

`text = "ABABDABACDABABC"`, `pattern = "ABABC"`. M = 5.
`d = 10` (für eine einfachere mathematische Darstellung), `q = 13`.
`h = 10^4 % 13 = 3`.

1. **Anfängliche Hashes:**
   - Hash von `"ABABC"` wird berechnet. `p_hash = 8`.
   - Hash des ersten Fensters `"ABABD"` wird berechnet. `t_hash = 2`.
2. **Fenster 0 (`"ABABD"`):**
   - `t_hash (2) != p_hash (8)`. Keine Übereinstimmung!
   - Hash rollen: Subtrahiere `"A"`, verschiebe nach links `* 10`, addiere `"B"`. Neuer `t_hash` wird in $O(1)$ berechnet.
3. **Fenster 1 (`"BABDA"`):**
   - Hashes stimmen nicht überein. Hash rollen.
...
10. **Fenster 10 (`"ABABC"`):**
    - `t_hash (8) == p_hash (8)`! Hashes stimmen überein!
    - Sicherheitsprüfung: Vergleiche `"ABABC"` mit `"ABABC"` Zeichen für Zeichen.
    - Perfekte Übereinstimmung! Index `10` zu den Ergebnissen hinzufügen.
11. Ende der Schleife. Rückgabe `[10]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N + M)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N + M)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N \times M)$ | $O(1)$ |

Die anfängliche Hash-Berechnung benötigt $O(M)$ Zeit.
Das Verschieben des Fensters erfordert $O(N)$ Schritte. Jeder Schritt benötigt $O(1)$ Zeit, um den Hash zu aktualisieren.
Wenn die Hashes übereinstimmen, führen wir eine $O(M)$-Verifizierung durch.
Da unser Primzahl-Modulo q groß ist, sind Hash-Kollisionen extrem selten. Die durchschnittliche Zeitkomplexität beträgt sauber $O(N + M)$.
**SCHLECHTESTER FALL:** Wenn wir eine schlechte Hash-Funktion haben (oder bösartige Daten wie `text="AAAAAAAAA", pattern="AAAA"`), erzeugt jedes einzelne Fenster eine Hash-Kollision! Wir müssten bei jedem Schritt die $O(M)$-String-Verifizierung durchführen, was den Algorithmus auf $O(N \times M)$ verschlechtert!
Die Platzkomplexität beträgt strikt $O(1)$ konstante Zeit.

## Varianten & Optimierungen

- **Suche nach mehreren Patterns:** Wenn Sie nach K verschiedenen Patterns der Länge M suchen, berechnen Sie alle K Hashes und speichern diese in einem Hash Set. Während Sie den Text-Hash rollen, prüfen Sie einfach, ob `t_hash in pattern_hashes_set`! Dies sucht nach tausenden von Patterns gleichzeitig in exakt derselben $O(N)$-Zeit!

## Anwendungen in der Praxis

- **Anti-Plagiats-Software:** Turnitin und Moss verwenden Rabin-Karp, um studentische Arbeiten in 50-Zeichen-Blöcke zu zerlegen, diese zu hashen und mit einer riesigen Datenbank von Millionen von Hashes zu vergleichen, um wörtliche Kopien zu erkennen.

## Verwandte Algorithmen in cOde(n)

- **[string_03 - KMP Pattern Matching](string_03_kmp-string-matching.md)** — Die mathematisch überlegene Alternative, die durch den vollständigen Verzicht auf Hashing und Kollisionen eine Worst-Case-Zeit von $O(N+M)$ garantiert.
- **[hashing_01 - Two Sum](../hashing/hash_01_two-sum.md)** — Das grundlegende Konzept, komplexe Daten (oder erwartete Ziele) auf Integer abzubilden, um $O(1)$-Lookups zu ermöglichen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*