from setuptools import setup

def pre_install():
    # f = open("readme.md",'r')
    # text = f.read()
    text = "mori cyber hello"
    return text

setup(
    name="morteza_pythonpackage",
    version="1.0.0",
    author="mori_cyber",
    description="A test package for pydeploy students",
    long_description=pre_install(),
    requires=[],
    author_email="moridh1355@gmail.com",
    packages=["morteza_pythonpackage"],
    
)
