"""Diagnostic script to understand the import issue."""

import sys
from pathlib import Path

print("=" * 60)
print("PYTHON PATH DIAGNOSTIC")
print("=" * 60)

print(f"\nCurrent working directory: {Path.cwd()}")
print(f"Python executable: {sys.executable}")

print("\nPython sys.path:")
for i, p in enumerate(sys.path, 1):
    print(f"  {i}. {p}")

print("\n" + "=" * 60)
print("PROJECT STRUCTURE DIAGNOSTIC")
print("=" * 60)

# Check if backend is a package
backend_path = Path("backend")
if backend_path.exists():
    print(f"\n[OK] backend directory exists at: {backend_path.absolute()}")
    init_py = backend_path / "__init__.py"
    if init_py.exists():
        print(f"[OK] backend/__init__.py exists (backend IS a package)")
    else:
        print(f"[MISSING] backend/__init__.py (backend is NOT a package)")
else:
    print(f"\n[NOT FOUND] backend directory")

# Check src structure
src_path = Path("backend/src")
if src_path.exists():
    print(f"\n[OK] backend/src directory exists")
    init_py = src_path / "__init__.py"
    if init_py.exists():
        print(f"[OK] backend/src/__init__.py exists")
    else:
        print(f"[MISSING] backend/src/__init__.py")
else:
    print(f"\n[NOT FOUND] backend/src directory")

print("\n" + "=" * 60)
print("IMPORT TEST")
print("=" * 60)

# Try importing
print("\nAttempting: import backend")
try:
    import backend
    print(f"[OK] Successfully imported backend: {backend}")
except ImportError as e:
    print(f"[FAILED] Failed to import backend: {e}")

print("\nAttempting: from backend.src.bootstrap.app_factory import create_app")
try:
    from backend.src.bootstrap.app_factory import create_app
    print(f"[OK] Successfully imported create_app: {create_app}")
except ImportError as e:
    print(f"[FAILED] Failed to import create_app: {e}")

print("\n" + "=" * 60)
print("ROOT CAUSE ANALYSIS")
print("=" * 60)

if not (Path("backend") / "__init__.py").exists():
    print("\nROOT CAUSE IDENTIFIED:")
    print("  The 'backend' directory is missing __init__.py")
    print("  Without __init__.py, Python doesn't recognize it as a package.")
    print("\nSOLUTIONS:")
    print("  1. Create backend/__init__.py (empty file)")
    print("  2. OR run pytest from parent directory with PYTHONPATH set")
    print("  3. OR use relative imports in tests")
else:
    print("\nCheck PYTHONPATH configuration or run from project root.")

print("\n" + "=" * 60)