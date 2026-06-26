# Formale mathematische Spezifikation: Anagramm-Äquivalenz

## 1. Definitionen und Notation
Sei $\Sigma$ ein endliches Alphabet. Seien $S, T \in \Sigma^*$ zwei Strings der Längen $n = |S|$ und $m = |T|$.
Ein String $S$ ist definiert als eine geordnete Sequenz von Zeichen $S = (s_1, s_2, \dots, s_n)$ mit $s_i \in \Sigma$.

Sei $\Pi_n$ die symmetrische Gruppe aller Permutationen auf $n$ Elementen.
Zwei Strings $S$ und $T$ sind genau dann als **Anagramme** definiert (geschrieben $S \sim T$), wenn:
1. $n = m$
2. $\exists \pi \in \Pi_n$, sodass $\forall i \in \{1, \dots, n\}, s_i = t_{\pi(i)}$

## 2. Algebraische Charakterisierung über Häufigkeitsvektoren
Für jeden String $S$ definieren wir seinen **Häufigkeitsvektor** $\mathbf{v}_S \in \mathbb{N}^{|\Sigma|}$ so, dass die dem Zeichen $c \in \Sigma$ entsprechende Komponente wie folgt definiert ist:
$$ \mathbf{v}_S(c) = \sum_{i=1}^n \mathbb{I}(s_i = c) $$
wobei $\mathbb{I}$ die Indikatorfunktion bezeichnet.

**Satz 1:** $S \sim T \iff \mathbf{v}_S = \mathbf{v}_T$

**Beweis:**
($\implies$) Angenommen, $S \sim T$. Dann gilt $|S| = |T| = n$ und es existiert eine Bijektion $\pi : \{1..n\} \to \{1..n\}$, sodass $s_i = t_{\pi(i)}$. Für jedes $c \in \Sigma$ ist die Anzahl der Vorkommen in $S$ genau die Anzahl der Indizes $i$, für die $s_i = c$ gilt. Da $\pi$ bijektiv ist, erhält die Abbildung $i \mapsto \pi(i)$ die Mächtigkeit der Indexmenge. Folglich gilt $\mathbf{v}_S(c) = \mathbf{v}_T(c)$.
($\impliedby$) Angenommen, $\mathbf{v}_S = \mathbf{v}_T$. Sei $n = \sum_{c \in \Sigma} \mathbf{v}_S(c)$. Da die Gesamtlänge identisch ist, gilt $|S| = |T| = n$. Da jedes Zeichen $c$ exakt gleich oft in $S$ und $T$ vorkommt, können wir eine Bijektion $\pi$ konstruieren, indem wir das $k$-te Vorkommen von $c$ in $S$ auf das $k$-te Vorkommen von $c$ in $T$ abbilden. Folglich gilt $S \sim T$. $\blacksquare$

## 3. Formalisierung des Algorithmus
Der optimale Algorithmus berechnet den Differenzvektor $\mathbf{\Delta} = \mathbf{v}_S - \mathbf{v}_T$.
Nach Satz 1 gilt $S \sim T \iff \mathbf{\Delta} = \mathbf{0}$.

Wir definieren den Zustand im Schritt $k$ (für $1 \leq k \leq n$) as $\mathbf{\Delta}^{(k)} \in \mathbb{Z}^{|\Sigma|}$ mit der Rekursionsgleichung:
$$ \mathbf{\Delta}^{(0)} = \mathbf{0} $$
$$ \mathbf{\Delta}^{(k)}(c) = \mathbf{\Delta}^{(k-1)}(c) + \mathbb{I}(s_k = c) - \mathbb{I}(t_k = c) $$

Der Algorithmus sichert zu, dass $\mathbf{\Delta}^{(n)} = \mathbf{0}$.

## 4. Komplexitätsanalyse
- **Zeitkomplexität:** Die Rekursionsgleichung wird $n$-mal ausgewertet. Jede Auswertung umfasst zwei $O(1)$-Operationen (Zugriff auf ein Vektorelement und Arithmetik). Die Überprüfung von $\mathbf{\Delta}^{(n)} = \mathbf{0}$ erfordert das Iterieren über $|\Sigma|$ Elemente. Folglich ist die Zeitkomplexität strikt durch $O(n + |\Sigma|)$ beschränkt.
- **Platzkomplexität:** Der Algorithmus verwaltet genau einen Zustandsvektor $\mathbf{\Delta}$ in $\mathbb{Z}^{|\Sigma|}$. Die Platzkomplexität beträgt exakt $O(|\Sigma|)$, was in Bezug auf $n$ gleich $O(1)$ ist.