import os
import sys

def repo_cloning():
	url = "git clone git@github.com:zeomega/"+sys.argv[1]+".git"
	os.system(url)
	print "Repo Created"
	os.chdir(sys.argv[1])
	os.system("git checkout "+sys.argv[2])
	print "Checkout to branch "
	os.system("git tag "+sys.argv[3])
	print "Tag is created"
	os.system("git config --global push.default simple")
	print "Push to remote"


if __name__ == "__main__":
	repo_cloning()
