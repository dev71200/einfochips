from einfochips.providers.gcp.resources.projects import Projects
from einfochips.providers.gcp.resources.gke.clusters import Clusters


class KubernetesEngine(Projects):
    _children = [
        (Clusters, 'clusters')
    ]

    async def fetch_all(self):
        await Projects.fetch_all(self)
