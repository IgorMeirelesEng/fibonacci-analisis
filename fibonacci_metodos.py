"""
fibonacci_metodos.py
────────────────────
Análise de Algoritmos Recursivos — UEA/EST
Algoritmo: Fibonacci

Define as três implementações e as funções auxiliares de contagem.
Não depende de matplotlib — importe este módulo no seu notebook ou
em qualquer outro script.

Uso:
    from fibonacci_metodos import (
        fib_recursivo,
        fib_memoizacao,
        fib_iterativo,
        contar_operacoes_recursivo,
        contar_operacoes_memoizacao,
        medir_tempo,
    )
"""

import sys
import time

sys.setrecursionlimit(10_000)

PHI = (1 + 5 ** 0.5) / 2   # razão áurea ≈ 1.618


# ══════════════════════════════════════════════════════════
# 1. IMPLEMENTAÇÕES
# ══════════════════════════════════════════════════════════

def fib_recursivo(n: int) -> int:
    """
    Fibonacci Recursivo Ingênuo.

    Recorrência: T(n) = T(n-1) + T(n-2) + Θ(1)
    Forma fechada: C(n) = φⁿ⁺¹ − 1
    Classe: Θ(φⁿ) ≈ Θ(2ⁿ)

    Parâmetros
    ----------
    n : int
        Índice do termo desejado (n ≥ 0).

    Retorna
    -------
    int
        n-ésimo número de Fibonacci.
    """
    if n < 0:
        raise ValueError(f"n deve ser ≥ 0, recebido: {n}")
    if n <= 1:
        return n
    return fib_recursivo(n - 1) + fib_recursivo(n - 2)


def fib_memoizacao(n: int, memo: dict | None = None) -> int:
    """
    Fibonacci com Memoização (Top-Down DP).

    Cada subproblema é resolvido exatamente uma vez e armazenado
    no dicionário `memo`. Elimina as chamadas duplicadas do recursivo
    ingênuo sem eliminar a estrutura recursiva.

    Recorrência após memoização: C(n) = n − 1 somas
    Classe: Θ(n) tempo · Θ(n) espaço (cache + pilha)

    Parâmetros
    ----------
    n    : int
        Índice do termo desejado (n ≥ 0).
    memo : dict, opcional
        Cache compartilhado entre chamadas. Criado internamente
        se não fornecido.

    Retorna
    -------
    int
        n-ésimo número de Fibonacci.
    """
    if n < 0:
        raise ValueError(f"n deve ser ≥ 0, recebido: {n}")
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memoizacao(n - 1, memo) + fib_memoizacao(n - 2, memo)
    return memo[n]


def fib_iterativo(n: int) -> int:
    """
    Fibonacci Iterativo (Bottom-Up).

    Percorre de fib(0) até fib(n) mantendo apenas dois valores,
    eliminando completamente a pilha de recursão.

    Operações: exatamente n − 1 somas (uma por iteração).
    Classe: Θ(n) tempo · Θ(1) espaço

    Parâmetros
    ----------
    n : int
        Índice do termo desejado (n ≥ 0).

    Retorna
    -------
    int
        n-ésimo número de Fibonacci.
    """
    if n < 0:
        raise ValueError(f"n deve ser ≥ 0, recebido: {n}")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b   # ← operação básica Op (1 soma por iteração)
    return b


# ══════════════════════════════════════════════════════════
# 2. CONTAGEM DE OPERAÇÕES (analítica, sem executar recursão)
# ══════════════════════════════════════════════════════════

def contar_operacoes_recursivo(n: int) -> int:
    """
    Calcula C(n) — número de somas do recursivo ingênuo — via
    programação dinâmica bottom-up, sem disparar as chamadas reais.

    Segue a recorrência do Passo 4:
        C(n) = C(n-1) + C(n-2) + 1
        C(0) = C(1) = 0

    Parâmetros
    ----------
    n : int  (n ≥ 0)

    Retorna
    -------
    int
        Número exato de somas que fib_recursivo(n) realizaria.
    """
    if n <= 1:
        return 0
    cache = {0: 0, 1: 0}
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2] + 1
    return cache[n]


def contar_operacoes_memoizacao(n: int) -> int:
    """
    Calcula C(n) para a versão com memoização.

    Cada subproblema é resolvido uma única vez →
    exatamente n − 1 somas para n > 1.

    Parâmetros
    ----------
    n : int  (n ≥ 0)

    Retorna
    -------
    int
    """
    return max(0, n - 1)


def contar_operacoes_iterativo(n: int) -> int:
    """
    Calcula C(n) para a versão iterativa.

    O laço executa de 2 até n inclusive → n − 1 iterações,
    cada uma com exatamente 1 soma.

    Parâmetros
    ----------
    n : int  (n ≥ 0)

    Retorna
    -------
    int
    """
    return max(0, n - 1)


def forma_fechada(n: int) -> float:
    """
    Aproximação de C(n) pela forma fechada derivada via equação
    característica:

        C(n) ≈ φⁿ / √5    (Passo 5 do plano de análise)

    Parâmetros
    ----------
    n : int  (n ≥ 0)

    Retorna
    -------
    float
    """
    return PHI ** n / (5 ** 0.5)


# ══════════════════════════════════════════════════════════
# 3. MEDIÇÃO DE TEMPO
# ══════════════════════════════════════════════════════════

def medir_tempo(func, n_values: list[int], repeticoes: int = 5) -> list[float]:
    """
    Mede o tempo médio de execução de `func(n)` para cada n em
    `n_values`, repetindo `repeticoes` vezes para estabilizar.

    Parâmetros
    ----------
    func       : callable  — função a medir, assinatura f(n) -> int
    n_values   : list[int] — valores de n a testar
    repeticoes : int       — número de repetições por ponto

    Retorna
    -------
    list[float]
        Tempos médios em segundos, na mesma ordem de n_values.
    """
    tempos = []
    for n in n_values:
        total = 0.0
        for _ in range(repeticoes):
            inicio = time.perf_counter()
            func(n)
            total += time.perf_counter() - inicio
        tempos.append(total / repeticoes)
    return tempos


# ══════════════════════════════════════════════════════════
# 4. AUTO-TESTE (executa só quando chamado diretamente)
# ══════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 52)
    print("  Auto-teste: fibonacci_metodos.py")
    print("=" * 52)

    print(f"\n{'n':>4}  {'fib':>6}  {'C_rec':>7}  {'C_memo':>7}  {'C_iter':>7}  {'φⁿ/√5':>10}")
    print("-" * 52)

    for n in range(12):
        fib  = fib_iterativo(n)
        c_r  = contar_operacoes_recursivo(n)
        c_m  = contar_operacoes_memoizacao(n)
        c_i  = contar_operacoes_iterativo(n)
        phi_n = forma_fechada(n)

        # Verifica consistência entre as três implementações
        assert fib_recursivo(n) == fib_memoizacao(n) == fib, \
            f"Divergência em n={n}"
        assert c_m == c_i, f"C_memo ≠ C_iter em n={n}"

        print(f"{n:>4}  {fib:>6}  {c_r:>7}  {c_m:>7}  {c_i:>7}  {phi_n:>10.2f}")

    print("\n✓ Todos os testes passaram.")