#!/usr/bin/python3
'''
Fabric Deployment:
    do_pack() compacts the web_static directory into a .tgz file.
    do_deploy() deploys the compressed content to the hosts in env.hosts.
    deploy() combines the previous two methods.
'''
from fabric.api import local, put, run, env
from datetime import datetime
import os


env.hosts = ['206.189.113.113', '206.189.113.133']
env.user = 'root'


def do_pack():
    '''
    Creates a tgz archive from the contents of the web_static dir .
    '''
    try:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        local('mkdir -p versions')
        f = 'versions/web_static_' + time + '.tgz'
        local('tar -vzcf {} web_static'.format(f))
        return f
    except:
        return None


def do_deploy(archive_path):
    '''
    Deploys the compressed contents of web_static to the web servers defined in
    env.hosts.
    '''
    path_existence = os.path.exists(archive_path)
    if path_existence is False:
        return False
    try:
        path_split = archive_path.replace('/', ' ').replace('.', ' ').split()
        just_directory = path_split[0]
        no_tgz_name = path_split[1]
        full_filename = path_split[1] + '.' + path_split[2]
        folder = '/data/web_static/releases/{}/'.format(no_tgz_name)
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(folder))
        run('tar -xzf /tmp/{} -C {}/'.format(full_filename, folder))
        run('rm /tmp/{}'.format(full_filename))
        run('mv {}/web_static/* {}'.format(folder, folder))
        run('rm -rf {}/web_static'.format(folder))
        current = '/data/web_static/current'
        run('rm -rf {}'.format(current))
        run('ln -s {}/ {}'.format(folder, current))
        return True
    except:
        return False


def deploy():
    '''
    Combines do_pack() and do_deploy() into one full deployment.
    '''
    my_path = do_pack()
    if my_path is None:
        return False
    my_result = do_deploy(my_path)
    return my_result
