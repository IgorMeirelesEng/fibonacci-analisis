# 📊 Fibonacci — Análise de Algoritmos Recursivos
### Disciplina: Análise de Algoritmos · UEA / EST · Apresentação em Dupla

---

## 📁 Arquivos do Projeto

| Arquivo | Descrição |
|---|---|
| `fibonacci_analise_v2.pptx` | Apresentação principal — 15 slides |
| `slide_iterativo.pptx` | Slide avulso da Abordagem 3 (Iterativo) |
| `fibonacci_metodos.py` | Implementações das 3 abordagens + funções de contagem |
| `fibonacci_graficos.py` | Geração dos 5 gráficos (depende de `fibonacci_metodos.py`) |
| `fig1_operacoes.png` | Gráfico: C(n) recursivo vs memoização vs φⁿ/√5 |
| `fig2_tempo.png` | Gráfico: tempo de execução real (escala linear + detalhe µs) |
| `fig3_arvore.png` | Árvore de chamadas fib(5) — subproblemas repetidos |
| `fig4_tabela.png` | Tabela de valores C(n) validando a forma fechada |
| `fig5_comparacao.png` | Comparação de desempenho (barras log + detalhe linear) |
| `README.md` | Este arquivo |

### Como rodar os gráficos

```bash
# Instalar dependências (se necessário)
pip install matplotlib numpy

# Coloque os dois arquivos na mesma pasta e execute:
python fibonacci_graficos.py
```

Os 5 PNGs são salvos na **mesma pasta** do script automaticamente.

---

## ⏱ Estrutura de Tempo da Apresentação

> Tempo total sugerido: **20 minutos** + arguição

| # | Slides | Conteúdo | Tempo |
|---|--------|----------|-------|
| 1 | 1 | Capa e contextualização | 1 min |
| 2 | 2 | Plano de análise — os 5 passos | 2 min |
| 3 | 3 | Passos 1 e 2 — medida n e operação básica | 2 min |
| 4 | 4 | Passo 3 — há melhor/pior caso? | 1 min |
| 5 | 5 | Passo 4 — relação de recorrência R(n) | 3 min |
| 6 | 6 | Passo 5a — por que substituições para trás falham | 2 min |
| 7 | 7 | Passo 5b — equação característica passo a passo | 3 min |
| 8 | 8 | Comparativo: Fatorial · Hanói · Fibonacci | 2 min |
| 9 | 9–13 | Gráficos e confirmação empírica | 2 min |
| 10 | 14–15 | Memoização, Iterativo e conclusões | 2 min |

---

## 🎤 Roteiro de Apresentação — Fala por Slide

---

### Slide 1 — Capa

> *"Hoje vamos apresentar a análise do algoritmo de Fibonacci recursivo, seguindo exatamente o plano de análise de ARs estudado em aula — os 5 passos. Fibonacci é um problema clássico que ilustra de forma perfeita por que a escolha de implementação importa: a diferença entre as abordagens vai de exponencial para linear."*

---

### Slide 2 — Plano de Análise de ARs (5 Passos)

> *"Este é o plano geral que o professor apresentou. Vamos aplicar cada um dos 5 passos ao Fibonacci. Começamos decidindo a medida do tamanho da entrada, depois identificamos a operação básica, verificamos se há casos diferentes, montamos a recorrência e finalmente encontramos a forma fechada com sua classe assintótica."*

---

### Slide 3 — Passos 1 e 2

**Passo 1 — Medida n:**
> *"A medida de tamanho é o índice n do termo desejado. Não é o valor de fib(n) — é o índice. fib(10) tem n = 10."*

**Passo 2 — Operação básica:**
> *"A operação básica é a soma: `fib(n-1) + fib(n-2)`. Por que soma e não a comparação `n <= 1`? Porque a comparação ocorre em todas as chamadas, inclusive nos casos base onde não há trabalho computacional útil. A soma só aparece nas chamadas não-base — ela representa o trabalho que cresce com n."*

---

