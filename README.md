<br/>
<p align="center">
  <a href="https://github.com/ckoorosh/WeTube">
    <img src="https://raw.githubusercontent.com/ckoorosh/WeTube/master/WeTube/home/static/images/WeTube-Logo.png" alt="Logo">
  </a>

  <h3 align="center">WeTube</h3>

  <p align="center">
    An online video sharing and streaming app developed with Django framework
    <br/>
    <br/>
  </p>
</p>

## About The Project

![Screen Shot](https://raw.githubusercontent.com/ckoorosh/WeTube/master/docs/home.png)

WeTube is an online video sharing and streaming app developed with Django framework. The app is designed to be a clone of YouTube with some of its basic features. It is developed as a project for the "Computer Networks" course at Sharif University of Technology.

## Built With

* [Django](https://www.djangoproject.com/)
* [Font Awesome](https://fontawesome.com)


## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.7
* Django 3.1.2


### Installation

1. Clone the repo

```sh
git clone https://github.com/ckoorosh/WeTube.git
```

2. Install Python packages

```sh
pip install -r requirements.txt
```

3. Run the server

```sh
python WeTube/manage.py runserver
```

For using the proxy, you also need to run the proxy server:

```sh
python proxy/manage.py runserver
```

4. Open the app in your browser

```sh
http://127.0.0.1:8080
```

## License

Distributed under the MIT License. See [LICENSE](https://github.com/ckoorosh/WeTube/blob/master/LICENSE) for more information.
