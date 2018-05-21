try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

from .exceptions import DictRequiredError
from .utils import force_text, SimplerXMLGenerator


class DictToXML:

    charset = 'utf-8'

    @classmethod
    def get_xml(cls, data, root_tag_name=None, declaration=True):
        cls.root_tag_name = root_tag_name

        if not isinstance(data, dict):
            DictRequiredError(
                "Need to pass either a dict or an OrderedDictionary"
            )

        stream = StringIO()

        xml = SimplerXMLGenerator(stream, cls.charset)
        if root_tag_name:
            attrs = data.pop('tag_attrs', {})
            xml.startElement(cls.root_tag_name, attrs)
        cls._to_xml(xml, data)
        if root_tag_name:
            xml.endElement(cls.root_tag_name)
        xml.endDocument()
        if declaration:
            return "<?xml version='1.0' encoding='%s'?>%s" % (
                cls.charset, stream.getvalue())
        return stream.getvalue()

    @classmethod
    def _to_xml(cls, xml, data):
        if isinstance(data, (list, tuple)):
            for item in data:
                cls._to_xml(xml, item)

        elif isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, dict):
                    attrs = value.pop('tag_attrs', {})
                else:
                    attrs = {}
                xml.startElement(key, attrs)
                cls._to_xml(xml, value)
                xml.endElement(key)
        else:
            xml.characters(force_text(data))


dict2xml = DictToXML.get_xml
