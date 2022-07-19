#!/usr/bin/env python
# Installs django-scim2

import os

from setuptools import find_packages, setup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def long_description():
    """Get the long description from the README"""
    return open(os.path.join(BASE_DIR, "README.md")).read()


def run_tests():
    os.environ["DJANGO_SETTINGS_MODULE"] = os.environ.get(
        "DJANGO_SETTINGS_MODULE", "test_settings"
    )

    import django

    django.setup()

    pass


setup(
    name="django-log-api",
    version="0.1.0",
    description="Allows download django log file via api",
    maintainer="luocy",
    maintainer_email="luocy77@gmail.com",
    author="luocy",
    author_email="luocy77@gmail.com",
    keywords="django log drf",
    license="MIT",
    long_description=long_description(),
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "Django>=2.2",
        "djangorestframework>=3.9.2",
        "tailhead>=1.0.2",
    ],
    tests_require=[
        "mock",
        "Django>=2.2,<4",
    ],
    test_suite="setup.run_tests",
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
