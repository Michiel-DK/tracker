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

heroku_backup:
	@heroku pg:backups:restore ${LOCAL_DUMP} DATABASE_URL --app stoml --confirm stoml

heroku_push:
	@heroku pg:push iex DATABASE_URL --app stoml


# ----------------------------------
#      POSTGRES
# ----------------------------------

postgres_dump:
	@pg_dump -U postgres -h localhost -p 54321 tracker > database_dump/tracker.dump

# ----------------------------------
#      API
# ----------------------------------

run_api:
	@uvicorn fast.api:app --reload  # load web server with code autoreload

# ----------------------------------
#      STREAMLIT
# ----------------------------------

run_streamlit:
	@streamlit run app.py 