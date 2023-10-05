#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from fabric.api import *
from datetime import datetime
import os

env.hosts = ["ubuntu@54.90.32.25", "ubuntu@100.25.222.248"]

def do_pack():
    """Create a compressed archive from web_static folder."""
    local("mkdir -p versions")
    now = datetime.now()
    archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    result = local("tar -cvzf versions/{} web_static".format(archive_name))
    if result.succeeded:
        return os.path.join("versions", archive_name)
    else:
        return None

def do_deploy(archive_path):
    """Fabric script that distributes an archive to web servers"""
    try:
        with_ext = archive_path.split("/")[-1]
        without_ext = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp")
        run("mkdir -p /data/web_static/releases/" + without_ext)
        run(
            "tar -xzf /tmp/"
            + with_ext + " -C /data/web_static/releases/"
            + without_ext
        )
        run("rm /tmp/" + with_ext)
        run(
            "mv /data/web_static/releases/"
            + without_ext
            + "/web_static/* /data/web_static/releases/"
            + without_ext
        )
        run("rm -rf /data/web_static/releases/"
            + without_ext + "/web_static")
        run("rm -rf /data/web_static/current")
        run(
            "ln -s /data/web_static/releases/"
            + without_ext
            + "/ /data/web_static/current"
        )
        return True
    except Exception:
        return False


