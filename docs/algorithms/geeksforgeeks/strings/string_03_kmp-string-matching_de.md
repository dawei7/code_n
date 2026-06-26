# KMP String Matching

| | |
|---|---|
| **ID** | `string_03` |
| **Kategorie** | strings |
| **Komplexität (erforderlich)** | $O(N + M)$ |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **Wikipedia** | [Knuth-Morris-Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm) |

## Problemstellung

Gegeben sind zwei Strings: ein `text` der Länge `N` und ein `pattern` der Länge `M`.
Finde alle Startindizes im `text`, an denen das `pattern` als zusammenhängender Teilstring vorkommt.

**Eingabe:** Zwei Strings `text` und `pattern`.
**Ausgabe:** Eine Liste von Ganzzahlen, die die Startindizes der Übereinstimmungen repräsentieren.

**Beispiel:**
`text = "ABABDABACDABABCABAB"`, `pattern = "ABABCABAB"`
Ausgabe: `[10]`.

## Wann man es verwendet

- Bei der Suche in Strings, wenn die naive Zeitkomplexität von $O(N \times M)$ zu langsam ist und eine garantierte lineare Zeitkomplexität von $O(N + M)$ benötigt wird.
- Es ist die kanonische Lösung für das String-Matching-Problem.

## Ansatz

Bei der naiven Suche (`string_04`) verschieben wir das `pattern` bei einem Mismatch an Position 5 um nur eine Stelle nach rechts und beginnen den Vergleich von vorne.
Der **Knuth-Morris-Pratt (KMP)** Algorithmus erkennt, dass *wir bereits wissen*, was die vorherigen 4 Zeichen waren! Wir sollten diese Information nicht verwerfen.

KMP verwendet ein Hilfs-Array, das **LPS-Array (Longest Proper Prefix which is also Suffix)** genannt wird.
Für das `pattern` `"ABABCABAB"` sagt uns das LPS-Array: "Wenn an Index `i` ein Mismatch auftritt, wie lang ist das längste Präfix des `pattern`, das korrekt mit dem Suffix des gerade ausgewerteten Abschnitts übereinstimmt?"
Dies sagt uns genau, wie weit wir unseren `pattern`-Pointer `j` zurücksetzen müssen, ohne jemals unseren `text`-Pointer `i` rückwärts zu bewegen!

**Schritt 1: Berechne das LPS-Array für das `pattern` in $O(M)$ Zeit.**
Verfolge für jeden Index die Länge des längsten echten Präfixes, das mit dem Suffix übereinstimmt, welches an diesem Index endet.

**Schritt 2: Durchsuche den `text` in $O(N)$ Zeit.**
Verwende zwei Pointer: `i` für den `text`, `j` für das `pattern`.
- Wenn `text[i] == pattern[j]`, inkrementiere beide.
- Wenn `j == M`, haben wir eine Übereinstimmung gefunden! Speichere den Startindex. Setze `j = lps[j-1]`, um nach überlappenden Übereinstimmungen weiterzusuchen.
- Wenn `text[i] != pattern[j]`:
  - Wenn `j > 0`, beginnen wir nicht von vorne! Wir setzen `j` auf `lps[j-1]` zurück.
  - Wenn `j == 0`, inkrementieren wir einfach `i` (wir befinden uns am Anfang des `pattern` und kein Präfix stimmte überein).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_03: KMP String Matching.

