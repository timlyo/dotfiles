#! /usr/bin/env
import pacman
import shutil
import os

HOME_DIR = os.path.expanduser("~")
CONFIG_DIR = HOME_DIR + "/.config/"


def make_dir(dir):
	try:
		os.makedirs(dir)
	except FileExistsError:
		pass


if __name__ == "__main__":
	# install software
	print("Installing desktop stuff")

	packages = ["i3lock", "xautolock", "compton"]
	for package in packages:
		print("Installing " + package)
		pacman.install(package)

	aurPackages = ["i3-gaps-git"]
	pacman.program = "yaourt"
	pacman.verbose = True
	for package in aurPackages:
		print("Installing " + package)
		pacman.install(package)


	# i3 files
	make_dir(CONFIG_DIR + "i3")
	shutil.copy("i3/config", CONFIG_DIR + "i3")
