# recruitment_portal_service
A python back-end service for a job recruitment portal


# Basic Requirement
Python3.6


# Steps to run the project locally:
1. Clone the repo https://github.com/AbhijithSivarajan/recruitment_portal_service
2. Run following command to install the dependencies (https://github.com/AbhijithSivarajan/recruitment_portal_service/blob/master/requirements.txt)

    pip3 install -r requirements.txt
3. python3 manage.py makemigrations
4. python3 manage.py migrate
5. python3 manage.py runserver
6. Service will start on http://localhost:8000
7. Try out the following APIs:

    a. '/api/v1/applicants/'

    b. '/api/v1/organizations/'

    c. '/api/v1/recruiters/'


# Technologies Used:
1. Django (2.0.7) WEB framework.
