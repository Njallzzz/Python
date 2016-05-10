import stagger
import os
from os.path import join
import shutil

def title_to_title_and_artist(file):
    split_title = [x.strip() for x in file['title'].split('-')]
    if len(split_title) > 3:
        split_title = split_title[:2] + [' '.join(split_title[2:])]
    file.setdefault('artist', split_title[0])
    file['title'] = os.path.splitext(split_title[-1])[0]
    return file

def construct_export_string(output, file):
    if len(file.keys()) == 1:   # Everything is missing
        return join( output, os.path.split(file['origin'])[1] )
    extension = os.path.splitext(file['origin'])[1]
    path = output
    if 'artist' in file.keys():
        path = join(path, file['artist'])
    if 'album' in file.keys():
        path = join(path, file['album'])
    if 'title' in file.keys():
        path = join(path, file['title'] + extension)
    return path

def format_text(text):
    mid = text.strip().title().replace('&', 'and').replace('"', '').replace('/', '-').replace(':', '').replace('?', '')
    if mid.startswith('...'):
        mid = mid[3:]
    return mid

filelist = []
for path, subdirs, files in os.walk('ipod'):
    for file in files:
        cpath = os.path.join(path,file)
        cfile = {'origin': cpath}
        try:
            tag = stagger.read_tag(cpath)
            if tag.album:
                cfile['album'] = format_text(tag.album)
            if tag.artist:
                cfile['artist'] = format_text(tag.artist)
            if tag.title:
                cfile['title'] = format_text(tag.title)
        except stagger.errors.NoTagError:
            pass
        
        if len(cfile.keys()) == 2:
            if 'title' in cfile.keys():
                cfile = title_to_title_and_artist(cfile)
            else:
                print('Unhandled file meta data format:', cfile['origin'])

        filelist.append(cfile)
        
for file in filelist:
    export = construct_export_string('Music', file)
    try:
        os.makedirs(os.path.split(export)[0])
    except FileExistsError:
        pass
    shutil.copy2(file['origin'], export)

