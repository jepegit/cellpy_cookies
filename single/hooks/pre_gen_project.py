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
    print(" ERROR ".center(80, "="))
    print()
    print("  Cellpy Cookie says: 'OH NO!!!!'")
    print("  Cellpy Cookie says: 'Your version of cellpy is too old - aborting!'")
    print(f"  Cellpy Cookie says: 'this cookie needs cellpy >= {MIN_CELLPY_MAJOR}.{MIN_CELLPY_MINOR},")
    print(f"                       you are running cellpy {cellpy_version}'")
    print()
    print("  Cellpy Cookie says: 'please update cellpy'")
    print()
    print("    $ python -m pip install cellpy --upgrade")
    print()
    print(80 * "=")
    print()
    sys.exit(1)
print("   Cellpy Cookie says: 'using cookie from the cellpy_cookies repository'")
print("   Cellpy Cookie says: 'setting up project in the following directory:'")
print(f"      {os.getcwd()}'")
print()
