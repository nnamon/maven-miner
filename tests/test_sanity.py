#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module provides a single sanity test to demonstrate the import of the module is successful.
"""

import maven_miner.version


def test_project_version_exists():
    """Tests that the type of the version attribute of the package is string.
    """
    assert type(maven_miner.version.__version__) is str
