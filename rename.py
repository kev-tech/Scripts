#Script to rename files in bulk.
import os
path = '' #Set string to appropriate file path.
files = os.listdir(path)

#Change the file extension to suit your needs.
for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str('file'+ index), '.jpg'])))
