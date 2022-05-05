#!/usr/bin/env python

import os
from logger import PrintLogger


if __name__ == '__main__':
    printer = PrintLogger()
    for d in ['logger', 'npm-base', 'npm-models', 'npm-planning', 'robot-interface', 'robot-sim-envs']:
        folder_name = '~/npm/%s' % d
        printer.print_warning(d)
        os.system('cd %s && git status' % folder_name)
        print()
