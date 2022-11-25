from einfochips.providers.aliyun.resources.regions import Regions
from einfochips.providers.aliyun.resources.vpc.vpcs import VPCs
from einfochips.providers.aliyun.facade.base import AliyunFacade


class VPC(Regions):
    _children = [
        (VPCs, 'vpcs')
    ]

    def __init__(self, facade: AliyunFacade):
        super().__init__('vpc', facade)
