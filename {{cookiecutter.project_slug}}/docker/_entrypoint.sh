#!/bin/bash
set -euxo pipefail

USER="user"
id -g "${GID}" &>/dev/null || groupadd --gid ${GID} ${USER}
id -u "${UID}" &>/dev/null || useradd \
    --uid ${UID} \
    --gid ${GID} \
    --create-home \
    --home /home/${USER} \
    --shell /bin/bash \
    --comment "${USER}" \
    ${USER}

# should get here if 'docker run...' was passed -u with a numeric UID
export USER="$USER"
export HOME="/home/$USER"

echo "Starting with UID: $(id -u $USER), GID: $(id -g $USER) - $@"

exec /usr/local/bin/gosu ${USER} "$@"