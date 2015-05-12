# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import collective.contact.demo


class CollectiveContactDemoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            collective.contact.demo,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.contact.demo:default')


COLLECTIVE_CONTACT_DEMO_FIXTURE = CollectiveContactDemoLayer()


COLLECTIVE_CONTACT_DEMO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_CONTACT_DEMO_FIXTURE,),
    name='CollectiveContactDemoLayer:IntegrationTesting'
)


COLLECTIVE_CONTACT_DEMO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_CONTACT_DEMO_FIXTURE,),
    name='CollectiveContactDemoLayer:FunctionalTesting'
)


COLLECTIVE_CONTACT_DEMO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_CONTACT_DEMO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveContactDemoLayer:AcceptanceTesting'
)
