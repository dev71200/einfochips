from einfochips.providers.gcp.resources.gce.subnetworks import Subnetworks
from einfochips.providers.gcp.resources.regions import Regions


class GCERegions(Regions):
    _children = [
        (Subnetworks, 'subnetworks')
    ]
