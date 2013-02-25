from distutils.core import setup

setup(
    name='alexa',
    version='0.1.0',
    author='Ben Belchak',
    author_email='ben@belchak.com',
    packages=['alexa', 'alexa.api'],
    url='http://pypi.python.org/pypi/py-alexa/',
    description='Pythonic Alexa Web Information Service API',
    install_requires=[
        "requests >= 1.1.0",
        ],
    )