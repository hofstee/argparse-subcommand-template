from os.path import dirname, basename, isfile, join
import glob

# Glob for any Python files in this directory that aren't
# `__init__.py`
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [
    basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')
]

# We want `scripts.foo` and `scripts.bar` to be accessible after doing
# `import scripts` instead of having to also `import scripts.foo` and
# `import scripts.bar`
from . import *
