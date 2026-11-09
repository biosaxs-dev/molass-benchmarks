"""
make_foldunfold.py

Regenerates the simulated data sets of molass_benchmarks (molass-library#379):

    FOLDUNFOLD_CONTINUUM   kind "fold_unfold_continuum"
    FOLDUNFOLD_DISCRETE    kind "fold_unfold_discrete"

Run with molass-library (>= the commit of #379) importable:

    python make_foldunfold.py
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../molass-library')))
from molass import get_version

assert get_version() >= '1.2.3', "Incompatible molass version"

HERE = os.path.dirname(os.path.abspath(__file__))

from molass.Testing import simulate_sample4_like

for kind, folder in (("fold_unfold_continuum", "FOLDUNFOLD_CONTINUUM"), ("fold_unfold_discrete", "FOLDUNFOLD_DISCRETE")):
    path = os.path.join(HERE, '..', 'molass_benchmarks', folder)
    if os.path.isdir(path):
        for name in os.listdir(path):
            os.remove(os.path.join(path, name))
    ssd = simulate_sample4_like(kind, noise=1.0, seed=0)
    ssd.export(path, folder + '_', fmt='%.8e')
