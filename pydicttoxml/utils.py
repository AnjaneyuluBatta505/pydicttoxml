import re
from collections import OrderedDict
from xml.sax.saxutils import XMLGenerator

from .exceptions import UnserializableContentError


class SimplerXMLGenerator(XMLGenerator):

    def addQuickElement(self, name, contents=None, attrs=None):
        "Convenience method for adding an element with no children"
        if attrs is None:
            attrs = {}
        self.startElement(name, attrs)
        if contents is not None:
            self.characters(contents)
        self.endElement(name)

    def characters(self, content):
        if content and re.search(r'[\x00-\x08\x0B-\x0C\x0E-\x1F]', content):
            # Fail when content has control chars(unsupported in XML 1.0)
            # See http://www.w3.org/International/questions/qa-controls
            raise UnserializableContentError(
                "Control characters are not supported in XML 1.0"
            )
        XMLGenerator.characters(self, content)

    def startElement(self, name, attrs):
        # Sort attrs for a deterministic output.
        sorted_attrs = OrderedDict(sorted(attrs.items())) if attrs else attrs
        super(SimplerXMLGenerator, self).startElement(name, sorted_attrs)


def force_text(s, encoding='utf-8', strings_only=False, errors='strict'):
    """
        Convert bytes and other data types into a string data type
    """
    if issubclass(type(s), str):
        return s
    if isinstance(s, bytes):
        s = str(s, encoding, errors)
    else:
        s = str(s)
    return s
