import os
for root,dirs,files,rootfd in os.fwalk('/usr/lib/python3.6'):
    print(root,"consumes",end=" ")
    print(sum([os.stat(name,dir_fd=rootfd).st_size for name in files]),end="")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS') #don't visit CVS directories


