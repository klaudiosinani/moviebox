#!/usr/bin/env python3
import shutil

from termcolor import colored
from os.path import (exists, abspath)

green = 'green'  # Green colored text
yellow = 'yellow'  # Yellow colored text

distDir = abspath('dist')  # Dist directory
eggDir = abspath('moviebox.egg-info')  # Egg directory

if (exists(distDir)):
    # Check if the `dist` directory exists
    shutil.rmtree(distDir)
    print(colored('✔ Cleaned up ' + distDir, green))

if (exists(eggDir)):
    shutil.rmtree(eggDir)
    print(colored('✔ Cleaned up ' + eggDir, green))
