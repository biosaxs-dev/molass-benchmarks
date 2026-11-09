"""
molass_benchmarks

Benchmark data sets of known composition for the Molass Library: a measured mixture of five proteins and
simulated data with known truth. Each attribute holds the path of a data folder::

    from molass_benchmarks import PROTEINS5               # measured (formerly SAMPLE6 of molass_data 0.5.0)
    from molass_benchmarks import FOLDUNFOLD_CONTINUUM    # simulated, truth known
    from molass_benchmarks import FOLDUNFOLD_DISCRETE     # simulated, truth known
"""


def get_version(toml_only=False):
    """
    Returns the version of the molass_benchmarks package.
    """
    from molass import _get_version_impl
    return _get_version_impl(toml_only, __file__, __package__)


def get_data_path(subfolder):
    """
    Returns the path of a data folder of this package.
    """
    import os
    this_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(this_dir, subfolder)


PROTEINS5 = get_data_path("PROTEINS5")
FOLDUNFOLD_CONTINUUM = get_data_path("FOLDUNFOLD_CONTINUUM")
FOLDUNFOLD_DISCRETE = get_data_path("FOLDUNFOLD_DISCRETE")
