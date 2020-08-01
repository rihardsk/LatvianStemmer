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

Usage
-----

```sh
pip install LatvianStemmer
lvstemmer < input.txt > output.txt
# or
lvstemmer input1.txt input2.txt > output.txt
```
