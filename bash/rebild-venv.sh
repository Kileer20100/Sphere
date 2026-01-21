rm -rf .venv
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .
pip install maturin
pip install typer
maturin dev
./bash/fix.sh
