# 목표

Django 애플리케이션의 기본 뼈대를 제공한다. Two Scoops of Django 책을 참고로 작성하였다.

cookiecutter를 올바로 활용하려면 다소 많은 배경지식을 필요로 해서 간단한 템플릿을 만들고자 한다.

가장 기본이 되는 내용으로 구성하고 --template 옵션으로 새 프로젝트를 간단히 시작할 수 있도록 한다.

## 프로젝트의 생성

```
django-admin.py startproject --template https://gitlab.com/mairoo/django-quickstarter/repository/archive.zip repo
```

## 프로젝트 실행

서버 실행을 하려면 설정 모듈을 정확히 지정해야 한다.

* 명령행 옵션으로 지정: ```--settings=config.settings.local```
* 환경변수로 지정: ```DJANGO_SETTINGS_MODULE=config.settings.local```

아래와 같이 명령행 옵션으로 테스트 서버를 구동할 수 있다.

```
manage.py runserver --settings=config.settings.local
```

위 예시의 ```local```이 아닌 ```production```, ```test``` 등으로 구체적인 설정 파일을 지정할 수 있다.

# Djagno-Quickstarter

## 템플릿 구조

굳이 저장소 루트와 프로젝트 루트 단계를 나눌 필요는 없을 것 같아 repository-config 2단계 구조로 정의한다.

다만 다른 프로젝트와 구별할 수 있도록 프로젝트 이름의 최상위 디렉토리의 이름을 짓는다.

```
<프로젝트_이름>/
    repo/
        conf/
            settings/
                base.py
                local.py
                production.py
        manage.py
    venv/
    run/
        uwsgi.ini
        uwsgi.sock
        gunicorn.sock
    logs/
        access.log
        error.log
        uwsgi.log
    ssl/
```

```프로젝트_이름``` 최상위 디렉토리의 하위 디렉토리 5개의 의미는 다음과 같다.

* ```repo```: 저장소 루트 디렉토리이면서 동시에 프로젝트 루트가 된다.
* ```venv```: 종속성 분리를 제공하기 위한 독립된 가상환경 virtualenv 디렉토리이다.
* ```run```: uWSGI 서버 배포시 소켓이 저장되는 디렉토리이다. ```manage.py runserver```로 서버를 구동한다면 불필요하다.
* ```logs```: uWSGI 서버 로그 및 nginx 로그 등이 저장되는 디렉토리이다.
* ```ssl```: SSL 서버 운영을 위해 여러 공개키/비공개키 등을 저장하는 디렉토리이다.

```repo```, ```venv```, ```run```, ```logs```, ```ssl``` 디렉토리 모두 이름을 약속해서 다른 Django 프로젝트를 개발하더라도 쉽게 구조를 파악할 수 있도록 같은 이름으로 일관성을 유지한다.

## 명령어 요약

```
## 명령어 정리

본 프로젝트의 구조를 위한 아래와 같이 정리할 수 있다.

```
pyvenv venv
source venv/bin/activate
pip install Django
mkdir repo run logs ssl
sudo chown $(whoami):www-data run
cd repo
django-admin.py startproject conf .
```
