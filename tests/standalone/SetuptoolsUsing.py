#     Copyright 2024, Kay Hayen, mailto:kay.hayen@gmail.com find license text at end of file


# nuitka-project: --standalone
# nuitka-project: --noinclude-setuptools-mode=allow

from __future__ import print_function

# Demonstrate that this module, that anti-bloat fights really hard to
# avoid, actually still works.
import setuptools

print("OK.")

#     Python test originally created or extracted from other peoples work. The
#     parts from me are licensed as below. It is at least Free Software where
#     it's copied from other people. In these cases, that will normally be
#     indicated.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.