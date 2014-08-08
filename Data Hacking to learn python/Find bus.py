__author__ = 'ddsnowboard'
from xml.etree.cElementTree import parse

doc = parse('rt22.xml')
buses = []
winner = None
lats = []
done = False
for bus in doc.findall('bus'):
    d = bus.findtext('d')
    lat = float(bus.findtext('lat'))
    if d.lower() == "north bound" and lat > 41.980262:
        buses.append(bus)
for b in buses:
    print b.findtext('id')