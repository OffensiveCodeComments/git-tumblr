#!/usr/bin/python3

from enum import Enum

class PostAttribute(Enum):
    TITLE       = 1

class Attribute:
    """Represents the value of a particular attribute of a post."""

    def get_attr(self) -> PostAttribute:
        """Return the PostAttribute specifying this attribute of the post."""
        raise NotImplementedError

class AttributeDelta:
    """Represents a change in a particular attribute of a post."""

    def get_attr(self) -> PostAttribute:
        """Return the PostAttribute specifying this attribute of the post."""
        raise NotImplementedError

class AttributeEditor:
    """Knows how to compute and apply AttributeDeltas for a particular
    attribute of a post."""

    def compute_delta(self, before: Attribute, after: Attribute) -> AttributeDelta:
        """Generate an AttributeDelta representing the change from before
        to after."""
        raise NotImplementedError

    def apply_delta(self, target: Attribute, delta: AttributeDelta) -> bool:
        """Apply the AttributeDelta to the target Attribute.
        Returns true if and only if the attribute changed."""
        raise NotImplementedError

class AttributeApplicationError(Exception):
    """Indicates an error while applying an AttributeDelta."""
    
    def __init__(self, message: str, target: Attribute, delta: AttributeDelta):
        self.target = target
        self.delta = delta
        Exception.__init__(self, message)

    def get_target(self) -> Attribute:
        return self.target

    def get_delta(self) -> AttributeDelta:
        return self.delta



class TitleAttrBase:
    """Provides the get_attr method for all title-related classes."""
    def get_attr(self):
        return PostAttribute.TITLE

class TitleAttribute(Attribute, TitleAttrBase):
    """Attribute class representing the post title."""

    def __init__(self, title: str):
        if title.__class__ is str:
            self.value = title
        else:
            raise TypeError("TitleAttribute requires a string title.")

    def get_value(self) -> str:
        return self.value

    def set_value(self, title: str):
        if title.__class__ is str:
            self.value = title
        else:
            raise TypeError("TitleAttribute requires a string title.")

class TitleAttributeDelta(AttributeDelta, TitleAttrBase):
    """AttributeDelta class representing a change in post title."""

    def __init__(self, previousTitle: str, newTitle: str):
        if (previousTitle.__class__ is str) and (newTitle.__class__ is str):
            self.previousTitle = previousTitle
            self.newTitle = newTitle
        else:
            raise TypeError("TitleAttributeDelta requires string titles.")

    def get_previous_title(self) -> str:
        return self.previousTitle

    def get_new_title(self) -> str:
        return self.newTitle


class TitleAttributeEditor(AttributeEditor, TitleAttrBase):
    """AttributeEditor for post titles."""

    def apply_delta(self, target: TitleAttribute, delta: TitleAttributeDelta) -> bool:
        if isinstance(target, TitleAttribute) and isinstance(delta, TitleAttributeDelta):
            if target.get_value() == delta.get_previous_title():
                target.set_value(delta.get_new_title())
            else:
                raise AttributeApplicationError("Previous title does not match.", target, delta)
        else:
            raise TypeError("TitleAttributeEditor can only edit post titles.")

    def compute_delta(self, before: TitleAttribute, after: TitleAttribute) -> TitleAttributeDelta:
        if isinstance(before, TitleAttribute) and isinstance(after, TitleAttribute):
            return TitleAttributeDelta(before.get_value(), after.get_value())


##### TESTS #####
if __name__ == "__main__":
    HELLO = "Hello, world."
    GOODBYE = "Goodbye, cruel world."

    title1 = TitleAttribute(HELLO)
    title2 = TitleAttribute(GOODBYE)
    assert title1.get_value() == HELLO
    assert title2.get_value() == GOODBYE

    editor = TitleAttributeEditor()
    delta = editor.compute_delta(title1, title2)
    assert delta.get_previous_title() == HELLO
    assert delta.get_new_title() == GOODBYE

    editor.apply_delta(title1, delta)
    assert title2.get_value() == GOODBYE

    try:
        editor.apply_delta(title2, delta)
    except AttributeApplicationError as err:
        assert err.get_target() is title2
        assert err.get_delta() is delta

    print("All tests passed.")
