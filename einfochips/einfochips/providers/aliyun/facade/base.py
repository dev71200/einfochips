from collections import Counter

from aliyunsdkcore.endpoint.local_config_regional_endpoint_resolver import LocalConfigRegionalEndpointResolver

from einfochips.providers.aliyun.authentication_strategy import AliyunCredentials
from einfochips.providers.aliyun.facade.actiontrail import ActiontrailFacade
from einfochips.providers.aliyun.facade.ecs import ECSFacade
from einfochips.providers.aliyun.facade.kms import KMSFacade
from einfochips.providers.aliyun.facade.ram import RAMFacade
from einfochips.providers.aliyun.facade.rds import RDSFacade
from einfochips.providers.aliyun.facade.vpc import VPCFacade
from einfochips.providers.aliyun.facade.oss import OSSFacade
from einfochips.providers.utils import run_concurrently


class AliyunFacade:
    def __init__(self, credentials: AliyunCredentials):
        self._credentials = credentials
        self._instantiate_facades()
        self._resolver = LocalConfigRegionalEndpointResolver()

    def _instantiate_facades(self):
        self.actiontrail = ActiontrailFacade(self._credentials)
        self.ram = RAMFacade(self._credentials)
        self.ecs = ECSFacade(self._credentials)
        self.rds = RDSFacade(self._credentials)
        self.vpc = VPCFacade(self._credentials)
        self.kms = KMSFacade(self._credentials)
        self.oss = OSSFacade(self._credentials)

    async def build_region_list(self, service: str, chosen_regions=None):

        # TODO could need this for service ids
        # service = 'ec2containerservice' if service == 'ecs' else service

        # TODO does a similar endpoint exist?
        # available_services = await run_concurrently(lambda: Session().get_available_services())
        # if service not in available_services:
        #     raise Exception('Service ' + service + ' is not available.')

        regions = await run_concurrently(
            lambda: self._resolver.get_valid_region_ids_by_product(product_code=service))

        if chosen_regions:
            return list((Counter(regions) & Counter(chosen_regions)).elements())
        else:
            return regions
