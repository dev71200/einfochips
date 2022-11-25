#!/bin/bash
cat <<'EOF' >> /root/.bashrc
export TERM=linux
cd ${HOME}
source ${HOME}/einfochips/bin/activate
echo -e "Welcome to Seinfochips!\nYou are already in the einfochips virtual environment, so just type \`einfo\` to run it!\n    (for example: \`einfo -h\` to see the help documentation).\n\nHave fun!\n\n"
EOF
