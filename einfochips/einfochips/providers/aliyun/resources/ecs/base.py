from einfochips.providers.aliyun.facade.base import AliyunFacade
from einfochips.providers.aliyun.resources.regions import Regions
from einfochips.providers.aliyun.resources.ecs.instances import Instances


class ECS(Regions):
    _children = [
        (Instances, 'instances')
    ]

    def __init__(self, facade: AliyunFacade):
        super().__init__('ecs', facade)
