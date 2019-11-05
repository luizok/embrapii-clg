# Desafio Embrapii

## Carta 1

![carta.jpeg](./cartas/1/carta.jpeg "Carta 1")

### Dimensão

480 x 480

### Distribuição de Cores

![bar_color.png](./cartas/1/bar_color.png "dist_color 1")

### Filtros Úteis

![blur_threshold.png](./cartas/1/blur_threshold.png "blur_thresh 1")
![canny_edge.png](./cartas/1/canny_edge.png "canny_edge 1")

### Outras observações

- Cartas em sequência de 2 a 6, inclusive
- 3 naipes diferentes

---

## Carta 2

![carta.jpeg](./cartas/2/carta.jpeg "Carta 2")

### Dimensão

480 x 480

### Distribuição de Cores

![bar_color.png](./cartas/2/bar_color.png "dist_color 2")

### Filtros Úteis

![blur_threshold.png](./cartas/2/blur_threshold.png "blur_thresh 2")
![canny_edge.png](./cartas/2/canny_edge.png "canny_edge 2")

### Outras observações

- Cartas em sequência crescente de A a 6, inclusive
- As cartas são dividas igualmente entre 2 naipes
- 2 naipes diferentes com cores diferentes
- Os naipes são semelhantes se espelhados no eixo x

---

## Carta 3

![carta.jpeg](./cartas/3/carta.jpeg "Carta 3")

### Dimensão

480 x 480

### Distribuição de Cores

![bar_color.png](./cartas/3/bar_color.png "dist_color 3")

### Filtros Úteis

![blur_threshold.png](./cartas/3/blur_threshold.png "blur_thresh 3")
![canny_edge.png](./cartas/3/canny_edge.png "canny_edge 3")

### Outras observações

- Cartas em sequência crescente de 10 a A, inclusive
- Todas do mesmo naipe
- Somente as 2 das pontas não possuem uma imagem (desenho)
- Somente as 3 cartas do meio possuem a cor amarela

---

## Carta 4

![carta.jpeg](./cartas/4/carta.jpeg "Carta 4")

### Dimensão

480 x 480

### Distribuição de Cores

![bar_color.png](./cartas/4/bar_color.png "dist_color 4")

### Filtros Úteis

![blur_threshold.png](./cartas/4/blur_threshold.png "blur_thresh 4")
![canny_edge.png](./cartas/4/canny_edge.png "canny_edge 4")

### Outras observações

- 4 conjunto de cartas, cada um com um naipe específico
- Cores distribuídas em forma de X
- NAIPE PAUS
    - Cartas em sequência decrescente de 9 a 6, inclusive
    - 4 cartas
- NAIPE OUROS
    - Cartas em sequência decrescente de 5 a A, inclusive
    - 5 cartas
- NAIPE COPAS
    - Cartas em sequência decrescente de J a 6, inclusive
    - 6 cartas
- NAIPE ESPADAS
    - 4 cartas
    - diferença entre o valor das cartas 2 a 2 é 1
        (2 - A) = (10 - 9) = 1
- As cartas de OUROS podem ser concatenadas tanto com as de PAUS 
    quanto as de COPAS formando sequências maiores
    - OUROS U PAUS = [9, 8, ..., 2, A]
    - OUROS U COPAS = [J, 10, ..., 2, A]

---

## Carta 5

![carta.jpeg](./cartas/5/carta.jpeg "Carta 5")

### Dimensão

480 x 480

### Distribuição de Cores

![bar_color.png](./cartas/5/bar_color.png "dist_color 5")

### Filtros Úteis

![blur_threshold.png](./cartas/5/blur_threshold.png "blur_thresh 5")
![canny_edge.png](./cartas/5/canny_edge.png "canny_edge 5")

## Comentários

- Os filtros aplicados não foram utilizados de qualquer maneira significativa
    pois implementação de algoritmos levariam algum tempo. Utilizando os mesmos
    poderia ser possível identificar por exemplo a quantidade de cartas de um
    determinado naipe, assim como as cartas de forma individual.
- Os filtros utilizados foram blur + threshold e detecção de bordas (canny)
- A barra de cores frequentes apresenta as 7 cores mais frequentes
- Tive dificuldade em reconhecer algum padrão ou em extrair alguma informação
    na 5 (o filtro de bordas não seria de muita ajuda nesse caso específico).
