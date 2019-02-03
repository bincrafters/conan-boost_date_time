#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostDate_TimeConan(base.BoostBaseConan):
    name = "boost_date_time"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_date_time"
    lib_short_names = ["date_time"]
    cycle_group = "boost_cycle_group_c"
    b2_requires = ["boost_cycle_group_c"]
