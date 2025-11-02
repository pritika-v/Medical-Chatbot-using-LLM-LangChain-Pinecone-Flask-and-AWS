from setuptools import find_packages, setup

setup(
    name="medical_chatbot",
    version="0.1.0",
    author="V Pritika",
    author_email="pritikavijayakumar@gmail.com",
    packages=find_packages(), #Automatically detects all Python packages (folders with __init__.py) inside your project. .
    install_requires=[] #Lists external libraries your project depends on. These are automatically installed when someone installs your package.
)

#setup file helps us install any kinds of folder as local package
# The setup.py file tells Python how to install your project as a package

# pip install -e .
# it reads your setup.py and registers your folder (like medical_chatbot/) 
# as a package you can import anywhere on your system.

# This is especially useful for modular projects like your medical chatbot, 
# which might have submodules for data loading, vector creation, or chatbot logic.
    
# packages=find_packages():
# Because there’s an __init__.py inside the medical_chatbot/ folder,
# that folder is recognized as a Python package.

# All .py files inside that folder (like helper.py, prompt.py, etc.)
# are automatically included when you call find_packages().