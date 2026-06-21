# Formale mathematische Spezifikation: Inversionen zählen (mittels BIT)

## 1. Definitionen und Notation

Sei $A = [a_1, a_2, \dots, a_n]$ eine Sequenz von $n$ Ganzzahlen.

**Definition 1 (Inversion):** Eine Inversion in $A$ ist ein Paar von Indizes $(i, j)$, sodass $1 \le i < j \le n$ und $a_i > a_j$ gilt. Die Menge aller Inversionen wird als $\mathcal{I} = \{ (i, j) \in \mathbb{Z}^2 \mid 1 \le i < j \le n, a_i > a_j \}$ bezeichnet. Das Ziel ist die Berechnung der Kardinalität $|\mathcal{I}|$.

**Definition 2 (Koordinatenkompression):** Sei $U = \{u_1, u_2, \dots, u_m\}$ die Menge der eindeutigen Elemente in $A$, sortiert sodass $u_1 < u_2 < \dots < u_m$, wobei $m \le n$. Wir definieren eine Rangfunktion $\rho: A \to \{1, 2, \dots, m\}$, sodass $\rho(a_i) = k$ gilt, falls $a_i = u_k$. Die transformierte Sequenz ist $A' = [\rho(a_1), \rho(a_2), \dots, \rho(a_n)]$.

**Definition 3 (Fenwick Tree):** Ein Fenwick Tree (Binary Indexed Tree) ist eine Datenstruktur, die durch ein Array $B$ der Größe $m+1$ repräsentiert wird und zwei Operationen unterstützt:
1. $\text{Update}(k, \delta)$: $B[j] \leftarrow B[j] + \delta$ für alle $j$, sodass $j$ ein Vorfahre von $k$ in der BIT-Struktur ist.
2. $\text{Query}(k)$: $\sum_{j=1}^k B[j]$, was die Präfixsumme der Häufigkeiten zurückgibt.

## 2. Algebraische Charakterisierung

Die Gesamtzahl der Inversionen kann als die Summe der Inversionen ausgedrückt werden, die durch jedes Element $a_j$ beim Durchlaufen des Arrays beigetragen werden:
$$|\mathcal{I}| = \sum_{j=1}^n |\{ i < j \mid a_i > a_j \}|$$

Durch Iteration von $j = n$ abwärts bis $1$ pflegen wir eine Häufigkeitsverteilung der bereits verarbeiteten Elemente. Sei $S_j$ die Menge der Elemente $\{a_{j+1}, \dots, a_n\}$. Für ein festes $j$ ist die Anzahl der Inversionen, die $a_j$ betreffen, die Anzahl der Elemente in $S_j$, die strikt kleiner als $a_j$ sind:
$$|\mathcal{I}_j| = \sum_{x \in S_j} \mathbb{I}(x < a_j)$$
wobei $\mathbb{I}(\cdot)$ die Indikatorfunktion ist. Unter Verwendung der Rangfunktion $\rho$ ergibt sich:
$$|\mathcal{I}_j| = \text{Query}(\rho(a_j) - 1)$$

**Schleifeninvariante:** Zu Beginn der Iteration $j$ (wobei $j$ von $n$ abwärts bis $1$ läuft) speichert der Fenwick Tree $B$ die Häufigkeitsverteilung der Menge $\{ \rho(a_{j+1}), \dots, \rho(a_n) \}$. Speziell gilt für jedes $k \in \{1, \dots, m\}$, dass die Präfixsumme $\text{Query}(k)$ den Wert $|\{ i > j \mid \rho(a_i) \le k \}|$ zurückgibt.

Die gesamte Inversionsanzahl ist die Akkumulation dieser Queries:
$$|\mathcal{I}| = \sum_{j=1}^n \text{Query}(\rho(a_j) - 1)$$
gefolgt von dem Update $\text{Update}(\rho(a_j), 1)$ in jedem Schritt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus zwei primären Phasen:
1. **Koordinatenkompression:** Das Sortieren der eindeutigen Elemente von $A$ benötigt $O(n \log n)$. Das Abbilden der Elemente auf Ränge mittels einer Hash Map oder binärer Suche benötigt $O(n \log n)$.
2. **BIT-Operationen:** Der Algorithmus führt $n$ Iterationen durch. In jeder Iteration werden eine `Query`- und eine `Update`-Operation ausgeführt. Beide Operationen durchlaufen die Höhe des BIT, welche $\lceil \log_2 m \rceil$ beträgt. Da $m \le n$ gilt, ist jede Operation $O(\log n)$.

Die gesamte Zeitkomplexität beträgt:
$$T(n) = O(n \log n) + \sum_{j=1}^n O(\log n) = O(n \log n)$$

### Platzkomplexität
1. **Koordinatenkompression:** Das Speichern der eindeutigen Elemente und der Rangabbildung erfordert $O(n)$ Platz.
2. **Fenwick Tree:** Das BIT-Array $B$ erfordert $O(m)$ Platz, wobei $m \le n$.
3. **Eingabespeicherung:** Das komprimierte Array $A'$ erfordert $O(n)$ Platz.

Die gesamte Platzkomplexität beträgt:
$$S(n) = O(n) + O(m) + O(n) = O(n)$$