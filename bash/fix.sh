
cat > .venv/bin/sph << 'EOF'
#!/usr/bin/env python3
import sys
import os

# Добавляем путь к проекту
sys.path.insert(0, '/home/kiril/Sphere')

from sphere.cli import app

if __name__ == '__main__':
    sys.exit(app())
EOF

chmod +x .venv/bin/sph

echo "Shebang fixed in .venv/bin/sph"
echo "sph Version:"
sph v