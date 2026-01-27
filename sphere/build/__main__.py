import sys
from .builder import build

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m sphere.build <target>")
        return

    build(sys.argv[1])

if __name__ == "__main__":
    main()