Knuth-Morris-Pratt: build a failure function over the pattern,
then scan the text without ever restarting.
"""


def solve(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1

    pi = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and pattern[k] != pattern[i]:
            k = pi[k - 1]
        if pattern[k] == pattern[i]:
            k += 1
        pi[i] = k

    k = 0
    for i in range(n):
        while k > 0 and pattern[k] != text[i]:
            k = pi[k - 1]
        if pattern[k] == text[i]:
            k += 1
        if k == m:
            return i - m + 1
    return -1
```

</details>

## Durchlauf

Erstellen wir das LPS für `pattern = "AAAC"`. `M = 4`.
- `lps[0] = 0`.
- `i=1` ('A'): `pat[1] == pat[0]`. `length = 1`. `lps[1] = 1`.
- `i=2` ('A'): `pat[2] == pat[1]`. `length = 2`. `lps[2] = 2`.
- `i=3` ('C'): `pat[3] != pat[2]`. Backtrack: `length = lps[1] = 1`.
- `i=3` ('C'): `pat[3] != pat[1]`. Backtrack: `length = lps[0] = 0`.
- `i=3` ('C'): `pat[3] != pat[0]`. Länge ist 0. `lps[3] = 0`. `i += 1`.
LPS = `[0, 1, 2, 0]`.

`text = "AAAAC"`. `i=0, j=0`.
- `i=0,1,2`: Match 'A', 'A', 'A'. `j=3`.
- `i=3`: `text[3]` ('A') != `pat[3]` ('C'). Mismatch!
  - `j` setzt zurück auf `lps[j-1] = lps[2] = 2`.
  - Beachte, dass `i` IMMER NOCH 3 ist. Wir haben den Text-Pointer nicht zurückgesetzt!
- `i=3`: `text[3]` ('A') == `pat[2]` ('A'). Match! `i=4, j=3`.
- `i=4`: `text[4]` ('C') == `pat[3]` ('C'). Match! `i=5, j=4`.
- `j == 4`. Match gefunden an Index `i - j = 5 - 4 = 1`.

Ausgabe: `[1]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N + M)$ | $O(M)$ |
| **Durchschnittlicher Fall** | $O(N + M)$ | $O(M)$ |
| **Schlechtester Fall** | $O(N + M)$ | $O(M)$ |

Die Berechnung des LPS-Arrays benötigt $O(M)$ Zeit.
Die Suchschleife iteriert durch das Text-Array der Größe N. Obwohl das innere `if/else` den Pointer `j` in einer `while`-artigen Weise zurücksetzen kann, verringert sich `i` niemals, und `j` ist durch `i` begrenzt. Eine amortisierte Analyse beweist, dass die Suchschleife höchstens 2N Operationen ausführt. Daher ist die Zeitkomplexität strikt $O(N + M)$.
Die Platzkomplexität beträgt $O(M)$, um das LPS-Array zu speichern.

## Varianten & Optimierungen

- **Aho-Corasick-Algorithmus:** Wenn Sie nach *mehreren* Mustern gleichzeitig (z. B. einem Wörterbuch mit verbotenen Wörtern) in einem einzigen Text suchen müssen, benötigt die KMP-Ausführung für K Muster $O(K \cdot (N+M))$. Aho-Corasick erstellt einen Automaten (einen Trie mit LPS-ähnlichen Fehler-Links), um nach ALLEN Mustern gleichzeitig in $O(N + M + \text{Matches})$ Zeit zu suchen!

## Anwendungen in der Praxis

- **Texteditoren:** Die `Strg+F` oder "Suchen"-Funktionalität in IDEs und Texteditoren verlässt sich stark auf KMP oder ähnliche String-Suchalgorithmen mit linearer Laufzeit, um ein Einfrieren bei massiven Log-Dateien zu verhindern.

## Verwandte Algorithmen in cOde(n)

- **[string_04 - Naive Pattern Search](string_04_naive-pattern-search.md)** — Der Brute-Force-Ansatz mit $O(N \times M)$.
- **[string_06 - Rabin-Karp](string_06_rabin-karp.md)** — Eine alternative $O(N+M)$-Suche unter Verwendung von Rolling Hashes anstelle eines LPS-Arrays.
- **[string_07 - Z-Algorithm](string_07_z-algorithm.md)** — Ein weiterer Algorithmus für Pattern Matching in linearer Zeit, der ein anderes Präfix-Array-Konzept verwendet.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*