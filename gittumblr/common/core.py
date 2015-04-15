#!/usr/bin/python3

from enum import Enum

class PostState(Enum):
    """An enum listing all possible states a post can be in.

    Each enum member has a string value, which is the value
    used in Tumblr's API and in git-tumblr directives."""
    PUBLISHED   = "published"
    PRIVATE     = "private"
    DRAFT       = "draft"
    QUEUED      = "queued"

class PostType(Enum):
    """An enum listing all possible post types.

    Each enum member has a string value, which is the value
    used in Tumblr's API and in git-tumblr directives."""
    TEXT        = "text"
    QUOTE       = "quote"
    LINK        = "link"
    ANSWER      = "answer"
    VIDEO       = "video"
    AUDIO       = "audio"
    PHOTO       = "photo"
    CHAT        = "chat"
