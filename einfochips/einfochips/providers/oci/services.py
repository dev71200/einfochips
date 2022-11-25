from einfochips.providers.oci.authentication_strategy import OracleCredentials
from einfochips.providers.oci.facade.base import OracleFacade
from einfochips.providers.oci.resources.identity.base import Identity
from einfochips.providers.oci.resources.kms.base import KMS
from einfochips.providers.oci.resources.objectstorage.base import ObjectStorage
from einfochips.providers.base.services import BaseServicesConfig


class OracleServicesConfig(BaseServicesConfig):
    def __init__(self, credentials: OracleCredentials = None, **kwargs):
        super().__init__(credentials)

        facade = OracleFacade(credentials)

        self.identity = Identity(facade)
        self.objectstorage = ObjectStorage(facade)
        self.kms = KMS(facade)

    def _is_provider(self, provider_name):
        return provider_name == 'oci'
