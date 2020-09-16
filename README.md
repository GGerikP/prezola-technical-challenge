# Wedding Shop Technical Test (Prezola)

# (Meta Data normally not included in a repo): Candidate:
 - (Giles) Gerik Peterson
 - Submission Date: 16 Sept 2020
 - Source: https://github.com/GGerikP/prezola-technical-challenge

## Application Overview:

This is a simple application for creating a gift registry for wedding couples.  It uses Django as it's core, the rest_framework for a JSON API for accessing the data, and a handful of very simple Django templates to provide as an example of consuming the API endpoints.

## Installation:

### Dependencies:
 - python3.7
 - virtualenv
 - docker-compose (optional for running via docker)

### Setup:
 - configure and run your virtualenv
 - cd gift_registry
 - pip install -r requirements.txt
 - cp .env.example .env
 - fill in the relevant fields in the .env file
 - run ./setup.py (THIS WILL DELETE THE db.sqlite3 DATABASE if one exists in the project root directory - use with caution)
 - run ./manage changepassword admin (this is a dummy user)

### Run with Docker Compose
 - docker-compose up --build

### Run with django manager
 - ./manage.py runserver

## Unit Tests:
 - ./manage.py test

## Features:
The following are functions available to for the application:
- Add a gift to the list
- Remove a gift from the list
- List the already added gifts of the list 
- Purchase a gift from the list
- Generate a report from the list which will print out the gifts and their statuses.
  - The report must include two sections:
    - Purchased gifts: each purchased gift with their details.
    - Not purchased gifts: each available gift with their details.

## Extended Versions of the application would normally include:
 - A proper database (postgres, informix, mysql, etc)
 - Integration tests
 - A fully extracted front end (possibly React or angular) (The gift_registry_web would be removed along with all it's templates)
 - More thorough unit tests
 - Possibly a restructure using Flask rather than Django so that the models can be re-used in other applications (and more of the parts of the application turned into libraries)
 - It'd also be useful to link this up to Sentry so that we have an Exception notification system


