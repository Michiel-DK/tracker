# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

check_code:
	@flake8 scripts/* tracker/*.py

black:
	@black scripts/* tracker/*.py

test:
	@coverage run -m pytest tests/*.py
	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"

ftest:
	@Write me

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr tracker-*.dist-info
	@rm -fr tracker.egg-info

install:
	@pip install . -U

all: clean install test black check_code

count_lines:
	@find ./ -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./scripts -name '*-*' -exec  wc -l {} \; | sort -n| awk \
		        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''

# ----------------------------------
#      UPLOAD PACKAGE TO PYPI
# ----------------------------------
PYPI_USERNAME=<AUTHOR>
build:
	@python setup.py sdist bdist_wheel

pypi_test:
	@twine upload -r testpypi dist/* -u $(PYPI_USERNAME)

pypi:
	@twine upload dist/* -u $(PYPI_USERNAME)



# ----------------------------------
#      CUSTOM HEROKU
# ----------------------------------

DATABASE_URL=postgres://burbwipnotnpnj:768bc2d4ef63c1ec1523a50c5957ad2e22a254bd8d9f60c97c842d28bfbbf0d1@ec2-52-211-158-144.eu-west-1.compute.amazonaws.com:5432/d4ms4jn7avepi2
LOCAL_DUMP=https://www.dropbox.com/s/6cmn7kplrito4uc/tracker.dump?dl=0

heroku_backup:
	@heroku pg:backups:restore ${LOCAL_DUMP} ${DATABASE_URL} -a stoml
