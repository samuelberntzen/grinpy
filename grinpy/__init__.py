# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>

"""Top-level package for GrinPy."""

# check Python version
import sys

if sys.version_info[:2] < (3, 4):
    m = "Python 3.4 or later is required for GrinPy (%d.%d detected)."
    raise ImportError(m % sys.version_info[:2])
del sys

__author__ = """David Amos, Randy Davila"""
__email__ = "somacdivad@gmail.com, dvilar@uhd.edu"
__version__ = "0.2.0"

# import NetworkX dependency
import networkx
from networkx import *

# the following are imported orderwise
import grinpy.classes
from grinpy.classes import *

import grinpy.functions
from grinpy.functions import *

import grinpy.invariants
from grinpy.invariants import *
