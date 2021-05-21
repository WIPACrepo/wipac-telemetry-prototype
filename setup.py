"""Setup."""


import os
import subprocess

from setuptools import setup  # type: ignore[import]

subprocess.run(
    "pip install git+https://github.com/WIPACrepo/wipac-dev-tools.git".split(),
    check=True,
)
from wipac_dev_tools import SetupShop  # noqa: E402  # pylint: disable=C0413

shop = SetupShop(
    "wipac_telemetry",
    os.path.abspath(os.path.dirname(__file__)),
    ((3, 6), (3, 8)),
    "WIPAC-Specific OpenTelemetry Tools",
)

setup(
    **shop.get_kwargs(
        other_classifiers=["License :: OSI Approved :: MIT License"],
        subpackages=["tracing_tools"],
    ),
    url="https://github.com/WIPACrepo/wipac-telemetry-prototype",
    license="MIT",
    package_data={shop.name: ["py.typed"]},
)