### Slide 4 — Passo 3

> *"Passo 3: há melhor caso, pior caso ou caso médio? Não. Para qualquer entrada de valor n, o algoritmo executa sempre exatamente C(n) somas. Não existe um fib(10) mais fácil que outro fib(10) — o único parâmetro é n. Isso contrasta com, por exemplo, a busca linear, onde a posição do elemento muda o número de comparações. Portanto avançamos com análise única."*

---

### Slide 5 — Passo 4: Relação de Recorrência

> *"Passo 4 — a relação de recorrência. Cada chamada a fib(n) realiza duas chamadas menores: fib(n-1) com custo C(n-1), e fib(n-2) com custo C(n-2). E executa uma única soma, o +1. Chegamos a:*
> *C(n) = C(n-1) + C(n-2) + 1, com C(0) = C(1) = 0.*
> *A tabela à direita confirma isso numericamente: para n=5, C(5) = 7 somas, para n=10, C(10) = 88."*

---

### Slide 6 — Passo 5a: Por que substituições para trás falham

> *"No Fatorial, o professor resolveu por substituições para trás: C(n) = C(n-1)+1 vira uma cadeia linear — substituímos i vezes e chegamos a C(0)+n = n. Simples. Mas no Fibonacci isso não funciona diretamente. Na primeira substituição de C(n-1) surgem 3 termos. Na segunda, 5. Os termos dobram a cada passo — é impossível somar diretamente. Precisamos de outro método."*

---

### Slide 7 — Passo 5b: Equação Característica

> *"O método correto para recorrências lineares com dois termos é a equação característica. São 6 sub-passos:*
> *①  Separamos a parte homogênea: rⁿ = rⁿ⁻¹ + rⁿ⁻²*
> *②  Dividimos por rⁿ⁻², chegando a r² − r − 1 = 0*
> *③  As raízes são φ = (1+√5)/2 ≈ 1,618 e ψ ≈ −0,618 — a razão áurea!*
> *④  Solução geral: A·φⁿ + B·ψⁿ mais a solução particular (−1 para o +1 constante)*
> *⑤  Como |ψ| < 1, o termo B·ψⁿ vai a zero e não domina assintoticamente*
> *⑥  Resultado: C(n) = φⁿ⁺¹ − 1 ≈ φⁿ/√5 — classe Θ(φⁿ) ≈ Θ(2ⁿ)"*

---

### Slide 8 — Comparativo: Fatorial · Hanói · Fibonacci

> *"Para contextualizar, aqui estão os três exemplos do slide do professor lado a lado. O Fatorial tem uma chamada recursiva → Θ(n). O Hanói tem duas chamadas iguais → 2C(n-1)+1 → Θ(2ⁿ), resolvido por substituições para trás com soma geométrica. O Fibonacci tem duas chamadas distintas → equação característica → Θ(φⁿ). O padrão fica claro: 1 chamada = linear; 2 chamadas distintas = exponencial com base φ; 2 chamadas iguais = exponencial com base 2."*

---

### Slides 9–13 — Gráficos

> *"Os gráficos confirmam toda a análise teórica:*
> *— Gráfico 1: C(n) do recursivo sobe exponencialmente enquanto memoização sobe linearmente. A curva φⁿ/√5 coincide com C(n), validando a forma fechada do Passo 5.*
> *— Gráfico 2: o recursivo atinge 300ms em n=32. Memoização e iterativo são imperceptíveis até n=200.*
> *— Gráfico 3: a árvore de chamadas de fib(5) mostra visualmente os subproblemas duplicados.*
> *— Gráfico 4: tabela numérica confirmando C(n) ≈ ⌈φⁿ/√5⌉.*
> *— Gráfico 5: comparação de barras — em escala log todas as três aparecem; no detalhe linear vemos que iterativo é cerca de 4× mais rápido que memoização por não ter overhead de pilha."*

---

### Slides 14–15 — Memoização, Iterativo e Conclusões

