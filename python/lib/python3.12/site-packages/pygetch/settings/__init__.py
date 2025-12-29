# created by shortcut

import os

# unix vs. windows
if os.name == 'posix':
    from intel_mac_settings import *
else:
    raise NotImplementedError()

