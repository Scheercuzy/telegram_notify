from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="Telegram Notify",
    version="1",
    python_requires=">=3.6",
    description="""A way to send notifications through Telegram""",
    long_description=readme(),
    url="https://github.com/Scheercuzy/telegram_notify",
    author="MX",
    author_email="maxi730@gmail.com",
    license="MIT",
    install_requires=[
        "amqp==5.0.1; python_version >= '3.6'",
        "appdirs==1.4.4",
        "apscheduler==3.6.3",
        "attrs==20.2.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "billiard==3.6.3.0",
        "black==19.10b0; python_version >= '3.6'",
        "cached-property==1.5.2",
        "celery==5.0.1",
        "cerberus==1.3.2",
        "certifi==2020.6.20",
        "cffi==1.14.3",
        "chardet==3.0.4",
        "click==7.1.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "click-didyoumean==0.0.3",
        "click-repl==0.1.6",
        "colorama==0.4.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "cryptography==3.1.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "decorator==4.4.2",
        "distlib==0.3.1",
        "flask==1.1.2",
        "idna==2.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "importlib-metadata==2.0.0; python_version < '3.8'",
        "itsdangerous==1.1.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "jinja2==2.11.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "kombu==5.0.2; python_version >= '3.6'",
        "markupsafe==1.1.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "orderedmultidict==1.0.1",
        "packaging==20.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "pathspec==0.8.0",
        "pep517==0.9.1",
        "pip-shims==0.5.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "pipenv-setup==3.1.1",
        "pipfile==0.0.2",
        "plette[validation]==0.2.3; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "prompt-toolkit==3.0.8; python_full_version >= '3.6.1'",
        "pycparser==2.20; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "pyparsing==2.4.7; python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "python-dateutil==2.8.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "python-telegram-bot==13.0",
        "pytz==2020.1",
        "redis==3.5.3",
        "regex==2020.10.15",
        "requests==2.24.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "requirementslib==1.5.13; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "six==1.15.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "sqlalchemy==1.3.20",
        "toml==0.10.1",
        "tomlkit==0.7.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "tornado==6.0.4; python_version >= '3.5'",
        "typed-ast==1.4.1",
        "typing==3.7.4.3; python_version < '3.7'",
        "tzlocal==2.1",
        "urllib3==1.25.11; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
        "uwsgi==2.0.19.1",
        "vine==5.0.0; python_version >= '3.6'",
        "vistir==0.5.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "wcwidth==0.2.5",
        "werkzeug==1.0.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "wheel==0.35.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "zipp==3.3.1; python_version < '3.8'",
    ],
    dependency_links=[],
    packages=find_packages(),
    include_package_data=True,
)
