#!/usr/bin/env python
#
#CustomScript extension
#
# Copyright 2014 Microsoft Corporation
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
#
# Requires Python 2.6+
#
import sys
import unittest
import env
import os
import json
import datetime
import installer

class TestInstall(unittest.TestCase):
    def test_install_psutil(self):
        buildDir = os.path.join(env.root, "../../Common/libpsutil")
        build = installer.find_psutil_build(buildDir)
        self.assertNotEquals(None, build)

if __name__ == '__main__':
    unittest.main()
