"""Behavioural tests for pypitools' package-name helpers.

get_package_filename and get_package_wheelname build dist paths from
the package full name. The full name itself comes from setup.py via a
subprocess, so it is patched out; the pure path-joining logic under
test is real.
"""

import os
import unittest
from unittest import mock

from pypitools import name_utils


class NameUtilsTests(unittest.TestCase):
    def test_filename_is_sdist_tarball_in_dist(self) -> None:
        with mock.patch.object(name_utils, "get_package_fullname", return_value="pypitools-1.2.3"):
            self.assertEqual(name_utils.get_package_filename(), os.path.join("dist", "pypitools-1.2.3.tar.gz"))

    def test_wheelname_is_py3_none_any_wheel_in_dist(self) -> None:
        with mock.patch.object(name_utils, "get_package_fullname", return_value="pypitools-1.2.3"):
            self.assertEqual(
                name_utils.get_package_wheelname(),
                os.path.join("dist", "pypitools-1.2.3-py3-none-any.whl"),
            )

    def test_filename_reflects_the_fullname(self) -> None:
        with mock.patch.object(name_utils, "get_package_fullname", return_value="other-9.9"):
            self.assertEqual(name_utils.get_package_filename(), os.path.join("dist", "other-9.9.tar.gz"))


if __name__ == "__main__":
    unittest.main()
