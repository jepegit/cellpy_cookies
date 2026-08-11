import os
import sys


MIN_CELLPY_MAJOR, MIN_CELLPY_MINOR = 2, 1
cellpy_version = "{{ cookiecutter.cellpy_version }}"
major, minor = cellpy_version.split(".")[:2]
major, minor = int(major), int(minor)
too_old = False

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
    print(f"  Cellpy Cookie: this cookie needs cellpy >= {MIN_CELLPY_MAJOR}.{MIN_CELLPY_MINOR},")
    print(f"                 you are running cellpy {cellpy_version}")
    print("  Cellpy Cookie: either update cellpy:")
    print("    $ python -m pip install cellpy --upgrade")
    print("  Cellpy Cookie: or use the cookie for cellpy 1.x instead:")
    print("    $ cookiecutter gh:jepegit/cellpy_cookies --directory ife_1_x")
    print(80 * "=")
    print()
    sys.exit(1)

print(f"setting up project in the following directory: {os.getcwd()}")
