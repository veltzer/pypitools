#!/bin/sh -e
PACKAGE=pypitools
# either remove the files that sphinx-apidoc generated
# or pass a -f flag to it
#rm -f doc/$PACKAGE.rst doc/$PACKAGE.scripts.rst doc/modules.rst
sphinx-apidoc -f -o doc $PACKAGE > /dev/null


\rm -rf out
# there is no need to pass '-b html' to sphinx-build since
# this is it's default
sphinx-build doc out
