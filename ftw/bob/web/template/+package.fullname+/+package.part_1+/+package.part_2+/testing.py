from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig


class ErsigenLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        xmlconfig.string(
            '<configure xmlns="http://namespaces.zope.org/zope">'
            '  <include package="z3c.autoinclude" file="meta.zcml" />'
            '  <includePlugins package="plone" />'
            '  <includePluginsOverrides package="plone" />'
            '</configure>',
            context=configurationContext)

        z2.installProduct(app, 'ftw.simplelayout')
        z2.installProduct(app, 'ftw.file')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ersigen.web:default')


ERSIGEN_FIXTURE = ErsigenLayer()
ERSIGEN_FUNCTIONAL = FunctionalTesting(
    bases=(ERSIGEN_FIXTURE, ),
    name="ersigen.web:functional")
