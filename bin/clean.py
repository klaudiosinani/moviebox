# -*- coding: utf-8 -*-
import shutil

from termcolor import colored
from os.path import (exists, abspath)

green = 'green'  # Green colored text
yellow = 'yellow'  # Yellow colored text

distDir = abspath('dist')  # Dist directory
buildDir = abspath('build')  # Build directory
eggDir = abspath('moviebox.egg-info')  # Egg directory

if (exists(distDir)):
    # Check if the `dist` directory exists
    shutil.rmtree(distDir)
    print(colored('✔ Cleaned up ' + distDir, green))

if (exists(buildDir)):
    # Check if the `build` directory exists
    shutil.rmtree(buildDir)
    print(colored('✔ Cleaned up ' + buildDir, green))

if (exists(eggDir)):
    # Check if the `egg` directory exists
    shutil.rmtree(eggDir)
    print(colored('✔ Cleaned up ' + eggDir, green))
