#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostDate_TimeConan(base.BoostBaseConan):
    name = "boost_date_time"
    url = "https://github.com/bincrafters/conan-boost_date_time"
    lib_short_names = ["date_time"]
    cycle_group = "boost_level11group"
    b2_requires = [
        "boost_level11group",
    ]