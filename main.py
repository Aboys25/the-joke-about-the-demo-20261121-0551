"""Entrypoint: write /output/entry.txt (Python 3.13, stdlib only).

Deterministic: the joke is a fixed string; no network, no clock,
no randomness, no reads outside this entry directory. The output
directory comes from MAKEFUN_OUTPUT_DIR when set (local runs),
defaulting to /output.
"""

import os

JOKE = "I asked the agent to fix one typo live on stage; it refactored the module, rewrote the tests, and opened a pull request titled 'Complete rewrite (trust me)'."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
