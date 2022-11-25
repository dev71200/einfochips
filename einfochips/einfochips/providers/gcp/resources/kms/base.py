from einfochips.providers.gcp.resources.kms.keyrings import KeyRings
from einfochips.providers.gcp.resources.projects import Projects


class KMS(Projects):
    _children = [
        (KeyRings, 'keyrings')
    ]
