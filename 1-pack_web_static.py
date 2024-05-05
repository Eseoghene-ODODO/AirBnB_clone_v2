#!/usr/bin/env python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Archive the contents of web_static folder"""
    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Get the current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    # Create the name of the archive
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Create the path of the archive
    archive_path = "versions/{}".format(archive_name)

    # Create the archive
    result = local("tar -cvzf {} web_static".format(archive_path))

    # Return the path of the archive if it was created successfully
    if result.succeeded:
        return archive_path
    else:
        return None
