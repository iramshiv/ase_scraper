from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.pycharm")

name = "jobhunt_ase"
version = "1.0"

summary = "Wb Scraper / Git project"
url = "https://github.com/iramshiv/jobhunt_ase"

description = """Web Scraping."""

Author = "iramshiv"
license = "None"
default_task = "publish"


@init
def initialize(project):
    project.build_depends_on("mockito")


@init
def set_properties(project):
    pass
