# -*- coding: utf-8 -*-
import os.path
from datetime import date

from zope.component import getUtility
from zope.interface import alsoProvides
from zope.intid.interfaces import IIntIds

from plone import api

from eea.facetednavigation.settings.interfaces import IHidePloneLeftColumn
from eea.facetednavigation.settings.interfaces import IHidePloneRightColumn
from eea.facetednavigation.subtypes.interfaces import IFacetedNavigable
from eea.facetednavigation.subtypes.interfaces import IFacetedSearchMode
from z3c.relationfield.relation import RelationValue


def isNotCurrentProfile(context):
    return context.readDataFile('collectivecontactdemo_marker.txt') is None


def post_install(context):
    """Post install script"""
    if isNotCurrentProfile(context):
        return

    portal = api.portal.get()
    if 'contacts' not in portal:
        setup_contacts_demo(portal)


def setup_contacts_demo(portal):
    """Add demo data for contacts."""
    position_types = [
        {'name': u'CEO', 'token': 'ceo'},
        {'name': u'CTO', 'token': 'cto'},
        {'name': u'CMO', 'token': 'cmo'},
        {'name': u'CSO', 'token': 'cso'},
        {'name': u'President', 'token': 'president'},
        {'name': u'Director', 'token': 'director'},
        {'name': u'Engineer', 'token': 'engineer'},
        {'name': u'Salesman', 'token': 'salesman'},
        ]

    organization_types = [
        {'name': u'Company', 'token': 'company'},
        {'name': u'NGO', 'token': 'ngo'},
        {'name': u'Association', 'token': 'association'},
        {'name': u'Region', 'token': 'region'},
        ]

    organization_levels = [
        {'name': u'Department', 'token': 'department'},
        {'name': u'Service', 'token': 'service'},
        ]

    # Create contacts directory
    params = {'title': "Contacts",
              'position_types': position_types,
              'organization_types': organization_types,
              'organization_levels': organization_levels,
             }
    portal.invokeFactory('directory', 'contacts', **params)
    contacts = portal['contacts']
    api.content.transition(contacts, 'publish')

    # Create organizations
    params = {'title': u"Pear",
              'organization_type': u'company',
              'zip_code': u'',
              'city': u'London',
              'street': u"Bridge street",
              'number': u'1',
              'phone': u'022/100.789',
              'email': u'contact@pear.com',
             }
    contacts.invokeFactory('organization', 'pear', **params)
    pear = contacts['pear']

    params = {'title': u"Wikimedia Foundation",
              'organization_type': u'ngo',
              'zip_code': u'60020',
              'city': u'New-York',
              'street': u"Central Park street",
              'number': u'198',
              'phone': u'010/000.888',
              'email': u'contact@wikimedia.org',
             }
    contacts.invokeFactory('organization', 'wikimedia', **params)
    wikimedia = contacts['wikimedia']

    params = {'title': u"Plone Foundation",
              'organization_type': u'association',
              'zip_code': u'46038',
              'city': u'Fishers',
              'region': 'Indiana',
              'phone': u'012/345.678',
              'email': u'contact@plone.org',
             }
    contacts.invokeFactory('organization', 'plone', **params)
    plone = contacts['plone']

    # Create some organizations in Pear company
    # Departments
    params = {'title': u"HR",
              'organization_level': u'department',
             }
    pear.invokeFactory('organization', 'hr', **params)

    params['title'] = "Research and Development"
    pear.invokeFactory('organization', 'randd', **params)

    params['title'] = "Operations"
    pear.invokeFactory('organization', 'operations', **params)
    operations = pear['operations']

    params['title'] = "Marketing and Sales"
    pear.invokeFactory('organization', 'mands', **params)
    mands = pear['mands']

    # Services
    params['organization_level'] = "service"

    params['title'] = "Marketing"
    mands.invokeFactory('organization', 'marketing', **params)

    params['title'] = "Sales"
    mands.invokeFactory('organization', 'sales', **params)

    params['title'] = "Engineering"
    operations.invokeFactory('organization', 'engineering', **params)
    engineering = operations['engineering']

    params['title'] = "Quality Assurance"
    operations.invokeFactory('organization', 'qa', **params)

    # Create positions
    params = {'title': u"CEO",
              'position_type': u'ceo',
             }
    pear.invokeFactory('position', 'ceo', **params)
    pear_ceo = pear['ceo']

    params = {'title': u"CTO",
              'position_type': u'cto',
             }
    pear.invokeFactory('position', 'cto', **params)
    pear_cto = pear['cto']

    params = {'title': u"CMO",
              'position_type': u'cmo',
             }
    pear.invokeFactory('position', 'cmo', **params)

    params = {'title': u"President",
              'position_type': u'president',
             }
    plone.invokeFactory('position', 'president', **params)
    wikimedia.invokeFactory('position', 'president', **params)
    plone_president = plone['president']
    wikimedia_president = wikimedia['president']

    params = {'title': u"Study and Development Engineer",
              'position_type': u'engineer',
             }
    engineering.invokeFactory('position', 'engineer', **params)
    pear_engineer = engineering['engineer']

    # Create persons
    params = {'lastname': u'Doe',
              'firstname': u'John',
              'gender': u'M',
              'person_title': u'Mr',
              'birthday': date(1967, 11, 22),
              'email': u'johndoe@example.com',
              'phone': u'012/345.678',
             }
    contacts.invokeFactory('person', 'johndoe', **params)
    johndoe = contacts['johndoe']

    params = {'lastname': u'Doe',
              'firstname': u'Jane',
              'gender': u'F',
              'person_title': u'Mrs',
              'birthday': date(1976, 3, 2),
              'email': u'janedoe@example.com',
              'phone': u'012/997.670',
             }
    contacts.invokeFactory('person', 'janedoe', **params)
    janedoe = contacts['janedoe']

    params = {'lastname': u'Smith',
              'firstname': u'John',
              'gender': u'M',
              'person_title': u'Mr',
              'birthday': date(1977, 9, 2),
              'email': u'johnsmith@example.com',
              'phone': u'011/008.670',
             }
    contacts.invokeFactory('person', 'johnsmith', **params)
    johnsmith = contacts['johnsmith']

    params = {'lastname': u'Smith',
              'firstname': u'Peter',
              'gender': u'M',
              'person_title': u'Mr',
              'birthday': date(1966, 3, 2),
              'email': u'petersmith@example.com',
              'phone': u'012/978.070',
             }
    contacts.invokeFactory('person', 'petersmith', **params)
    petersmith = contacts['petersmith']

    # Add some held positions for these persons
    intids = getUtility(IIntIds)

    # link to a defined position
    params = {'start_date': date(2001, 5, 25),
              'position': RelationValue(intids.getId(pear_engineer)),
             }
    johndoe.invokeFactory('held_position', 'engineer-pear', **params)

    params = {'start_date': date(2002, 2, 11),
              'end_date': date(2010, 5, 31),
              'position': RelationValue(intids.getId(pear_cto)),
             }
    petersmith.invokeFactory('held_position', 'pear-cto', **params)

    params = {'start_date': date(2010, 6, 1),
              'position': RelationValue(intids.getId(pear_ceo)),
             }
    petersmith.invokeFactory('held_position', 'pear-ceo', **params)

    params = {'start_date': date(2008, 8, 1),
              'position': RelationValue(intids.getId(wikimedia_president)),
             }
    johnsmith.invokeFactory('held_position', 'wikimedia-pdt', **params)

    params = {'start_date': date(2009, 1, 1),
              'position': RelationValue(intids.getId(plone_president)),
             }
    johnsmith.invokeFactory('held_position', 'plone-pdt', **params)

    # link to an organization
    params = {'start_date': date(2007, 2, 11),
              'position': RelationValue(intids.getId(plone)),
             }
    petersmith.invokeFactory('held_position', 'plone-member', **params)

    params = {'start_date': date(2002, 9, 1),
              'position': RelationValue(intids.getId(plone)),
             }
    janedoe.invokeFactory('held_position', 'plone-member', **params)

    # we configure faceted navigations for contacts
    alsoProvides(contacts, IFacetedNavigable)
    alsoProvides(contacts, IFacetedSearchMode)
    alsoProvides(contacts, IHidePloneLeftColumn)
    alsoProvides(contacts, IHidePloneRightColumn)
    filename = os.path.dirname(__file__) + '/faceted_conf/contacts-example.xml'
    contacts.unrestrictedTraverse('@@faceted_exportimport').import_xml(
        import_file=open(filename))
