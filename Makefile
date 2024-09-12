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