from einfochips.providers.gcp.resources.projects import Projects
from einfochips.providers.gcp.resources.iam.member_bindings import Bindings
from einfochips.providers.gcp.resources.iam.users import Users
from einfochips.providers.gcp.resources.iam.groups import Groups
from einfochips.providers.gcp.resources.iam.domains import Domains
from einfochips.providers.gcp.resources.iam.service_accounts import ServiceAccounts
from einfochips.providers.gcp.resources.iam.bindings_separation_duties import BindingsSeparationDuties


class IAM(Projects):
    _children = [
        (Bindings, 'bindings'),
        (Users, 'users'),
        (Groups, 'groups'),
        (ServiceAccounts, 'service_accounts'),
        (Domains, "domains"),
        (BindingsSeparationDuties, 'bindings_separation_duties')
    ]
