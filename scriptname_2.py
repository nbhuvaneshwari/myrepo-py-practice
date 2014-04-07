from git import *

import shlex

import sys
import os

def repo_creation():
	print "entered"
	repo_name=sys.argv[1]
	my_branch_name=sys.argv[2]
	my_tag=sys.argv[3]
	repo_exist=os.path.isdir('/home/admin/Desktop/practice/GitPython-0.3.2.RC1/abc/')
	repo_clone(sys.argv[1])
	repo_change_branch(sys.argv[1],sys.argv[2])
	repo_create_tag(sys.argv[1],sys.argv[3])	
		
def repo_clone(repo_name):
	""" Cloning the repo locally """
 	
	try:

		print "cloning started"
		#import pdb;pdb.set_trace()
		import git 
		git.Git().clone("git@github.com:nbhuvaneshwari/"+repo_name+".git")
		print "Cloning done..."
	except Exception,e:
		print "Repo already exist.."
		#raise GitCommandError(command, status, stderr_value)
 
def repo_change_branch(repo_name,my_branch_name):
	""" Checkout to the branch """
	repo=Repo('/home/admin/Desktop/practice/GitPython-0.3.2.RC1/abc/'+repo_name)
	git = repo.git
	try:	
		
	#heads = repo.heads
	#master = heads.reference      
	#master.commit              
	#master.rename("new_name") 

		git.checkout('HEAD', b=my_branch_name)
		print "Repo changed to branch"+my_branch_name
	except Exception,e:
		print "Branch doesn't exist"
		git.branch('HEAD', b=my_branch_name)
		git.checkout('HEAD', b=my_branch_name)
		print "Branch created and shited too"


def repo_create_tag(repo_name,my_tag):

	""" Creation of tag """

	repo=Repo('/home/admin/Desktop/practice/GitPython-0.3.2.RC1/abc/'+repo_name)
	git = repo.git
	try:
		repo.create_tag(my_tag)
		print "Tag is created"
	except Exception,e:
		print "Tag already exist"


#def push_repo():
	
		#"""Push the repo"""
		#origin = repo.remotes.origin
		#origin.refs                     
		#o = origin.rename('my_branch_name') 
		#o.push()

	

if __name__=="__main__":
	repo_creation()



