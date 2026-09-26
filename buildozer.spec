[app]

# (str) Title of your application
title = Game Center

# (str) Package name
package.name = gamecenter

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (INCLUDE ALL YOUR FILES HERE)
source.include_exts = py,png,jpg,kv,atlas,txt

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets custom source for any requirement with recipes
# requirements.source.kivy = ../kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
#android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (list) List of inclusions using pattern matching
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = error, 1 = warning)
warn_on_root = 1
