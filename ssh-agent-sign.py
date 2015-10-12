# -*- coding: utf-8 -*-
"""
@author: Tobias Kienzler
"""

from __future__ import print_function
import paramiko
import fileinput
import hexdump


if __name__ == "__main__":
    agent = paramiko.Agent()
    key = agent.get_keys()[0]  # TODO: Key selection
    for line in fileinput.input():
        signature = key.sign_ssh_data(line)
        print(hexdump.dump(signature,sep=''))
