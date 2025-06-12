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
"""
export_onnx.py  ·  Generate tiny ONNX graphs for all four WFGY modules
Will auto-install `onnx` if missing (Colab-friendly).
"""

import subprocess, sys, importlib.util, os
import numpy as np

# ── ensure onnx is available ────────────────────────────────────────────
if importlib.util.find_spec("onnx") is None:
    print("🔄  Installing onnx …")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "onnx", "-q"])

import onnx
from onnx import helper, TensorProto

os.makedirs("specs/onnx", exist_ok=True)

def tiny_graph(name, dim=128):
    X = helper.make_tensor_value_info("X", TensorProto.FLOAT, [None, dim])
    Y = helper.make_tensor_value_info("Y", TensorProto.FLOAT, [None, dim])
    node = helper.make_node("Identity", ["X"], ["Y"], name=f"{name}_pass")
    graph = helper.make_graph([node], f"{name}_graph", [X], [Y])
    return helper.make_model(graph, producer_name="wfgy-dummy")

for mod in ["bbmc", "bbpf", "bbcr", "bbam"]:
    onnx.save(tiny_graph(mod.upper()), f"specs/onnx/{mod}.onnx")

print("✅ ONNX graphs saved to specs/onnx/")
