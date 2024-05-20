# About CLEARPATH

ClearPath is a web Project Management tool to help Project Management Professional manage projects and teams of any demand and size respectively.

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Contributing (Optional)](#contributing)
* [Installation-MacOs](#installation-macos)
* [Installation-Windows](#installation-windows)
* [Continue](#continue)
* [Commands used-OS X or Linux](#commands-used-os-x-or-linux)
* [Commands used-Windows](#commands-used-windows)
* [Libraries](#libraries)
* [Best Practices](#best-practices)
* [Git commit message types](#git-commit-message-types)
* [Streamlining Workflow with Git Flow Branch Naming Conventions](#streamlining-workflow-with-git-flow-branch-naming-conventions)
* [Contribution](#contribution)
* [Additional Information (Optional)](#additional-information)

## Installation

Here are the steps to install and run the project:

1. Clone the repository ...
2. Checkout to "feature" branch
3. Install dependencies ...
4. Run the project ...

## Usage

Here's how to use the project functionalities:

* ... (instructions with code snippets or screenshots)

## Contributing

We welcome contributions to this project! Here's how you can get involved:

* Below are contribution guidelines to follow:

## Installation-MacOS

Always refer to the [Django Installation](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)

1. Clone this repo and navigate to gospives folder
2. Set Up Virtual Environment: `python3 -m venv venv`
3. Activate Virtual Environment: `source venv/bin/activate`

## Installation-Windows

1. Clone this repo and navigate to Backend folder
2. Set Up Virtual Environment: `python -m venv venv`
3. Activate Virtual Environment: `source venv\Scripts\activate.bat`

## Continue

1. Install all dependecies: `pip install -r requirements.txt`
2. Create `.env` file in the root folder.
3. Perform Initial Database Migrations: `python3 manage.py migrate`
4. (Optional) Create Superuser: `python3 manage.py createsuperuser`
5. Run Development Server: `python3 manage.py runserver`

## Commands used-OS X or Linux

* `python3 -m venv venv`
* `source venv/bin/activate`
* `python -m pip install --upgrade pip`
* `django-admin startproject clearpath_home .`
* `python3 manage.py migrate`
* `python3 manage.py runserver`
* `python3 manage.py createsuperuser`
* `python3 manage.py startapp [AppName]`
* Add these dependencies to your requirements.txt file:`pip freeze > requirements.txt`
* Protect SECRET_KEYS - `pip install python-dotenv`

## Commands used-Windows

* `python -m venv venv`
* `source venv\Scripts\activate.bat`
* `django-admin startproject clearpath_home .`
* `python manage.py migrate`
* `python manage.py runserver`
* `python manage.py createsuperuser`
* `python manage.py startapp [AppName]`
* Add these dependencies to your requirements.txt file:`pip freeze > requirements.txt`
* Protect SECRET_KEYS - `pip install python-dotenv`

## Libraries

1. [Django REST framework](https://www.django-rest-framework.org/)
2. [django-cors-headers](https://pypi.org/project/django-cors-headers/)
3. [django-rest-auth](https://django-rest-auth.readthedocs.io/en/latest/installation.html)
4. [django-allauth](https://docs.allauth.org/en/latest/installation/quickstart.html)
5. [django-nextjs](https://pypi.org/project/django-nextjs/)

## Best Practices

1. Keep Django Updated: Always stay on the latest version of Django. Regularly update your project to benefit from security fixes and improvements. Major releases occur approximately every 9 months, with minor releases addressing security and bugs almost monthly (<https://learndjango.com/tutorials/django-best-practices-security>)

2. Environment Variables:
    * Use environment variables to manage settings between local development and production environments. These variables allow you to switch configurations seamlessly.
    * Consider using packages like `environs` to handle environment variables effectively.

3. DEBUG Mode:
In your `settings.py`, ensure that the `DEBUG` setting is set to `False` in production. Debug mode provides detailed error pages, which can be a security risk if exposed publicly. Read more on: (<https://learndjango.com/tutorials/django-best-practices-security>)

4. SECRET_KEY:
    * Keep the `SECRET_KEY` confidential. It’s used for cryptographic signing and should never be shared or exposed.
    * Generate a strong, random `SECRET_KEY` during project setup.
    * To Generate a New `SECRET_KEY` in Django, follow the instructions provided on this website: (<https://www.makeuseof.com/django-secret-key-generate-new/>)

5. Authorization and Authentication:
    * Implement robust authorization and authentication mechanisms using Gmail, iCloud and other Social Media platforms.
    * Avoid custom authentication solutions unless necessary.

6. Secure Configurations:
    * Properly configure the application settings. Guard against common vulnerabilities like cross-site scripting (XSS) and cross-site request forgery (CSRF).
    * Use HTTPS to encrypt data in transit.

7. Rate Limiting and Brute-Force Protection:
    * Implement rate limiting to prevent brute-force attacks.
    * Consider using packages like `django_ratelimit` or `django-axes`.

8. Third-Party Dependencies:
    * Regularly review and update third-party packages. Vulnerabilities in dependencies can impact the application’s security.
    * Use tools like `pip-tools` to manage dependencies efficiently.

9. Security Audits:
    * Perform automated security audits regularly. Tools like `Lynis` can help identify potential issues.
    * Monitor logs and track suspicious activity.

10. Database Security:
    * Secure your database connections. Use strong passwords and restrict access.
    * Avoid using default database credentials.

## Git commit message types

1. *feat:* Introducing new features or significant improvements.
2. *fix:* Bug fixes that resolve issues in your code.
3. *docs:* Updates or additions to documentation.
4. *style:* Cosmetic changes that don't affect code functionality (like formatting).
5. *refactor:* Code changes that neither fix a bug nor add a feature but improve structure.
6. *test:* Everything about testing - adding or fixing tests.
7. *chore:* Routine tasks or updates to the build process.
8. *perf:* Enhancements that improve performance.
9. *ci:* Modifications related to CI/CD processes.
10. *build:* Changes affecting the build system or external dependencies.
11. *revert:* Undoing previous changes.

## Streamlining Workflow with Git Flow Branch Naming Conventions

*Git Flow* is a branching strategy that helps manage and structure various phases of a project.

1. *master:* The source of truth for production-ready states.
2. *develop:* The integration branch for development work.
3. *feature/:* For developing new features, e.g., feature/add-login.
4. *release/:* Preparing a new production release, e.g., release/1.2.0.
5. *hotfix/:* Quick fixes for the production version, e.g., hotfix/critical-login-bug.
6. *support/:* Long-term support for older versions, e.g., support/1.x.
7. *bugfix/:* For specific bug fixes (optional), e.g., bugfix/login-error.

## Contribution

Please refer to the CONTRIBUTING.md for guidance.

## Additional Information

* website: <https://clearpath.com>
* E-mail: <contributions@clearpath.com>
