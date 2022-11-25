#!/bin/bash

# =====================================
# install einfochips into a virtual env
# =====================================

WORKDIR=/root
TMPDIR=/tmp

# =====================================
# install einfochips
# =====================================
cd ${WORKDIR}
virtualenv -p python3 einfochips
source ${WORKDIR}/einfochips/bin/activate
pip install einfochips

echo -e "\n\neinfochips Installation Complete!\n\n"
