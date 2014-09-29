from distutils.core import setup

setup(
    name='LatvianStemmer',
    version='1.0.1',
    description='Light stemmer for Latvian.',
    py_modules=['LatvianStemmer'],
    author='Rihards Krišlauks',
    author_email='rihizs@gmail.com',
    url='https://github.com/rihardsk/LatvianStemmer',
    license='Apache License, Version 2.0',
    long_description='''==============
LatvianStemmer
==============

The original Java code can be found in https://github.com/apache/lucene-solr

Ported to Python by Rihards Krišlauks with minor modifications

Light stemmer for Latvian.
--------------------------

This is a light version of the algorithm in Karlis Kreslin's PhD thesis *A stemming algorithm for Latvian* with the following modifications:

* Only explicitly stems noun and adjective morphology
* Stricter length/vowel checks for the resulting stems (verb etc suffix stripping is removed)
* Removes only the primary inflectional suffixes: case and number for nouns case, number, gender, and definitiveness for adjectives.
* Palatalization is only handled when a declension II,V,VI noun suffix is removed.

''',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)