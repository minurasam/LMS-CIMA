An E-Learning Platform for CIMA Students 

## Getting Started
### Installation

1. Clone the respository:

    ```
    git clone https://github.com/minurasam/LMS-CIMA.git
    ```
This will be an online website hosted by Heroku 
https://dashboard.heroku.com/apps/lms-cima/deploy/github

Install the requirements:

```bashRun 
pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)
pip freeze > requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

## Built With

* [Python/Django](https://www.djangoproject.com/start/overview)
* [Bootstrap](https://github.com/twbs/bootstrap)
* [Font Awesome](https://github.com/FortAwesome/Font-Awesome)


## Authors

See the detailed list of [contributors](https://github.com/minurasam123/MainDashboard/graphs/contributors) who contributed to this project.

## License

This project is licensed under the [GPL-3 License.](https://github.com/AromedMedical/aromed-web/blob/master/LICENSE)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
