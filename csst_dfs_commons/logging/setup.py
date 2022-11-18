#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Shoulin Wei
#
# This file is part of CSST.

# coding: utf-8
import os
import path
import logging
import logging.handlers

def setup_logging():
    """ Setup logging configuration """

    cfmt = logging.Formatter(('%(asctime)s- %(name)s - %(filename)s - %(levelname)s - %(message)s'))

    # File formatter, mention time
    ffmt = logging.Formatter(('%(asctime)s - %(filename)s - %(levelname)s - %(message)s'))


    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(cfmt)

    logs_dir = os.getenv("CSST_DFS_LOGS_DIR", "logs")    

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    # File handler
    fh = logging.handlers.RotatingFileHandler(os.path.join(logs_dir, 'csst_dfs.log'),
        maxBytes=10*1024*1024, backupCount=10)
    fh.setLevel(logging.INFO)
    fh.setFormatter(ffmt)

    # Create the logger,
    # adding the console and file handler
    csst_logger = logging.getLogger('csst')
    csst_logger.handlers = []
    csst_logger.setLevel(logging.DEBUG)
    csst_logger.addHandler(ch)
    csst_logger.addHandler(fh)

    # Set up the concurrent.futures logger
    cf_logger = logging.getLogger('concurrent.futures')
    cf_logger.setLevel(logging.DEBUG)
    cf_logger.addHandler(ch)
    cf_logger.addHandler(fh)

    return csst_logger

def setup_test_logging():
    # Console formatter, mention name
    cfmt = logging.Formatter(('%(name)s - %(levelname)s - %(message)s'))

    # File formatter, mention time
    ffmt = logging.Formatter(('%(asctime)s - %(levelname)s - %(message)s'))

    # Only warnings and more serious stuff on the console
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARN)
    ch.setFormatter(cfmt)

    logs_dir = os.getenv("CSST_DFS_LOGS_DIR", "logs")    

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    # Outputs DEBUG level logging to file
    fh = logging.FileHandler(os.path.join(logs_dir, 'csst_dfs_test.log'),
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(ffmt)

    # Set up the montblanc logger
    csst_logger = logging.getLogger('csst')
    csst_logger.handlers = []
    csst_logger.setLevel(logging.DEBUG)
    csst_logger.addHandler(ch)
    csst_logger.addHandler(fh)

    # Set up the concurrent.futures logger
    cf_logger = logging.getLogger('concurrent.futures')
    cf_logger.setLevel(logging.DEBUG)
    cf_logger.addHandler(ch)
    cf_logger.addHandler(fh)

    return csst_logger