"""
fibonacci_graficos.py
─────────────────────
Análise de Algoritmos Recursivos — UEA/EST
Algoritmo: Fibonacci

Gera e salva os 5 gráficos da análise.
Depende de: fibonacci_metodos.py (deve estar na mesma pasta)

Uso:
    python fibonacci_graficos.py

Os arquivos PNG são salvos na mesma pasta do script.
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── Importa os métodos do módulo separado ──────────────────
from fibonacci_metodos import (
    fib_recursivo,
    fib_memoizacao,
    fib_iterativo,
    contar_operacoes_recursivo,
    contar_operacoes_memoizacao,
    contar_operacoes_iterativo,
    forma_fechada,
    medir_tempo,
    PHI,
)

# ══════════════════════════════════════════════════════════
# CONFIGURAÇÃO GLOBAL
# ══════════════════════════════════════════════════════════

# Os PNGs são salvos na mesma pasta deste script
PASTA_SAIDA = os.path.dirname(os.path.abspath(__file__))

CORES = {
    "rec":  "#E63946",   # vermelho  — recursivo ingênuo
    "memo": "#2A9D8F",   # teal      — memoização
    "iter": "#264653",   # azul esc. — iterativo
    "phi":  "#F4A261",   # laranja   — curva φⁿ/√5
    "bg":   "#FAFAFA",   # fundo dos gráficos
}

plt.rcParams.update({
    "font.family":     "DejaVu Sans",
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.grid":         True,
    "grid.color":        "#CCCCCC",
    "grid.linestyle":    "--",
    "grid.linewidth":    0.6,
})


def _salvar(fig: plt.Figure, nome: str) -> None:
    caminho = os.path.join(PASTA_SAIDA, nome)
    fig.savefig(caminho, dpi=150, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  ✓  {nome}  →  {caminho}")


# ══════════════════════════════════════════════════════════
# GRÁFICO 1 — Número de operações C(n): recursivo vs memoização
# ══════════════════════════════════════════════════════════

def grafico_operacoes(n_max: int = 20) -> None:
    """
    Plota C(n) do recursivo ingênuo e da memoização lado a lado,
    com a curva φⁿ/√5 para validar a forma fechada (Passo 5).
    """
    ns        = list(range(0, n_max + 1))
    ops_rec   = [contar_operacoes_recursivo(n)  for n in ns]
    ops_memo  = [contar_operacoes_memoizacao(n) for n in ns]
    phi_curve = [forma_fechada(n)               for n in ns]

    fig, ax = plt.subplots(figsize=(9, 5))
    fig.patch.set_facecolor(CORES["bg"])
    ax.set_facecolor(CORES["bg"])

    ax.plot(ns, ops_rec,   color=CORES["rec"],  lw=2.5, marker="o", ms=5,
            label="Recursivo ingênuo  —  Θ(φⁿ)")
    ax.plot(ns, ops_memo,  color=CORES["memo"], lw=2.5, marker="s", ms=5,
            label="Memoização  —  Θ(n)")
    ax.plot(ns, phi_curve, color=CORES["phi"],  lw=1.5, ls="--",
            label="φⁿ/√5  (forma fechada)")

    ax.set_xlabel("n  (índice Fibonacci)", fontsize=12)
    ax.set_ylabel("C(n)  —  número de somas", fontsize=12)
    ax.set_title("Gráfico 1 — Operações: Recursivo vs Memoização\n"
                 "Passo 5: confirmação empírica de C(n) ≈ φⁿ/√5",
                 fontsize=12, fontweight="bold")
    ax.legend(fontsize=10)

    _salvar(fig, "fig1_operacoes.png")


# ══════════════════════════════════════════════════════════
# GRÁFICO 2 — Tempo de execução real
# ══════════════════════════════════════════════════════════

def grafico_tempo_execucao(n_max_rec: int = 32,
                           n_max_fast: int = 200,
                           repeticoes: int = 5) -> None:
    """
    Dois subgráficos:
    - Esquerda: recursivo ingênuo em escala linear (curva sobe visivelmente).
    - Direita:  memoização vs iterativo em µs (ambos lineares, quase planos).
    """
    ns_rec  = list(range(0, n_max_rec  + 1))
    ns_fast = list(range(0, n_max_fast + 1))

    print("  Medindo recursivo ingênuo…")
    t_rec  = medir_tempo(fib_recursivo,  ns_rec,  repeticoes)
    print("  Medindo memoização…")
    t_memo = medir_tempo(fib_memoizacao, ns_fast, repeticoes)
    print("  Medindo iterativo…")
    t_iter = medir_tempo(fib_iterativo,  ns_fast, repeticoes)

    fig, (ax_esq, ax_dir) = plt.subplots(1, 2, figsize=(13, 5))
    fig.patch.set_facecolor(CORES["bg"])

    for ax in (ax_esq, ax_dir):
        ax.set_facecolor(CORES["bg"])

    # Esquerda — escala LINEAR: curva exponencial sobe visualmente
    # (em escala log ficaria reta, o que parece linear para quem olha)
    t_rec_ms = [t * 1000 for t in t_rec]
    ax_esq.plot(ns_rec, t_rec_ms,
                color=CORES["rec"], lw=2.5, marker="o", ms=4)
    ax_esq.fill_between(ns_rec, t_rec_ms, alpha=0.15, color=CORES["rec"])
    ax_esq.set_title("Recursivo Ingênuo (escala linear)\nΘ(φⁿ) — curva explode exponencialmente",
                     fontsize=11, fontweight="bold")
    ax_esq.set_xlabel("n")
    ax_esq.set_ylabel("Tempo médio (ms)")

    # Direita — µs, com ylim no percentil 98 para cortar spikes de ruído do SO
    memo_us = [t * 1e6 for t in t_memo]
    iter_us = [t * 1e6 for t in t_iter]
    teto = float(np.percentile(memo_us + iter_us, 98)) * 1.15

    ax_dir.plot(ns_fast, memo_us,
                color=CORES["memo"], lw=2, label="Memoização  Θ(n)")
    ax_dir.plot(ns_fast, iter_us,
                color=CORES["iter"], lw=2, ls="--", label="Iterativo  Θ(n)")
    ax_dir.set_ylim(bottom=0, top=teto)
    ax_dir.set_title("Memoização vs Iterativo\nΘ(n) — crescimento linear",
                     fontsize=11, fontweight="bold")
    ax_dir.set_xlabel("n")
    ax_dir.set_ylabel("Tempo médio (µs)")
    ax_dir.legend(fontsize=10)

    fig.suptitle("Gráfico 2 — Tempo de Execução Real",
                 fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()

    _salvar(fig, "fig2_tempo.png")


# ══════════════════════════════════════════════════════════
# GRÁFICO 3 — Árvore de chamadas de fib(5)
# ══════════════════════════════════════════════════════════

def grafico_arvore_chamadas() -> None:
    """
    Visualiza a árvore de chamadas de fib(5) mostrando
    quais nós são calculados mais de uma vez (★).
    """
    fig, ax = plt.subplots(figsize=(11, 5.5))
    fig.patch.set_facecolor(CORES["bg"])
    ax.set_facecolor(CORES["bg"])
    ax.axis("off")

    # (x, y) de cada nó na figura
    pos = {
        "fib5":  (5.0, 4.3),
        "fib4":  (2.8, 3.3),
        "fib3a": (7.2, 3.3),   # duplicado
        "fib3b": (1.3, 2.3),   # duplicado
        "fib2a": (4.3, 2.3),   # duplicado
        "fib2b": (6.3, 2.3),   # duplicado
        "fib2c": (8.1, 2.3),   # duplicado
        "fib1a": (0.6, 1.3),   # base
        "fib2d": (2.0, 1.3),   # duplicado
        "fib1b": (3.6, 1.3),   # base
        "fib1c": (5.0, 1.3),   # base
        "fib0a": (1.3, 0.3),   # base
        "fib1d": (2.7, 0.3),   # base
    }

    labels = {
        "fib5":  "fib(5)",    "fib4":  "fib(4)",
        "fib3a": "fib(3)★",  "fib3b": "fib(3)★",
        "fib2a": "fib(2)★",  "fib2b": "fib(2)★",
        "fib2c": "fib(2)★",  "fib2d": "fib(2)★",
        "fib1a": "fib(1)=1", "fib1b": "fib(1)=1",
        "fib1c": "fib(1)=1", "fib1d": "fib(1)=1",
        "fib0a": "fib(0)=0",
    }

    unicos = {"fib5", "fib4"}
    bases  = {"fib1a", "fib1b", "fib1c", "fib1d", "fib0a"}
    # todos os outros são duplicados

    arestas = [
        ("fib5",  "fib4"),  ("fib5",  "fib3a"),
        ("fib4",  "fib3b"), ("fib4",  "fib2a"),
        ("fib3a", "fib2b"), ("fib3a", "fib2c"),
        ("fib3b", "fib1a"), ("fib3b", "fib2d"),
        ("fib2a", "fib1b"), ("fib2a", "fib1c"),
        ("fib2d", "fib0a"), ("fib2d", "fib1d"),
    ]

    RAIO = 0.22

    for u, v in arestas:
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        ax.plot([x1, x2], [y1 - RAIO, y2 + RAIO],
                color="#AAAAAA", lw=1.2, zorder=1)

    for key, (x, y) in pos.items():
        if key in unicos:
            cor = CORES["iter"]
        elif key in bases:
            cor = CORES["memo"]
        else:
            cor = CORES["rec"]

        circ = plt.Circle((x, y), RAIO, color=cor, zorder=3)
        ax.add_patch(circ)
        ax.text(x, y, labels[key], ha="center", va="center",
                fontsize=6.5, color="white", fontweight="bold", zorder=4)

    ax.set_xlim(-0.3, 9.8)
    ax.set_ylim(-0.6, 5.1)

    legenda = [
        mpatches.Patch(color=CORES["iter"], label="Chamada única"),
        mpatches.Patch(color=CORES["rec"],  label="Chamada duplicada ★"),
        mpatches.Patch(color=CORES["memo"], label="Caso base"),
    ]
    ax.legend(handles=legenda, loc="upper right", fontsize=9,
              framealpha=0.85)
    ax.set_title("Gráfico 3 — Árvore de Chamadas: fib(5)\n"
                 "Subproblemas marcados com ★ são recalculados desnecessariamente",
                 fontsize=11, fontweight="bold")

    _salvar(fig, "fig3_arvore.png")


# ══════════════════════════════════════════════════════════
# GRÁFICO 4 — Tabela: C(n) vs φⁿ/√5
# ══════════════════════════════════════════════════════════

def grafico_tabela_valores(n_max: int = 10) -> None:
    """
    Tabela visual comparando fib(n), C(n) do recursivo e a
    aproximação φⁿ/√5, validando a forma fechada (Passo 5).
    """
    ns         = list(range(n_max + 1))
    fibs       = [fib_iterativo(n)              for n in ns]
    ops_rec    = [contar_operacoes_recursivo(n)  for n in ns]
    phi_approx = [round(forma_fechada(n))        for n in ns]

    fig, ax = plt.subplots(figsize=(10, 3.8))
    fig.patch.set_facecolor(CORES["bg"])
    ax.set_facecolor(CORES["bg"])
    ax.axis("off")

    cabecalho   = ["n", "fib(n)", "C(n)  somas recursivo", "⌈φⁿ/√5⌉  (aprox.)"]
    dados_tabela = [[n, fibs[i], ops_rec[i], phi_approx[i]]
                    for i, n in enumerate(ns)]

    tbl = ax.table(
        cellText=dados_tabela,
        colLabels=cabecalho,
        loc="center",
        cellLoc="center",
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(10)
    tbl.scale(1, 1.65)

    for (r, c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor("#264653")
            cell.set_text_props(color="white", fontweight="bold")
        elif r % 2 == 0:
            cell.set_facecolor("#EAF4F4")
        else:
            cell.set_facecolor("#FFFFFF")
        cell.set_edgecolor("#CCCCCC")

    ax.set_title("Gráfico 4 — Tabela de Valores: C(n) vs φⁿ/√5\n"
                 "Passo 5: validação empírica da forma fechada",
                 fontsize=11, fontweight="bold", pad=14)

    _salvar(fig, "fig4_tabela.png")


# ══════════════════════════════════════════════════════════
# GRÁFICO 5 — Comparação de desempenho (barras agrupadas)
# ══════════════════════════════════════════════════════════

def grafico_comparacao_barras(ns_teste: list[int] | None = None,
                              repeticoes: int = 5) -> None:
    """
    Dois subgráficos lado a lado:
    - Esquerda: as três abordagens em escala logarítmica (mostra todas).
    - Direita:  só memoização e iterativo em escala linear (µs),
                para detalhar a diferença entre as duas.

    O motivo do split: memoização e iterativo são ~1000× mais rápidos
    que o recursivo — numa escala linear única elas somem no eixo.
    """
    if ns_teste is None:
        ns_teste = [10, 15, 20, 25, 30]

    print("  Medindo para gráfico de barras…")
    t_rec  = medir_tempo(fib_recursivo,  ns_teste, repeticoes)
    t_memo = medir_tempo(fib_memoizacao, ns_teste, repeticoes)
    t_iter = medir_tempo(fib_iterativo,  ns_teste, repeticoes)

    x = np.arange(len(ns_teste))
    labels_x = [f"n={n}" for n in ns_teste]
    w = 0.25

    fig, (ax_log, ax_lin) = plt.subplots(1, 2, figsize=(13, 5))
    fig.patch.set_facecolor(CORES["bg"])

    # ── Esquerda: escala log — todas as três abordagens visíveis ──
    ax_log.set_facecolor(CORES["bg"])

    rec_ms  = [max(t * 1000, 1e-6) for t in t_rec]
    memo_ms = [max(t * 1000, 1e-6) for t in t_memo]
    iter_ms = [max(t * 1000, 1e-6) for t in t_iter]

    ax_log.bar(x - w, rec_ms,  w, label="Recursivo  Θ(φⁿ)",
               color=CORES["rec"],  alpha=0.9)
    ax_log.bar(x,     memo_ms, w, label="Memoização  Θ(n)",
               color=CORES["memo"], alpha=0.9)
    ax_log.bar(x + w, iter_ms, w, label="Iterativo  Θ(n)",
               color=CORES["iter"], alpha=0.9)

    ax_log.set_yscale("log")
    ax_log.set_xticks(x)
    ax_log.set_xticklabels(labels_x)
    ax_log.set_ylabel("Tempo médio (ms) — escala log")
    ax_log.set_title("Todas as abordagens\n(escala logarítmica)",
                     fontsize=11, fontweight="bold")
    ax_log.legend(fontsize=9)
    ax_log.grid(True, axis="y", which="both")

    # ── Direita: escala linear em µs — detalhe memoização vs iterativo ──
    ax_lin.set_facecolor(CORES["bg"])

    memo_us = [t * 1e6 for t in t_memo]
    iter_us = [t * 1e6 for t in t_iter]

    ax_lin.bar(x - w / 2, memo_us, w, label="Memoização  Θ(n)",
               color=CORES["memo"], alpha=0.9)
    ax_lin.bar(x + w / 2, iter_us, w, label="Iterativo  Θ(n)",
               color=CORES["iter"], alpha=0.9)

    ax_lin.set_xticks(x)
    ax_lin.set_xticklabels(labels_x)
    ax_lin.set_ylabel("Tempo médio (µs) — escala linear")
    ax_lin.set_title("Memoização vs Iterativo em detalhe\n(escala linear, µs)",
                     fontsize=11, fontweight="bold")
    ax_lin.legend(fontsize=9)
    ax_lin.grid(True, axis="y")

    fig.suptitle("Gráfico 5 — Comparação de Desempenho: Três Abordagens",
                 fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()

    _salvar(fig, "fig5_comparacao.png")


# ══════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════

if __name__ == "__main__":
    print()
    print("=" * 55)
    print("  fibonacci_graficos.py  —  Gerando 5 gráficos")
    print("=" * 55)
    print(f"  Salvando em: {PASTA_SAIDA}")
    print()

    grafico_operacoes()
    grafico_tempo_execucao()
    grafico_arvore_chamadas()
    grafico_tabela_valores()
    grafico_comparacao_barras()

    print()
    print("✅  Concluído — 5 arquivos PNG gerados.")