from einfochips.providers.aws.facade.base import AWSFacade
from einfochips.providers.aws.resources.regions import Regions

from .vpcs import ELBv2Vpcs


class ELBv2(Regions):
    _children = [
        (ELBv2Vpcs, 'vpcs')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('elbv2', facade)
