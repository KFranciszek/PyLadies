#!/usr/bin/python
# -*- coding: UTF-8 -*-

from swDict import swDict

hero200plusFile = open('hero200plus.txt', 'w')
heroShortFile = open('heroShort.txt', 'w')

for name, traits in swDict.items():
    if swDict[name]['height'] > 200:
        hero200plusFile.write('{}\n'.format(str({name: traits})))
    else:
        heroShortFile.write('{}\n'.format(str({name: traits})))

hero200plusFile.close()
heroShortFile.close()
