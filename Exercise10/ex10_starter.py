import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# Use the glob.glob() function to obtain the list of filenames
mystuff = glob.glob(pattern)
for things in mystuff:
    # a test to only display files that are not zero length - used fact 0 evaluates as false
 if os.path.getsize(things):
     # Remove the leading directory name(s) from each filename before you print it
  print(os.path.basename(things))



