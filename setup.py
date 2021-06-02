import setuptools
import os
import site
from typing import List
from setuptools import find_packages
with open("README.rst", "r") as fh:
    long_description = fh.read()


def find_stub_files(name: str) -> List[str]:
    result = []
    for root, dirs, files in os.walk(name):
        for file in files:
            if file.endswith(".pyi"):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result

def build_data_files_list() -> List[tuple]:
    result = []
    for package in os.listdir("circuitpython-stubs"):
        result.append((site.getsitepackages()[0] + "/" + package + "/",
                       ["circuitpython-stubs/{}/__init__.pyi".format(package)]))
    return result

setuptools.setup(
    name="circuitpython-stubs-foamyguy",
    version="0.0.1",
    author="Tim C",
    author_email="foamyguy@gmail.com",
    description="Stubs For CircuitPython Project",
    long_description="Stubs For CircuitPython Project",
    #long_description_content_type="x-rst",
    url="https://github.com/adafruit/circuitpython",
    #packages=["circuitpython-stubs", "circuitpython-stubs.digitalio"],
    #packages=["digitalio"],
    #package_data={"digitalio-stubs": ["digitalio/__init__.pyi"]},
    #packages=["circuitpython-stubs"],
    #package_data={"circuitpython-stubs/": find_stub_files("circuitpython-stubs")},
                  #"digitalio": ["circuitpython-stubs/digitalio/__init_..pyi"]},
    data_files=build_data_files_list(),
    # data_files=[
    #     ("lib/python3.8/site-packages/digitalio/", ["circuitpython-stubs/digitalio/__init__.pyi"])
    # ],
    #package_dir={"": "circuitpython-stubs"},
    #packages=["circuitpython-stubs"],
    #py_modules=["digitalio"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
