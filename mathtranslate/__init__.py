__version__ = "1.1.3"
__author__ = "Jiace Sun"

import os
ROOT = os.path.dirname(os.path.abspath(__file__))
from . import config
from . import tencent
from .translate import translate
