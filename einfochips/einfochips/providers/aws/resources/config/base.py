from einfochips.providers.aws.facade.base import AWSFacade
from einfochips.providers.aws.resources.config.recorders import Recorders
from einfochips.providers.aws.resources.config.rules import Rules
from einfochips.providers.aws.resources.regions import Regions


class Config(Regions):
    _children = [
        (Recorders, 'recorders'),
        (Rules, 'rules')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('config', facade)