> *"A memoização elimina os subproblemas sobrepostos armazenando cada resultado em um dicionário. De Θ(φⁿ) passamos para Θ(n) tempo — mas espaço continua Θ(n) porque ainda há pilha de recursão e ainda há cache.*
>
> *O iterativo vai além: sem recursão, sem pilha, apenas dois inteiros. Θ(n) tempo e Θ(1) espaço — a solução ótima na prática.*
>
> *Resumindo os 5 passos aplicados: n é o índice, Op é a soma, não há casos separados, R(n) = C(n-1)+C(n-2)+1, e C(n) = φⁿ⁺¹−1 ∈ Θ(φⁿ). O Fibonacci é o exemplo-texto de subproblemas sobrepostos e a motivação clássica para Programação Dinâmica."*

---

## ❓ Perguntas do Professor — Respostas Completas

> As questões estão agrupadas por tema. Leia as marcadas com 🔥 com prioridade — maior probabilidade de cair na arguição.

---

### Tema 1 — Plano de Análise (Passos 1–3)

---

#### Q1 🔥 Por que a operação básica é a soma e não a comparação `n <= 1`?

A comparação ocorre em **todas** as chamadas, inclusive nos casos base onde não há trabalho útil. Ela não representa o esforço computacional que cresce com n. A soma ocorre exatamente uma vez por chamada não-base — é a operação que captura o crescimento de C(n). Além disso, comparações são operações de custo unitário enquanto somas de inteiros grandes podem ter custo variável, tornando a soma ainda mais relevante como operação dominante.

---

#### Q2 🔥 Por que não há melhor caso, pior caso ou caso médio para o Fibonacci?

Dado o valor de n, o algoritmo executa sempre exatamente o mesmo conjunto de operações. A entrada é apenas um inteiro — não tem estrutura interna (como posição de elemento num array) que possa variar a execução. Isso contrasta com busca linear, onde a posição do elemento muda o número de comparações entre 1 (melhor) e n (pior). Para Fibonacci, Fatorial e Hanói: dado n, C(n) é único e determinístico.

---

#### Q3 Qual a diferença entre a recorrência do Fatorial e a do Fibonacci?

O Fatorial tem **uma chamada recursiva** → `C(n) = C(n-1) + 1` → cadeia linear → Θ(n). O Fibonacci tem **duas chamadas recursivas de tamanhos distintos** → `C(n) = C(n-1) + C(n-2) + 1` → árvore binária → Θ(φⁿ). Essa bifurcação é a causa direta do crescimento exponencial. Fatorial: n multiplicações. Fibonacci: ~φⁿ somas.

---

### Tema 2 — Recorrência e Forma Fechada (Passos 4–5)

---

#### Q4 🔥 Como montar corretamente a recorrência `C(n) = C(n-1) + C(n-2) + 1`?

Cada chamada a `fib(n)` realiza:
- `fib(n-1)` → custo `C(n-1)` somas
- `fib(n-2)` → custo `C(n-2)` somas
- `fib(n-1) + fib(n-2)` → **+1 soma** (a operação básica Op)

Somando: `C(n) = C(n-1) + C(n-2) + 1`. Casos base: `C(0) = C(1) = 0` pois `n <= 1` retorna sem fazer nenhuma soma.

---

#### Q5 🔥 Por que substituições para trás não resolvem diretamente a recorrência do Fibonacci?

No Fatorial, substituições para trás produzem uma **cadeia linear** de termos:
```
C(n) = C(n-1)+1 = C(n-2)+2 = ... = C(n-i)+i = C(0)+n = n
```

No Fibonacci, cada substituição **dobra** o número de termos recursivos:
```
C(n) = C(n-1) + C(n-2) + 1
     = [C(n-2)+C(n-3)+1] + C(n-2) + 1   → 3 termos recursivos
     = 2C(n-2) + C(n-3) + 2
     → na próxima: 5 termos → depois 8 → ...
```
Os termos crescem exponencialmente — impossível somar diretamente. Solução: **equação característica**.

