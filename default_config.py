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
# default_config.py
# Centralised defaults for WFGY SDK 1.0
# Author: PSBigBig & Contributors
# License: MIT

DEFAULT_CONFIG = {
    # --- BBMC (Semantic Residue) ---
    "m": 1.0,                  # Matching coefficient
    "c": 1.0,                  # Context factor

    # --- BBPF (Progression) ---
    "noise_scale": 0.02,       # Gaussian noise σ
    "k_paths": 3,              # Number of perturbation paths

    # --- BBCR (Collapse-Rebirth) ---
    "Bc": 1.0,                 # Residue threshold
    "eps": 0.05,               # f_S threshold
    "max_retries": 3,          # Max collapse cycles

    # --- BBAM (Attention Modulation) ---
    "gamma": 0.5,              # Variance gate strength
    "window_size": None        # Use global σ (set int for local)
}

# Humorous prompt for smoke test
PROMPT_HUMOROUS = "Why don't AIs like to take showers?"
