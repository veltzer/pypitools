.PHONY: all

all:
	@pylint --rcfile=.pylint.rc --reports=n --score=n pypitools tests
	@pyflakes pypitools tests
	@pytest -qq > /dev/null


.PHONY: black
black:
	black --target-version py36 pypitools tests config
