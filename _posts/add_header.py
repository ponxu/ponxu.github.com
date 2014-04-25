#eding: utf8
import os


def walk_path(p, callback=None):
    for root, dirs, files in os.walk(p):
        for name in files:
            if callback: callback(os.path.join(root, name))

def add_jekyll_post_header(filepath):
    if not filepath.endswith('md'): return

    filename = os.path.basename(filepath)
    filefolder = filepath.split('/')
    filefolder = filefolder[len(filefolder) - 2]

    f = open(filepath, 'r')
    content = f.read( )
    f.close()

    f = open(filepath, 'w')

    h = """\
---
layout: post
title: %s
description: %s
category: %s
tags: %s
comments: yes
---

""" % (filename[:-3], filename[:-3], filefolder, filefolder)

    f.write(h + content)
    f.close()
    
    print filefolder, filename, 'Done'



walk_path('.', add_jekyll_post_header)