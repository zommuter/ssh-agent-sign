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
    key = agent.get_keys()[0]  # TODO: #2 Key selection
    for line in fileinput.input():
        signature = key.sign_ssh_data(line)[15:]
        # TODO: #4 figure out whether it's always 15 bytes to skip (and why)
        print(hexdump.dump(signature,sep=''))
