from einfochips.providers.aws.facade.base import AWSFacade
from einfochips.providers.aws.resources.regions import Regions
from .stacks import Stacks


class CloudFormation(Regions):
    _children = [
        (Stacks, 'stacks')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('cloudformation', facade)
