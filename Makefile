.PHONY: all

all:
	@pylint --rcfile=.pylint.rc --reports=n --score=n pypitools tests
	@pyflakes pypitools tests
	@pytest -qq > /dev/null
