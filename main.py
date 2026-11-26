"""Root CLI entrypoint for MediShield — Track 3: Secret Wards."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "medishield"))

from main import run_pipeline  # noqa: E402
import argparse  # noqa: E402


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MediShield Offline Privacy Firewall CLI")
    parser.add_argument("--input", required=True, help="Input directory")
    parser.add_argument("--output", required=True, help="Output directory")
    args = parser.parse_args()
    run_pipeline(Path(args.input), Path(args.output))
