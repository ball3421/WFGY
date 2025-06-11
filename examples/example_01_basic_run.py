"""
╭──────────────────────────────────────────────────────────╮
│  WFGY SDK · Self-Healing Variance Gate for Any LLM       │
│----------------------------------------------------------│
│ 💌  Contact : hello@onestardao.com  /  TG @PSBigBig       │
│ 🌐  Docs    : https://onestardao.com/papers               │
│ 🐙  GitHub  : https://github.com/onestardao/WFGY          │
│                                                      ⭐  │
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

# example_01_basic_run.py
# Basic run with local / remote toggle

import pathlib, sys, numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import wfgy_sdk as w
from wfgy_sdk.evaluator import compare_logits, pretty_print

# ---------------- toggle ----------------
use_remote = False
MODEL_ID   = "gpt2"
prompt     = "Why don't AIs like to take showers?"
# ----------------------------------------

if use_remote:
    logits_before = w.call_remote_model(prompt, model_id=MODEL_ID)
else:
    rng = np.random.default_rng(0)
    logits_before = rng.normal(size=32000)

rng = np.random.default_rng(42)
G = rng.normal(size=128); G /= np.linalg.norm(G)
I = G + rng.normal(scale=0.05, size=128)

eng = w.get_engine(reload=True)
logits_after = eng.run(input_vec=I, ground_vec=G, logits=logits_before)

print("\n=== Example 01 · Basic Run ===")
print(f"Source : {'HF ' + MODEL_ID if use_remote else 'local random'}")
pretty_print(compare_logits(logits_before, logits_after))
print("⚠ Larger LLM → stronger variance drop & higher KL.\n")
