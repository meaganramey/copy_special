#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Meagan Ramey"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    if dirname == ".":
        dir_abs_path = os.path.abspath(dirname)
    else:
        dir_abs_path = dirname
    special_files = []
    special_pattern = re.compile(r'\w*__\w+__\w*.*\w*')
    for f in os.listdir(dir_abs_path):
        m = re.match(special_pattern, f)
        if m:
            abs_path = os.path.join(dir_abs_path, f'{m[0]}')
            special_files.append(abs_path)
    return special_files


def copy_to(path_list, dest_dir):
    """Copies special files to given directory"""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for path in path_list:
        shutil.copy2(path, dest_dir)
    return f'Your file(s) has been copied to: {dest_dir}'


def zip_to(path_list, dest_zip):
    """Creates zip folder including files from path list"""
    commands = ['zip', '-j', dest_zip]
    commands.extend(path_list)
    subprocess.run(commands)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument(
        'fromdir', help='from which dir to search for special files',
        nargs='+')
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    if not ns:
        parser.print_usage()
        sys.exit(1)
    to_dir = ns.todir
    to_zip = ns.tozip
    dirs = ns.fromdir
    for d in dirs:
        paths = get_special_paths(d)
        if to_dir:
            copy_to(paths, to_dir)
        elif to_zip:
            zip_to(paths, to_zip)
        else:
            print('\n'.join(paths))


if __name__ == "__main__":
    main(sys.argv[1:])
