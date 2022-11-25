from einfochips.providers.aws.facade.base import AWSFacade
from einfochips.providers.aws.resources.base import AWSResources
from einfochips.providers.utils import get_non_provider_id


class SecurityGroups(AWSResources):
    def __init__(self, facade: AWSFacade, region: str):
        super().__init__(facade)
        self.region = region

    async def fetch_all(self):
        raw_security_groups = await self.facade.rds.get_security_groups(self.region)
        for raw_security_group in raw_security_groups:
            name, resource = self._parse_security_group(raw_security_group)
            self[name] = resource

    def _parse_security_group(self, raw_security_group):
        raw_security_group['arn'] = raw_security_group.pop('DBSecurityGroupArn')
        raw_security_group['name'] = raw_security_group.pop('DBSecurityGroupName')
        return get_non_provider_id(raw_security_group['name']), raw_security_group
