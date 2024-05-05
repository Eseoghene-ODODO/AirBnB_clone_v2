#!/usr/bin/env python3
"""
Fabric script that deletes out-of-date archives
"""

from fabric.api import *
import os


env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = '<username>'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = int(number)
    if number < 0:
        return None
    elif number == 0 or number == 1:
        number = 1
    else:
        number += 1

    with cd('/data/web_static/releases'):
        # List all archives
        archives = run("ls -1t").split()
        for arch in archives[number:]:
            # Delete old archives
            run("rm -rf {}".format(arch))

    with cd('/data/web_static/releases'):
        # List all directories
        directories = run("ls -1d */").split()
        for dire in directories:
            if dire != "test/":
                # Create path
                path = "/data/web_static/releases/" + dire
                # Get timestamp of directory
                date_str = run("stat -c %y {}".format(path))
                date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
                # Check if directory is old
                if (datetime.now() - date).days >= 30:
                    # Delete old directories
                    run("rm -rf {}".format(path))

    with lcd('versions'):
        # List all archives
        archives = local("ls -1t").split()
        for arch in archives[number:]:
            # Delete old archives
            local("rm -rf {}".format(arch))
