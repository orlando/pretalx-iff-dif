import os
from distutils.command.build import build

from django.core import management
from setuptools import find_packages, setup

try:
    with open(
        os.path.join(os.path.dirname(__file__), "README.rst"), encoding="utf-8"
    ) as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""


class CustomBuild(build):
    def run(self):
        management.call_command("compilemessages", verbosity=1)
        build.run(self)


cmdclass = {"build": CustomBuild}


setup(
    name="pretalx-iff-dif",
    version="0.0.0",
    description="Plugin to add a way to manage speakers applying for the IFF Diversity and Inclusion Fund",
    long_description=long_description,
    url="https://github.com/internetfreedomfestival/pretalx-iff-dif",
    author="Orlando Del Aguila",
    author_email="orlando@hashlabs.com",
    license="Apache Software License",
    install_requires=[],
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretalx.plugin]
pretalx_iff_dif=pretalx_iff_dif:PretalxPluginMeta
""",
)
