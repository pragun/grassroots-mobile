#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(url='sqlite:///db/sqlite/test.db', debug='False', repository='db/test')
