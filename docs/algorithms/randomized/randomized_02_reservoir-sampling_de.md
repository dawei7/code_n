# Reservoir Sampling

| | |
|---|---|
| **ID** | `randomized_02` |
| **Kategorie** | randomized |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(K)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/) |

## Problemstellung

Gegeben ist ein ankommender Datenstrom (Stream) von Elementen unbekannter Größe N (wobei N zu groß sein kann, um in den Arbeitsspeicher zu passen). Es sollen K Elemente gleichverteilt zufällig aus dem Stream ausgewählt werden.
Mit "gleichverteilt zufällig" ist gemeint, dass am Ende des Streams jedes verarbeitete Element mit einer Wahrscheinlichkeit von genau \frac{K}{N} in der finalen Stichprobe enthalten sein muss.
Es ist nur ein einziger Durchlauf über die Daten erlaubt, und es dürfen nur K Elemente gleichzeitig im Arbeitsspeicher gehalten werden.

**Eingabe:** Ein Stream von Datenelementen und eine Ganzzahl K.
**Ausgabe:** Ein Array der Größe K, das die zufällig ausgewählten Elemente enthält.

## Anwendungsbereiche

- Wenn Sie zufällige Elemente aus einem Datensatz auswählen müssen, der entweder live gestreamt wird oder zu umfangreich ist, um ihn im Voraus zu zählen (wie eine 10 TB große Log-Datei oder ein Live-Twitter-Feed).

## Ansatz

Wenn wir N im Voraus kennen würden, könnten wir einfach K zufällige Indizes zwischen 0 und N-1 generieren und diese auswählen. Aber wir kennen N nicht. Der Stream läuft kontinuierlich weiter.

**Der Algorithmus (Algorithmus R):**
1. Verwalten Sie ein Array namens `reservoir` der Größe K.
2. Während die ersten K Elemente aus dem Stream eintreffen, fügen Sie diese direkt in das `reservoir` ein.
3. Für das i-te Element, das aus dem Stream eintrifft (wobei i > K):
   - Wählen Sie eine zufällige Ganzzahl `j` zwischen 1 und i (einschließlich).
   - Wenn `j <= K` (was mit einer Wahrscheinlichkeit von \frac{K}{i} eintritt):
     - Ersetzen Sie `reservoir[j]` durch das neue i-te Element!
   - Andernfalls verwerfen Sie das i-te Element.

**Warum funktioniert das? (Die Mathematik)**
Wie hoch ist für ein spezifisches Element (sagen wir, das allererste Element) die Wahrscheinlichkeit, dass es bis zum Ende eines Streams der Größe N überlebt?
Es gelangt mit einer Wahrscheinlichkeit von 1 in das `reservoir`.
Wenn das (K+1)-te Element eintrifft, ersetzt es ein bestehendes Element mit einer Wahrscheinlichkeit von \frac{K}{K+1}. Die Chance, dass es *unser spezifisches Element* ersetzt, beträgt \frac{1}{K+1}. Die Chance, dass unser Element überlebt, ist also 1 - \frac{1}{K+1} = \frac{K}{K+1}.
Wenn das (K+2)-te Element eintrifft, ist die Chance, dass unser Element überlebt, \frac{K+1}{K+2}.
...
Wenn das N-te Element eintrifft, ist die Chance, dass unser Element überlebt, \frac{N-1}{N}.
Gesamtwahrscheinlichkeit des Überlebens = 1 x \frac{K}{K+1} x \frac{K+1}{K+2} x \dots x \frac{N-1}{N}.
Alle Zwischenterme kürzen sich perfekt heraus, sodass genau \frac{K}{N} übrig bleibt!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for randomized_02: Reservoir Sampling.

Pick k items uniformly at random from a stream of unknown
length. Standard algorithm: fill the reservoir with the first
k items; for each subsequent item i (i >= k), replace a
random reservoir index with probability k / (i + 1).
"""


def solve(stream, k, n):
    import random
    if k <= 0 or n == 0:
        return []
    reservoir = list(stream[:k])
    for i in range(k, n):
        j = random.randint(0, i)
        if j < k:
            reservoir[j] = stream[i]
    return reservoir
```

</details>

## Durchlauf

`stream = [A, B, C, D]`, `k = 2`.

1. `i=0, item=A`: `i < 2`. `reservoir = [A]`.
2. `i=1, item=B`: `i < 2`. `reservoir = [A, B]`.
3. `i=2, item=C`: `i = 2`.
   - `random.randint(0, 2)` ergibt `0`.
   - `0 < 2` ist True. `reservoir[0] = C`.
   - `reservoir = [C, B]`.
   *(Wahrscheinlichkeit, dass C gewählt wurde: 2/3. Wahrscheinlichkeit, dass A überlebte: 1 * 1/2 = 1/2... Moment, meine obige Rechnung basierte auf 1-Indizierung. Bei 0-Indizierung ist die Wahrscheinlichkeit, A spezifisch zu ersetzen, 1/3, das Überleben beträgt 2/3. Die Mathematik stimmt!)*
4. `i=3, item=D`: `i = 3`.
   - `random.randint(0, 3)` ergibt `3`.
   - `3 < 2` ist False. D wird ignoriert.
   - `reservoir = [C, B]`.

Finale Stichprobe: `[C, B]`. Jedes Element hatte eine Chance von genau 2/4 = 50 %, im `reservoir` zu landen. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(K)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(K)$ |
| **Schlechtester Fall** | $O(N)$ | $O(K)$ |

Wir verarbeiten jedes Element im Stream genau einmal. Dabei führen wir $O(1)$ Zufallszahlengenerierungen und Array-Einfügungen durch. Die Zeitkomplexität ist strikt $O(N)$.
Wir speichern nur die finalen K Elemente im Arbeitsspeicher. Die Platzkomplexität beträgt $O(K)$.

## Varianten & Optimierungen

- **Algorithmus L:** Das Generieren einer Zufallszahl für *jedes* Element in einem massiven Stream kann rechenintensiv sein. Algorithmus L optimiert dies, indem er mathematisch die "Sprungdistanz" berechnet (wie viele Elemente übersprungen werden sollen, bevor das nächste akzeptiert wird), unter Verwendung von inversen kumulativen Verteilungsfunktionen. Dies reduziert die Anzahl der `random()`-Aufrufe von $O(N)$ auf $O(K log(N/K))$!

## Praxisanwendungen

- **A/B-Testing-Telemetrie:** Auswahl einer gleichverteilten Stichprobe von 10.000 Benutzersitzungen aus einem massiven Datenstrom von Milliarden von Sitzungen, um Absturzprotokolle zu analysieren, ohne die Metrik-Server zu überlasten.

## Verwandte Algorithmen in cOde(n)

- **[randomized_03 - Fisher-Yates Shuffle](randomized_03_fisher-yates-shuffle.md)** — Verwendet eine sehr ähnliche probabilistische Logik, mischt jedoch ein gesamtes Array im Arbeitsspeicher, anstatt aus einem Stream zu sampeln.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*