#! /usr/bin/env
import pacman


if __name__ == "__main__":


	# install software
	print("Installing desktop stuff")

	packages = ["i3lock", "xautolock"]
	pacman.install(packages)
