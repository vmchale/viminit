import argparse
import os


def parser():
    parser = argparse.ArgumentParser(description='Set up a vimscript project')
    parser.add_argument('type', metavar='EXTENSION', type=str, default='syntax',
            help='Type of extension, e.g. suite, plugin, syntax, ftplugin, colorscheme, etc.')
    parser.add_argument('name', metavar='PROJECT', type=str,
            help='Project name')
    parser.add_argument('--license', metavar='LICENSE', type=str,
            help='License to use, e.g. BSD3, MIT, GPL, etc.', default='BDS3')
    parser.add_argument('-a', dest='autoload', action="store_true", default=False, 
            help='Whether to make a dir for autoload')
    return parser.parse_args()


def subdir(base, name):
    if not os.path.exists(base + "/" + name):
        os.makedirs(base + "/" + name)


# Create documentation if necessary
def docs(basedir, name):
    subdir(basedir, "docs")
    f = open(basedir + "/docs/" + name + ".txt", 'w+')


def autload(basedir, name):
    subdir(basedir, "autoload")


# Create plugin dir if necessary. Place plugin files within.
def plugin(basedir, name):
    docs(basedir, name)
    subdir(basedir, "plugin")
    f = open(basedir + "/plugin/" + name + ".vim", 'w+')


def colors(basedir):
    subdir(basedir, "colors")


def syntax(basedir, name):
    subdir(basedir, "syntax")
    f = open(basedir + "/syntax/" + name + ".vim", 'w+')


def ft_plugin(basedir, name):
    docs(basedir)
    subdir(basedir, "ftdetect")
    subdir(basedir, "ftplugin")
    syntax(basedir, name)
    f1 = open(basedir + "/ftplugin/" + basedir + ".vim", 'w+')
    f2 = open(basedir + "/ftdetect/" + basedir + ".vim", 'w+')
