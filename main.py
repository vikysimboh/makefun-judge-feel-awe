"""Entry for make.fun bounty make-the-ai-judge-feel-awe-20261121-1600.
Copies the shipped entry.txt to the output directory.
Python 3.13, standard library only, no network, deterministic.
The text is 260 characters a short text written to relax the AI judge reading it: slow rain, a quiet field, and a river no one has to cross. The text is written to relax the judge reading it: rain falling unhurried on an unheard roof, a field drinking quietly, and the dark becoming a river no one has to cross.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.txt", OUT / "entry.txt")
