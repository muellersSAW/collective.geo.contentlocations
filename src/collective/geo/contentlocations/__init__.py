from zope.i18nmessageid import MessageFactory
from . import config

ContentLocationsMessageFactory = MessageFactory(config.PROJECTNAME)

_ = ContentLocationsMessageFactory
COORDTYPE = [('Point', _(u'Point')),
             ('LineString', _(u'LineString')),
             ('Polygon', _(u'Polygon'))]
