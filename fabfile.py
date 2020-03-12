from fabric.api import *
from fabric.contrib import project
import os

global sudo


env.user = os.getenv("DEPLOY_USER")
env.root_dir = "/opt/local/share"
env.app_directory = "/mnt3/pranshu/few_shot/"
local_dir = "*"
remote_dir = "/mnt3/pranshu/few_shot/fewshot-egnn"
exclude = ["*~", "*.pyc"]


def internal_rsync(local_dir, remote_dir, exclude, default_opts='-rltgoDv -O'):
    project.rsync_project(local_dir=local_dir, remote_dir=remote_dir, exclude=exclude, default_opts=default_opts)

def restart_console_apis():
    pass

def prod():
    env.role = "production"
    env.hosts = ['10.9.61.4']

def all():
    internal_rsync(local_dir=local_dir, remote_dir=remote_dir, exclude=exclude)
