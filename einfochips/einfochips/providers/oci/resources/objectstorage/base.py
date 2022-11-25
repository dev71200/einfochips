from einfochips.providers.oci.facade.base import OracleFacade
from einfochips.providers.oci.resources.base import OracleCompositeResources
from einfochips.providers.oci.resources.objectstorage.buckets import Buckets


class ObjectStorage(OracleCompositeResources):
    _children = [
        (Buckets, 'buckets')
    ]

    def __init__(self, facade: OracleFacade):
        super().__init__(facade)
        self.service = 'objectstorage'

    async def fetch_all(self, **kwargs):
        await self._fetch_children(resource_parent=self)
