import argparse
import shutil
from pathlib import Path

if __name__ == "__main__":

    MIN_YEAR = 2015
    MAX_YEAR = 2022

    parser = argparse.ArgumentParser()

    parser.add_argument("year", type=int)
    parser.add_argument("day", type=str)
    args = parser.parse_args()

    if not (MIN_YEAR <= args.year <= MAX_YEAR):
        raise argparse.ArgumentTypeError("invalid year")

    if not (1 <= int(args.day) <= 31):
        raise argparse.ArgumentTypeError("invalid day")

    base_path = Path(__file__).parent.absolute()
    template_dir = base_path / "template"
    day_dir = base_path / f"{args.year}" / f"{args.day}"

    Path(day_dir).mkdir(parents=True, exist_ok=True)

    for file_path in template_dir.iterdir():
        target_path = day_dir / file_path.name
        resp = ""
        if target_path.exists():
            while resp not in ("y", "n"):
                resp = (
                    str(input("File already exists, copy anyways? (y or n)"))
                    .lower()
                    .strip()
                )

        if not target_path.exists() or resp == "y":
            shutil.copy(file_path, target_path)
