#!/usr/bin/env python

#===============================================================================
# Copyright 2015 Geoscience Australia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================

"""dbcleanup.py - Script to clean up the test database server.

This script attempts to drop all the temporary test databases on
the test database server. These may be left behind if the test that
creates them is unable to remove them after running for some reason.

It uses the dbutil TESTSERVER object, which can drop databases being
pooled by pgbouncer.

Note that running this script may cause tests currently running to fail
(by dropping their databases out from under them).
"""
from __future__ import absolute_import
import re
from . import dbutil

#
# Temporary test database pattern
#
# This is the regular expression used to identify a test database.
#
# The current pattern looks for a name containing 'test' and ending
# in an underscore followed by a 9 digit number.
#

TESTDB_PATTERN = r".*test.*_\d{9}$"

#
# Main program
#

db_list = dbutil.TESTSERVER.dblist()

test_db_list = [db for db in db_list if re.match(TESTDB_PATTERN, db)]

print "Dropping temporary test databases:"

if test_db_list:
    for db_name in db_list:
        if re.match(TESTDB_PATTERN, db_name):
            print "    %s" % db_name
            dbutil.TESTSERVER.drop(db_name)

else:
    print "    nothing to do."
