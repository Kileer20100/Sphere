from pathlib import Path
import shutil
import tarfile

ROOT = Path(__file__).resolve().parents[2] 

def build(target: str):
    if not target.startswith("linux-"):
        raise ValueError("Only linux targets supported")

    build_dir = ROOT / "build" / target

    if build_dir.exists():
        shutil.rmtree(build_dir)

    build_dir.mkdir(parents=True)

    print(f"[BUILD] {target}")

    shutil.copytree(
        ROOT / "sphere",
        build_dir / "sphere",
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc")
    )

    # 3. архивируем
    archive = ROOT / "build" / f"sphere-{target}.tar.gz"
    with tarfile.open(archive, "w:gz") as tar:
        tar.add(build_dir, arcname="sphere")

    print(f"[OK] Build ready: {archive}")


