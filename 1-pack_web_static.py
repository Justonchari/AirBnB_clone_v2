#!/usr/bin/python3
""" Fabric script that generates a .tgz archive """
from fabric.api import local
from datetime import datetime
import os


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
