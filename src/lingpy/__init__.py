"""
LingPy package for quantitative tasks in historical linguistics.

Documentation is available in the docstrings. Online documentation is available
at http://lingpy.org

Subpackages
-----------
algorithm  --- Basic Algorithms for Sequence Comparison
align      --- Specific Algorithms Alignment Analyses
basic      --- Basic Classes for Language Comparison
compare    --- Basic Modules for Language Comparison
convert    --- Functions for Format Conversion
data       --- Data Handling
evaluate   --- Basic Classes and Functions for Algorithm Evaluation
read       --- Basic Functions for Data Input
sequence   --- Basic Functions for Sequence Modeling
thirdparty --- Temporary Forks of Third-Party-Modules

"""

__author__ = "Johann-Mattis List, and Robert Forkel (with contributions by Simon J. Greenhill, Tiago Tresoldi, Gereon Kaiping, Steven Moran, Taraka Rama, Johannes Dellert, Frank Nagel, and Peter Bouda, and Taraka Rama)"
__date__ = "2021-06-07"
__version__ = "2.6.9.dev0"

# We exempt this module from QA, because it only provides import shortcuts.
# flake8: noqa
# import settings
from lingpy.settings import rc

# general imports
from lingpy.basic.wordlist import Wordlist, get_wordlist
from lingpy.basic.tree import Tree
from lingpy.basic.ops import iter_rows

# import converts
# from .convert import *

# we don't import align for the moment for safety reasons...
from lingpy.align import Pairwise, Multiple, SCA, MSA, PSA, Alignments, edit_dist, \
        pw_align, nw_align, sw_align, we_align, structalign, turchin, \
        mult_align

# load the sound-class models
from lingpy.data import Model

# import reading routine
from lingpy.read.csv import csv2list, csv2dict

# import sequence routines
from lingpy.sequence.sound_classes import ipa2tokens, tokens2class, prosodic_string, \
        prosodic_weights, class2tokens, pid, sampa2uni
from clldutils.text import strip_chars

# import lexstat
from lingpy.compare.lexstat import LexStat

# import algorithm-stuff
from lingpy.algorithm.clustering import upgma, neighbor, flat_upgma, flat_cluster, \
        fuzzy, link_clustering, mcl