---

#### Q6 🔥 Derive passo a passo a forma fechada pelo método da equação característica.

**①** Recorrência homogênea (ignora o +1): `rⁿ = rⁿ⁻¹ + rⁿ⁻²`

**②** Dividir por `rⁿ⁻²`: `r² = r + 1` → equação característica: `r² − r − 1 = 0`

**③** Fórmula de Bhaskara: `r = (1 ± √5) / 2`
- `r₁ = φ = (1+√5)/2 ≈ 1,618` (razão áurea)
- `r₂ = ψ = (1−√5)/2 ≈ −0,618`

**④** Solução geral da homogênea: `C_h(n) = A·φⁿ + B·ψⁿ`

**⑤** Solução particular para `+1` constante: tentativa `C_p = k` → `k = k+k+1` não funciona; tentativa `C_p = −1` → `−1 = −1+(−1)+1 = −1` ✓

**⑥** Solução completa: `C(n) = A·φⁿ + B·ψⁿ − 1`

**⑦** Condições iniciais `C(0)=0, C(1)=0` determinam A e B → resultado: `C(n) = φⁿ⁺¹ − 1`

**⑧** Como `|ψ| < 1`, o termo `B·ψⁿ → 0` — a exponencial dominante é `φⁿ`:

**→ `C(n) ∈ Θ(φⁿ) ≈ Θ(2ⁿ)`**

---

#### Q7 Qual a relação entre C(n) e a própria sequência de Fibonacci?

A recorrência `C(n) = C(n-1) + C(n-2) + 1` tem a mesma estrutura de `fib(n) = fib(n-1) + fib(n-2)`, por isso `C(n) = fib(n+1) − 1` exatamente. Isso confirma que o número de somas cresce como os próprios termos de Fibonacci — que por sua vez crescem como φⁿ.

---

### Tema 3 — Comparativo com Fatorial e Hanói

---

#### Q8 🔥 Compare estruturalmente Fatorial, Hanói e Fibonacci — recorrência, método e resultado.

| Algoritmo | Recorrência | Chamadas | Método | Forma Fechada | Classe |
|-----------|-------------|----------|--------|---------------|--------|
| Fatorial | `C(n) = C(n-1) + 1` | 1 | Substituições para trás | `C(n) = n` | Θ(n) |
| Hanói | `C(n) = 2C(n-1) + 1` | 2 iguais | Subst. + soma geométrica | `C(n) = 2ⁿ−1` | Θ(2ⁿ) |
| Fibonacci | `C(n) = C(n-1)+C(n-2)+1` | 2 distintas | Equação característica | `C(n) = φⁿ⁺¹−1` | Θ(φⁿ) |

Regra geral: **1 chamada → linear; 2 iguais → base 2; 2 distintas → base φ ≈ 1,618**.

---

#### Q9 Hanói e Fibonacci têm ambos dois termos recursivos. Por que Hanói resolve por substituições para trás e Fibonacci não?

Em Hanói os dois termos são **idênticos** (`C(n-1) + C(n-1) = 2C(n-1)`), permitindo fatoração imediata:
```
C(n) = 2C(n-1)+1 = 2[2C(n-2)+1]+1 = 2²C(n-2)+2+1 = ... = 2ⁿC(0) + 2ⁿ−1 = 2ⁿ−1
```
A progressão geométrica `1+2+4+...+2ⁿ⁻¹` tem fórmula fechada direta. Em Fibonacci os dois termos têm **índices diferentes** (`n-1` e `n-2`), impedindo a fatoração — a cada substituição surgem dois termos novos de tamanhos diferentes, crescendo exponencialmente.

---

#### Q10 O professor mostrou que Hanói com n=3 exige exatamente 7 movimentos. Verifique.

`C(3) = 2·C(2) + 1 = 2·(2·C(1)+1) + 1 = 2·(2·1+1) + 1 = 2·3 + 1 = 7 = 2³−1` ✓

