.PHONY: installDependencies
installDependencies:
	sudo pip install pigpio
	sudo pip install pynput
	sudo pip install nose

.SILENT:
