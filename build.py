from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.pycharm")

name = "jobhunt_ase"
version = "1.0"

summary = "Wb Scraper / Git project"
url = "https://github.com/iramshiv/jobhunt_ase"

description = """Web Scraping."""

Author = "iramshiv"
default_task = "publish"


@init
def initialize(project):
    project.build_depends_on("mockito")
    project.set_property("run_unit_tests_command", "py.test %s" % project.expand_path("/src/main/unittest/python"))
    project.set_property("run_unit_tests_propagate_stdout", True)
    project.set_property("run_unit_tests_propagate_stderr", True)


@init
def set_properties(project):
    pass
