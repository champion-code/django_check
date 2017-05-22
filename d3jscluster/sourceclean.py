import os

ignore_list= []

def clean_for_git(source_dir):
	for name in os.listdir(source_dir):
		new_path = os.path.join(source_dir, name)
		if os.path.isdir(new_path):
			if not name in ignore_list:
				clean_for_git(new_path)
		if name.endswith(".pyc"):
			print "remove file:%s" % new_path
			os.remove(new_path)


if __name__ == "__main__":
	clean_for_git(".")
