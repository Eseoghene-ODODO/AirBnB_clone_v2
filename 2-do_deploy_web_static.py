#!/usr/bin/env python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import env, run, put
from os.path import exists


env.hosts = ['35.175.132.186', '54.164.162.231']


def do_deploy(archive_path):
    """Distribute an archive to the web servers"""

    # Check if the archive file exists
    if not exists(archive_path):
        return False
    # Get the name of the archive file without the extension
    archive_filename = archive_path.split("/")[-1]
    archive_basename = archive_filename.split(".")[0]
    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, "/tmp/{}".format(archive_filename))
    run("mkdir -p /data/web_static/releases/{}/".format(archive_basename))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
        .format(archive_filename, archive_basename))
    # Delete the archive from the web server
    run("rm /tmp/{}".format(archive_filename))
    run("mv /data/web_static/releases/{}/web_static/*
        /data/web_static/releases/{}/"
        .format(archive_basename, archive_basename))
    # Remove the empty web_static directory
    run("rm -rf /data/web_static/releases/{}/web_static"
        .format(archive_basename))
    # Delete the symbolic link /data/web_static/current from the web server
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(archive_basename))
    return True
