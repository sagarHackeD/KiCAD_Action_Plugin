# This file is executed when the package is imported (on PCB editor startup)

from .complex_plugin_action import ComplexPluginAction # Note the relative import!
ComplexPluginAction().register() # Instantiate and register to PCB editor