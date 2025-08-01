from setuptools import setup, find_packages

setup(
    name="apipie",  # MUST be unique on PyPI
    version="0.4.51",
    description="A simple API proxy with rate limiting and API key support for api organization.",
    author="kokorocks",
    packages=find_packages(),  # No 'where="src"' needed
    install_requires=[
        "sanic",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "apipie=apipie.main:main"  # Refers to apipie/main.py
        ]
    },
    python_requires=">=3.7",
)
