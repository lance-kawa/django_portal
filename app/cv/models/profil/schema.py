from cv.models.theme import Theme
from cv.models.diplome import Diplome
from cv.models.experience import Experience
from cv.models.skill import Skill
from cv.models.project import Project
import typing as t

SubProfil = t.Union[Diplome, Experience, Skill, Project, Theme]