
rm db.sqlite3
rm apps/gift_registry_api/migrations/0001_initial.py
./manage.py makemigrations
./manage.py migrate
./manage.py loaddata apps/gift_registry_api/fixtures/seed.json

