from einfochips.providers.aliyun.resources.regions import Regions
from einfochips.providers.aliyun.resources.rds.instances import Instances
from einfochips.providers.aliyun.facade.base import AliyunFacade


class RDS(Regions):
    _children = [
        (Instances, 'instances')
    ]

    def __init__(self, facade: AliyunFacade):
        super().__init__('rds', facade)

