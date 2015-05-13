### Introduction

Demo/tutorial that will guide you through the basics of `collective.contact.*` suite for Plone.


### Installation

Use buildout to install the demo:

    $ python bootstrap.py
    $ bin/buildout

Then, create a new Plone site. Install `collective.contact.demo` profile. It will install and integrate `collective.contact.core`, `collective.contact.widget` and `collective.contact.facetednav` modules and add some demo data to your Plone site.


### Main concepts

`collective.contact.core` adds five content types:

  * `directory`: a special folder that contains contact data and basic configuration to choose available organization types, organization levels and position types. A Plone site can only have one directory.
  * `organization`: represents the organizations. Organizations that are directly added to the directory are root organizations. For example, they represent companies, associations, etc. Organizations can be added in organizations. In such cases, they are called sub-organizations, they can represent different levels in the organization such as departments, services, etc.
  * `position`: optional content type that describes the available roles in an organization. 
  * `person`: represents the people.
  * `held_position`: used to describe the fact that a person occupies a position or belongs to an organization. 

The philosophy behind these types is to be able to describe organization charts (that are not supposed to change often) independently from the persons roles in the organization. Then, you can add held positions to persons to describe the fact that this person occupied this position during a certain period of time. It also permit to add multiple held positions to a person (for example Peter Smith may be CEO of Pear company and member of Plone foundation).


`collective.contact.core` also adds the following dexterity behaviors:

  * `IBirthday`: adds a birth date field.
  * `IContactDetails`: adds fields related to contact information (phone numbers, email, etc) and address. It is enabled by default for person, organization and position content types.
  * `IGlobalPositioning`: adds global positioning informations. Deprecated and will probably be removed, you should rather use [plone.formwidget.geolocation](https://github.com/collective/plone.formwidget.geolocation).
  * `IRelatedOrganizations`: adds a contact field to manage related organizations.

Such as every other dexterity content-types, you can extend the contact types with your own behaviors. The fields added via behaviors or through the web will appear in the contents view.


### collective.contact.demo walkthrough

After the `collective.contact.demo` installation, you can explore the *Contacts* directory. It contains all contact data created by the profile.

For example, on [Pear company's page](http://localhost:8080/Plone/contacts/pear), you will see that it contains four departments and that some of these departments contains services. Pear also contains three positions: CEO, CTO and CMO. Peter Smith held position CTO from  Feb 11, 2002 to May 31, 2010 and holds position CEO from Jun 01, 2010.


### The widget

`collective.contact.widget` provides a powerful widget to search and create contact content types from another contact. The aim of this widget is to avoid duplicates amongst organizations and persons.

To try this widget, go in an organization, e.g. [Pear](http://localhost:8080/Plone/contacts/pear/) and click the "Create contact" link.

The "Create contact" form that pops up contains 2 contact widgets. By default, *Pear* organization is selected in the organization field but you can search for another organization. If you don't find your organization, you can also create a new organization from this widget.

The person field works the same way but it searches in persons contents. 

You can use contact widget in your own schemas and configure its source so it searches amongst the contact content types you want. See held position content type's position field for an example.


### Additional modules

You can choose to use the following modules to enhance `collective.contact.*` experience.

#### collective.contact.facetednav

[This module](https://github.com/collective/collective.contact.facetednav) provides views and utils to visualize contacts with a faceted navigation (see [eea.facetednavigation](https://github.com/eea/eea.facetednavigation)).

It also provides batch actions for contacts. When actions are enabled, it adds a checkbox in front of each result in the faceted navigation. User can select contacts and select which action will be performed. By default, the module provides the following actions: delete and edit. If you have [collective.excelexport](https://github.com/collective/collective.excelexport) installed, it also adds excel export to actions.
You can also easily add your own actions. For more details, see [collective.contact.facetednav README](https://github.com/collective/collective.contact.facetednav).


#### collective.contact.duplicated

[This module](https://github.com/collective/collective.contact.duplicated) provides a tool to manage duplicated organizations, persons or held positions.

For the moment, this needs [collective.contact.facetednav](https://github.com/collective/collective.contact.facetednav) with batch actions allowed. Select two (or more) contacts (organization, held_position, person, etc) and click on "Merge duplicated" button. You can then choose for each field how these contents will be merged.


#### collective.contact.membrane

[This module](https://github.com/collective/collective.contact.contactlist) provides adapters and behaviors to make persons behaves as Plone users and organizations/positions as Plone groups. Only persons in *active* review state will behave as Plone users. Persons that have an *active* held position in an organization automatically become members of the Plone group represented by the organization.

For more details, see [dexterity.membrane](https://github.com/collective/dexterity.membrane) and [Products.membrane](https://github.com/collective/Products.membrane).


#### collective.contact.contactlist

[This module](https://github.com/collective/collective.contact.contactlist) provides "by user" lists of contacts. You can add/remove contacts from your lists and then export your lists in excel format. You can also add your own actions (for example to use contact lists as mailing lists).
