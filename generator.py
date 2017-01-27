#!/usr/bin/env python
'''
Filename:             generator.py
Date Created:         2017-01-27
Date Modified:        2017-01-27
Author:               Bastiaan van der Laaken
email:                mannerisms@gmail.com
Description:

Generates a number of files and folders with dummy data for testing purposes

'''

from mods.runner import Runner


def main():

    run = Runner()
    run.run()


if __name__ == '__main__':
    main()
