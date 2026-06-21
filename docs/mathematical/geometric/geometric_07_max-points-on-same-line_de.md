# Formale mathematische Spezifikation: Max Points on a Line

## 1. Definitionen und Notation

Sei $P = \{p_1, p_2, \dots, p_n\}$ eine Menge von $n$ verschiedenen Punkten in der euklidischen Ebene $\mathbb{R}^2$, wobei jeder Punkt $p_i$ durch das Koordinatenpaar $(x_i, y_i) \in \mathbb{Z}^2$ repräsentiert wird.

*   **Kollinearität:** Eine Teilmenge von Punkten $S \subseteq P$ ist kollinear, wenn eine Gerade $L \subset \mathbb{R}^2$ existiert, sodass $S \subseteq L$.
*   **Steigungsrepräsentation:** Für zwei beliebige verschiedene Punkte $p_i, p_j \in P$ ist die Steigung $m_{ij}$ durch den Vektor $\vec{v} = (x_j - x_i, y_j - y_i) = (\Delta x, \Delta y)$ definiert. Um eine Fließkommadarstellung zu vermeiden, definieren wir die kanonische Steigung als den gekürzten Bruch:
    $$\sigma(p_i, p_j) = \left( \frac{\Delta y}{g}, \frac{\Delta x}{g} \right) \quad \text{wobei } g = \gcd(|\Delta x|, |\Delta y|)$$
    Um eine eindeutige Repräsentation für eine Gerade zu gewährleisten, erzwingen wir eine Vorzeichenkonvention: Wenn $\Delta x < 0$, negieren wir beide Komponenten; wenn $\Delta x = 0$, setzen wir die Steigung auf $(1, 0)$ (vertikal).
*   **Zielsetzung:** Bestimmung der Kardinalität der größten Teilmenge $S \subseteq P$, sodass alle $p \in S$ kollinear sind. Sei $\mathcal{L}$ die Menge aller Geraden, die durch mindestens zwei Punkte in $P$ verlaufen. Wir suchen:
    $$\max_{L \in \mathcal{L}} |\{p \in P : p \in L\}|$$

## 2. Algebraische Charakterisierung

Für einen festen Ankerpunkt $p_i \in P$ sei $S_i$ die Menge aller Geraden, die durch $p_i$ und mindestens einen weiteren Punkt $p_j \in P \setminus \{p_i\}$ verlaufen. Wir definieren eine Abbildung $f_i: P \setminus \{p_i\} \to \mathbb{Z}^2$, sodass $f_i(p_j) = \sigma(p_i, p_j)$.

Die Anzahl der Punkte, die mit $p_i$ entlang einer spezifischen Steigung $\vec{s} \in \mathbb{Z}^2$ kollinear sind, ist gegeben durch:
$$N(p_i, \vec{s}) = 1 + \sum_{j \neq i, p_j \neq p_i} \mathbb{I}(f_i(p_j) = \vec{s})$$
wobei $\mathbb{I}(\cdot)$ die Indikatorfunktion ist. Unter Einbeziehung von Punkten, die mit $p_i$ zusammenfallen (Duplikate), sei $D_i = \{p_j \in P : p_j = p_i, j \neq i\}$. Die Gesamtzahl der Punkte auf einer Geraden, die durch $p_i$ mit der Steigung $\vec{s}$ verläuft, ist:
$$C(p_i, \vec{s}) = |D_i| + 1 + \sum_{j \neq i, p_j \neq p_i} \mathbb{I}(f_i(p_j) = \vec{s})$$

Der Algorithmus berechnet das globale Maximum:
$$\text{Result} = \max_{p_i \in P} \left( \max_{\vec{s} \in \text{Im}(f_i)} C(p_i, \vec{s}) \right)$$

**Schleifeninvariante:** Zu Beginn jeder Iteration $i$ der äußeren Schleife speichert die Variable `best` den Wert $\max_{k < i} (\text{max. kollineare Punkte durch } p_k)$. Innerhalb der inneren Schleife $j$ verwaltet die Hash Map `slopes` die Häufigkeitsverteilung der kanonischen Steigungen $\sigma(p_i, p_j)$, wodurch sichergestellt wird, dass alle Punkte $p_j$, die dieselbe Steigung relativ zu $p_i$ aufweisen, korrekt aggregiert werden.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus einer verschachtelten Schleifenstruktur. Die äußere Schleife iteriert $n$-mal. Die innere Schleife iteriert $n-1$-mal.
1.  **GCD-Berechnung:** Der euklidische Algorithmus für $\gcd(\Delta x, \Delta y)$ benötigt $O(\log(\min(|\Delta x|, |\Delta y|)))$ Zeit. Sei $M$ der maximale Koordinatenwert, sodass $\log M$ die GCD-Operation begrenzt.
2.  **Hash Map Operationen:** Einfügen und Nachschlagen in der Hash Map erfolgen im Durchschnitt in $O(1)$.
3.  **Gesamtaufwand:** Die gesamte Zeitkomplexität beträgt:
    $$T(n) = \sum_{i=1}^{n} \sum_{j=1, j \neq i}^{n} O(\log M) = O(n^2 \log M)$$
Da $\log M$ bei Festkommaarithmetik typischerweise als Konstante betrachtet wird, beträgt die Komplexität $O(n^2)$.

### Platzkomplexität
Die Platzkomplexität wird durch die Speicherung der Hash Map für jeden Ankerpunkt $p_i$ dominiert.
1.  **Hilfsspeicher:** Für ein festes $i$ speichert die Hash Map höchstens $n-1$ verschiedene Steigungen. Somit beträgt der benötigte Speicher $O(n)$.
2.  **Gesamtspeicher:** Da die Hash Map für jedes $i$ neu initialisiert wird, beträgt die maximale zusätzliche Platzkomplexität $O(n)$. Der Speicher für die Eingabe beträgt $O(n)$, was zu einer gesamten Platzkomplexität von $O(n)$ führt.