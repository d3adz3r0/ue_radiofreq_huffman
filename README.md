# DM Huffman

Program made for the informatic course of Pierre-Aimé Agnel, at the Institut Villebon Georges Charpak. Convert an ASCII text into a binary text compressed with
the Huffman coding.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure your machine have Python 3.6 up to date as well as the module 'sys' installed.

### Installing

Download the two files (class_arbre_feuille.py and huffman.py).
Place the two files into the repositorie  you want to use it into, then import it into your project, as follow:

```
import huffman.py
```

The module is now ready to be used.

## Running the tests

You can test the module is well imported by trying :

```
>>> Huffman(frequences('ABRACADABRA')).compresse('ABRACADABRA')
```

It should return:

```
01101110100010101101110
```

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/)
* [GitHub](https://github.com)

## Contributing

* **Pierre-Aimé Agnel** - *Help* - [PA-Agnel](https://github.com/PA-Agnel)

## Authors

* **Mathieu Van de catsije** - *Initial work* - [d3adz3r0](https://github.com/d3adz3r0)

## Acknowledgments

* [Python-prepa](https://python-prepa.github.io/information_theory.html)
* Many different post on the [Stackoverflow](https://stackoverflow.com/) forum

