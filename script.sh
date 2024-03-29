#!/bin/bash

##
# Script to delete remote git branches
##

# Loop through all remote merged branches
for branch in $(git branch -r --merged origin/test | grep -v HEAD | grep -v dev | grep -v master | sed /\*/d); do
                echo -e `git show --format="%ci %cr %an" ${branch} | head -n 1` \\t$branch
                remote_branch=$(echo ${branch} | sed 's#origin/##' )
                git branch --delete ${remote_branch}
done
