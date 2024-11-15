#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################################
# @Author: yangzhengfeng
# @Date: 2017-04-28 14:24:22
# @Last Modified by:  yangzhengfeng
# @Last Modified time: 2017-04-28 14:24:22
#####################################################

import shutil
import os
import json

def pjson(obj):
    print(json.dumps(obj, indent=2))

def get_files():
    sider = ''
    for dpath, _, fnames in os.walk('.'):
        if dpath in ['.','static', '.obsidian']:
            continue
        sider +='== {}'.format(dpath[2:]) + '\n'
        for fname in fnames:
            if '.md' in fname:
                fmt = '* [{name}]({path})'
                sider += fmt.format(name = fname.replace('.md',''), path = dpath + '/' + fname) + '\n'
    with open('_sidebar.md', 'w+') as f:
        f.write(sider)
    print(sider)
    return

def main():
    get_files()
    print('done...')

if __name__ == '__main__':
    main()

