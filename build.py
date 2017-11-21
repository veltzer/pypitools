#!/usr/bin/env python

from pydmt.builders.sphinx import Sphinx
from pydmt.core.pydmt import PyDMT
from pydmt.features.templating import Templating
import pylogconf

pylogconf.setup()
p = PyDMT()
f = Templating()
f.setup(p)
b = Sphinx(package_name="pypitools")
p.add_builder(b)
p.build_all()
