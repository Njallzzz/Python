import stagger
import os
from os.path import join
import shutil
import argparse

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

def analyze_and_move(inputdir, outputdir, delete):
    filelist = []
    for path, subdirs, files in os.walk(inputdir):
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
        export = construct_export_string(outputdir, file)
        try:
            os.makedirs(os.path.split(export)[0])
        except FileExistsError:
            pass
        if not delete:
            try:
                shutil.copy2(file['origin'], export)
            except FileNotFoundError:
                shutil.copy2(file['origin'], join(os.path.split(export)[0], file['title'].split('.')[0] + os.path.splitext(file['origin'])[1]))
        else:
            try:
                shutil.move(file['origin'], export)
            except FileNotFoundError:
                shutil.move(file['origin'], join(os.path.split(export)[0], file['title'].split('.')[0] + os.path.splitext(file['origin'])[1]))
    if delete:
        shutil.rmtree(inputdir)

def main():
    pars = argparse.ArgumentParser(description='ID3 File Parser and organizer for music files')
    pars.add_argument('--input', '-i', nargs=1, help='Input directory to search')
    pars.add_argument('--output', '-o', nargs=1, help='Output directory to move the files to')
    pars.add_argument('--delete', '-d', default=False, help='Whether to delete the original file') 
    args = pars.parse_args()

    if args.input and args.output:
        analyze_and_move(args.input[0], args.output[0], args.delete)

if __name__ == '__main__':
  main()

