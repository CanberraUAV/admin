#!/bin/sh
#
# Hudson admin task
#
# Assumes this script is run from Hudson:
#  * whenever changes to the github repository are detected
#  * every day, e.g. at 6am
#
# This implies the Hudson user (OS) has access to the internet,
# and a github account that can push to CanberraUAV etc.
#
# Also, implies this script is run from a job with source code
# management configured for the CanberraUAV git repository.
# That means, when the script is run, $WORKSPACE is set to a
# current copy of the source
DMIN_DIR=$WORKSPACE/administrivia
MEETING_TEMPLATE=$ADMIN_DIR/minutes/template.rst.copyme

# make sure we are on the right branch and up to date
git checkout master
git pull

# this may or may not have an effect
cd $ADMIN_DIR
./generate_agenda.py > $MEETING_TEMPLATE

FOUND_GIT_STAT_STR=`git status | grep -v "^#"`
CHANGE_GIT_STAT_STR='no changes added to commit (use "git add" and/or "git commit -a")'

if [ "$FOUND_GIT_STAT_STR" = "$CHANGE_GIT_STAT_STR" ]
then
    # the agenda needs changing
    git add -A
    git commit -m "meeting template updated by the admin-robot"
    git push
fi
