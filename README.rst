#######
Renamer
#######

Rename files to countable number.

.. code-block:: python3

  % python3 -m renamer -s tests/sample
  Candidate to rename files (before ---> after).
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  0: tests/sample/a.txt ---> tests/sample/001.txt
  1: tests/sample/b.txt ---> tests/sample/002.txt
  Rename files? [y/N]: y
  Done.

Usage
#####

You have options.

.. code-block:: python3

  % python3 -m renamer -h
  usage: cli.py [-h] [-s SRC_DIR] [-i INDEX] [-r]

  optional arguments:
    -h, --help            show this help message and exit
    -s SRC_DIR, --src SRC_DIR
                          src directory to search files.
    -i INDEX, --index INDEX
                          start number to count (e.g. 001, 002, ...)
    -r, --recursive       search src directories recursively.


Author
######

sourjp

License
#######

MIT
