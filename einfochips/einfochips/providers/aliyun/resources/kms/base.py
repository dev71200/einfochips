from einfochips.providers.aliyun.resources.regions import Regions
from einfochips.providers.aliyun.facade.base import AliyunFacade
from einfochips.providers.aliyun.resources.kms.keys import Keys


class KMS(Regions):
    _children = [
        (Keys, 'keys')
    ]

    def __init__(self, facade: AliyunFacade):
        super().__init__('kms', facade)
