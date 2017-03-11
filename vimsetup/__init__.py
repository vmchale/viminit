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
    parser.add_argument('-e', dest='external', action="store_true", default=False, 
            help='Whether to make a dir for extra dependencies.')
    return parser.parse_args()

def subdir(base, name):
    if not os.path.exists(base + "/" + name):
        os.makedirs(base + "/" + name)

## Create documentation if necessary
def docs(base):
    subdir(base, "docs")
    file = open(base + "/docs/" + base + ".txt", 'w+')

def suite(base):
    plugin(base)
    subdir(base, "autoload")

## Create plugin dir if necessary. Place plugin files within.
def plugin(base):
    docs(base)
    subdir(base, "plugin")
    file = open(base + "/plugin/" + base + ".vim", 'w+')

def colors(base):
    subdir(base, "colors")

def syntax():
    subdir(base, "syntax")

def ft_plugin(base):
    docs(base)
    subdir(base, "ftdetect")
    subdir(base, "ftplugin")
