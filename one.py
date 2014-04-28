import os
import sys
import subprocess

def repo_cloning(repo_name, branch_name,tag_version):
    print repo_name
    url = "git clone git@github.com:Sadashiv/%s" %repo_name
    print url
    subprocess.call(url, shell=True)
    print "Repo cloning"
    os.chdir(repo_name)
    print "Checkout to branch "
    subprocess.call("git checkout %s" %branch_name , shell=True)
    print "Tag is created"
    subprocess.call("git tag v%s -m 'Tag created'" %tag_version , shell=True)

if __name__ == "__main__":
    repo_name = sys.argv[1]
    branch_name = sys.argv[2]
    tag_version = sys.argv[3]
    repo_cloning(repo_name, branch_name, tag_version)
