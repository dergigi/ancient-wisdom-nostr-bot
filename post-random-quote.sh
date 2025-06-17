#!/bin/bash

MYDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Get a random number between 0 and the number of quotes
RANDQ=$(cat $MYDIR/quotes.json | jq '. | length')
RANDQ=$((RANDOM % RANDQ))

# Get the quote and author
QUOTE=$(cat $MYDIR/quotes.json | jq -r --arg i $RANDQ '.[$i|tonumber].quote')
AUTHOR=$(cat $MYDIR/quotes.json | jq -r --arg i $RANDQ '.[$i|tonumber].author')

# Format the note with quote and author
NOTE="\"$QUOTE\" —$AUTHOR"
echo $NOTE

GOBINPATH=($HOME/go/bin)
# $GOBINPATH/noscl publish "$NOTE"
