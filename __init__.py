#!/usr/bin/env python 
 # encoding: utf-8
"""
The Spike Package

"""
# from __future__ import absolute_import not needed anymore in 2.7
import os, sys

# Import exceptions
from NPKError import NPKError

# version.py defines static version names
from version import version as __version__
from version import VersionName as __version_info__
from version import ProgramName as __program_name__
#from version import revision as __revision__
from version import rev_date as __date__

__author__ = "Marc A. Delsuc <delsuc@igbmc.fr>, Marie-Aude Coutouly, Lionel Chiron"
SPIKE_version = __version__


#### Header to set-up the whole SPIKE environment
import NPKData

### plugins to the spike.NPKData class.
# simply put a xxx.py in the plugins folder - and define the interface as described in the doc
from plugins import load

load()
