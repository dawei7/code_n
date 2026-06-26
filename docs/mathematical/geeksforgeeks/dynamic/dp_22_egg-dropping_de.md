# Formale mathematische Spezifikation: Egg Dropping (Mathematisch $O(K \log N)$)

## 1. Definitionen und Notation

Sei $k \in \mathbb{Z}^+$ die Anzahl der verfügbaren Eier und $n \in \mathbb{Z}^+$ die Anzahl der Stockwerke im Gebäude. Wir definieren das Ziel als die Bestimmung der minimalen Anzahl an Versuchen $m$, die erforderlich sind, um das kritische Stockwerk $f_c \in \{0, 1, \dots, n\}$ zu finden, wobei $f_c$ das höchste Stockwerk ist, von dem aus ein Ei fallen gelassen werden kann, ohne zu zerbrechen.

Wir definieren den Zustandsraum $\mathcal{S}$ über die Funktion $f(m, k)$, welche die maximale Anzahl an Stockwerken repräsentiert, die bei gegebenen $m$ Zügen und $k$ Eiern eindeutig getestet werden können.
- Der Definitionsbereich von $m$ ist $\mathbb{Z}_{\ge 0}$.
- Der Definitionsbereich von $k$ ist $\mathbb{Z}_{\ge 0}$.
- Der Wertebereich ist $\mathbb{Z}_{\ge 0}$, was die Kapazität der Teststrategie darstellt.

Das Problem ist äquivalent zur Suche nach dem kleinsten $m$, sodass gilt:
$$f(m, k) \ge n$$

## 2. Algebraische Charakterisierung

Um die Rekursionsgleichung herzuleiten, betrachten wir den Zustand $(m, k)$. Nach dem Fallenlassen eines Eies von einem beliebigen Stockwerk treten zwei sich gegenseitig ausschließende Ergebnisse ein:
1. **Das Ei zerbricht:** Wir haben 1 Zug und 1 Ei verbraucht. Um das Ergebnis zu garantieren, müssen wir in der Lage sein, die verbleibenden Stockwerke unterhalb des aktuellen zu testen. Die maximale Anzahl solcher Stockwerke ist $f(m-1, k-1)$.
2. **Das Ei überlebt:** Wir haben 1 Zug und 0 Eier verbraucht. Wir müssen in der Lage sein, die verbleibenden Stockwerke oberhalb des aktuellen zu testen. Die maximale Anzahl solcher Stockwerke ist $f(m-1, k)$.

Unter Einbeziehung des Stockwerks, von dem aus der Wurf initiiert wurde, ist die Rekursionsgleichung definiert als:
$$f(m, k) = f(m-1, k-1) + f(m-1, k) + 1$$

**Randbedingungen:**
- $f(m, 0) = 0$ (Null Eier können keine Stockwerke testen).
- $f(0, k) = 0$ (Null Züge können keine Stockwerke testen).
- $f(m, 1) = m$ (Mit einem Ei müssen wir die Stockwerke nacheinander testen).

**Geschlossene Form:**
Durch vollständige Induktion lässt sich die Rekursionsgleichung $f(m, k) = \sum_{i=1}^{k} \binom{m}{i}$ herleiten. Diese Identität zeigt, dass die maximale Anzahl testbarer Stockwerke der Summe der ersten $k$ Binomialkoeffizienten von $m$ entspricht.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus sucht das kleinste $m$, sodass $\sum_{i=1}^{k} \binom{m}{i} \ge n$ gilt.
1. **Suchraum:** Da $f(m, k)$ streng monoton steigend in Bezug auf $m$ ist und $f(m, k) \approx \frac{m^k}{k!}$ für $m \gg k$ gilt, ist der Wert von $m$ im Schlechtesten Fall durch $O(n)$ ($k=1$) und für $k \ge \log_2 n$ durch $O(\log n)$ beschränkt.
2. **Berechnung:** Für ein festes $m$ kann die Berechnung der Summe $\sum_{i=1}^{k} \binom{m}{i}$ in $O(k)$ Zeit unter Verwendung der Identität $\binom{m}{i} = \binom{m}{i-1} \times \frac{m-i+1}{i}$ durchgeführt werden.
3. **Binäre Suche:** Durch die Durchführung einer binären Suche über den Bereich $[1, n]$ nach dem optimalen $m$ werten wir die Summe $O(\log n)$ Mal aus.

Somit ergibt sich die gesamte Zeitkomplexität zu:
$$T(n, k) = O(k \log n)$$

### Platzkomplexität
Der Algorithmus verwendet ein 1D-Array der Größe $k+1$, um die Werte von $f(m, \cdot)$ für die aktuelle Iteration der Züge zu speichern.
- Der Zustandsübergang $f(m, k) = f(m-1, k-1) + f(m-1, k) + 1$ ermöglicht In-Place-Updates, wenn das Array in absteigender Reihenfolge von $k$ durchlaufen wird (ähnlich der Optimierung beim 0/1-Rucksackproblem).
- Der benötigte zusätzliche Speicherplatz beträgt $O(k)$, um den Zustandsvektor zu verwalten.

Somit ergibt sich die gesamte Platzkomplexität zu:
$$S(n, k) = O(k)$$