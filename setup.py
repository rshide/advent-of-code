import argparse
import shutil
from pathlib import Path

if __name__ == "__main__":

    MIN_YEAR = 2015
    MAX_YEAR = 2022

    parser = argparse.ArgumentParser()

    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)
    args = parser.parse_args()

    if not (MIN_YEAR <= args.year <= MAX_YEAR):
        raise argparse.ArgumentTypeError("invalid year")

    if not (1 <= args.day <= 31):
        raise argparse.ArgumentTypeError("invalid day")

    base_path = Path(__file__).parent.absolute()
    template_dir = base_path / "template"
    day_dir = base_path / f"{args.year}" / f"{args.day}"

    Path(day_dir).mkdir(parents=True, exist_ok=True)

    for file_path in template_dir.iterdir():
        shutil.copy(file_path, day_dir / file_path.name)
