#!/usr/bin/python3

from fabric.api import run, put, env
from os.path import exists
env.hosts = ['52.204.74.122', '35.153.51.106']

def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        archive = archive_path.split('/')[-1]
        folder = archive.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(folder))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive, folder))
        run('rm /tmp/{}'.format(archive))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(folder, folder))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(folder))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(folder))
        return True
    except:
        return False
