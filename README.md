# KiCAD_Action_Plugin

  KiCad supports plugins, which are extensions or additional scripts that users can create to enhance or customize the functionality of the software. 
  These plugins can automate repetitive tasks, add new features, or integrate with other tools.

  On startup kicad look for python scripts in specific directories. If found kicad use those scripts

These specific directories can be found on your system by doing 
  "PCB editor" -> Tools -> External Plugins -> Open Plugin directory.
  or
  "PCB editor" -> Tools -> Scripting console -> "import pcbnew; print(pcbnew.PLUGIN_DIRECTORIES_SEARCH)"

There is currently two ways a plugin can be written:
  1) Simple Plugin
  2) Complex Plugin

   ## Simple Plugin:

   When your script is a single file.
   
     + ~/.kicad_plugins/ # A folder in the KiCad plugin path
          - simple_plugin.py
          - simple_plugin.png (optional)

  simple_plugin.py contains the following.

  ```
  import pcbnew
  import os
  
  class SimplePlugin(pcbnew.ActionPlugin):
      def defaults(self):
          self.name = "Plugin Name as shown in Pcbnew: Tools->External Plugins"
          self.category = "A descriptive category name"
          self.description = "A description of the plugin and what it does"
          self.show_toolbar_button = False # Optional, defaults to False
          self.icon_file_name = os.path.join(os.path.dirname(__file__), 'simple_plugin.png') # Optional, defaults to ""
  
      def Run(self):
          # The entry function of the plugin that is executed on user action
          print("Hello World")
  
  SimplePlugin().register() # Instantiate and register to Pcbnew
```

## Complex Plugin

When your script has more than one file.

  + ~/.kicad_plugins/ # this directory has to be in the plugin path
      + complex_plugin/ # The plugin directory (A Python package)
          - __init__.py # This file is executed when the package is imported (on PCB editor startup)
          - __main__.py # This file is optional. See below
          - complex_plugin_action.py # The ActionPlugin derived class lives here
          - complex_plugin_utils.py # Other Python parts of the plugin
          - icon.png
          + otherstuff/
              - otherfile.png
              - misc.txt
           
At minimum only ```__init__.py``` and ```complex_plugin_action.py``` are needed for a working kicad plugin.

"\_\_init__.py" contains the following:
```
from .complex_plugin_action import ComplexPluginAction # Note the relative import!
ComplexPluginAction().register() # Instantiate and register to PCB editor
```

"complex_plugin_action.py" contains the following:
```
import pcbnew
import os

class ComplexPluginAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "A complex action plugin"
        self.category = "A descriptive category name"
        self.description = "A description of the plugin"
        self.show_toolbar_button = True # Optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png') # Optional

    def Run(self):
        # The entry function of the plugin that is executed on user action
        print("Hello World")
```

The official KiCAD Documentation is [here](https://dev-docs.kicad.org/en/apis-and-binding/pcbnew/)
