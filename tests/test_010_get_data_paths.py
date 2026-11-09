import sys
sys.path.insert(0, '../../molass-library')
sys.path.insert(0, '..')
from molass_benchmarks import get_version, PROTEINS5, FOLDUNFOLD_CONTINUUM, FOLDUNFOLD_DISCRETE
print("Library version:", get_version())
print("PROTEINS5 path:", PROTEINS5)
print("FOLDUNFOLD_CONTINUUM path:", FOLDUNFOLD_CONTINUUM)
print("FOLDUNFOLD_DISCRETE path:", FOLDUNFOLD_DISCRETE)
