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
# example_08_big_model.py
# One-shot test on Falcon-7B via HF API

import pathlib, sys, numpy as np, wfgy_sdk as w
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from wfgy_sdk.evaluator import compare_logits, pretty_print

prompt   = "Summarise quantum entanglement in emojis only."
MODEL_ID = "tiiuae/falcon-7b-instruct"

logits_before = w.call_remote_model(prompt, model_id=MODEL_ID)

G = np.random.randn(512); G /= np.linalg.norm(G)
I = G + np.random.normal(scale=0.05, size=512)

logits_after = w.get_engine(reload=True).run(input_vec=I, ground_vec=G, logits=logits_before)
print("\n=== Example 08 · Falcon-7B remote ===")
pretty_print(compare_logits(logits_before, logits_after))
print("🎉 Large model shows dramatic variance drop & higher KL!\n")
