# Longest Palindromic Substring

| | |
|---|---|
| **ID** | `string_02` |
| **Kategorie** | strings |
| **Komplexität (erforderlich)** | $O(N^2)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |

## Problemstellung

Gegeben sei ein String `s`. Geben Sie den **längsten palindromischen Teilstring** in `s` zurück.
Ein String ist ein Palindrom, wenn er vorwärts und rückwärts gelesen identisch ist.

**Eingabe:** Ein String `s`.
**Ausgabe:** Ein String, der das längste Palindrom repräsentiert.

**Beispiel 1:**
`s = "babad"`
Ausgabe: `"bab"` (oder `"aba"`).

**Beispiel 2:**
`s = "cbbd"`
Ausgabe: `"bb"`.

## Anwendung

- Ein klassisches Problem in Vorstellungsgesprächen, um die Fähigkeit zu testen, die "Expand Around Center"-Logik gegenüber einem naiven $O(N^3)$ Brute-Force-Ansatz zu erkennen und zu optimieren.

## Ansatz

Der naive Brute-Force-Ansatz prüft jeden möglichen Teilstring darauf, ob er ein Palindrom ist. Es gibt $O(N^2)$ Teilstrings, und die Überprüfung jedes einzelnen benötigt $O(N)$ Zeit, was zu einer Gesamtlaufzeit von $O(N^3)$ führt.

**Expand Around Center ($O(N^2)$):**
Jedes Palindrom besitzt ein Zentrum. Wir können über den String iterieren und jedes einzelne Zeichen als potenzielles Zentrum eines Palindroms betrachten, wobei wir uns nach links und rechts ausdehnen, solange die Zeichen übereinstimmen!
Palindrome können jedoch zwei Arten von Zentren haben:
1. **Ungerade Länge** (z. B. `"aba"`): Das Zentrum ist ein einzelnes Zeichen (`'b'`).
2. **Gerade Länge** (z. B. `"abba"`): Das Zentrum ist der unsichtbare Raum *zwischen* zwei identischen Zeichen (`'b'` und `'b'`).

Daher müssen wir für jeden Index `i` versuchen, uns zweimal nach außen auszudehnen:
- Ausdehnung mit `i` als Zentrum (ungerade Länge).
- Ausdehnung mit `i` und `i+1` als Zentrum (gerade Länge).

Wir speichern dabei die Start- und Endindizes der längsten gültigen Ausdehnung, die im gesamten String gefunden wurde.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_02: Longest Palindromic Substring.

Expand around every center, track the longest palindrome, return
the leftmost on tie.
"""


def solve(s):
    n = len(s)
    if n == 0:
        return ""
    best_lo, best_hi = 0, 0

    def expand(lo, hi):
        while lo >= 0 and hi < n and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        return lo + 1, hi - 1

    for c in range(n):
        lo, hi = expand(c, c)
        if hi - lo > best_hi - best_lo:
            best_lo, best_hi = lo, hi
        if c > 0:
            lo, hi = expand(c - 1, c)
            if hi - lo > best_hi - best_lo:
                best_lo, best_hi = lo, hi

    return s[best_lo:best_hi + 1]
```

</details>

## Durchlauf

`s = "cbbd"`

- **i = 0 ('c'):**
  - Ungerade Ausdehnung: `L=0, R=0` -> Stimmt mit 'c' überein. Ausdehnung -> `L=-1, R=1` (außerhalb der Grenzen). Länge = 1.
  - Gerade Ausdehnung: `L=0, R=1` -> 'c' != 'b'. Keine Übereinstimmung. Länge = 0.
  - Max = 1. `max_len = 1`. `start = 0`. Aktuell = `"c"`.
- **i = 1 ('b'):**
  - Ungerade Ausdehnung: `L=1, R=1` -> Stimmt mit 'b' überein. Ausdehnung -> `L=0, R=2` ('c' != 'b'). Keine Übereinstimmung. Länge = 1.
  - Gerade Ausdehnung: `L=1, R=2` -> 'b' == 'b'. Übereinstimmung! Ausdehnung -> `L=0, R=3` ('c' != 'd'). Keine Übereinstimmung. Länge = 2.
  - Max = 2. `max_len = 2`. `start = 1 - (2-1)//2 = 1`. Aktuell = `"bb"`.
- **i = 2 ('b'):**
  - Ungerade Ausdehnung: Länge = 1.
  - Gerade Ausdehnung: `L=2, R=3` ('b' != 'd'). Länge = 0.
- **i = 3 ('d'):**
  - Ungerade Ausdehnung: Länge = 1.

Final `start = 1`, `max_len = 2`.
Ausgabe: `s[1:3]` = `"bb"`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N^2)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(1)$ |

Die äußere Schleife läuft N-mal durch. Im schlechtesten Fall (z. B. ein String aus identischen Zeichen wie `"aaaaa"`) dehnt sich die innere `expand_around_center`-Schleife jedes Mal bis an die Ränder aus, was $O(N)$ Operationen pro Iteration erfordert. Somit beträgt die Zeitkomplexität im schlechtesten Fall $O(N^2)$.
Die Platzkomplexität ist $O(1)$, da wir lediglich Integer-Indizes speichern, die die Grenzen repräsentieren.

## Varianten & Optimierungen

- **Dynamische Programmierung $O(N^2)$:** Man kann ein 2D-Boolean-Array `dp[i][j]` verwenden, das darstellt, ob der Teilstring vom Index i bis j ein Palindrom ist. `dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]`. Während dies eine Zeitkomplexität von $O(N^2)$ aufweist, benötigt es $O(N^2)$ Platz, was die "Expand Around Center"-Methode in Bezug auf die Speichereffizienz überlegen macht.
- **Manacher-Algorithmus $O(N)$:** Es ist mathematisch möglich, den längsten palindromischen Teilstring in strikt linearer $O(N)$-Zeit zu finden! Der Manacher-Algorithmus erreicht dies, indem er die Ausdehnungslängen geschickt in einem Array speichert und die gespiegelten Eigenschaften kleinerer Palindrome, die in größeren Palindromen enthalten sind, nutzt, um redundante Ausdehnungsprüfungen zu überspringen. Er ist jedoch bekanntermaßen komplex und wird in Standard-Vorstellungsgesprächen selten erwartet.

## Anwendungen in der Praxis

- **Bioinformatik:** Erkennung von genomischen Palindromen in DNA-Sequenzen (z. B. Erkennungsstellen für Restriktionsenzyme), obwohl sich biologische Palindrome oft auf reverse Komplemente beziehen und nicht auf direkte Spiegelungen der Sequenz.

## Verwandte Algorithmen in cOde(n)

- **[dynamic_27 - Longest Palindromic Subsequence](../dynamic/dp_27_longest-palindromic-subsequence.md)** — Ein eng verwandtes Problem der dynamischen Programmierung, bei dem die Zeichen nicht zusammenhängend sein müssen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*