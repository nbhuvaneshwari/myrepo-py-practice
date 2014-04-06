from git import *
#from subprocess import *
import sys


def gitpy():

		""" Cloning the repo locally """
		print "cloning started"
		
		import git
		git.Git().clone("git@github.com:nbhuvaneshwari/"+sys.argv[1]+".git")
		
		""" Change directory """

		#call(["cd","practice"])

		repo=Repo('/home/admin/Desktop/practice/GitPython-0.3.2.RC1/abc')
		git = repo.git

		heads = repo.heads
		master = heads.master      
		master.commit              
		#master.rename("new_name") 

		""" Checkout to the branch """
		my_branch_name=sys.argv[2]
		git.checkout('HEAD', b='my_branch_name')

		""" Creation of tag """
		my_tag=sys.argv[3]
		repo.create_tag("my_tag")

		"""Push the repo"""
		origin = repo.remotes.origin
		origin.refs                     
		o = origin.rename('my_branch_name') 
		o.push()

	

if __name__=="__main__":
	gitpy()



