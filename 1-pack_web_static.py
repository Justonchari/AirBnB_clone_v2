from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Create a compressed archive from web_static folder."""
    # Create the versions directory if it doesn't exist
    local("mkdir -p versions")

    # Generate the archive name with timestamp
    now = datetime.now()
    archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

    # Create the archive using tar with gzip compression
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    if result.succeeded:
        return os.path.join("versions", archive_name)
    else:
        return None
