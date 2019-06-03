#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: boluo
@LastEditors: boluo
@Date: 2019-06-03 13:37:42
@LastEditTime: 2019-06-03 13:45:44
@Description: 
'''
import time
import subprocess
def run_test_auto():
    download = subprocess.call(['wget', '-O', 'speedtest-cli',
                                'https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py'])
    add_run = subprocess.call(['chmod', '+x', 'speedtest-cli'])
    run_test = subprocess.call(['./speedtest-cli'])

if __name__ == "__main__":
    run_test_auto()
