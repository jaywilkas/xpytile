from setuptools import setup, find_packages

setup(
    name="xpytile",
    version="1.0.0",
    url="https://github.com/jaywilkas/xpytile.git",
    author="jaywilkas",
    description="Tiling and simultaneous resizing of side-by-side windows (not only) for Xfce",
    packages=find_packages(),
    install_requires=["python-xlib"],
    entry_points={
        "console_scripts": [
            "xpytile=xpytile:main",
            "getModifierCode=getModifierCode:main",
        ],
    },
)
