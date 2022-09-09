from .base import *
import os
if config('PRODUCTION_ENV', default=None):
    from .production import *
else:
    from .local import *
