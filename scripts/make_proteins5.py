"""
make_proteins5.py

PROTEINS5 is the measured data set 20191006_proteins5 (formerly SAMPLE6 of molass_data 0.5.0); its files are
named PROTEINS5_*.dat.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../molass-library')))
from molass import get_version

assert get_version() >= '0.4.0', "Incompatible molass version"

from molass.Local import get_local_settings
from molass.Global.Options import set_molass_options
set_molass_options(flowchange='auto')
local_settings = get_local_settings()
DATA_ROOT_FOLDER = local_settings['DATA_ROOT_FOLDER']

DATA = os.path.join(DATA_ROOT_FOLDER, "20191006_proteins5")
HERE = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(HERE, '..', 'molass_benchmarks', 'PROTEINS5')

import matplotlib.pyplot as plt
from molass.DataObjects import SecSaxsData as SSD
ssd = SSD(DATA)
ssd.plot_compact()
plt.show()

ssd.export(FOLDER, 'PROTEINS5_', fmt='%.8e')

check_ssd = SSD(FOLDER)
check_ssd.plot_compact()
plt.show()
