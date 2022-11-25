from einfochips.providers.gcp.resources.projects import Projects
from einfochips.providers.gcp.resources.stackdriverlogging.logging_metrics import LoggingMetrics
from einfochips.providers.gcp.resources.stackdriverlogging.sinks import Sinks
from einfochips.providers.gcp.resources.stackdriverlogging.metrics import Metrics


class StackdriverLogging(Projects):
    _children = [ 
        (Sinks, 'sinks'),
        (Metrics, 'metrics'),
        (LoggingMetrics, 'logging_metrics')
    ]
