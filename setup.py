from distutils.core import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name='LatvianStemmer',
    version='1.0.2',
    description='Light stemmer for Latvian.',
    py_modules=['LatvianStemmer'],
    author='Rihards Krišlauks',
    author_email='rihizs@gmail.com',
    url='https://github.com/rihardsk/LatvianStemmer',
    license='Apache License, Version 2.0',
    long_description=readme,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        "console_scripts": [
            "lvstemmer = LatvianStemmer:main"
        ]
    }
)
