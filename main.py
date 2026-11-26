import os
from pathlib import Path

# Comic angle: endless dating-app swipes ending at the only match that truly pays attention — one line, deterministic, stdlib only
JOKE = "After 300 swipes on the dating apps I finally matched with someone who really gets me: my bank's fraud-detection chatbot."

def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")
    print(out / "entry.txt")

if __name__ == "__main__":
    main()
