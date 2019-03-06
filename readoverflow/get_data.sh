#!/usr/bin/env bash

export GOOGLE_APPLICATION_CREDENTIALS=./credential.json

export limit=1000000

if [ "$#" -eq 1 ]; then
    export limit=$1
fi

# for table in 'stackoverflow_posts'
for table in 'stackoverflow_posts' 'votes' 'users' 'tags' 'posts_wiki_placeholder' 'posts_tag_wiki_excerpt' 'posts_tag_wiki' \
        'posts_questions' 'posts_privilege_wiki' 'posts_orphaned_tag_wiki' 'posts_moderator_nomination' \
        'posts_answers' 'post_links' 'post_history' 'comments' 'badges'
do
    python read_stackoverflow.py ${limit} ${table}
done