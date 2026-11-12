# Coolest art entry (Python 3.13, standard library only): the art is the entry.png
# beside this file, and the program copies it to /output/entry.png.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "entry.png")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
dst = os.path.join(out_dir, "entry.png")
shutil.copyfile(src, dst)
size = os.path.getsize(dst)
assert size <= 1_048_576, f"entry.png too big: {size} bytes"
print(f"wrote {dst} ({size} bytes)")
