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
    special_files = []
    special_pattern = re.compile(r'\w*__\w+__\w*.\w*')
    for __, __, file_names in os.walk(dirname):
        for f in file_names:
            m = re.match(special_pattern, f)
            if m:
                abs_path = os.path.abspath(f'{m[0]}')
                special_files.append(abs_path)
    return special_files


def copy_to(path_list, dest_dir):
    # your code here
    return


def zip_to(path_list, dest_zip):
    # your code here
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument(
        'fromdir', help='from which dir to search for special files')
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    to_dir = ns.todir
    to_zip = ns.tozip
    from_dir = ns.fromdir
    if not ns:
        parser.print_usage()
        sys.exit(1)
    paths = get_special_paths(from_dir)
    if to_dir:
        copy_to(paths, to_dir)
    elif to_zip:
        zip_to(paths, to_zip)


if __name__ == "__main__":
    main(sys.argv[1:])
