###############################################################################
# Ganga Project. http://cern.ch/ganga
#
# $Id: AttributeMigration.py,v 1.1 2008-07-17 16:41:13 moscicki Exp $
###############################################################################

from GangaCore.GPIDev.Base import GangaObject
from GangaCore.GPIDev.Schema import *


class TestAttribute(GangaObject):

    """The test attribute for the migration framework"""

    _schema = Schema(
        Version(1, 0), {'options': SimpleItem(defvalue='', doc='Attribute options')})

    _category = 'testAttributes'
    _name = 'TestAttribute'
    _exportmethods = []
