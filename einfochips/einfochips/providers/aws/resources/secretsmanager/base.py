from einfochips.providers.aws.facade.base import AWSFacade
from einfochips.providers.aws.resources.regions import Regions

from .secrets import Secrets


class SecretsManager(Regions):
    _children = [
        (Secrets, 'secrets')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('secretsmanager', facade)
