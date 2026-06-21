# Longest Repeated Substring

| | |
|---|---|
| **ID** | `suffix_05` |
| **Kategorie** | suffix_array |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **GeeksForGeeks Äquivalent** | [Longest Repeating Substring](https://www.geeksforgeeks.org/longest-repeating-substring-using-suffix-automaton/) |

## Problemstellung

Gegeben ist ein String `s`. Finde den längsten Teilstring, der mindestens zweimal im String vorkommt.
Die beiden Vorkommen dürfen sich überlappen.
Falls kein solcher Teilstring existiert, gib `""` zurück.

**Eingabe:** Ein String `s`.
**Ausgabe:** Ein String, der den längsten wiederholten Teilstring repräsentiert.

## Wann man es verwendet

- Um den größten wiederkehrenden Datenblock in einer Datei zu finden.
- Es ist das befriedigendste und absolut einfachste Problem, das man lösen kann, sobald das LCP Array erstellt wurde.

## Ansatz

**1. Die Erkenntnis der "benachbarten Sortierung":**
Wenn man eine riesige Liste völlig zufälliger Wörter hat und die zwei Wörter finden möchte, die das längste gemeinsame Präfix teilen, erfordert ein naiver Ansatz den Vergleich jedes Wortes mit jedem anderen Wort ($O(N^2)$).
Wenn man die Liste jedoch alphabetisch sortiert, sind Wörter mit übereinstimmenden Präfixen mathematisch gezwungen, direkt nebeneinander zu stehen!
Um das längste gemeinsame Präfix innerhalb des gesamten Datensatzes zu finden, muss man nur benachbarte Elemente vergleichen!

**2. Die LCP Array Lösung:**
Ein Suffix Array ist buchstäblich eine sortierte Liste aller möglichen Suffixe (Teilstrings) des Textes.
Daher MÜSSEN die zwei Suffixe im Text, die das längste Präfix teilen, im Suffix Array direkt nebeneinander liegen.
Welche Datenstruktur speichert die Länge des übereinstimmenden Präfixes zwischen benachbarten Elementen im Suffix Array? Das **LCP Array**!
Daher ist der längste wiederholte Teilstring im gesamten Text einfach der **MAXIMALWERT** innerhalb des LCP Array!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for suffix_05: Longest Repeated Substring.

Find the length of the longest substring of s
"""


def solve(s, n):
    """Length of the longest repeated substring."""
    if n == 0:
        return 0
    # Build the suffix array naively.
    sa = sorted(range(n), key=lambda i: s[i:])
    # Build the LCP array.
    rank = [0] * n
    for i, idx in enumerate(sa):
        rank[idx] = i
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    # Return the max LCP (lcp[0] is 0, so the max is over i >= 1).
    return max(lcp)
```

</details>

## Durchlauf

`s = "banana"`, N = 6.

1. Suffix Array erstellen: `[5, 3, 1, 0, 4, 2]`
   - `0: "a"`
   - `1: "ana"`
   - `2: "anana"`
   - `3: "banana"`
   - `4: "na"`
   - `5: "nana"`
2. LCP Array erstellen: `[0, 1, 3, 0, 0, 2]`.
   - Der Wert an Index 2 ist `3` (Vergleich von `"anana"` mit `"ana"`).
   - Der Wert an Index 5 ist `2` (Vergleich von `"nana"` mit `"na"`).
3. LCP Array nach dem Maximalwert durchsuchen.
   - Maximalwert ist `3` bei `lcp_arr[2]`.
   - `max_len = 3`.
   - Das Suffix, das dies erzeugt hat, ist `suffix_arr[2]`, was Index `1` im ursprünglichen String entspricht!
4. Teilstring ab Index 1 mit Länge 3 zurückgeben: `s[1 : 1+3]`.

Ausgabe: `"ana"`. ✓ (Es kommt zweimal vor: b**ana**na und ban**ana**).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(N)$ |

Das Erstellen des Suffix Array benötigt $O(N \log N)$.
Das Erstellen des LCP Array benötigt $O(N)$.
Das Finden des Maximalwerts im LCP Array benötigt $O(N)$.
Die Zeitkomplexität wird durch das Sortieren des Suffix Array begrenzt: $O(N \log N)$.
Die Platzkomplexität beträgt $O(N)$ für die Arrays.

## Varianten & Optimierungen

- **Dynamische Programmierung ($O(N^2)$):** Wenn man den Suffix Array Algorithmus nicht kennt, kann man dies in $O(N^2)$ Zeit lösen, indem man exakt dieselbe 2D DP-Matrix wie beim Longest Common Substring (`string_05`) verwendet, jedoch `s` und `s` als beide Argumente übergibt und es mit `i != j` einschränkt!
- **Rabin-Karp Binäre Suche ($O(N \log N)$ Zeit, $O(1)$ Platz):** Eine erstaunlich clevere Alternative! Man führt eine binäre Suche über die *Länge* der Antwort durch! Man rät, die Antwort habe die Länge K = N/2. Man verwendet einen Rolling Hash, um jedes Fenster der Länge K zu hashen. Wenn man einen doppelten Hash sieht, bedeutet das, dass ein wiederholter Teilstring der Länge K existiert! Man aktualisiert die binäre Suche, um ein größeres K zu versuchen. Wenn keine doppelten Hashes existieren, versucht man ein kleineres K. Dies erfordert kein Suffix Array und benötigt fast keinen zusätzlichen Platz!

## Anwendungen in der Praxis

- **Verlustfreie Audiokompression (FLAC):** Auffinden massiver, exakt wiederkehrender Wellenformen (wie ein konsistenter Schlagzeug-Beat) in einer Audiodatei, um diese nur ein einziges Mal zu kodieren.

## Verwandte Algorithmen in cOde(n)

- **[suffix_03 - LCP Array](suffix_03_lcp-array-kasai-s-algorithm.md)** — Die Engine, die diese $O(1)$ Suche ermöglicht.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*