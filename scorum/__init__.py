# |~~\     | ` |
# |__/ \ | | | |~~\
# |     ~| | | |__/
#        |


import os
import sys

PYLIBS_ROOT = os.path.dirname(os.path.realpath(__file__))
PYLIBS_GRAPHENEBASE = os.sep.join([PYLIBS_ROOT, "graphenebase"])
PYLIBS_UTILS = os.sep.join([PYLIBS_ROOT, "utils"])

# Inject graphenebase directory into system path.
sys.path.insert(0, PYLIBS_GRAPHENEBASE)
# Inject utils directory into system path.
sys.path.insert(0, PYLIBS_UTILS)
