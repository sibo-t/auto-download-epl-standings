# Makefile to create a text file with the passed argument

all: run, install, bad

run:
	python3 main.py $(ARG)

install:
	$(eval ver=$(shell sh check_chrome_version.sh))
	$(shell sh install_selenium.sh $(ver))