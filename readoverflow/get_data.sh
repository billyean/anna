#!/usr/bin/env bash

set GOOGLE_APPLICATION_CREDENTIALS=./credential.json

set limit = 100000

for table in 'votes' 'users' 'tags' 'posts_wiki_placeholder' 'posts_tag_wiki_excerpt' 'posts_tag_wiki' \
        'posts_questions' 'posts_privilege_wiki' 'posts_orphaned_tag_wiki' 'posts_moderator_nomination' \
        'posts_answers' 'post_links' 'post_history' 'comments' 'badges'
do
    python read_stackoverflow.py ${limit} ${table}
done