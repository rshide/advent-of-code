import argparse
import shutil
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--year', type=int, required=True)
    parser.add_argument('--day', type=int, required=True)
    args = parser.parse_args()

    base_path = Path(__file__).parent.absolute()
    template_dir = base_path / 'template'
    day_dir = base_path / f"{args.year}" / f"{args.day}"

    Path(day_dir).mkdir(parents=True, exist_ok=True)

    for file_path in template_dir.iterdir():
        shutil.copy(file_path, day_dir / file_path.name)


