from gpt_engineer.ai import AI
from gpt_engineer.project import Project


class SoftEngAgent:
    def __init__(self, ai: AI):
        self.ai = ai
        # TODO: should we pass project on init?
        #  i.e. 1 agent <-> 1 project or 1 agent <-> N projects

    def create_spec(self, user_input: str) -> str:
        """Creates spec from user's prompt. Asks clarifying questions."""
        # uses steps here
        raise NotImplementedError

    def update_project(self, project: Project, spec: str) -> Project:
        """Update project based on the spec. Project can be empty."""
        # uses steps here
        raise NotImplementedError

    def run_tests(self, project: Project):
        """Runs tests for the project"""
        # uses steps here
        raise NotImplementedError

    def run_project(self, project: Project):
        """Runs project locally"""
        # uses steps here
        raise NotImplementedError

    def deploy_project(self, project: Project):
        """Deploys project"""
        # uses steps here
        raise NotImplementedError
