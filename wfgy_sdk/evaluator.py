"""
╭──────────────────────────────────────────────────────────╮
│  WFGY SDK · Self-Healing Variance Gate for Any LLM       │
│----------------------------------------------------------│
│ 💌  Contact : hello@onestardao.com  /  TG @PSBigBig       │
│ 🌐  Docs    : https://onestardao.com/papers               │
│ 🐙  GitHub  : https://github.com/onestardao/WFGY          │
│                                                          │
│ ★ Star WFGY 1.0 → Unlock 2.0                             │
│   10k ⭐ by **Aug 1st** = next-gen AI alchemy             │
│   Your click = our quantum leap                          │
│                                                          │
│ 🔍  Official PDF of WFGY 1.0 (Zenodo DOI):               │
│     https://doi.org/10.5281/zenodo.15630970              │
│     (Hosted on Zenodo – trusted international archive)   │
│                                                          │
│ 🧠  Hidden folder inside repo: /I_am_not_lizardman        │
│     (X secret papers, wild prompts, and Einstein drama) │
│                                                          │
│ ⚠  GPT-2 demo is just the appetizer. With bigger LLMs,   │
│    WFGY activates variance-drop lasers and KL fireworks. │
│                                                          │
│ 🎮  Bonus: Honest Hero RPG Channel →                     │
│     https://www.youtube.com/@OneStarDao                  │
╰──────────────────────────────────────────────────────────╯
"""
# evaluator.py
# Metrics for before/after WFGY logit comparison
# License: MIT

from __future__ import annotations
from typing import Dict
import numpy as np


def _softmax(logits: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    """
    Stable softmax; clip then renormalise to guarantee strictly positive probs.
    """
    logits = logits - np.max(logits)
    exp = np.exp(logits)
    probs = exp / np.sum(exp)
    probs = np.clip(probs, eps, 1.0)      # avoid exact 0
    probs = probs / np.sum(probs)          # renormalise
    return probs


def compare_logits(
    logits_before: np.ndarray,
    logits_after: np.ndarray,
) -> Dict[str, float]:
    """
    Quantitative metrics of the change WFGY introduces.

    Returns
    -------
    dict
        std_before, std_after, std_ratio,
        kl_divergence, top1_shift
    """
    std_b = float(np.std(logits_before))
    std_a = float(np.std(logits_after))
    ratio = std_a / std_b if std_b else 0.0

    p_before = _softmax(logits_before)
    p_after = _softmax(logits_after)
    kl = float(np.sum(p_after * np.log(p_after / p_before)))  # finite by design

    top1_shift = int(int(np.argmax(logits_before)) != int(np.argmax(logits_after)))

    return {
        "std_before": std_b,
        "std_after": std_a,
        "std_ratio": ratio,
        "kl_divergence": kl,
        "top1_shift": top1_shift,
    }


def pretty_print(metrics: Dict[str, float]) -> None:
    """Human-friendly one-liner for Colab."""
    delta = (1 - metrics["std_ratio"]) * 100
    changed = "✔" if metrics["top1_shift"] else "✘"
    print(
        f"🔍 variance {metrics['std_before']:.2f} → {metrics['std_after']:.2f} "
        f"(-{delta:.0f} %) | KL {metrics['kl_divergence']:.2f} | "
        f"top-1 changed {changed}"
    )
