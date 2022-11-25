from einfochips.providers.aws.facade.base import AWSFacade
from einfochips.providers.aws.resources.regions import Regions

from .queues import Queues


class SQS(Regions):
    _children = [
        (Queues, 'queues')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('sqs', facade)
