# Makefile to create a text file with the passed argument

all: create_file, install

create_file:
	echo "$(d)" > dir.txt

install:
	$(eval ver=$(shell sh check_chrome_version.sh))
	$(shell sh install_selenium.sh $(ver))
