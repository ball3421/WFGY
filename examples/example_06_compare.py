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
│     https://doi.org/10.5281/zenodo.15630969              │
│     (Hosted on Zenodo – trusted international archive)   │
│                                                          │
│ 🧬  WFGY BigBang Prompt Pack (v1.0):                     │
│     https://doi.org/10.5281/zenodo.15657016              │
│     (Prompts to trigger the gate; multilingual updates coming) │
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
# example_06_compare.py
# GPT-2 local vs optional remote compare

import pathlib, sys, numpy as np, torch
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import wfgy_sdk as w
from wfgy_sdk.evaluator import compare_logits, pretty_print

use_remote = False
MODEL_ID   = "gpt2"            # remote model id

prompt = "Explain the Navier–Stokes millennium problem in 50 words."

if use_remote:
    logits_before = w.call_remote_model(prompt, model_id=MODEL_ID)
else:
    tok = GPT2TokenizerFast.from_pretrained("gpt2")
    gpt2 = GPT2LMHeadModel.from_pretrained("gpt2").eval()
    ids = tok(prompt, return_tensors="pt").input_ids
    with torch.no_grad():
        logits_before = gpt2(ids).logits[0, -1].cpu().numpy()

G = np.random.randn(256); G /= np.linalg.norm(G)
I = G + np.random.normal(scale=0.05, size=256)

eng = w.get_engine(reload=True)
logits_after = eng.run(input_vec=I, ground_vec=G, logits=logits_before)

print("\n=== Example 06 · Logit compare ===")
pretty_print(compare_logits(logits_before, logits_after))
print("⚠ Larger LLM → stronger variance drop & higher KL.\n")
