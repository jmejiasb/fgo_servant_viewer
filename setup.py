from setuptools import setup

setup(
    name="servant_viewer",
    version="0.0.1",
    packages=["servant_viewer"],
    entry_points={
        "console_scripts": [
            "servant_viewer = servant_viewer.__main__:main"
        ]
    },
    install_requires=["pyqt6"]
)