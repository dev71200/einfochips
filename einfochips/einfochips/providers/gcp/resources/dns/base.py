from einfochips.providers.gcp.resources.projects import Projects
from einfochips.providers.gcp.resources.dns.managed_zones import ManagedZones


class DNS(Projects):
    _children = [ 
        (ManagedZones, 'managed_zones')
     ]
