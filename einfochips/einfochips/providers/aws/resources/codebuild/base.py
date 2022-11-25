from einfochips.providers.aws.facade.base import AWSFacade
from einfochips.providers.aws.resources.regions import Regions

from .build_projects import BuildProjects


class CodeBuild(Regions):
    _children = [
        (BuildProjects, 'build_projects')
    ]

    def __init__(self, facade: AWSFacade):
        super().__init__('codebuild', facade)
