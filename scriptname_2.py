import git
from git import *
from subprocess import *
import sys


def gitpy():

		""" Cloning the repo locally """
		print "cloning started"
		git.Git().clone("git@github.com:nbhuvaneshwari/myrepo-py-practice.git")
		
		""" Change directory """

		call(["cd","practice"])

		repo=Repo('/home/admin/Desktop/practice/GitPython-0.3.2.RC1/abc/GitPython-0.3.2.RC1/jivacore.ui')
		git = repo.git

		""" Checkout to the branch """
		my_branch_name=sys.argv[2]
		git.checkout('HEAD', b='my_branch_name')

		""" Creation of tag """
		my_tag=sys.argv[3]
		new_tag = repo.create_tag('my_tag', 'first tag created')

	

if __name__=="__main__":
	gitpy()



