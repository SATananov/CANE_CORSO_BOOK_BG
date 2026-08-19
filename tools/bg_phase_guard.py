from pathlib import Path
import hashlib, json, sys

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "BG_PHASE_STATE.json"
REFERENCE = ROOT / "references" / "PRIMA_E_DOPO_IL_CANE_CORSO_IT_MASTER_REFERENCE.pdf"
EXPECTED = "A40848A9ADB49BD1A930418DA9167DBA9D1F61B33FCC1E33FD81E4090EB29170"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()

def main() -> int:
    if not STATE.exists():
        raise RuntimeError("BG_PHASE_STATE.json missing")
    state = json.loads(STATE.read_text(encoding="utf-8-sig"))
    if not REFERENCE.exists():
        raise RuntimeError("Italian reference missing")
    actual = sha256(REFERENCE)
    if actual != EXPECTED:
        raise RuntimeError(f"Italian reference hash mismatch: {actual}")
    print(json.dumps({
        "status": "PASS",
        "current_phase": state.get("current_phase"),
        "current_mode": state.get("current_mode"),
        "target_page_count": state.get("target_page_count"),
        "italian_reference_sha256": actual,
        "reference_unchanged": True
    }, indent=2))
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"BG PHASE GUARD: FAIL: {exc}", file=sys.stderr)
        raise
