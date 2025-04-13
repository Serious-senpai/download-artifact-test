import random
import string
import sys
from pathlib import Path
from hashlib import sha256


ROOT = Path(__file__).parent.resolve()
data = sha256(b"", usedforsecurity=False).digest()
for value in sys.argv[1:]:
    data += value.encode("utf-8")
    data = sha256(data, usedforsecurity=False).digest()


output_dir = ROOT / "outputs"
output_dir.mkdir(exist_ok=True)


filename = "output-" + "".join(random.choices(string.hexdigits, k=8)) + ".txt"
with open(output_dir / filename, "w") as f:
    for _ in range(100):
        f.write(data.hex())
        data = sha256(data, usedforsecurity=False).digest()
