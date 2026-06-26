# Formale mathematische Spezifikation: Smallest Window

## 1. Definitionen und Notation
Seien $S \in \Sigma^*$ und $P \in \Sigma^*$ zwei Strings der Längen $n$ und $m$.
Wir suchen Indizes $i^*, j^*$, sodass $1 \leq i^* \leq j^* \leq n$ gilt, die Multimenge der Zeichen in $P$ eine Teilmenge der Multimenge der Zeichen in $S[i^* \dots j^*]$ ist und die Länge $(j^* - i^* + 1)$ minimiert wird.

## 2. Formalisierung mittels Sliding Window
Es sei $H_P : \Sigma \to \mathbb{N}$ die Häufigkeitsabbildung von $P$.
Es sei $H_W : \Sigma \to \mathbb{N}$ die Häufigkeitsabbildung des aktuellen Fensters $S[L \dots R]$.
Ein Fenster ist gültig, wenn $\forall c \in \Sigma, H_W(c) \geq H_P(c)$ gilt.
Wir definieren die Defektfunktion $\mathcal{D}(H_W) = \sum_{c \in \Sigma} \max(0, H_P(c) - H_W(c))$.
Das Fenster ist genau dann gültig, wenn $\mathcal{D}(H_W) = 0$ gilt.

## 3. Zustandsübergänge des Algorithmus
Wir verwalten Pointer $L, R \in \{1 \dots n\}$, die bei 1 starten.
- **Expansion (Erhöhen von $R$)**: Füge $S[R]$ zu $H_W$ hinzu. Wenn $H_W(S[R]) \leq H_P(S[R])$, dekrementiere den Defekt.
- **Kontraktion (Erhöhen von $L$)**: Wenn $\mathcal{D}(H_W) = 0$, zeichne die Fenstergröße $(R - L + 1)$ auf. Entferne $S[L]$ aus $H_W$. Wenn $H_W(S[L]) < H_P(S[L])$, inkrementiere den Defekt.

## 4. Komplexitätsanalyse
- **Zeitkomplexität:** Die Pointer $L$ und $R$ durchlaufen den String $S$ jeweils genau einmal monoton. Folglich gibt es $O(n)$ Pointer-Aktualisierungen. Hash-Map-Aktualisierungen sind in $O(1)$. Die gesamte Zeitkomplexität ist strikt $O(n)$.
- **Platzkomplexität:** Der Algorithmus verwaltet Hash Maps, die Elemente aus $\Sigma$ auf ganze Zahlen abbilden. Die Platzkomplexität beträgt $O(|\Sigma|)$, was einen konstanten Overhead von $O(1)$ relativ zu $n$ darstellt.