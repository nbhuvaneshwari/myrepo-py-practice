from git import *
import sys
import os
import exceptions



def create_repo(repo_name):
	""" Cloning Repo"""
	print "cloning started"
	#import pdb;pdb.set_trace()
	import git 
	git.Git().clone("git@github.com:nbhuvaneshwari/"+repo_name+".git")
	print "Cloning done..."
	return True

def checkout_iff_branch_exists(repo_name,my_branch_name):
	""" Checkout to the branch """
	repo=Repo(os.getcwd()+"/"+repo_name)
	git = repo.git
	git.checkout('HEAD', b=my_branch_name)
	print "Repo changed to branch "+my_branch_name

def create_tag(repo_name,my_tag):
	""" Creation of tag """

	repo=Repo(os.getcwd()+"/"+repo_name)
	git = repo.git
	repo.create_tag(my_tag)
	print "Tag is created"

def push_changes():
	
	"""Push the repo"""
	origin= repo.remotes.origin                     
	o = origin.rename('my_branch_name') 
	origin.push(kargv={Tags:"my_tag"})
	print "repo pushed "


def proces_req():
	repo_name=sys.argv[1]
	my_branch_name=sys.argv[2]
	my_tag=sys.argv[3]
	try:
		repo_exist=os.path.isdir(os.getcwd())
		create_repo(repo_name)
		checkout_iff_branch_exists(repo_name,my_branch_name,)
		create_tag(repo_name,my_tag)
		#import pdb;pdb.set_trace()
		if (repo_exist):
			#push_changes()
	except (ValueError,AttributeError,TypeError,NoSuchPathError,InvalidGitRepositoryError),e:
		print e 
		
 
	 
if __name__=="__main__":
	proces_req()
    
