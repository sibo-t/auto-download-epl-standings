# Makefile to install chromedriver and run python script
# Author: Sibonelo Msabala
# Email: stmsabala@gmail.com

.PHONY: all


all: install run

ifeq ($(shell whereis chromedriver), "/usr/bin/chromedriver")
install:
	$(eval ver=$(shell sh check_chrome_version.sh))
	$(shell sh install_selenium.sh $(ver))
	@echo "$(shell chromedriver --version) is now installed"

else
install:
	@echo "$(shell chromedriver --version) is installed"
endif

run:
	python3 main.py $(ARG)

	

