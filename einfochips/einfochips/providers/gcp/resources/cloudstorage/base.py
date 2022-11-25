from einfochips.providers.gcp.resources.projects import Projects
from einfochips.providers.gcp.resources.cloudstorage.buckets import Buckets


class CloudStorage(Projects):
    _children = [ 
        (Buckets, 'buckets')
    ]
