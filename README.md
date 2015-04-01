#Git-Tumblr: Version Control for Tumblr

######Jordan Rickman
######[https://github.com/OffensiveCodeComments/git-tumblr](https://github.com/OffensiveCodeComments/git-tumblr)

Git-Tumblr is a Git extension written in Python that synchronizes a Tumblog with a Git repository. It is bidirectional, and can be used for backup, authoring, or both.

Git-Tumblr repositories consist of flat files and an index file `git-tumblr-index` in the repository root. Each post corresponds to a single file in HTML, Markdown, or plaintext format, and tumblr metadata and options are inserted using specially formatted HTML comments called **Git-Tumblr directives**.

Text files may be arranged in any hierarchy desired, though they are placed in the root directory by default when fetched. Photos, audio clips, and video clips will be downloaded if they are hosted by tumblr, and may be placed in the repository to be uploaded. The corresponding directives use relative filepaths to refer to them.

