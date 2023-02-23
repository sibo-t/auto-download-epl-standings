#!/bin/bash

#Read from input
v=$1

#Work from home dir
echo $(cd)

# Remove characters after third dot using sed
mod_v=$(echo $v | cut -d "." -f 1-3)

url="https://chromedriver.storage.googleapis.com/LATEST_RELEASE_"

ver="${url}${mod_v}"

d_ver=$(curl -s $ver)

link="curl https://chromedriver.storage.googleapis.com/"
end="/chromedriver_linux64.zip -o ~/chromedriver.zip \
    && unzip ~/chromedriver.zip -d /bin/ \
    && rm ~/chromedriver.zip"

cmd="${link}${d_ver}${end}"

#Download chromdriver
echo $cmd

echo $(chmod +x /bin/chromedriver)