Sequência de movimentos: (1) disco 1: ORI→AUX; (2) disco 2: ORI→DEST; (3) disco 1: AUX→DEST; (4) disco 3: ORI→AUX; (5) disco 1: DEST→ORI; (6) disco 2: DEST→AUX; (7) disco 1: ORI→AUX — total: 7. A solução é ótima pois mover o disco maior exige obrigatoriamente que todos os n−1 menores estejam no pino auxiliar — pelo menos `2C(n-1)+1` movimentos, que é o próprio limite inferior.

---

#### Q11 No NumDigBin (Exemplo 3 do slide), qual a recorrência e a forma fechada?

`C(n) = C(⌊n/2⌋) + 1`, `C(1) = 0`. A cada chamada n é dividido por 2, então o número de chamadas é o número de vezes que se pode dividir n por 2 até chegar a 1: **`C(n) = ⌊log₂ n⌋ ∈ Θ(log n)`**. Isso ilustra a regra: *dividir por constante b a cada chamada → Θ(log n)*.

---

### Tema 4 — Memoização e Iterativo

---

#### Q12 🔥 Por que a memoização não reduz a classe assintótica de espaço?

Ambos — recursivo ingênuo e memoização — usam **Θ(n) espaço**, mas pelas motivos diferentes:
- **Recursivo ingênuo**: pilha de recursão de profundidade n (caminho `n → n-1 → ... → 0`)
- **Memoização**: dicionário de tamanho n + pilha de profundidade n

A memoização reduz o *número total de chamadas* de Θ(φⁿ) para Θ(n), mas não elimina a pilha de recursão. O iterativo resolve isso: nenhuma pilha, apenas dois inteiros — Θ(1) espaço.

---

#### Q13 Memoização e Programação Dinâmica são a mesma coisa?

São relacionadas mas não idênticas. **Memoização** é PD *top-down*: começa pelo problema grande, desce recursivamente, armazena resultados conforme sobe. **PD Bottom-Up** (iterativo) resolve subproblemas menores primeiro, sem recursão. Ambas têm Θ(n) para Fibonacci e ambas exploram *subproblemas sobrepostos*. A diferença prática: memoização tem overhead de pilha de recursão e de hash do dicionário; o iterativo tem overhead zero de pilha.

---

#### Q14 Por que a Fórmula de Binet (forma fechada direta) não é prática para n grande, mesmo sendo O(1)?

`fib(n) = (φⁿ − ψⁿ) / √5`. O problema: `φⁿ` para n grande tem centenas de dígitos — ponto flutuante `float64` tem apenas ~15 dígitos significativos. Para `n > 70` o erro de arredondamento já corrompe o resultado. Usar `Decimal` de precisão arbitrária resolveria a precisão, mas o custo de calcular `φⁿ` com precisão suficiente passa a ser Θ(n) ou Θ(log n · M(n)) onde M(n) é o custo de multiplicar números grandes — não há ganho real sobre o iterativo.

---

#### Q15 Existe Fibonacci com complexidade menor que Θ(n)?

**Sim.** Exponenciação de matrizes resolve em **Θ(log n)**:

```
[fib(n+1)]   [1 1]ⁿ   [1]
[fib(n)  ] = [1 0]  · [0]
```

Usando *exponentiation by squaring*, a n-ésima potência de uma matriz 2×2 é computada em `⌊log₂ n⌋` multiplicações de matrizes — cada uma O(1) — totalizando **Θ(log n)**. É a solução assintoticamente ótima para Fibonacci exato com inteiros.

---

### Tema 5 — Perguntas Conceituais e Pegadinhas

---

#### Q16 Por que aumentar `sys.setrecursionlimit` não resolve o problema do recursivo ingênuo para n grande?

`setrecursionlimit` evita o `RecursionError`, mas não muda a complexidade Θ(φⁿ). A *profundidade* da pilha é Θ(n) — razoável — mas o *número total de chamadas* é Θ(φⁿ). Para `fib(50)`: ~2²⁵ ≈ 33 milhões de chamadas. Para `fib(100)`: ~2⁵⁰ ≈ 10¹⁵ chamadas — inviável independentemente de qualquer configuração de Python.

