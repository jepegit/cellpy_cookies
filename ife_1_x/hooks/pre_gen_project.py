import os
import sys


MIN_CELLPY_MAJOR, MIN_CELLPY_MINOR = 0, 5
MAX_CELLPY_MAJOR = 1
cellpy_version = "{{ cookiecutter.cellpy_version }}"
major, minor = cellpy_version.split(".")[:2]
major, minor = int(major), int(minor)
too_old = False

if major > MAX_CELLPY_MAJOR:
    print()
    print(80 * "=")
    print("  Cellpy Cookie: OH NO!!!!")
    print("  Cellpy Cookie: This cookie is for cellpy 1.x only - aborting!")
    print(f"  Cellpy Cookie: you are running cellpy {cellpy_version}")
    print("  Cellpy Cookie: use the ife cookie instead:")
    print("    $ cellpy new --template ife")
    print(80 * "=")
    print()
    sys.exit(1)

if major < MIN_CELLPY_MAJOR:
    too_old = True

if major == MIN_CELLPY_MAJOR:
    if minor < MIN_CELLPY_MINOR:
        too_old = True

if too_old:
    print()
    print(80 * "=")
    print("  Cellpy Cookie: OH NO!!!!")
    print("  Cellpy Cookie: Your version of cellpy is too old - aborting!")
    print(80 * "=")
    print()
    sys.exit(1)

print(f"setting up project in the following directory: {os.getcwd()}")
