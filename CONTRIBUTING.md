# Contributing

## To add a destination

Add an entry to data.json with a name and lat/long coordinates.  Github will auto-update the index and publish the page.

When adding a destination, please make sure to use public, fairly generic locations and names.  No need to expose anyones personal details, including your own.
If I find personal details, I reserve the right to yank and purge data and ban users in response.

## To make changes to the script

### Requirements

- python3

### Steps

- git checkout git@github.com:jalangle/destinations.git
- python3 -m venv venv
- source venv/bin/activate
- python3 -m pip install -r requirements.txt
