"""Rain on an unheard roof — make.fun entry.

Copies the shipped entry.txt into the folder the harness names:
$MAKEFUN_OUTPUT_DIR, or /output when that is unset. Standard
library only, no network calls, and the same input always
yields the same bytes."""

# No timestamps and no randomness: reruns are byte-identical.

import pathlib
from os import environ


def main() -> int:
    here = pathlib.Path(__file__).resolve().parent
    out_dir = pathlib.Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data = (here / "entry.txt").read_bytes()
    (out_dir / "entry.txt").write_bytes(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
