# recruitment_portal_service
A python back-end service for a job recruitment portal


# Basic Requirement
Python3.6


# Steps to run the current project locally (On Linux Machine):
1. Clone the repo https://github.com/AbhijithSivarajan/recruitment_portal_service
2. Run following command to install the dependencies (https://github.com/AbhijithSivarajan/recruitment_portal_service/blob/master/requirements.txt)

    pip install requirements.txt
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver
6. Service will start on http://localhost:8000
7. Try out the following APIs:

    a. '/api/v1/applicants/'

    b. '/api/v1/applicants/<<id>>'

    c. '/api/v1/organizations/'

    d. '/api/v1/organizations/<<id>>'

    e. '/api/v1/recruiters/'

    f. '/api/v1/recruiters/<<id>>'


# Technologies Used:
1. Django (2.0.7) WEB framework.
