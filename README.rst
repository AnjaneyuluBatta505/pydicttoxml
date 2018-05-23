Pydicttoxml
===========

Convert python dictionary into a xml equivalent output

Usage of Pydicttoxml

.. code:: python

  d = {
    'student': {
        'name': 'Shera',
        'age': 25,
        'address': {
            'pin': 500082,
            'city': 'Hyderabad',
            'state': 'telangana',
            'country': 'India'
        }
     }
  }
  
  from pydicttoxml import dict2xml
  xml = dict2xml(d, root_tag="data")
  
  
Output

.. code:: xml

  <?xml version="1.0" encoding="UTF-8"?>
  <data>
    <student>
      <name>Shera</name>
      <age>25</age>
      <address>
        <pin>500082</pin>
        <city>Hyderabad</city>
        <state>telangana</state>
        <country>India</country>
      </address>
    </student>
  </data>
