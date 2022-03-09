# Contributing

## To add a destination

Add an JSON file in the data folder or update an existing one with a name and lat/long coordinates.  The "origin.json" file is special and should only have one entry for the "origin" for all measurements.

When adding a destination, please make sure to use public, fairly generic locations and names.  No need to expose anyones personal details, including your own.
If I find personal details, I reserve the right to yank and purge data and ban users in response.

Github will auto-update the index and publish the page so no need to run any tooling locally, provided the JSON is correct.

## To make changes to the script

### Requirements

- python3

### Steps

- git checkout git@github.com:jalangle/destinations.git
- python3 -m venv venv
- source venv/bin/activate
- python3 -m pip install -r requirements.txt
