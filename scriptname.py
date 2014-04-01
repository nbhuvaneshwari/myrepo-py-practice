import os
import sys
def func():
	url = "git clone git@github.com:zeomega/"+sys.argv[1]+".git"
	os.system(url)
	os.system("cd "+sys.argv[1])
	os.system("git checkout "+sys.argv[2])
	os.system("git tag "+sys.argv[3])
	os.system("git push")

if __name__ == "__main__":
	func()
