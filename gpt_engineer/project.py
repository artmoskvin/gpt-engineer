from gpt_engineer.db import DBs


class Project:
    def __init__(self, dbs: DBs):
        self.dbs = dbs

    def update(self, diff):
        """Updates project files based on the diff"""
        # TODO: how do we represent diff?
        raise NotImplementedError

    def run_tests(self):
        """Runs tests"""
        # TODO: should it be here?
        raise NotImplementedError
