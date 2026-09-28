#M1. importing the entire code 
# import external
# external.fn()

#M2. importing a specific part
# from external import fn
# fn()

# #M3 giving the import a name
# from external import fn as efn
# efn()

#M4 Relative imports
from .utils.customImpl import customCalc  #because of the dot it needs to recongnize this directory as a package rather than a standalone script
# so we have to run this file as a module not directly as script
# thus add __init__.py to this directory and then go out of this folder and run python -m importImpl.imports
customCalc()