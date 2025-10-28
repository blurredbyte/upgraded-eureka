# Git Exposed

**Category:** Secrets Hardcoded
**Difficulty:** Intermediate
**Points:** 200

## Description

Our team deployed a new website, but they seem to have misconfigured the web server. It looks like they accidentally exposed the `.git` directory in the web root.

This could be a major security risk. Can you investigate this and see if you can find any secrets?

We've managed to download a couple of interesting files that were exposed. They are in the `files` directory.

## Hints

*   The exposed files are a simulated log file and a git object file.
*   The log file shows the commit history. Look for interesting commit messages.
*   One of the commits seems to have removed a secret. Can you find the contents of that commit?
*   The "leaked git object" is not a binary file in this challenge, it's a text file representing the contents of a git object. Git objects store file contents.
