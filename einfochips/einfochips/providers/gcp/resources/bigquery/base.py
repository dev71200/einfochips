from einfochips.providers.gcp.resources.bigquery.datasets import Datasets
from einfochips.providers.gcp.resources.projects import Projects


class BigQuery(Projects):
    _children = [
        (Datasets, 'datasets')
    ]
