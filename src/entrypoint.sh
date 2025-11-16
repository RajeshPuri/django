#!/bin/sh

set -e

if [ "$SERVER_TYPE" == "PROD" ];
then
  cp /app/ssh/sshd_config /etc/ssh/sshd_config && chmod 644 /etc/ssh/sshd_config
  echo "-----BEGIN OPENSSH PRIVATE KEY-----" > /root/.ssh/id_git
  echo $SSH_PRIVATE_KEY | tr ' ' '\n' >> /root/.ssh/id_git
  echo "-----END OPENSSH PRIVATE KEY-----" >> /root/.ssh/id_git
  echo $SSH_PUBLIC_KEY > /root/.ssh/id_git.pub
  chmod 600 /root/.ssh/id_git
  python manage.py migrate
  supervisord
fi
exec "$@"