---

#### Q17 Fibonacci exibe "subestrutura ótima"? Isso é necessário para PD?

Fibonacci exibe *subestrutura* (solução de `fib(n)` depende de `fib(n-1)` e `fib(n-2)`), mas **não é um problema de otimização** — não há escolha a fazer, apenas cálculo. *Subestrutura ótima* no sentido clássico de PD aplica-se a problemas de otimização (menor caminho, mochila). Para Fibonacci, a propriedade relevante é apenas **subproblemas sobrepostos** (*overlapping subproblems*) — os mesmos subproblemas são recomputados repetidamente no recursivo ingênuo.

---

#### Q18 Por que a memoização é chamada de "top-down" e o iterativo de "bottom-up"?

**Top-down (memoização)**: começa do problema maior (`fib(n)`) e desce recursivamente até os casos base, armazenando resultados no caminho de volta. Resolve subproblemas *conforme são requisitados*.

**Bottom-up (iterativo)**: começa dos casos base (`fib(0)=0, fib(1)=1`) e constrói a solução subindo até `fib(n)`, sem recursão. Resolve subproblemas *em ordem crescente*, garantindo que cada subproblema está resolvido antes de ser necessário.

---

#### Q19 O número de chamadas do recursivo ingênuo é `2·fib(n+1) − 1`. Como verificar?

Definindo `K(n)` = número de chamadas (incluindo casos base):
- `K(0) = K(1) = 1` (casos base: 1 chamada cada)
- `K(n) = K(n-1) + K(n-2) + 1` para n ≥ 2

Isso resolve para `K(n) = 2·fib(n+1) − 1`. Para n=5: `K(5) = 2·fib(6) − 1 = 2·8 − 1 = 15` chamadas, das quais `C(5) = 7` são somas (apenas as não-base). Verificação: `K(n) = C(n) + (fib(n+1))` — o número de casos base atingidos é `fib(n+1)`.

---

#### Q20 Como instrumentar o código para contar as operações empiricamente e comparar com C(n) teórico?

```python
def fib_contado(n):
    contador = [0]
    def _fib(n):
        if n <= 1:
            return n
        contador[0] += 1   # conta a soma antes de fazê-la
        return _fib(n-1) + _fib(n-2)
    resultado = _fib(n)
    return resultado, contador[0]

# Verificação
for n in range(11):
    val, ops = fib_contado(n)
    teorico = contar_operacoes_recursivo(n)
    assert ops == teorico, f"Divergência em n={n}"
    print(f"fib({n}) = {val:3d}  |  ops empírico = {ops:3d}  |  C(n) teórico = {teorico:3d}")
```

---

## 📐 Referência Rápida — Fórmulas

```
Recorrência:    C(n) = C(n-1) + C(n-2) + 1,  C(0) = C(1) = 0

Forma fechada:  C(n) = φⁿ⁺¹ - 1  ≈  φⁿ / √5

Razão áurea:    φ = (1 + √5) / 2  ≈   1,6180339...

Classe:         C(n) ∈ Θ(φⁿ)  ≈  Θ(2ⁿ)

Equação
característica: r² - r - 1 = 0
                r₁ = φ ≈ 1,618   r₂ = ψ ≈ -0,618

Comparativo:
  Fatorial  →  C(n) = n          ∈  Θ(n)
  Hanói     →  C(n) = 2ⁿ - 1    ∈  Θ(2ⁿ)
  Fibonacci →  C(n) = φⁿ⁺¹ - 1  ∈  Θ(φⁿ)

Abordagens:
  Recursivo ingênuo  →  Θ(φⁿ) tempo  ·  Θ(n) espaço
  Memoização         →  Θ(n)  tempo  ·  Θ(n) espaço
  Iterativo          →  Θ(n)  tempo  ·  Θ(1) espaço  ← ótimo
```