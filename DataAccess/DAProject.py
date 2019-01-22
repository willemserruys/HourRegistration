import sqlite3

from BusinessEntities.Project import Project


class DAProject:
    def __init__(self, session):
        self.Session = session

    def GetAll(self, includeNotActive):
        if not includeNotActive:
            return self.Session.query(Project).filter(Project.Actief == 1).all()
        else:
            return self.Session.query(Project)

    def GetProjectIDFromDescription(self, projectName):
        return self.Session.query(Project.ID).filter(Project.Description == projectName).first()

    # def GetProjectExterneID(self, projectID):

    # def Create(self, project):

    # def Update(self, project):

    # def DeleteByID(self, projectID):

    # def DeleteAll(self):

    # def GetByButton(self, buttonID, includeNotActive=False):
