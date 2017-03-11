import argparse
import git
import os

parser = argparse.ArgumentParser(description='Set up a vimscript project')
parser.add_argument('type', metavar='EXTENSION', type=str, default='syntax',
                    help='Type of extension, e.g. suite, plugin, syntax, ftplugin, etc.')
parser.add_argument('name', metavar='PROJECT', type=str,
                    help='Project name')
parser.add_argument('--license', metavar='LICENSE', type=str,
                    help='License to use, e.g. BSD3, MIT, GPL, etc.', default='BDS3')
args = parser.parse_args()

## Create the directory
if not os.path.exists(args.name):
    os.makedirs(args.name)
else:
    print("Directory already exists. Aborting.")

## Create documentation if necessary
if not os.path.exists(args.name + "doc/") and (args.type=='plugin' or args.type=='ftplugin'):
    os.makedirs(args.name + "/doc")

## Create plugin dir if necessary

## Create the license file

## Create the gitignore file
print("*.vmb", args.name + "/.gitignore")

## Create the readme file

## Create vimball.txt listing all the files for the 

## Initialize git repo
g = git.cmd.Git(args.name)
g.init()
#git.add('*')
