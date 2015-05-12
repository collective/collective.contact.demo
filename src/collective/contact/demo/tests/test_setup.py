# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""
from collective.contact.demo.testing import COLLECTIVE_CONTACT_DEMO_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestInstall(unittest.TestCase):
    """Test installation of collective.contact.demo into Plone."""

    layer = COLLECTIVE_CONTACT_DEMO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.contact.demo is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.contact.demo'))

    def test_uninstall(self):
        """Test if collective.contact.demo is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.contact.demo'])
        self.assertFalse(self.installer.isProductInstalled('collective.contact.demo'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollectiveContactDemoLayer is registered."""
        from collective.contact.demo.interfaces import ICollectiveContactDemoLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveContactDemoLayer, utils.registered_layers())
