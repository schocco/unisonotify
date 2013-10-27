#!/usr/bin/python
# -*- coding: <utf-8> -*-
import getopt
import sys
import os
import subprocess
import pynotify

pathname = os.path.dirname(os.path.realpath(__file__))

def run_unison(profile, batch=True):
    args = ["unison", profile, "-maxthreads", "2"]
    if batch:
        args.append("-batch")
    return subprocess.call(args)

def notify(header, text):
    '''
    Display a notification with the given header and text.    
    '''
    if not pynotify.init("icon-summary-body"):
        sys.exit(1)

    n = pynotify.Notification(
        header,
        text,
        #"notification-message-im"
        os.path.join(pathname, "U.ico")
        )
    n.show()
    print pathname


#TODO: accept profile name as argument
if __name__ == "__main__":
    notify("Synchronization started", "Starting synchronisation with unison")
    # call unison and wait for completion
    exitcode = run_unison("documents")
    # display notification that sync was completed with exit code X
    if exitcode == 0:
        notify("Synchronization completed", "Unison successfully completed synchronization")
    elif exitcoe == 1:
        notify("Synchronization completed", "Some files were skipped, but all file transfers were successful")
    elif exitcode == 2:
        notify("Synchronization completed with failures", "Non-fatal failures occurred during file transfer")
    elif exitcode == 3:
        notify("Synchronization failed", "A fatal error occurred, or the execution was interrupted")
