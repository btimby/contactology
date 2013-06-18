#!/usr/bin/env python

import httplib

from urllib import quote
from functools import wraps

try:
    import simplejson as json
    json  # Make pyflakes happy!
except ImportError:
    import json


def optional(f):
    "Decorator that merges kwargs into optionalParameters keyword argument."
    @wraps(f)
    def merge_params(*args, **kwargs):
        op = kwargs.pop('optionalParameters', {})
        op.update(kwargs)
        kwargs['optionalParameters'] = op
        return f(*args, **kwargs)
    return merge_params


class Contactology:
    def __init__(self, key, useHTTPS=False):
        self.key = key
        self.host = "api.emailcampaigns.net:80"
        self.path = "/2/REST/"
        self.version = "1.3.9"
        self.useHTTPS = useHTTPS
        if self.useHTTPS:
            self.host = "api.emailcampaigns.net:443"

    def Integration_Upload_Csv(self, csv):
        '''
        Upload csv data for mapping and importing via the Contactology UI

        Required keyword arguments:

        csv (string) - Your CSV data

        Optional keyword arguments:


        Returns struct - A struct containing a path key to be used with the
        webapp
        '''

        args = {
            'key': self.key,
            'method': 'Integration_Upload_Csv',
            'csv': csv,
        }

        data = self.makeCall(args)
        return data

    def Integration_Get_Cookie(self, clientId, username, time):
        '''
        Integrate Contactology into your own web application by setting your
        CAMPAIGNS_SSO_COOKIE

        Required keyword arguments:

        clientId (int) - The client ID you are creating the cookie for, must be
            a client belonging to your reseller account
        username (string) - The belonging to the client ID you are logging in
            with the cookie
        time (int) - Cookie timeout in seconds

        Optional keyword arguments:


        Returns string - Cookie value to be set in CAMPAIGNS_SSO_COOKIE
        '''

        args = {
            'key': self.key,
            'method': 'Integration_Get_Cookie',
            'clientId': clientId,
            'username': username,
            'time': time,
        }

        data = self.makeCall(args)
        return data

    def Integration_Login_Get_Cookie(self, username, password, time):
        '''
        Integrate Contactology into your own web application by setting your
        CAMPAIGNS_SSO_COOKIE using your client's credentials

        Required keyword arguments:

        username (string) - The of the client
        password (string) - The current of the client
        time (int) - Cookie timeout in seconds

        Optional keyword arguments:


        Returns struct - Returns a struct on a valid username/password combo
        '''

        args = {
            'key': self.key,
            'method': 'Integration_Login_Get_Cookie',
            'username': username,
            'password': password,
            'time': time,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Add_Email(self, email, **kwargs):
        '''
        Add a single email address - does not support Custom Fields

        Required keyword arguments:

        email (string) - An address
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        activateDeleted (bool) - If this contact was already deleted,
        reactivate them - defaults to true

        Returns bool - Returns true on success
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Add_Email',
            'email': email,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Add(self, email, customFields, **kwargs):
        '''
        Add a contact with custom fields

        Required keyword arguments:

        email (string) - Email address of the contact
        customFields (dict) - is a container for custom field data
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true
        updateCustomFields (bool) - If this contact already exists, replace
            custom field values with values provided - defaults to false. Will
            not update the custom fields for a contact that is deactivated (
            bounced, globally unsubscribed, etc.)

        Returns bool - Returns true on success
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Add',
            'email': email,
            'customFields': customFields,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Add_Email_Multiple(self, emails, **kwargs):
        '''
        Add multiple email addresses - does not support Custom Fields

        Required keyword arguments:

        emails (array) - An list of email addresses
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true

        Returns struct - Returns a list of email addresses, each marked "true"
            or "false" showing whether they were suppressed
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Add_Email_Multiple',
            'emails': emails,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Add_Multiple(self, contacts, **kwargs):
        '''
        Add multiple contacts with Custom Fields

        Required keyword arguments:

        contacts (array) - Array of contact dicts
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true
        updateCustomFields (bool) - If this contact already exists, replace
            custom field values with values provided - defaults to false

        Returns struct - Aggregate import results
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Add_Multiple',
            'contacts': contacts,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Import(self, contacts, source, **kwargs):
        '''
        Import a collection of contacts. Can import up to 1000 contacts with
            a single call.

        Required keyword arguments:

        contacts (array) - Array of contact_hash items, as explained above
        source (string) - A short description of the of your contacts
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        listIds (list) - Import these contacts into all of the specified lists
        groupIds (list) - Import these contacts into all of the specified lists
        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true
        updateCustomFields (bool) - If this contact already exists, replace
            custom field values with values provided - defaults to false

        Returns struct - Aggregate import results
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Import',
            'contacts': contacts,
            'source': source,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Import_Delayed(self, contacts, source, callbackUrl, jobId,
                               chunkNum, **kwargs):
        '''
        Import a collection of contacts into a set of lists and groups
        asynchronously

        Required keyword arguments:

        contacts (array) - Array of contact_hash items, as explained above
        source (string) - A short description of the of your contacts
        callbackUrl (string) - A URL endpoint for the results of the import to
            be POSTed to
        jobId (string) - A Job ID used to match up the import in your webapp
        chunkNum (int) - An Import Chunk number used to match up in your
            webapp - use this to keep track of what chunks have been processed,
            they may not be handled in order
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        listIds (list) - Import these contacts into all of the specified lists
        groupIds (list) - Import these contacts into all of the specified
            groups
        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true
        updateCustomFields (bool) - If this contact already exists, replace
            custom field values with values provided - defaults to false

        Returns bool -
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Import_Delayed',
            'contacts': contacts,
            'source': source,
            'callbackUrl': callbackUrl,
            'jobId': jobId,
            'chunkNum': chunkNum,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Contact_Get_Active_Count(self):
        '''
        Get a count of active contacts

        Required keyword arguments:

        Optional keyword arguments:

        Returns int - Returns the number of active contacts for your account
        '''

        args = {
            'key': self.key,
            'method': 'Contact_Get_Active_Count',
        }

        data = self.makeCall(args)
        return data

    def Contact_Get_Active(self):
        '''
        Get a list of active contacts

        Required keyword arguments:

        Optional keyword arguments:

        Returns array - Returns an array containing the email addresses of
        active contacts
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Get_Active',
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Get(self, email, **kwargs):
        '''
        Get information on a single contact

        Required keyword arguments:

        email (string) - The address of the contact you want information for
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        customFields (list) - Array of custom field IDs or tokens you want
            included with the results (ex: ['first_name','last_name',
            'email_address'] OR [1,2,3])
        getAllCustomFields (bool) - As optionalParameter customFields, but
            automatically includes all custom fields. Overrides customFields
            value

        Returns struct - Returns a struct of structs, keyed off of email
        address, each containing the keys specified above
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Get',
            'email': email,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Find(self, **kwargs):
        '''
        Get a list of contacts

        Required keyword arguments:

        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        customFields (list) - Array of custom field IDs or tokens you want
            included with the results (ex: ['first_name','last_name',
            'email_address'] OR [1,2,3])
        status (string) - Get only contacts with a specific status, valid
            values: active, bounced, deleted, suppressed
        email (string) - Get only one specific contact
        source (string) - Get only contacts with the specified source
        scoreMin (int) - Get only contacts with an engagement score greater
            than or equal to the specified engagement score
        scoreMax (int) - Get only contacts with an engagement score less than
            or equal to the specified engagement score
        ratingMin (int) - Get only contacts with a contact rating greater than
            or equal to the specified contact rating
        ratingMax (int) - Get only contacts with a contact rating less than or
            equal to the specified contact rating
        getAllCustomFields (bool) - As optionalParameter customFields, but
            automatically includes all custom fields. Overrides customFields
            value
        sortDir (string) - Sort direction, valid values: U, D
        offset (int) - The number of records to skip (specify a starting point)
        num (int) - The maximum number of records to return

        Returns struct - Returns a struct of structs, keyed off of email
        address, each containing the keys specified above
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Find',
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Get_Count(self, **kwargs):
        '''
        Find count for a set of Contacts

        Required keyword arguments:

        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        status (string) - Get only contacts with a specific status, valid
            values: active, bounced, deleted, suppressed
        email (string) - Get only one specific contact
        source (string) - Get only contacts with the specified source
        scoreMin (int) - Get only contacts with an engagement score greater
            than or equal to the specified engagement score
        scoreMax (int) - Get only contacts with an engagement score less than
            or equal to the specified engagement score
        ratingMin (int) - Get only contacts with a contact rating greater than
            or equal to the specified contact rating
        ratingMax (int) - Get only contacts with a contact rating less than or
            equal to the specified contact rating

        Returns int - Number of contacts
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Get_Count',
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Find_Ids(self, **kwargs):
        '''
        Find a set of Contacts and return just the record IDs

        Required keyword arguments:

        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        status (string) - Get only contacts with a specific status, valid
            values: active, bounced, deleted, suppressed
        email (string) - Get only one specific contact
        source (string) - Get only contacts with the specified source
        scoreMin (int) - Get only contacts with an engagement score greater
            than or equal to the specified engagement score
        scoreMax (int) - Get only contacts with an engagement score less than
            or equal to the specified engagement score
        ratingMin (int) - Get only contacts with a contact rating greater than
            or equal to the specified contact rating
        ratingMax (int) - Get only contacts with a contact rating less than or
            equal to the specified contact rating

        Returns array - Contact Ids
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Find_Ids',
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Update(self, email, customFields, **kwargs):
        '''
        Update the custom fields of an existing contact

        Required keyword arguments:

        email (string) - The address of the contact you want to update
        customFields (dict) - The custom fields you want to update and their
            new values
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true

        Returns bool - Returns true on success
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Update',
            'email': email,
            'customFields': customFields,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Contact_Change_Email(self, email, newEmail):
        '''
        Change the email address for an existing contact while preserving list
        and group subscriptions

        Required keyword arguments:

        email (string) - The current address of the contact
        newEmail (string) - The contact's new email address

        Optional keyword arguments:

        Returns struct - Returns a struct of structs, keyed off of email
        address, each containing the keys specified below
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Change_Email',
            'email': email,
            'newEmail': newEmail,
        }

        data = self.makeCall(args)
        return data

    def Contact_Activate(self, email):
        '''
        Return a contact to active status

        Required keyword arguments:

        email (string) - The address of the contact you wish to activate

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Activate',
            'email': email,
        }

        data = self.makeCall(args)
        return data

    def Contact_Delete(self, email):
        '''
        Delete a contact

        Required keyword arguments:

        email (string) - An address

        Optional keyword arguments:

        Returns bool - True if delete was successful
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Delete',
            'email': email,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Suppress(self, email, **kwargs):
        '''
        Suppress a contact

        Required keyword arguments:

        email (string) - An address
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        campaignId (int) - The ID of the campaign tied to this suppression

        Returns bool - Returns true or false indicating whether the contact
        was suppressed
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Suppress',
            'email': email,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Suppress_Multiple(self, emails, **kwargs):
        '''
        Suppress multiple contacts

        Required keyword arguments:

        emails (array) - An list of email addresses
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        campaignId (int) - The ID of the campaign tied to this suppression

        Returns struct - Returns a list of email addresses, each marked "true"
        or "false" showing whether they were suppressed
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Suppress_Multiple',
            'emails': emails,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Contact_Purge(self, email):
        '''
        Purge a contact

        Required keyword arguments:

        email (string) - An address

        Optional keyword arguments:

        Returns bool - Returns true or false indicating whether the contact
        was purged
        '''

        args = {
            'key': self.key,
            'method': 'Contact_Purge',
            'email': email,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Get_History(self, email, **kwargs):
        '''
        Get the history for a contact

        Required keyword arguments:

        email (string) - An address
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        minDate (string) - Return contact history created on or after minDate.
            Format as UTC.
        maxDate (string) - Return contact history created on or before maxDate.
            Format as UTC.
        historyTypes (dict) - Limit the type of contact history data returned.
        campaignIds (dict) - A dict of campaign IDs

        Returns struct - Returns a struct of history information
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Get_History',
            'email': email,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Get_History_Multiple(self, **kwargs):
        '''
        Get the history for a set of contacts

        Required keyword arguments:

        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        addressIds (dict) - A dict of email address IDs
        campaignIds (dict) - A dict of campaign IDs
        minDate (string) - Return contact history created on or after minDate.
            Format as UTC.
        maxDate (string) - Return contact history created on or before maxDate.
            Format as UTC.
        historyTypes (dict) - Limit the type of contact history data returned.
        sortDir (string) - Sort direction, valid values: U, D
        offset (int) - The number of records to skip (specify a starting point)
        num (int) - The maximum number of records to return (must also specify
            an offset when using the num parameter)

        Returns struct - Returns a struct of history information
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Get_History_Multiple',
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Contact_Get_Subscriptions(self, email):
        '''
        Get the listIds for all the lists this contact is subscribed to

        Required keyword arguments:

        email (string) - An address

        Optional keyword arguments:


        Returns array - Returns an array of listIds
        '''

        args = {
            'key': self.key,
            'method': 'Contact_Get_Subscriptions',
            'email': email,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Contact_Set_Subscriptions(self, email, listIds, **kwargs):
        '''
        Unsubscribe a contact from all lists, then subscribe the contact to the
        specified lists.

        Required keyword arguments:

        email (string) - The address of the contact you wish to set the
            subscriptions of
        listIds (array) - An list of the contact should be subscribed to and
            unsubscribed from all others
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        campaignId (int) - The ID of the campaign tied to this subscription
            action

        Returns array - An array of all the lists the contact is subscribed to
        after the operation, should have the same values as listIds
        '''
        args = {
            'key': self.key,
            'method': 'Contact_Set_Subscriptions',
            'email': email,
            'listIds': listIds,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Contact_Get_No_Subscriptions(self):
        '''
        Get a list of all email addresses that are not subscribed to any list

        Required keyword arguments:

        Optional keyword arguments:

        Returns array - A list of email addresses that are not subscribed to
        any list
        '''

        args = {
            'key': self.key,
            'method': 'Contact_Get_No_Subscriptions',
        }

        data = self.makeCall(args)
        return data

    def Contact_Get_No_Activity(self):
        '''
        Get a list of all email addresses that have been sent campaigns but
        have not opened or clicked

        Required keyword arguments:

        Optional keyword arguments:

        sentCount (int) - Return email addresses who recieved campaigns but
        have taken no action (e.g.: find email addresses who have not opened or
        clicked on any of the 3 most recent campaigns)

        Returns array - A list of email addresses have been sent campaigns but
        have not opened or clicked
        '''

        args = {
            'key': self.key,
            'method': 'Contact_Get_No_Activity',
        }

        data = self.makeCall(args)
        return data

    def Contact_Delete_No_Activity(self):
        '''
        Delete all email addresses that have been sent campaigns but have not
        opened or clicked

        Required keyword arguments:

        Optional keyword arguments:

        sentCount (int) - Return email addresses who recieved campaigns but
        have taken no action (e.g.: find email addresses who have not opened or
        clicked on any of the 3 most recent campaigns)

        Returns int - The number of contacts that were deleted
        '''

        args = {
            'key': self.key,
            'method': 'Contact_Delete_No_Activity',
        }

        data = self.makeCall(args)
        return data

    def Contact_Get_Person_Code(self, email):
        '''
        Retrieve the Person Code for a given contact

        Required keyword arguments:

        email (string) - The contact's address you want the Person Code for

        Optional keyword arguments:

        Returns string - Person Code
        '''

        args = {
            'key': self.key,
            'method': 'Contact_Get_Person_Code',
            'email': email,
        }

        data = self.makeCall(args)
        return data

    def Contact_Delete_No_Subscriptions(self):
        '''
        Delete all email addresses that are not subscribed to any list

        Required keyword arguments:

        Optional keyword arguments:

        Returns int - The number of contacts that were deleted
        '''

        args = {
            'key': self.key,
            'method': 'Contact_Delete_No_Subscriptions',
        }

        data = self.makeCall(args)
        return data

    @optional
    def CustomField_Add_Textbox(self, fieldName, required, subscriberCanEdit,
                                **kwargs):
        '''
        Add a Textbox CustomField to your signup form

        Required keyword arguments:

        fieldName (string) - The name of your CustomField - this will be the
            label for your field on the form
        required (bool) - Is this field when the form is filled out?
        subscriberCanEdit (bool) - Can the subscriber edit this value later?
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        displayOrder (int) - A number indicating what order this field should
            appear in
        defaultValue (string) - Set a defaultValue if you want this field
            prepopulated on the form

        Returns struct - Returns a struct containing the new CustomFields
        fieldId and token
        '''
        args = {
            'key': self.key,
            'method': 'CustomField_Add_Textbox',
            'fieldName': fieldName,
            'required': required,
            'subscriberCanEdit': subscriberCanEdit,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def CustomField_Add_Decimal(self, fieldName, required, subscriberCanEdit,
                                **kwargs):
        '''
        Add a Decimal CustomField to your signup form

        Required keyword arguments:

        fieldName (string) - The name of your CustomField - this will be the
            label for your field on the form
        required (bool) - Is this field when the form is filled out?
        subscriberCanEdit (bool) - Can the subscriber edit this value later?
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        displayOrder (int) - A number indicating what order this field should
            appear in
        defaultValue (float) - Set a defaultValue if you want this field
            prepopulated on the form

        Returns struct - Returns a struct containing the new CustomFields
        fieldId and token
        '''
        args = {
            'key': self.key,
            'method': 'CustomField_Add_Decimal',
            'fieldName': fieldName,
            'required': required,
            'subscriberCanEdit': subscriberCanEdit,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def CustomField_Add_Integer(self, fieldName, required, subscriberCanEdit,
                                **kwargs):
        '''
        Add an Integer CustomField to your signup form

        Required keyword arguments:

        fieldName (string) - The name of your CustomField - this will be the
            label for your field on the form
        required (bool) - Is this field when the form is filled out?
        subscriberCanEdit (bool) - Can the subscriber edit this value later?
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        displayOrder (int) - A number indicating what order this field should
            appear in
        defaultValue (int) - Set a defaultValue if you want this field
            prepopulated on the form

        Returns struct - Returns a struct containing the new CustomFields
        fieldId and token
        '''
        args = {
            'key': self.key,
            'method': 'CustomField_Add_Integer',
            'fieldName': fieldName,
            'required': required,
            'subscriberCanEdit': subscriberCanEdit,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def CustomField_Add_Dropdown(self, fieldName, required, subscriberCanEdit,
                                 options, **kwargs):
        '''
        Add a Dropdown CustomField to your signup form

        Required keyword arguments:

        fieldName (string) - The name of your CustomField - this will be the
            label for your field on the form
        required (bool) - Is this field when the form is filled out?
        subscriberCanEdit (bool) - Can the subscriber edit this value later?
        options (array) - An list of strings to be shown in the dropdown
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        displayOrder (int) - A number indicating what order this field should
            appear in
        defaultValue (string) - Set a defaultValue if you want this field
            prepopulated on the form - your value must be present in the
            options list

        Returns struct - Returns a struct containing the new CustomFields
        fieldId and token
        '''
        args = {
            'key': self.key,
            'method': 'CustomField_Add_Dropdown',
            'fieldName': fieldName,
            'required': required,
            'subscriberCanEdit': subscriberCanEdit,
            'options': options,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def CustomField_Add_Radio(self, fieldName, required, subscriberCanEdit,
                              options, **kwargs):
        '''
        Add a Radio CustomField to your signup form

        Required keyword arguments:

        fieldName (string) - The name of your CustomField - this will be the
            label for your field on the form
        required (bool) - Is this field when the form is filled out?
        subscriberCanEdit (bool) - Can the subscriber edit this value later?
        options (array) - An list of strings, each value will have its own
            radio button
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        displayOrder (int) - A number indicating what order this field should
            appear in
        defaultValue (string) - Set a defaultValue if you a radio button
            preselected on the form - your value must be present in the options
            list

        Returns struct - Returns a struct containing the new CustomFields
        fieldId and token
        '''
        args = {
            'key': self.key,
            'method': 'CustomField_Add_Radio',
            'fieldName': fieldName,
            'required': required,
            'subscriberCanEdit': subscriberCanEdit,
            'options': options,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def CustomField_Add_Checkbox(self, fieldName, required, subscriberCanEdit,
                                 **kwargs):
        '''
        Add a single Checkbox CustomField to your signup form

        Required keyword arguments:

        fieldName (string) - The name of your CustomField - this will be the
            label for your field on the form
        required (bool) - Is this field when the form is filled out?
        subscriberCanEdit (bool) - Can the subscriber edit this value later?
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        displayOrder (int) - A number indicating what order this field should
            appear in
        defaultValue (bool) - Set a defaultValue if you want this field checked
            automatically

        Returns struct - Returns a struct containing the new CustomFields
        fieldId and token
        '''
        args = {
            'key': self.key,
            'method': 'CustomField_Add_Checkbox',
            'fieldName': fieldName,
            'required': required,
            'subscriberCanEdit': subscriberCanEdit,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def CustomField_Add_CheckboxList(self, fieldName, required,
                                     subscriberCanEdit, options, **kwargs):
        '''
        Add a CheckboxList CustomField to your signup form

        Required keyword arguments:

        fieldName (string) - The name of your CustomField - this will be the
            label for your field on the form
        required (bool) - Is this field when the form is filled out?
        subscriberCanEdit (bool) - Can the subscriber edit this value later?
        options (array) - An list of strings, each value will have its own
            checkbox
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        displayOrder (int) - A number indicating what order this field should
            appear in
        defaultValue (list) - Each string in this list must correspond to a
            string in options, the checkbox for each string in defaultValue
            will be checked initially

        Returns struct - Returns a struct containing the new CustomFields
        fieldId and token
        '''
        args = {
            'key': self.key,
            'method': 'CustomField_Add_CheckboxList',
            'fieldName': fieldName,
            'required': required,
            'subscriberCanEdit': subscriberCanEdit,
            'options': options,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def CustomField_Add_Date(self, fieldName, required, subscriberCanEdit,
                             **kwargs):
        '''
        Add a Date CustomField to your signup form

        Required keyword arguments:

        fieldName (string) - The name of your CustomField - this will be the
            label for your field on the form
        required (bool) - Is this field when the form is filled out?
        subscriberCanEdit (bool) - Can the subscriber edit this value later?
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        displayOrder (int) - A number indicating what order this field should
            appear in
        defaultValue (string) - Set a defaultValue if you want this field
            prepopulated on the form

        Returns struct - Returns a struct containing the new CustomFields
        fieldId and token
        '''
        args = {
            'key': self.key,
            'method': 'CustomField_Add_Date',
            'fieldName': fieldName,
            'required': required,
            'subscriberCanEdit': subscriberCanEdit,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def CustomField_Add_Email(self, fieldName, required, subscriberCanEdit,
                              **kwargs):
        '''
        Add an Email CustomField to your signup form

        Required keyword arguments:

        fieldName (string) - The name of your CustomField - this will be the
            label for your field on the form
        required (bool) - Is this field when the form is filled out?
        subscriberCanEdit (bool) - Can the subscriber edit this value later?
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        displayOrder (int) - A number indicating what order this field should
            appear in
        defaultValue (string) - Set a defaultValue if you want this field
            prepopulated on the form - must be a valid email address

        Returns struct - Returns a struct containing the new CustomFields
        fieldId and token
        '''
        args = {
            'key': self.key,
            'method': 'CustomField_Add_Email',
            'fieldName': fieldName,
            'required': required,
            'subscriberCanEdit': subscriberCanEdit,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def CustomField_Add_Phone(self, fieldName, required, subscriberCanEdit,
                              **kwargs):
        '''
        Add a Phone CustomField to your signup form

        Required keyword arguments:

        fieldName (string) - The name of your CustomField - this will be the
            label for your field on the form
        required (bool) - Is this field when the form is filled out?
        subscriberCanEdit (bool) - Can the subscriber edit this value later?
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        displayOrder (int) - A number indicating what order this field should
            appear in
        defaultValue (string) - Set a defaultValue if you want this field
            prepopulated on the form

        Returns struct - Returns a struct containing the new CustomFields
        fieldId and token
        '''
        args = {
            'key': self.key,
            'method': 'CustomField_Add_Phone',
            'fieldName': fieldName,
            'required': required,
            'subscriberCanEdit': subscriberCanEdit,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def CustomField_Add_StateDropdown(self, fieldName, required,
                                      subscriberCanEdit, **kwargs):
        '''
        Add a StateDropdown CustomField to your signup form

        Required keyword arguments:

        fieldName (string) - The name of your CustomField - this will be the
            label for your field on the form
        required (bool) - Is this field when the form is filled out?
        subscriberCanEdit (bool) - Can the subscriber edit this value later?
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        displayOrder (int) - A number indicating what order this field should
            appear in
        defaultValue (string) - Set a defaultValue if you want this value
            preselected in the dropdown - must be the full name of a valid
            state

        Returns struct - Returns a struct containing the new CustomFields
        fieldId and token
        '''
        args = {
            'key': self.key,
            'method': 'CustomField_Add_StateDropdown',
            'fieldName': fieldName,
            'required': required,
            'subscriberCanEdit': subscriberCanEdit,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def CustomField_Add_Address(self, fieldName, required, subscriberCanEdit,
                                **kwargs):
        '''
        Add an Address CustomField to your signup form

        Required keyword arguments:

        fieldName (string) - The name of your CustomField - this will be the
            label for your field on the form
        required (bool) - Is this field when the form is filled out?
        subscriberCanEdit (bool) - Can the subscriber edit this value later?
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        displayOrder (int) - A number indicating what order this field should
            appear in
        defaultValue (string) - Set a defaultValue if you want this field
            prepopulated on the form

        Returns struct - Returns a struct containing the new CustomFields
        fieldId and token
        '''
        args = {
            'key': self.key,
            'method': 'CustomField_Add_Address',
            'fieldName': fieldName,
            'required': required,
            'subscriberCanEdit': subscriberCanEdit,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def CustomField_Find(self, searchParameters=None):
        '''
        Get a list of CustomFields - excluding searchParameters indicates you
        want a list of all CustomFields

        Required keyword arguments:

        searchParameters (dict) - Provide a dict to narrow your results

        Optional keyword arguments:

        Returns struct - Returns a struct for each CustomField found
        '''

        if searchParameters is None:
            searchParameters = {}

        args = {
            'key': self.key,
            'method': 'CustomField_Find',
            'searchParameters': searchParameters,
        }

        data = self.makeCall(args)
        return data

    def CustomField_Get_All(self):
        '''
        Get a list of all current CustomFields

        Required keyword arguments:

        Optional keyword arguments:

        Returns struct - Returns a struct for each CustomField found
        '''

        args = {
            'key': self.key,
            'method': 'CustomField_Get_All',
        }

        data = self.makeCall(args)
        return data

    def CustomField_Update(self, fieldId, updateParameters):
        '''
        Update an existing CustomField

        Required keyword arguments:

        fieldId (int) - The of the CustomField you want to modify
        updateParameters (dict) - A dict of replacement values for your
            CustomField - only specify fields that you want to change

        Optional keyword arguments:

        Returns struct - Returns a struct with your CustomField's new
        properties
        '''

        args = {
            'key': self.key,
            'method': 'CustomField_Update',
            'fieldId': fieldId,
            'updateParameters': updateParameters,
        }

        data = self.makeCall(args)
        return data

    def CustomField_Reorder(self, reorder):
        '''
        Update the displayOrder property on multiple fields at once

        Required keyword arguments:

        reorder (dict) - A dict where each key is a fieldId and each value
            is the new displayOrder

        Optional keyword arguments:

        Returns struct - Returns a struct for each CustomField updated
        '''

        args = {
            'key': self.key,
            'method': 'CustomField_Reorder',
            'reorder': reorder,
        }

        data = self.makeCall(args)
        return data

    def CustomField_Delete(self, fieldId):
        '''
        Delete a CustomField - this action cannot be undone

        Required keyword arguments:

        fieldId (int) - The of the CustomField you want to delete -
            first_name, last_name and email_address cannot be deleted

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'CustomField_Delete',
            'fieldId': fieldId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def List_Add_Test(self, name, **kwargs):
        '''
        Create a new test contact list

        Required keyword arguments:

        name (string) - The of your list
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        description (string) - A short description for your list
        easycastName (string) - A one word shortcut for EasyCast access, will
            create an EasyCast email address in the format
            NAME.list.YOURID@send.emailcampaigns.net
        listOwnerEmail (string) - An email address that receives an email
            whenever a contact subscribes to this list, and can approve
            "EasyCast" messages

        Returns int - id Returns the List ID of your new List
        '''
        args = {
            'key': self.key,
            'method': 'List_Add_Test',
            'name': name,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def List_Add_Internal(self, name, **kwargs):
        '''
        Create a new internal contact list

        Required keyword arguments:

        name (string) - The of your list
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        description (string) - A short description for your list
        easycastName (string) - A one word shortcut for EasyCast access, will
            create an EasyCast email address in the format
            NAME.list.YOURID@send.emailcampaigns.net
        listOwnerEmail (string) - An email address that receives an email
            whenever a contact subscribes to this list, and can approve
            "EasyCast" messages

        Returns int - id Returns the List ID of your new List
        '''
        args = {
            'key': self.key,
            'method': 'List_Add_Internal',
            'name': name,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def List_Add_Private(self, name, **kwargs):
        '''
        Create a new private contact list

        Required keyword arguments:

        name (string) - The of your list
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        description (string) - A short description for your list
        easycastName (string) - A one word shortcut for EasyCast access, will
            create an EasyCast email address in the format
            NAME.list.YOURID@send.emailcampaigns.net
        listOwnerEmail (string) - An email address that receives an email
            whenever a contact subscribes to this list, and can approve
            "EasyCast" messages
        optIn (bool) - Setting this to true means that the system will send
            contacts a confirmation email before sending them messages
        optInFromEmail (string) - The email address that the optInMessage
            confirmation email will be sent from. Required if optIn is true
        optInFromEmailAlias (string) - The From Name that the optInMessage
            confirmation email will be sent from.
        optInSubject (string) - The subject line of the optInMessage
            confirmation email. Required if optIn is true
        optInMessage (string) - The HTML email body for the confirmation email.
            MUST include the {confirm_url} token that will insert the link to
            the correct subscription confirmation page. Required if optIn is
            true

        Returns int - id Returns the List ID of your new List
        '''
        args = {
            'key': self.key,
            'method': 'List_Add_Private',
            'name': name,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def List_Add_Public(self, name, **kwargs):
        '''
        Create a new public contact list

        Required keyword arguments:

        name (string) - The of your list
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        description (string) - A short description for your list
        easycastName (string) - A one word shortcut for EasyCast access, will
            create an EasyCast email address in the format
            NAME.list.YOURID@send.emailcampaigns.net
        listOwnerEmail (string) - An email address that receives an email
            whenever a contact subscribes to this list, and can approve
            "EasyCast" messages
        optIn (bool) - Setting this to true means that the system will send
            contacts a confirmation email before sending them messages
        optInFromEmail (string) - The email address that the optInMessage
            confirmation email will be sent from. Required if optIn is true
        optInFromEmailAlias (string) - The From Name that the optInMessage
            confirmation email will be sent from.
        optInSubject (string) - The subject line of the optInMessage
            confirmation email. Required if optIn is true
        optInMessage (string) - The HTML email body for the confirmation email.
            MUST include the {confirm_url} token that will insert the link to
            the correct subscription confirmation page. Required if optIn is
            true

        Returns int - id Returns the List ID of your new List
        '''
        args = {
            'key': self.key,
            'method': 'List_Add_Public',
            'name': name,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def List_Delete(self, listId):
        '''
        Delete a list you created

        Required keyword arguments:

        listId (int) - The List ID of the list you wish to delete

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'List_Delete',
            'listId': listId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def List_Subscribe(self, listId, email, **kwargs):
        '''
        Add an email address contact to an existing list

        Required keyword arguments:

        listId (int) - The ID of the list you want to subscribe the email
            address to
        email (string) - The address you are subscribing
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        campaignId (int) - The ID of the campaign tied to this subscription
            action
        source (string) - A short description of the source of your contact

        Returns bool - True on success
        '''

        if optionalParameters is None:
            optionalParameters = {}

        for k, v in kwargs.iteritems():
            optionalParameters[k] = v

        args = {
            'key': self.key,
            'method': 'List_Subscribe',
            'listId': listId,
            'email': email,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def List_Unsubscribe(self, listId, email, optionalParameters=None,
                         **kwargs):
        '''
        Remove an email address contact from an existing list

        Required keyword arguments:

        listId (int) - The ID of the list you want to unsubscribe the email
            address from
        email (string) - The address you are unsubscribing
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        campaignId (int) - The ID of the campaign tied to this subscription
            action

        Returns bool - True on success
        '''
        args = {
            'key': self.key,
            'method': 'List_Unsubscribe',
            'listId': listId,
            'email': email,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def List_Unsubscribe_Multiple(self, listId, emails):
        '''
        Remove multiple email address contacts from an existing list

        Required keyword arguments:

        listId (int) - The ID of the list you want to unsubscribe the email
            address from
        emails (array) - An list of email addresses you are unsubscribing

        Optional keyword arguments:

        Returns int - Returns the number of contacts removed
        '''

        args = {
            'key': self.key,
            'method': 'List_Unsubscribe_Multiple',
            'listId': listId,
            'emails': emails,
        }

        data = self.makeCall(args)
        return data

    @optional
    def List_Get_Contacts(self, listId, **kwargs):
        '''
        Retrieve a list of contacts in a given list

        Required keyword arguments:

        listId (int) - The ID of the list you retrieve contacts from
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        status (string) - Retrieve only contacts with a particular list status,
            valid values: subscribed, unsubscribed, bounced
        contactStatus (string) - Retrieve only contacts with a particular
            contact status, valid values: active, bounced, deleted, suppressed
        startDate (string) - Retrieve only contacts subscribed or updated on
            or after this date, format: YYYY-MM-DD HH:MM:SS
        endDate (string) - Retrieve only contacts subscribed or updated on or
            before this date, format: YYYY-MM-DD HH:MM:SS
        customFields (list) - Array of custom field IDs or tokens you want
            included with the results (ex: ['first_name','last_name',
            'email_address'] OR [1,2,3])
        sortDir (string) - Sort direction, valid values: U, D
        offset (int) - The number of records to skip (specify a starting point)
        num (int) - The maximum number of records to return

        Returns struct - Struct of records each with a key of email and values
        of contactId, email, source, status, statusCode and listStatus
        '''
        args = {
            'key': self.key,
            'method': 'List_Get_Contacts',
            'listId': listId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def List_Get_Active_Lists(self, **kwargs):
        '''
        Get a listing of currently active lists

        Required keyword arguments:

        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        type (string) - Return only lists of a given type, value values:
            public, private, test, internal
        sortBy (string) - Field to sort by, value values: name, description,
            id, type, status
        sortDir (string) - Sort direction, valid values: U, D
        offset (int) - The number of records to skip (specify a starting point)
        num (int) - The maximum number of records to return

        Returns struct - Array of records with the key of listId and values of
        listId, name, description, type and listOwnerEmail
        '''
        args = {
            'key': self.key,
            'method': 'List_Get_Active_Lists',
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def List_Get_Info(self, listId):
        '''
        Get information about a list, including name, type, created, easyCast,
        listOwner and optIn info (where applicable)

        Required keyword arguments:

        listId (int) - The ID of the list you are getting info for

        Optional keyword arguments:


        Returns struct - Returns info about the requested list
        '''

        args = {
            'key': self.key,
            'method': 'List_Get_Info',
            'listId': listId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def List_Import_Contacts(self, listId, source, contacts, **kwargs):
        '''
        Import a collection of contacts into a given list

        Required keyword arguments:

        listId (int) - The ID of the list you are importing contacts into
        source (string) - A short description of the of your contacts
        contacts (array) - Array of contact_hash items, as explained above
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true
        updateCustomFields (bool) - If this contact already exists, replace
            custom field values with values provided - defaults to false

        Returns struct - Aggregate import results
        '''
        args = {
            'key': self.key,
            'method': 'List_Import_Contacts',
            'listId': listId,
            'source': source,
            'contacts': contacts,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def List_Import_Contacts_Delayed(self, listId, source, contacts,
                                     callbackUrl, jobId, chunkNum, **kwargs):
        '''
        Import a collection of contacts into a given list asyncrhonously

        Required keyword arguments:

        listId (int) - The ID of the list you are importing contacts into
        source (string) - A short description of the of your contacts
        contacts (array) - Array of contact_hash items, as explained above
        callbackUrl (string) - A URL endpoint for the results of the import to
            be POSTed to
        jobId (string) - A Job ID used to match up the import in your webapp
        chunkNum (int) - An Import Chunk number used to match up in your
            webapp - use this to keep track of what chunks have been processed,
            they may not be handled in order
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true
        updateCustomFields (bool) - If this contact already exists, replace
            custom field values with values provided - defaults to false

        Returns bool -
        '''
        args = {
            'key': self.key,
            'method': 'List_Import_Contacts_Delayed',
            'listId': listId,
            'source': source,
            'contacts': contacts,
            'callbackUrl': callbackUrl,
            'jobId': jobId,
            'chunkNum': chunkNum,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def List_Evaluate_Contacts(self, contacts):
        '''
        Evaluate a collection of contacts

        Required keyword arguments:

        contacts (array) - Array of contact_hash items, as explained above

        Optional keyword arguments:

        Returns struct - Aggregate import results
        '''

        args = {
            'key': self.key,
            'method': 'List_Evaluate_Contacts',
            'contacts': contacts,
        }

        data = self.makeCall(args)
        return data

    def List_Get_Count(self, listId, status=''):
        '''
        Get the number of contacts in a given list

        Required keyword arguments:

        listId (int) - The ID of the list you want the count from
        status (string) - Count only contacts with a particular list status,
            valid values: subscribed, unsubscribed, bounced (defaults to
            subscribed)

        Optional keyword arguments:

        contactStatus (string) - Count only contacts with a particular contact
            status, valid values: active, bounced, deleted, suppressed

        Returns int - Number of contacts in list
        '''

        args = {
            'key': self.key,
            'method': 'List_Get_Count',
            'listId': listId,
            'status': status,
        }

        data = self.makeCall(args)
        return data

    def List_Update_Test(self, listId, updateParameters):
        '''
        Update an existing Test List

        Required keyword arguments:

        listId (int) - The of the list you want to modify
        updateParameters (dict) - A dict of replacement values for your list -
            only specify items that you want to change

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'List_Update_Test',
            'listId': listId,
            'updateParameters': updateParameters,
        }

        data = self.makeCall(args)
        return data

    def List_Update_Internal(self, listId, updateParameters):
        '''
        Update an existing Internal List

        Required keyword arguments:

        listId (int) - The of the list you want to modify
        updateParameters (dict) - A dict of replacement values for your list -
            only specify items that you want to change

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'List_Update_Internal',
            'listId': listId,
            'updateParameters': updateParameters,
        }

        data = self.makeCall(args)
        return data

    def List_Update_Private(self, listId, updateParameters):
        '''
        Update an existing Private List

        Required keyword arguments:

        listId (int) - The of the list you want to modify
        updateParameters (dict) - A dict of replacement values for your list -
            only specify items that you want to change

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'List_Update_Private',
            'listId': listId,
            'updateParameters': updateParameters,
        }

        data = self.makeCall(args)
        return data

    def List_Update_Public(self, listId, updateParameters):
        '''
        Update an existing Public List

        Required keyword arguments:

        listId (int) - The of the list you want to modify
        updateParameters (dict) - A dict of replacement values for your list -
            only specify items that you want to change

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'List_Update_Public',
            'listId': listId,
            'updateParameters': updateParameters,
        }

        data = self.makeCall(args)
        return data

    def Group_Create(self, name):
        '''
        Create a new Group

        Required keyword arguments:

        name (string) - The of your group

        Optional keyword arguments:

        Returns int - id Returns the Group ID of your new Group
        '''

        args = {
            'key': self.key,
            'method': 'Group_Create',
            'name': name,
        }

        data = self.makeCall(args)
        return data

    def Group_Update(self, groupId, name):
        '''
        Update an existing group

        Required keyword arguments:

        groupId (int) - The of the group you want to modify
        name (string) - The new of your group

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Group_Update',
            'groupId': groupId,
            'name': name,
        }

        data = self.makeCall(args)
        return data

    def Group_Delete(self, groupId):
        '''
        Delete a group you created

        Required keyword arguments:

        groupId (int) - The Group ID of the group you wish to delete

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Group_Delete',
            'groupId': groupId,
        }

        data = self.makeCall(args)
        return data

    def Group_Add_Contact(self, groupId, email):
        '''
        Add an email address contact to an existing group

        Required keyword arguments:

        groupId (int) - The ID of the group you want to subscribe the email
            address to
        email (string) - The address you are subscribing

        Optional keyword arguments:

        Returns bool - True on success
        '''

        args = {
            'key': self.key,
            'method': 'Group_Add_Contact',
            'groupId': groupId,
            'email': email,
        }

        data = self.makeCall(args)
        return data

    def Group_Remove_Contact(self, groupId, email):
        '''
        Remove an email address contact from an existing group

        Required keyword arguments:

        groupId (int) - The ID of the group you want to unsubscribe the email
            address to
        email (string) - The address you are unsubscribing

        Optional keyword arguments:

        Returns bool - True on success
        '''

        args = {
            'key': self.key,
            'method': 'Group_Remove_Contact',
            'groupId': groupId,
            'email': email,
        }

        data = self.makeCall(args)
        return data

    def Group_Remove_Contacts_Multiple(self, groupId, emails):
        '''
        Remove multiple email address contacts from an existing group

        Required keyword arguments:

        groupId (int) - The ID of the group you want to remove the email
            address from
        emails (array) - An list of email addresses you are removing from
            the group

        Optional keyword arguments:

        Returns int - Returns the number of contacts removed
        '''

        args = {
            'key': self.key,
            'method': 'Group_Remove_Contacts_Multiple',
            'groupId': groupId,
            'emails': emails,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Group_Get_Contacts(self, groupId, **kwargs):
        '''
        Retrieve a list of contacts in a given group

        Required keyword arguments:

        groupId (int) - The ID of the group you retrieve contacts from
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        customFields (list) - Array of custom field IDs or tokens you want
            included with the results (ex: ['first_name','last_name',
            'email_address'] OR [1,2,3])
        sortDir (string) - Sort direction, valid values: U, D
        offset (int) - The number of records to skip (specify a starting point)
        num (int) - The maximum number of records to return

        Returns struct - Struct of records each with a key of the contact's
        email addressemail and values of contactId, email, status and
        statusCode
        '''
        args = {
            'key': self.key,
            'method': 'Group_Get_Contacts',
            'groupId': groupId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Group_List(self):
        '''
        Get a listing of currently active groups

        Required keyword arguments:

        Optional keyword arguments:

        Returns struct - Struct of records with the key of groupId and value of
        name
        '''

        args = {
            'key': self.key,
            'method': 'Group_List',
        }

        data = self.makeCall(args)
        return data

    @optional
    def Group_Import_Contacts(self, groupId, source, contacts, **kwargs):
        '''
        Import a collection of contacts into a given group

        Required keyword arguments:

        groupId (int) - The ID of the group you are importing contacts into
        source (string) - A short description of the of your contacts
        contacts (array) - Array of contact_hash items, as explained above
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true
        updateCustomFields (bool) - If this contact already exists, replace
            custom field values with values provided - defaults to false

        Returns struct - Aggregate import results
        '''
        args = {
            'key': self.key,
            'method': 'Group_Import_Contacts',
            'groupId': groupId,
            'source': source,
            'contacts': contacts,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Group_Get_Count(self, groupId):
        '''
        Get the number of contacts in a given group

        Required keyword arguments:

        groupId (int) - The ID of the group you want the count from

        Optional keyword arguments:

        Returns int - Number of contacts in group
        '''

        args = {
            'key': self.key,
            'method': 'Group_Get_Count',
            'groupId': groupId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def SavedSearch_Create(self, name, advancedConditions, **kwargs):
        '''
        Create a new SavedSearch

        Required keyword arguments:

        name (string) - A for your saved search, must be unique
        advancedConditions (array) - An list of AdvancedCondition items - see
            AdvancedCondition for more info
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        logicalCondition (string) - Specify "Any" or "All", defaults to "Any".
            Used to govern if any or all AdvancedConditions must be met before
            a contact is returned

        Returns int - Returns the searchId of your new search
        '''
        args = {
            'key': self.key,
            'method': 'SavedSearch_Create',
            'name': name,
            'advancedConditions': advancedConditions,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def SavedSearch_Delete(self, searchId):
        '''
        Delete a savedSearch you created

        Required keyword arguments:

        searchId (int) - The SavedSearch ID of the savedSearch you wish to
            delete

        Optional keyword arguments:


        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'SavedSearch_Delete',
            'searchId': searchId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def SavedSearch_Get_Contacts(self, searchId, **kwargs):
        '''
        Retrieve a list of contacts found by a given saved search

        Required keyword arguments:

        searchId (int) - The ID of the savedSearch you retrieve contacts from
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        customFields (list) - Array of custom field IDs or tokens you want
            included with the results (ex: ["first_name","last_name",
            "email_address"] OR [1,2,3])
        sortDir (string) - Sort direction, valid values: U, D
        offset (int) - The number of records to skip (specify a starting point)
        num (int) - The maximum number of records to return

        Returns struct - Struct of records each with a key of email and values
        of contactId, email, status and statusCode
        '''
        args = {
            'key': self.key,
            'method': 'SavedSearch_Get_Contacts',
            'searchId': searchId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def SavedSearch_List(self):
        '''
        Get a listing of Saved Searches

        Required keyword arguments:

        Optional keyword arguments:

        Returns struct - Struct of records with the key of searchId and value
        of name
        '''

        args = {
            'key': self.key,
            'method': 'SavedSearch_List',
        }

        data = self.makeCall(args)
        return data

    def SavedSearch_Get_Count(self, searchId):
        '''
        Get the number of contacts in a given savedSearch

        Required keyword arguments:

        searchId (int) - The ID of the savedSearch you want the count from

        Optional keyword arguments:

        Returns int - Number of contacts in savedSearch
        '''

        args = {
            'key': self.key,
            'method': 'SavedSearch_Get_Count',
            'searchId': searchId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Create_Standard(self, recipients, campaignName, subject,
                                 senderEmail, senderName, content, **kwargs):
        '''
        Create a standard Contactology campaign

        Required keyword arguments:

        recipients (dict) - A dict which specifies the for your Campaign - can
            include list, group and search
        campaignName (string) - The name of this Campaign - not shown to
            recipients
        subject (string) - The line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        content (dict) - A dict which specifies the of the Campaign email - can
            include html and text
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        authenticate (bool) - Defaults to false. Authentication applies certain
            identifiers to your message to let the receiving servers know where
            the message is coming from. This helps with delivery of large
            mailings to major ISPs and some spam filters who often look for
            these identifiers to determine if a message is legit or not.
        replyToEmail (string) - Defaults to senderEmail. The email address
            that replies to your Campaign should go to. This will be
            overridden if you set trackReplies to true.
        replyToName (string) - Defaults to senderName. The display name of the
            replyToEmail
        trackReplies (bool) - Defaults to false. Whether or not replies should
            be tracked in your Campaign Report. Setting this to true will
            override your replyToEmail
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens
        showInArchive (bool) - Defaults to false. Whether or not this message
            should be show in your message archive.
        viewInBrowser (bool) - Defaults to false. Whether or not this message
            should include a "View In Browser" link.
        trackOpens (bool) - Defaults to true. Whether or not opens for this
            message should be tracked in your Campaign Report
        trackClickThruHTML (bool) - Defaults to true. Whether or not click
            tracking for links in the HTML body of this message should be
            tracked in your Campaign Report
        trackClickThruText (bool) - Defaults to true. Whether or not click
            tracking for links in the text body of this message should be
            tracked in your Campaign Report
        googleAnalyticsName (string) - Defaults to blank. If this is set,
            Google Analytics tracking will be turned on for this message with
            the specified name
        clickTaleName (string) - Defaults to blank. If this is set, ClickTale
            tracking will be turned on for this message with the specified
            name. Please note: you'll need to have ClickTale setup on your web
            site in order to use this feature.
        clickTaleCustomFields (list) - Defaults to blank. Accepts an list of
            CustomField IDs. clickTaleName must be set when using this
            parameter. Please do not use any personally identifiable
            information when using the ClickTale integration. This might
            include: First Name, Last Name, Company Name, Phone Number and
            Email Address. This policy applies to any other field that could
            identify your email subscriber within ClickTale tracking. Please
            note: you'll need to have ClickTale setup on your web site in order
            to use this feature.
        customUrlParameters (list) - The custom parameters to be appended to
            all urls orgainized into key / value pairs
        exclusions (dict) - A dict which specifies the recipients to exclude
            from your Campaign - can contain list, group, and  search
        footerId (int) - Defaults to your account's default footer. Set this
            to a valid footer ID to cause this campaign to use that footer
        facebookAutopost (dict) - A dict which contains information required to
            automatically post to Facebook upon completion of the campaign
        twitterAutopost (dict) - A dict which contains information required to
            automatically post to Twitter upon completion of the campaign

        Returns int - campaignId The ID for your new Campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Create_Standard',
            'recipients': recipients,
            'campaignName': campaignName,
            'subject': subject,
            'senderEmail': senderEmail,
            'senderName': senderName,
            'content': content,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Create_Standard_From_Url(self, recipients, campaignName,
                                          subject, senderEmail, senderName,
                                          content, **kwargs):
        '''
        Create a standard Contactology campaign

        Required keyword arguments:

        recipients (dict) - A dict which specifies the for your Campaign - can
            include list, group and search
        campaignName (string) - The name of this Campaign - not shown to
            recipients
        subject (string) - The line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        content (dict) - A dict which specifies the URLs that hold the of the
            Campaign email - can include htmlUrl and textUrl
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        generateTextFromHtml (bool) - Set to true to automatically generate the
            text part of a multipart email from the URL HTML content -
            overrides any textUrl given for the Campaign
        authenticate (bool) - Defaults to false. Authentication applies certain
            identifiers to your message to let the receiving servers know where
            the message is coming from. This helps with delivery of large
            mailings to major ISPs and some spam filters who often look for
            these identifiers to determine if a message is legit or not.
        replyToEmail (string) - Defaults to senderEmail. The email address
            that replies to your Campaign should go to. This will be
            overridden if you set trackReplies to true.
        replyToName (string) - Defaults to senderName. The display name of the
            replyToEmail
        trackReplies (bool) - Defaults to false. Whether or not replies should
            be tracked in your Campaign Report. Setting this to true will
            override your replyToEmail
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens
        showInArchive (bool) - Defaults to false. Whether or not this message
            should be show in your message archive.
        viewInBrowser (bool) - Defaults to false. Whether or not this message
            should include a "View In Browser" link.
        trackOpens (bool) - Defaults to true. Whether or not opens for this
            message should be tracked in your Campaign Report
        trackClickThruHTML (bool) - Defaults to true. Whether or not click
            tracking for links in the HTML body of this message should be
            tracked in your Campaign Report
        trackClickThruText (bool) - Defaults to true. Whether or not click
            tracking for links in the text body of this message should be
            tracked in your Campaign Report
        googleAnalyticsName (string) - Defaults to blank. If this is set,
            Google Analytics tracking will be turned on for this message with
            the specified name
        clickTaleName (string) - Defaults to blank. If this is set, ClickTale
            tracking will be turned on for this message with the specified
            name. Please note: you'll need to have ClickTale setup on your web
            site in order to use this feature.
        clickTaleCustomFields (list) - Defaults to blank. Accepts an list of
            CustomField IDs. clickTaleName must be set when using this
            parameter. Please do not use any personally identifiable
            information when using the ClickTale integration. This might
            include: First Name, Last Name, Company Name, Phone Number and
            Email Address. This policy applies to any other field that could
            identify your email subscriber within ClickTale tracking. Please
            note: you'll need to have ClickTale setup on your web site in order
            to use this feature.
        customUrlParameters (list) - The custom parameters to be appended to
            all urls orgainized into key / value pairs
        exclusions (dict) - A dict which specifies the recipients to exclude
            from your Campaign - can contain list, group, and  search
        footerId (int) - Defaults to your account's default footer. Set this to
            a valid footer ID to cause this campaign to use that footer
        facebookAutopost (dict) - A dict which contains information required to
            automatically post to Facebook upon completion of the campaign
        twitterAutopost (dict) - A dict which contains information required to
            automatically post to Twitter upon completion of the campaign

        Returns int - campaignId The ID for your new Campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Create_Standard_From_Url',
            'recipients': recipients,
            'campaignName': campaignName,
            'subject': subject,
            'senderEmail': senderEmail,
            'senderName': senderName,
            'content': content,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Create_Ad_Hoc(self, contacts, campaignName, subject,
                               senderEmail, senderName, content, **kwargs):
        '''
        Create a campaign to be sent to an ad hoc list of email addresses. The
        campaign will send immediately, it is not necessary to call
        Campaign_Send

        Required keyword arguments:

        contacts (array) - an list of contact items
        campaignName (string) - The name of this Campaign - not shown to
            recipients
        subject (string) - The line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        content (dict) - A dict which specifies the of the Campaign email - can
            include html and text
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        authenticate (bool) - Defaults to false. Authentication applies certain
            identifiers to your message to let the receiving servers know where
            the message is coming from. This helps with delivery of large
            mailings to major ISPs and some spam filters who often look for
            these identifiers to determine if a message is legit or not.
        replyToEmail (string) - Defaults to senderEmail. The email address that
            replies to your Campaign should go to. This will be overridden if
            you set trackReplies to true.
        replyToName (string) - Defaults to senderName. The display name of the
            replyToEmail
        trackReplies (bool) - Defaults to false. Whether or not replies should
            be tracked in your Campaign Report. Setting this to true will
            override your replyToEmail
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens
        showInArchive (bool) - Defaults to false. Whether or not this message
            should be show in your message archive.
        viewInBrowser (bool) - Defaults to false. Whether or not this message
            should include a "View In Browser" link.
        trackOpens (bool) - Defaults to true. Whether or not opens for this
            message should be tracked in your Campaign Report
        trackClickThruHTML (bool) - Defaults to true. Whether or not click
            tracking for links in the HTML body of this message should be
            tracked in your Campaign Report
        trackClickThruText (bool) - Defaults to true. Whether or not click
            tracking for links in the text body of this message should be
            tracked in your Campaign Report
        googleAnalyticsName (string) - Defaults to blank. If this is set,
            Google Analytics tracking will be turned on for this message with
            the specified name
        clickTaleName (string) - Defaults to blank. If this is set, ClickTale
            tracking will be turned on for this message with the specified
            name. Please note: you'll need to have ClickTale setup on your web
            site in order to use this feature.
        clickTaleCustomFields (list) - Defaults to blank. Accepts an list of
            CustomField IDs. clickTaleName must be set when using this
            parameter. Please do not use any personally identifiable
            information when using the ClickTale integration. This might
            include: First Name, Last Name, Company Name, Phone Number and
            Email Address. This policy applies to any other field that could
            identify your email subscriber within ClickTale tracking. Please
            note: you'll need to have ClickTale setup on your web site in order
            to use this feature.
        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true
        updateCustomFields (bool) - If this contact already exists, replace
            custom field values with values provided - defaults to false
        customUrlParameters (list) - The custom parameters to be appended to
            all urls orgainized into key / value pairs
        footerId (int) - Defaults to your account's default footer. Set this to
            a valid footer ID to cause this campaign to use that footer
        source (string) - A short description of the source of your contact
        facebookAutopost (dict) - A dict which contains information required to
            automatically post to Facebook upon completion of the campaign
        twitterAutopost (dict) - A dict which contains information required to
            automatically post to Twitter upon completion of the campaign

        Returns struct - Returns a struct containing info about the new
        campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Create_Ad_Hoc',
            'contacts': contacts,
            'campaignName': campaignName,
            'subject': subject,
            'senderEmail': senderEmail,
            'senderName': senderName,
            'content': content,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Create_Triggered_On_List_Subscription(self, listId, timeType,
                                                       timeValue, campaignName,
                                                       subject, senderEmail,
                                                       senderName, content,
                                                       advancedConditions=None,
                                                       **kwargs):
        '''
        Create an Triggered campaign that sends every time someone subscribes
        to a given List

        Required keyword arguments:

        listId (int) - The ID of the list that subscriptions to will trigger
        timeType (string) - The type of time interval for your Triggered
            Campaign - timeValue and go together to define the timing rule for
            your Triggered Campaign. Valid values: minutes, hours, days, weeks,
            months
        timeValue (int) - A number between 0 and 60 inclusive - and timeType go
            together to define the timing rule for your Triggered Campaign
        campaignName (string) - The name of this Campaign - not shown to
            recipients
        subject (string) - The line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        content (dict) - A dict which specifies the of the Campaign email - can
            include html and text
        advancedConditions (array) - An list of AdvancedCondition items that
            govern automation behavior
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        selectedAreas (list) - Limit what users trigger your Triggered Campaign
            by specifying where they signed up from (e.g.: via the API, via the
            Signup Form) - see AdvancedConditions for usage
        authenticate (bool) - Defaults to false. Authentication applies certain
            identifiers to your message to let the receiving servers know where
            the message is coming from. This helps with delivery of large
            mailings to major ISPs and some spam filters who often look for
            these identifiers to determine if a message is legit or not.
        replyToEmail (string) - Defaults to senderEmail. The email address that
            replies to your Campaign should go to. This will be overridden if
            you set trackReplies to true.
        replyToName (string) - Defaults to senderName. The display name of the
            replyToEmail
        trackReplies (bool) - Defaults to false. Whether or not replies should
            be tracked in your Campaign Report. Setting this to true will
            override your replyToEmail
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens
        showInArchive (bool) - Defaults to false. Whether or not this message
            should be show in your message archive.
        viewInBrowser (bool) - Defaults to false. Whether or not this message
            should include a "View In Browser" link.
        trackOpens (bool) - Defaults to true. Whether or not opens for this
            message should be tracked in your Campaign Report
        trackClickThruHTML (bool) - Defaults to true. Whether or not click
            tracking for links in the HTML body of this message should be
            tracked in your Campaign Report
        trackClickThruText (bool) - Defaults to true. Whether or not click
            tracking for links in the text body of this message should be
            tracked in your Campaign Report
        googleAnalyticsName (string) - Defaults to blank. If this is set,
            Google Analytics tracking will be turned on for this message with
            the specified name
        clickTaleName (string) - Defaults to blank. If this is set, ClickTale
            tracking will be turned on for this message with the specified
            name. Please note: you'll need to have ClickTale setup on your web
            site in order to use this feature.
        clickTaleCustomFields (list) - Defaults to blank. Accepts an list of
            CustomField IDs. clickTaleName must be set when using this
            parameter. Please do not use any personally identifiable
            information when using the ClickTale integration. This might
            include: First Name, Last Name, Company Name, Phone Number and
            Email Address. This policy applies to any other field that could
            identify your email subscriber within ClickTale tracking. Please
            note: you'll need to have ClickTale setup on your web site in order
            to use this feature.
        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true
        updateCustomFields (bool) - If this contact already exists, replace
            custom field values with values provided - defaults to false
        customUrlParameters (list) - The custom parameters to be appended to
            all urls orgainized into key / value pairs
        footerId (int) - Defaults to your account's default footer. Set this to
            a valid footer ID to cause this campaign to use that footer
        facebookAutopost (dict) - A dict which contains information required to
            automatically post to Facebook upon completion of the campaign
        twitterAutopost (dict) - A dict which contains information required to
            automatically post to Twitter upon completion of the campaign

        Returns int - campaignId The ID of your new Campaign
        '''
        if advancedConditions is None:
            advancedConditions = []

        args = {
            'key': self.key,
            'method': 'Campaign_Create_Triggered_On_List_Subscription',
            'listId': listId,
            'timeType': timeType,
            'timeValue': timeValue,
            'campaignName': campaignName,
            'subject': subject,
            'senderEmail': senderEmail,
            'senderName': senderName,
            'content': content,
            'advancedConditions': advancedConditions,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Create_Triggered_On_Date_CustomField(self, dateCustomFieldId,
                                                      timeType, timeValue,
                                                      timeDirection,
                                                      useCurrentYear, sendTime,
                                                      campaignName, subject,
                                                      senderEmail, senderName,
                                                      content,
                                                      advancedConditions=None,
                                                      **kwargs):
        '''
        Create an Triggered campaign that sends relative to a Date CustomField

        Required keyword arguments:

        dateCustomFieldId (int) - The ID of the CustomField of type Date whose
            value you want to use as a trigger
        timeType (string) - The type of time interval for your Triggered
            Campaign - timeValue and go together to define the timing rule for
            your Triggered Campaign. Valid values: days, weeks, months
        timeValue (int) - A number between 0 and 60 inclusive - and timeType go
            together to define the timing rule for your Triggered Campaign
        timeDirection (string) - The direction of the time interval for your
            Triggered Campaign - timeValue and timeType go together to define
            the timing rule for your Triggered Campaign. Valid values: before,
            after
        useCurrentYear (bool) - Set to true to ignore the Year value in the
            specified Date CustomField and base the trigger off of the current
            year instead.
        sendTime (int) - What hour of the day in the campaign should send in
            24-hour format, give a number between 0 and 23 inclusive
        campaignName (string) - The name of this Campaign - not shown to
            recipients
        subject (string) - The line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        content (dict) - A dict which specifies the of the Campaign email - can
            include html and text
        advancedConditions (array) - An list of AdvancedCondition items that
            govern automation behavior
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        selectedAreas (list) - Limit what users trigger your Triggered Campaign
            by specifying where they signed up from (e.g.: via the API, via the
            Signup Form) - see AdvancedConditions for usage
        authenticate (bool) - Defaults to false. Authentication applies certain
            identifiers to your message to let the receiving servers know where
            the message is coming from. This helps with delivery of large
            mailings to major ISPs and some spam filters who often look for
            these identifiers to determine if a message is legit or not.
        replyToEmail (string) - Defaults to senderEmail. The email address that
            replies to your Campaign should go to. This will be overridden if
            you set trackReplies to true.
        replyToName (string) - Defaults to senderName. The display name of the
            replyToEmail
        trackReplies (bool) - Defaults to false. Whether or not replies should
            be tracked in your Campaign Report. Setting this to true will
            override your replyToEmail
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens
        showInArchive (bool) - Defaults to false. Whether or not this message
            should be show in your message archive.
        viewInBrowser (bool) - Defaults to false. Whether or not this message
            should include a "View In Browser" link.
        trackOpens (bool) - Defaults to true. Whether or not opens for this
            message should be tracked in your Campaign Report
        trackClickThruHTML (bool) - Defaults to true. Whether or not click
            tracking for links in the HTML body of this message should be
            tracked in your Campaign Report
        trackClickThruText (bool) - Defaults to true. Whether or not click
            tracking for links in the text body of this message should be
            tracked in your Campaign Report
        googleAnalyticsName (string) - Defaults to blank. If this is set,
            Google Analytics tracking will be turned on for this message with
            the specified name
        clickTaleName (string) - Defaults to blank. If this is set, ClickTale
            tracking will be turned on for this message with the specified
            name. Please note: you'll need to have ClickTale setup on your web
            site in order to use this feature.
        clickTaleCustomFields (list) - Defaults to blank. Accepts an list of
            CustomField IDs. clickTaleName must be set when using this
            parameter. Please do not use any personally identifiable
            information when using the ClickTale integration. This might
            include: First Name, Last Name, Company Name, Phone Number and
            Email Address. This policy applies to any other field that could
            identify your email subscriber within ClickTale tracking. Please
            note: you'll need to have ClickTale setup on your web site in order
            to use this feature.
        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true
        updateCustomFields (bool) - If this contact already exists, replace
            custom field values with values provided - defaults to false
        customUrlParameters (list) - The custom parameters to be appended to
            all urls orgainized into key / value pairs
        footerId (int) - Defaults to your account's default footer. Set this to
            a valid footer ID to cause this campaign to use that footer
        facebookAutopost (dict) - A dict which contains information required to
            automatically post to Facebook upon completion of the campaign
        twitterAutopost (dict) - A dict which contains information required to
            automatically post to Twitter upon completion of the campaign

        Returns int - campaignId The ID of your new Campaign
        '''
        if advancedConditions is None:
            advancedConditions = []

        args = {
            'key': self.key,
            'method': 'Campaign_Create_Triggered_On_Date_CustomField',
            'dateCustomFieldId': dateCustomFieldId,
            'timeType': timeType,
            'timeValue': timeValue,
            'timeDirection': timeDirection,
            'useCurrentYear': useCurrentYear,
            'sendTime': sendTime,
            'campaignName': campaignName,
            'subject': subject,
            'senderEmail': senderEmail,
            'senderName': senderName,
            'content': content,
            'advancedConditions': advancedConditions,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Create_Recurring(self, timeFrame, sendHour, sendMinute,
                                  sendTimezone, recipients, campaignName,
                                  subject, senderEmail, senderName, content,
                                  **kwargs):
        '''
        Create a Recurring Campaign that sends regularly on a defined schedule

        Required keyword arguments:

        timeFrame (dict) - A definition of how often the Recurring Campaign
            should send (see notes above)
        sendHour (int) - What hour of the day the Recurring Campaign should be
            sent, in 24 hour format (0-23)
        sendMinute (int) - What minute of the day the Recurring Campaign should
            be sent (0-59)
        sendTimezone (string) - What Timezone is intended for use with sendHour
            and sendMinute
        recipients (dict) - A dict which specifies the for your Campaign - can
            include list, group and search
        campaignName (string) - The name of this Campaign - not shown to
            recipients
        subject (string) - The line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        content (dict) - A dict which specifies the of the Campaign email - can
            include html and text
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        authenticate (bool) - Defaults to false. Authentication applies certain
            identifiers to your message to let the receiving servers know where
            the message is coming from. This helps with delivery of large
            mailings to major ISPs and some spam filters who often look for
            these identifiers to determine if a message is legit or not.
        replyToEmail (string) - Defaults to senderEmail. The email address that
            replies to your Campaign should go to. This will be overridden if
                you set trackReplies to true.
        replyToName (string) - Defaults to senderName. The display name of the
            replyToEmail
        trackReplies (bool) - Defaults to false. Whether or not replies should
            be tracked in your Campaign Report. Setting this to true will
            override your replyToEmail
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens
        showInArchive (bool) - Defaults to false. Whether or not this message
            should be show in your message archive.
        viewInBrowser (bool) - Defaults to false. Whether or not this message
            should include a "View In Browser" link.
        trackOpens (bool) - Defaults to true. Whether or not opens for this
            message should be tracked in your Campaign Report
        trackClickThruHTML (bool) - Defaults to true. Whether or not click
            tracking for links in the HTML body of this message should be
            tracked in your Campaign Report
        trackClickThruText (bool) - Defaults to true. Whether or not click
            tracking for links in the text body of this message should be
            tracked in your Campaign Report
        googleAnalyticsName (string) - Defaults to blank. If this is set,
            Google Analytics tracking will be turned on for this message with
            the specified name
        clickTaleName (string) - Defaults to blank. If this is set, ClickTale
            tracking will be turned on for this message with the specified
            name. Please note: you'll need to have ClickTale setup on your web
            site in order to use this feature.
        clickTaleCustomFields (list) - Defaults to blank. Accepts an list of
            CustomField IDs. clickTaleName must be set when using this
            parameter. Please do not use any personally identifiable
            information when using the ClickTale integration. This might
            include: First Name, Last Name, Company Name, Phone Number and
            Email Address. This policy applies to any other field that could
            identify your email subscriber within ClickTale tracking. Please
            note: you'll need to have ClickTale setup on your web site in order
            to use this feature.
        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true
        updateCustomFields (bool) - If this contact already exists, replace
            custom field values with values provided - defaults to false
        customUrlParameters (list) - The custom parameters to be appended to
            all urls orgainized into key / value pairs
        exclusions (dict) - A dict which specifies the recipients to exclude
            from your Campaign - can contain list, group, and  search
        footerId (int) - Defaults to your account's default footer. Set this to
            a valid footer ID to cause this campaign to use that footer
        facebookAutopost (dict) - A dict which contains information required to
            automatically post to Facebook upon completion of the campaign
        twitterAutopost (dict) - A dict which contains information required to
            automatically post to Twitter upon completion of the campaign

        Returns int - campaignId The ID for your new Campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Create_Recurring',
            'timeFrame': timeFrame,
            'sendHour': sendHour,
            'sendMinute': sendMinute,
            'sendTimezone': sendTimezone,
            'recipients': recipients,
            'campaignName': campaignName,
            'subject': subject,
            'senderEmail': senderEmail,
            'senderName': senderName,
            'content': content,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Create_Recurring_From_Url(self, timeFrame, sendHour,
                                           sendMinute, sendTimezone,
                                           recipients, campaignName, subject,
                                           senderEmail, senderName, content,
                                           **kwargs):
        '''
        Create a Recurring Campaign that sends regularly on a defined schedule

        Required keyword arguments:

        timeFrame (dict) - A definition of how often the Recurring Campaign
            should send (see notes above)
        sendHour (int) - What hour of the day the Recurring Campaign should be
            sent, in 24 hour format (0-23)
        sendMinute (int) - What minute of the day the Recurring Campaign should
            be sent (0-59)
        sendTimezone (string) - What Timezone is intended for use with sendHour
            and sendMinute
        recipients (dict) - A dict which specifies the for your Campaign - can
            include list, group and search
        campaignName (string) - The name of this Campaign - not shown to
            recipients
        subject (string) - The line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        content (dict) - A dict which specifies the of the Campaign email - can
            include html and text
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        generateTextFromHtml (bool) - Set to true to automatically generate the
            text part of a multipart email from the URL HTML content -
            overrides any textUrl given for the Campaign
        authenticate (bool) - Defaults to false. Authentication applies certain
            identifiers to your message to let the receiving servers know where
            the message is coming from. This helps with delivery of large
            mailings to major ISPs and some spam filters who often look for
            these identifiers to determine if a message is legit or not.
        replyToEmail (string) - Defaults to senderEmail. The email address that
            replies to your Campaign should go to. This will be overridden if
            you set trackReplies to true.
        replyToName (string) - Defaults to senderName. The display name of the
            replyToEmail
        trackReplies (bool) - Defaults to false. Whether or not replies should
            be tracked in your Campaign Report. Setting this to true will
            override your replyToEmail
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens
        showInArchive (bool) - Defaults to false. Whether or not this message
            should be show in your message archive.
        viewInBrowser (bool) - Defaults to false. Whether or not this message
            should include a "View In Browser" link.
        trackOpens (bool) - Defaults to true. Whether or not opens for this
            message should be tracked in your Campaign Report
        trackClickThruHTML (bool) - Defaults to true. Whether or not click
            tracking for links in the HTML body of this message should be
            tracked in your Campaign Report
        trackClickThruText (bool) - Defaults to true. Whether or not click
            tracking for links in the text body of this message should be
            tracked in your Campaign Report
        googleAnalyticsName (string) - Defaults to blank. If this is set,
            Google Analytics tracking will be turned on for this message with
            the specified name
        clickTaleName (string) - Defaults to blank. If this is set, ClickTale
            tracking will be turned on for this message with the specified
            name. Please note: you'll need to have ClickTale setup on your web
            site in order to use this feature.
        clickTaleCustomFields (list) - Defaults to blank. Accepts an list of
            CustomField IDs. clickTaleName must be set when using this
            parameter. Please do not use any personally identifiable
            information when using the ClickTale integration. This might
            include: First Name, Last Name, Company Name, Phone Number and
            Email Address. This policy applies to any other field that could
            identify your email subscriber within ClickTale tracking. Please
            note: you'll need to have ClickTale setup on your web site in order
            to use this feature.
        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true
        updateCustomFields (bool) - If this contact already exists, replace
            custom field values with values provided - defaults to false
        customUrlParameters (list) - The custom parameters to be appended to
            all urls orgainized into key / value pairs
        exclusions (dict) - A dict which specifies the recipients to exclude
            from your Campaign - can contain list, group, and  search
        footerId (int) - Defaults to your account's default footer. Set this to
            a valid footer ID to cause this campaign to use that footer
        facebookAutopost (dict) - A dict which contains information required to
            automatically post to Facebook upon completion of the campaign
        twitterAutopost (dict) - A dict which contains information required to
            automatically post to Twitter upon completion of the campaign

        Returns int - campaignId The ID for your new Campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Create_Recurring_From_Url',
            'timeFrame': timeFrame,
            'sendHour': sendHour,
            'sendMinute': sendMinute,
            'sendTimezone': sendTimezone,
            'recipients': recipients,
            'campaignName': campaignName,
            'subject': subject,
            'senderEmail': senderEmail,
            'senderName': senderName,
            'content': content,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Create_Transactional(self, testContact, testReplacements,
                                      campaignName, subject, senderEmail,
                                      senderName, content, **kwargs):
        '''
        Create a transactional Contactology campaign

        Required keyword arguments:

        testContact (dict) - An initial contact to receive a test copy of the
            transactional email
        testReplacements (dict) - An initial set of test replacement values to
            be used for the testEmail
        campaignName (string) - The name of this Campaign - not shown to
            recipients
        subject (string) - The line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        content (dict) - A dict which specifies the of the Campaign email - can
            include html and text
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        authenticate (bool) - Defaults to false. Authentication applies certain
            identifiers to your message to let the receiving servers know where
            the message is coming from. This helps with delivery of large
            mailings to major ISPs and some spam filters who often look for
            these identifiers to determine if a message is legit or not.
        replyToEmail (string) - Defaults to senderEmail. The email address that
            replies to your Campaign should go to. This will be overridden if
            you set trackReplies to true.
        replyToName (string) - Defaults to senderName. The display name of the
            replyToEmail
        trackReplies (bool) - Defaults to false. Whether or not replies should
            be tracked in your Campaign Report. Setting this to true will
            override your replyToEmail
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens
        showInArchive (bool) - Defaults to false. Whether or not this message
            should be show in your message archive.
        viewInBrowser (bool) - Defaults to false. Whether or not this message
            should include a "View In Browser" link.
        trackOpens (bool) - Defaults to true. Whether or not opens for this
            message should be tracked in your Campaign Report
        trackClickThruHTML (bool) - Defaults to true. Whether or not click
            tracking for links in the HTML body of this message should be
            tracked in your Campaign Report
        trackClickThruText (bool) - Defaults to true. Whether or not click
            tracking for links in the text body of this message should be
            tracked in your Campaign Report
        googleAnalyticsName (string) - Defaults to blank. If this is set,
            Google Analytics tracking will be turned on for this message with
            the specified name
        clickTaleName (string) - Defaults to blank. If this is set, ClickTale
            tracking will be turned on for this message with the specified
            name. Please note: you'll need to have ClickTale setup on your web
            site in order to use this feature.
        clickTaleCustomFields (list) - Defaults to blank. Accepts an list of
            CustomField IDs. clickTaleName must be set when using this
            parameter. Please do not use any personally identifiable
            information when using the ClickTale integration. This might
            include: First Name, Last Name, Company Name, Phone Number and
            Email Address. This policy applies to any other field that could
            identify your email subscriber within ClickTale tracking. Please
            note: you'll need to have ClickTale setup on your web site in order
            to use this feature.
        customUrlParameters (list) - The custom parameters to be appended to
            all urls orgainized into key / value pairs
        footerId (int) - Defaults to your account's default footer. Set this to
            a valid footer ID to cause this campaign to use that footer
        facebookAutopost (dict) - A dict which contains information required to
            automatically post to Facebook upon completion of the campaign
        twitterAutopost (dict) - A dict which contains information required to
            automatically post to Twitter upon completion of the campaign
        appendFooter (bool) - Defaults to true. Whether or not a footer should
            be automatically appended to your message content

        Returns int - campaignId The ID for your new Campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Create_Transactional',
            'testContact': testContact,
            'testReplacements': testReplacements,
            'campaignName': campaignName,
            'subject': subject,
            'senderEmail': senderEmail,
            'senderName': senderName,
            'content': content,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Update_Standard(self, campaignId, **kwargs):
        '''
        Update properties of an existing Campaign. Only unsent campaigns in
        Draft status can be updated.

        Required keyword arguments:

        campaignId (int) - The Campaign id. The campaign must be in draft mode
            - an exception will be thrown if not.
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        campaignName (string) -
        list (int/list) - Include a single listId or list of listIds for the
            Campaign to be sent to - WILL REPLACE ANY CURRENTLY SELECTED LISTS
        group (int/list) - Include a single groupId or list of searchIds for
            the Campaign to be sent to - WILL REPLACE ANY CURRENTLY SELECTED
            GROUPS
        search (int/list) - Include a single searchId or list of searchIds for
            the Campaign to be sent to - WILL REPLACE ANY CURRENTLY SELECTED
            SAVED SEARCHES
        listExclude (int/list) - Exclude a single listId or list of listIds
            from the Campaign - WILL REPLACE ANY CURRENTLY EXCLUDED LISTS
        groupExclude (int/list) - Exclude a single groupId or list of searchIds
            from the Campaign - WILL REPLACE ANY CURRENTLY EXCLUDED GROUPS
        searchExclude (int/list) - Exclude a single searchId or list of
            searchIds from the Campaign - WILL REPLACE ANY CURRENTLY EXCLUDED
            SAVED SEARCHES
        subject (string) - The subject line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        html (string) - The HTML body of your message. Can only be provided for
            campaigns with content types "Editor" or "Copy/Paste".
        text (string) - The plain text body of your message
        generateTextFromHtml (bool) - Automatically create Text content from
            HTML content
        htmlUrl (string) - The URL to use for HTML content
        textUrl (string) - The URL to use for Text content
        authenticate (bool) - Defaults to false. Authentication applies certain
            identifiers to your message to let the receiving servers know where
            the message is coming from. This helps with delivery of large
            mailings to major ISPs and some spam filters who often look for
            these identifiers to determine if a message is legit or not.
        replyToEmail (string) - Defaults to senderEmail. The email address that
            replies to your Campaign should go to. This will be overridden if
            you set trackReplies to true.
        replyToName (string) - Defaults to senderName. The display name of the
            replyToEmail
        trackReplies (bool) - Defaults to false. Whether or not replies should
            be tracked in your Campaign Report. Setting this to true will
            override your replyToEmail
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens
        showInArchive (bool) - Defaults to false. Whether or not this message
            should be show in your message archive.
        viewInBrowser (bool) - Defaults to false. Whether or not this message
            should include a "View In Browser" link.
        trackOpens (bool) - Defaults to true. Whether or not opens for this
            message should be tracked in your Campaign Report
        trackClickThruHTML (bool) - Defaults to true. Whether or not click
            tracking for links in the HTML body of this message should be
            tracked in your Campaign Report
        trackClickThruText (bool) - Defaults to true. Whether or not click
            tracking for links in the text body of this message should be
            tracked in your Campaign Report
        googleAnalyticsName (string) - Defaults to blank. If this is set,
            Google Analytics tracking will be turned on for this message with
            the specified name
        clickTaleName (string) - Defaults to blank. Please see
            Campaign_Create_Standard for information.
        clickTaleCustomFields (list) - Defaults to blank. Please see
            Campaign_Create_Standard for information.
        useCustomUrlParameters (bool) - Whether or not to append custom
            parameters to the end of all urls
        customUrlParameters (list) - The custom parameters to be appended to
            all urls orgainized into key / value pairs
        footerId (int) - Defaults to your account's default footer. Set this
            to a valid footer ID to cause this campaign to use that footer. Set
            it to zero to use the Default Footer.
        facebookAutopost (dict) - A dict which contains information required to
            automatically post to Facebook upon completion of the campaign
        twitterAutopost (dict) - A dict which contains information required to
            automatically post to Twitter upon completion of the campaign

        Returns struct - Returns a struct containing standard Info for the
        campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Update_Standard',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Update_Triggered_On_List_Subscription(self, campaignId,
                                                       **kwargs):
        '''
        Update properties of an existing Triggered On List Subscription
        Campaign. Only unactivated campaigns in Draft status can be Updated

        Required keyword arguments:

        campaignId (int) - The Campaign id. The campaign must be in draft mode
            - an exception will be thrown if not.
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        campaignName (string) - The internal-use name of the campaign
        listId (int) - The ID of the list that subscriptions to will trigger
        timeType (string) - The type of time interval for your Triggered
            Campaign - timeValue and timeType go together to define the timing
            rule for your Triggered Campaign. Valid values: minutes, hours,
            days, weeks, months
        timeValue (int) - A number between 0 and 60 inclusive - timeValue and
            timeType go together to define the timing rule for your Triggered
            Campaign
        subject (string) - The subject line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        html (string) - The HTML body of your message
        text (string) - The plain text body of your message
        generateTextFromHtml (bool) - Automatically create Text content from
            HTML content
        htmlUrl (string) - The URL to use for HTML content
        textUrl (string) - The URL to use for Text content
        authenticate (bool) - Defaults to false. Authentication applies certain
            identifiers to your message to let the receiving servers know where
            the message is coming from. This helps with delivery of large
            mailings to major ISPs and some spam filters who often look for
            these identifiers to determine if a message is legit or not.
        replyToEmail (string) - Defaults to senderEmail. The email address that
            replies to your Campaign should go to. This will be overridden if
            you set trackReplies to true.
        replyToName (string) - Defaults to senderName. The display name of the
            replyToEmail
        trackReplies (bool) - Defaults to false. Whether or not replies should
            be tracked in your Campaign Report. Setting this to true will
            override your replyToEmail
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens
        showInArchive (bool) - Defaults to false. Whether or not this message
            should be show in your message archive.
        viewInBrowser (bool) - Defaults to false. Whether or not this message
            should include a "View In Browser" link.
        trackOpens (bool) - Defaults to true. Whether or not opens for this
            message should be tracked in your Campaign Report
        trackClickThruHTML (bool) - Defaults to true. Whether or not click
            tracking for links in the HTML body of this message should be
            tracked in your Campaign Report
        trackClickThruText (bool) - Defaults to true. Whether or not click
            tracking for links in the text body of this message should be
            tracked in your Campaign Report
        googleAnalyticsName (string) - Defaults to blank. If this is set,
            Google Analytics tracking will be turned on for this message with
            the specified name
        clickTaleName (string) - Defaults to blank. Please see
            Campaign_Create_Standard for information.
        clickTaleCustomFields (list) - Defaults to blank. Please see
            Campaign_Create_Standard for information.
        useCustomUrlParameters (bool) - Whether or not to append custom
            parameters to the end of all urls
        customUrlParameters (list) - The custom parameters to be appended to
            all urls orgainized into key / value pairs
        footerId (int) - Defaults to your account's default footer. Set this
            to a valid footer ID to cause this campaign to use that footer
        facebookAutopost (dict) - A dict which contains information required to
            automatically post to Facebook upon completion of the campaign
        twitterAutopost (dict) - A dict which contains information required to
            automatically post to Twitter upon completion of the campaign

        Returns struct - Returns a struct containing standard Info for the
        campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Update_Triggered_On_List_Subscription',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Update_Triggered_On_Date_CustomField(self, campaignId,
                                                      **kwargs):
        '''
        Update properties of an existing Triggered On Date CustomField
        Campaign. Only unactivated campaigns in Draft status can be Updated

        Required keyword arguments:

        campaignId (int) - The Campaign id. The campaign must be in draft mode
            - an exception will be thrown if not.
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        campaignName (string) - The internal-use name of the campaign
        dateCustomFieldId (int) - The ID of the CustomField of type Date whose
            value you want to use as a trigger
        timeType (string) - The type of time interval for your Triggered
            Campaign - timeValue and timeType go together to define the timing
            rule for your Triggered Campaign. Valid values: days, weeks, months
        timeValue (int) - A number between 0 and 60 inclusive - timeValue and
            timeType go together to define the timing rule for your Triggered
            Campaign
        timeDirection (string) - The direction of the time interval for your
            Triggered Campaign - timeValue and timeType go together to define
            the timing rule for your Triggered Campaign. Valid values: before,
            after
        useCurrentYear (bool) - Set to true to ignore the Year value in the
            specified Date CustomField and base the trigger off of the current
            year instead.
        sendTime (int) - What hour of the day in the campaign should send in
            24-hour format, give a number between 0 and 23 inclusive
        subject (string) - The subject line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        html (string) - The HTML body of your message
        text (string) - The plain text body of your message
        generateTextFromHtml (bool) - Automatically create Text content from
            HTML content
        htmlUrl (string) - The URL to use for HTML content
        textUrl (string) - The URL to use for Text content
        authenticate (bool) - Defaults to false. Authentication applies certain
            identifiers to your message to let the receiving servers know where
            the message is coming from. This helps with delivery of large
            mailings to major ISPs and some spam filters who often look for
            these identifiers to determine if a message is legit or not.
        replyToEmail (string) - Defaults to senderEmail. The email address that
            replies to your Campaign should go to. This will be overridden if
            you set trackReplies to true.
        replyToName (string) - Defaults to senderName. The display name of the
            replyToEmail
        trackReplies (bool) - Defaults to false. Whether or not replies should
            be tracked in your Campaign Report. Setting this to true will
            override your replyToEmail
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens
        showInArchive (bool) - Defaults to false. Whether or not this message
            should be show in your message archive.
        viewInBrowser (bool) - Defaults to false. Whether or not this message
            should include a "View In Browser" link.
        trackOpens (bool) - Defaults to true. Whether or not opens for this
            message should be tracked in your Campaign Report
        trackClickThruHTML (bool) - Defaults to true. Whether or not click
            tracking for links in the HTML body of this message should be
            tracked in your Campaign Report
        trackClickThruText (bool) - Defaults to true. Whether or not click
            tracking for links in the text body of this message should be
            tracked in your Campaign Report
        googleAnalyticsName (string) - Defaults to blank. If this is set,
            Google Analytics tracking will be turned on for this message with
            the specified name
        clickTaleName (string) - Defaults to blank. Please see
            Campaign_Create_Standard for information.
        clickTaleCustomFields (list) - Defaults to blank. Please see
            Campaign_Create_Standard for information.
        useCustomUrlParameters (bool) - Whether or not to append custom
            parameters to the end of all urls
        customUrlParameters (list) - The custom parameters to be appended to
            all urls orgainized into key / value pairs
        footerId (int) - Defaults to your account's default footer. Set this to
            a valid footer ID to cause this campaign to use that footer. Set to
            zero to use the Default Footer
        facebookAutopost (dict) - A dict which contains information required to
            automatically post to Facebook upon completion of the campaign
        twitterAutopost (dict) - A dict which contains information required to
            automatically post to Twitter upon completion of the campaign

        Returns struct - Returns a struct containing standard Info for the
        campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Update_Triggered_On_Date_CustomField',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Update_Recurring(self, campaignId, **kwargs):
        '''
        Update properties of an existing Recurring Campaign. Only unactivated
        campaigns in Draft status can be Updated

        Required keyword arguments:

        campaignId (int) - The Campaign id. The campaign must be in draft mode
        - an exception will be thrown if not.
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        campaignName (string) - The name of the campaign, for internal use
        timeFrame (dict) - A definition of how often the Recurring Campaign
            should send (see notes above)
        sendHour (int) - What hour of the day the Recurring Campaign should be
            sent, in 24 hour format (0-23)
        sendMinute (int) - What minute of the day the Recurring Campaign should
            be sent (0-59)
        sendTimezone (string) - What Timezone is intended for use with sendHour
            and sendMinute
        list (int/list) - Include a single listId or list of listIds for the
            Campaign to be sent to - WILL REPLACE ANY CURRENTLY SELECTED LISTS
        group (int/list) - Include a single groupId or list of searchIds for
            the Campaign to be sent to - WILL REPLACE ANY CURRENTLY SELECTED
            GROUPS
        search (int/list) - Include a single searchId or list of searchIds for
            the Campaign to be sent to - WILL REPLACE ANY CURRENTLY SELECTED
            SAVED SEARCHES
        listExclude (int/list) - Exclude a single listId or list of listIds
            from the Campaign - WILL REPLACE ANY CURRENTLY EXCLUDED LISTS
        groupExclude (int/list) - Exclude a single groupId or list of searchIds
            from the Campaign - WILL REPLACE ANY CURRENTLY EXCLUDED GROUPS
        searchExclude (int/list) - Exclude a single searchId or list of
            searchIds from the Campaign - WILL REPLACE ANY CURRENTLY EXCLUDED
            SAVED SEARCHES
        subject (string) - The subject line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        html (string) - The HTML body of your message
        text (string) - The plain text body of your message
        generateTextFromHtml (bool) - Automatically create Text content from
            HTML content
        htmlUrl (string) - The URL to use for HTML content
        textUrl (string) - The URL to use for Text content
        authenticate (bool) - Defaults to false. Authentication applies certain
            identifiers to your message to let the receiving servers know where
            the message is coming from. This helps with delivery of large
            mailings to major ISPs and some spam filters who often look for
            these identifiers to determine if a message is legit or not.
        replyToEmail (string) - Defaults to senderEmail. The email address that
            replies to your Campaign should go to. This will be overridden if
            you set trackReplies to true.
        replyToName (string) - Defaults to senderName. The display name of the
            replyToEmail
        trackReplies (bool) - Defaults to false. Whether or not replies should
            be tracked in your Campaign Report. Setting this to true will
            override your replyToEmail
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens
        showInArchive (bool) - Defaults to false. Whether or not this message
            should be show in your message archive.
        viewInBrowser (bool) - Defaults to false. Whether or not this message
            should include a "View In Browser" link.
        trackOpens (bool) - Defaults to true. Whether or not opens for this
            message should be tracked in your Campaign Report
        trackClickThruHTML (bool) - Defaults to true. Whether or not click
            tracking for links in the HTML body of this message should be
            tracked in your Campaign Report
        trackClickThruText (bool) - Defaults to true. Whether or not click
            tracking for links in the text body of this message should be
            tracked in your Campaign Report
        googleAnalyticsName (string) - Defaults to blank. If this is set,
            Google Analytics tracking will be turned on for this message with
            the specified name
        clickTaleName (string) - Defaults to blank. Please see
            Campaign_Create_Standard for information.
        clickTaleCustomFields (list) - Defaults to blank. Please see
            Campaign_Create_Standard for information.
        useCustomUrlParameters (bool) - Whether or not to append custom
            parameters to the end of all urls
        customUrlParameters (list) - The custom parameters to be appended to
            all urls orgainized into key / value pairs
        footerId (int) - Defaults to your account's default footer. Set this
            to a valid footer ID to cause this campaign to use that footer. Set
            to zero to use the Default Footer
        facebookAutopost (dict) - A dict which contains information required to
            automatically post to Facebook upon completion of the campaign
        twitterAutopost (dict) - A dict which contains information required to
            automatically post to Twitter upon completion of the campaign

        Returns struct - Returns a struct containing standard Info for the
        campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Update_Recurring',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Refresh_Url_Content(self, campaignId, **kwargs):
        '''
        Refresh the content of a URL based Campaign in Draft status

        Required keyword arguments:

        campaignId (int) - The Campaign id. The campaign must be in draft mode
            - an exception will be thrown if not.
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        generateTextFromHtml (bool) - Set to true to automatically generate the
            text part of a multipart email from the URL HTML content -
            overrides any textUrl given for the Campaign

        Returns struct - Returns a struct containing a preview of the campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Refresh_Url_Content',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Campaign_Get_Info(self, campaignId):
        '''
        Get Info for a specified Campaign

        Required keyword arguments:

        campaignId (int) - The Campaign ID of the Campaign you want Info on

        Optional keyword arguments:

        Returns struct -
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Get_Info',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Find(self, searchParameters=None):
        '''
        Find Info for a set of Campaigns

        Required keyword arguments:

        searchParameters (dict) - A dict of search parameters, any combination
            of which can be used

        Optional keyword arguments:

        Returns struct -
        '''

        if searchParameters is None:
            searchParameters = {}

        args = {
            'key': self.key,
            'method': 'Campaign_Find',
            'searchParameters': searchParameters,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Get_Count(self, searchParameters=None):
        '''
        Find count for a set of Campaigns

        Required keyword arguments:

        searchParameters (dict) - A dict of search parameters, any combination
            of which can be used

        Optional keyword arguments:

        Returns int - Number of campaigns
        '''

        if searchParameters is None:
            searchParameters = {}

        args = {
            'key': self.key,
            'method': 'Campaign_Get_Count',
            'searchParameters': searchParameters,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Find_Ids(self, searchParameters=None):
        '''
        Find a set of Campaigns and return just the record IDs

        Required keyword arguments:

        searchParameters (dict) - A dict of search parameters, any combination
            of which can be used

        Optional keyword arguments:

        Returns array - Campaign Ids
        '''

        if searchParameters is None:
            searchParameters = {}

        args = {
            'key': self.key,
            'method': 'Campaign_Find_Ids',
            'searchParameters': searchParameters,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Preview(self, campaignId):
        '''
        Get a preview of a Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to preview

        Optional keyword arguments:

        Returns struct - Returns a struct containing a preview of the campaign
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Preview',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Copy(self, campaignId, **kwargs):
        '''
        Create a duplicate of a campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to copy
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        campaignName (string) - Replace the name of the copied campaign with
            this

        Returns struct - Returns Info about the newly created campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Copy',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Send_Test(self, campaignId, **kwargs):
        '''
        Send a test of your Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to test
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        testEmail (string/list) - A single email or list of email addresses to
            send this test to
        testListId (int/list) - A single listId or list of listIds to send this
            test to - all lists specified must be Test Lists (see
            List_Add_Test)
        note (string) - A note to be inserted at the top of the campaign, used
            to point out changes or request feedback from your test recipients

        Returns bool - True on success
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Send_Test',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Report(self, campaignId, **kwargs):
        '''
        Get a report on a Completed Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to generate a report for
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        cached (bool) - Return a cached set of campaign data, defaults to true.
        formatted (bool) - Return the campaign data with formatting applied,
            defaults to false.
        urlDetails (bool) - Return detailed information for every link in the
            campaign, defaults to true.

        Returns struct - Returns report data from the specified campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Report',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Campaign_Delete(self, campaignId):
        '''
        Delete a specified campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to delete

        Optional keyword arguments:


        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Delete',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Add_Recipients(self, campaignId, contacts, **kwargs):
        '''
        Adds an adhoc grouping of contacts to a campaign. The recipients are
        added and will be sent in the next send cycle. This can be used to send
        transactional or ongoing type messages.

        Required keyword arguments:

        campaignId (integer) - a valid campaign id
        contacts (array) - an list of contact items
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        activateDeleted (bool) - If this contact was already deleted,
            reactivate them - defaults to true
        updateCustomFields (bool) - If this contact already exists, replace
            custom field values with values provided - defaults to false

        Returns struct - Returns contact add results
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Add_Recipients',
            'campaignId': campaignId,
            'contacts': contacts,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Campaign_Send(self, campaignId):
        '''
        Send a Campaign currently in Draft status

        Required keyword arguments:

        campaignId (int) - The campaign you wish to send

        Optional keyword arguments:

        Returns struct - Returns boolean success and an array of issues
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Send',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Send_Transactional(self, campaignId, contact, source,
                                    replacements):
        '''
        Send a new message in a transactional Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to send
        contact (dict) - The you wish to send this transactional campaign to
        source (string) - A short description of the of your contact
        replacements (dict) - Token replacement values to be swapped in the
            message body

        Optional keyword arguments:

        Returns mixed - Returns true on success, returns a struct on failure
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Send_Transactional',
            'campaignId': campaignId,
            'contact': contact,
            'source': source,
            'replacements': replacements,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Send_Transactional_Multiple(self, campaignId, contacts,
                                             source, replacements, **kwargs):
        '''
        Send a new message in a transactional Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to send
        contacts (array) - An list of dicts containing the you wish to send
            this transactional campaign to
        source (string) - A short description of the of your contact
        replacements (array) - An list of token replacement values to be
            swapped in the message body
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        continueOnError (bool) - Send to good contacts even if bad contacts are
            found, defaults to false

        Returns mixed - Returns true on success, returns a struct on failure
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Send_Transactional_Multiple',
            'campaignId': campaignId,
            'contacts': contacts,
            'source': source,
            'replacements': replacements,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Campaign_Send_Reconfirmation(self, email):
        '''
        Send a new message in a reconfirmation campaign

        Required keyword arguments:

        email (string) - The you wish to send this transactional campaign to

        Optional keyword arguments:

        Returns mixed - Returns true on success, returns a struct on failure
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Send_Reconfirmation',
            'email': email,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Schedule(self, campaignId, time):
        '''
        Schedule a Campaign to send at a specified date and time

        Required keyword arguments:

        campaignId (int) - The campaign you wish to schedule
        time (string) - a timeString in UTC timezone

        Optional keyword arguments:

        Returns struct - Returns boolean success and an array of issues
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Schedule',
            'campaignId': campaignId,
            'time': time,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Schedule_Cancel(self, campaignId):
        '''
        Clear a Scheduled Campaign's scheduled time and return the Campaign to
        Draft mode

        Required keyword arguments:

        campaignId (int) - The campaign you wish to schedule

        Optional keyword arguments:

        Returns struct -
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Schedule_Cancel',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Resend_Bounces(self, campaignId):
        '''
        Resend the Campaign to Contacts who soft-bounced

        Required keyword arguments:

        campaignId (int) - The campaign you wish to schedule

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Resend_Bounces',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Get_Delivered_Contacts(self, campaignId, **kwargs):
        '''
        Get a list of all Contacts who have the Delivered status for the
        specified Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to find delivered contacts for
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        minDate (timeString) - Find only Contacts who were Delivered on or
            after this date
        maxDate (timeString) - Find only Contacts who were Delivered on or
            before this date

        Returns struct - Returns a struct containing all found contacts
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Get_Delivered_Contacts',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Get_Hard_Bounced_Contacts(self, campaignId, **kwargs):
        '''
        Get a list of all Contacts who Hard Bounced for the specified Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to find hard bounced contacts
            for
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        minDate (timeString) - Find only Contacts who Hard Bounced on or after
            this date
        maxDate (timeString) - Find only Contacts who Hard Bounced on or before
            this date

        Returns struct - Returns a struct containing all found contacts
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Get_Hard_Bounced_Contacts',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Get_Opened_Contacts(self, campaignId, **kwargs):
        '''
        Get a list of all Contacts who Opened the specified Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to find contacts who opened
            said campaign
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        minDate (timeString) - Find only Contacts who opened this campaign on
            or after this date
        maxDate (timeString) - Find only Contacts who opened this campaign on
            or before this date

        Returns struct - Returns a struct containing all found contacts
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Get_Opened_Contacts',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Get_ClickThru_Contacts(self, campaignId, **kwargs):
        '''
        Get a list of all Contacts who Clicked Thru for the specified Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to find clicked thru contacts
            for
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        minDate (timeString) - Find only Contacts who Clicked Thru on or after
            this date
        maxDate (timeString) - Find only Contacts who Clicked Thru on or before
            this date
        urlId (int) - Find only Contacts who clicked on the given link

        Returns struct - Returns a struct containing all found contacts
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Get_ClickThru_Contacts',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Get_Replied_Contacts(self, campaignId, **kwargs):
        '''
        Get a list of all Contacts who Replied To the specified Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to find contacts who replied
            to said campaign
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        minDate (timeString) - Find only Contacts who replied to this campaign
            on or after this date
        maxDate (timeString) - Find only Contacts who replied to this campaign
            on or before this date

        Returns struct - Returns a struct containing all found contacts
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Get_Replied_Contacts',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Get_Unsubscribed_Contacts(self, campaignId, **kwargs):
        '''
        Get a list of all Contacts who Unsubscribed from the specified Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to find contacts who
            unsubscribed from said campaign
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        minDate (timeString) - Find only Contacts who unsubscribed from this
            campaign on or after this date
        maxDate (timeString) - Find only Contacts who unsubscribed from this
            campaign on or before this date

        Returns struct - Returns a struct containing all found contacts
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Get_Unsubscribed_Contacts',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Get_Subscribed_Contacts(self, campaignId, **kwargs):
        '''
        Get a list of all Contacts who Subscribed from the specified Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to find contacts who
            subscribed from said campaign
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        minDate (timeString) - Find only Contacts who subscribed from this
            campaign on or after this date
        maxDate (timeString) - Find only Contacts who subscribed from this
            campaign on or before this date

        Returns struct - Returns a struct containing all found contacts
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Get_Subscribed_Contacts',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Get_Forwarded_Contacts(self, campaignId,**kwargs):
        '''
        Get a list of all Contacts who Forwarded the specified Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to find contacts who forwarded
            said campaign
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        minDate (timeString) - Find only Contacts who forwarded this campaign
            on or after this date
        maxDate (timeString) - Find only Contacts who forwarded this campaign
            on or before this date

        Returns struct - Returns a struct containing all found contacts
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Get_Forwarded_Contacts',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Campaign_Get_Urls(self, campaignId):
        '''
        Get a list of URLs in a given campaign, for use with the
            Campaign_Get_ClickThru_Contacts call

        Required keyword arguments:

        campaignId (int) - The campaign you wish to find contacts who forwarded
            said campaign

        Optional keyword arguments:

        Returns struct -
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Get_Urls',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Activate_Triggered(self, campaignId):
        '''
        Activate an Triggered Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to activate

        Optional keyword arguments:

        Returns struct -
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Activate_Triggered',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Activate_Recurring(self, campaignId):
        '''
        Activate a Recurring Campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to activate

        Optional keyword arguments:

        Returns struct -
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Activate_Recurring',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Deactivate_Triggered(self, campaignId):
        '''
        Deactivate an active Triggered campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to deactivate

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Deactivate_Triggered',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Deactivate_Recurring(self, campaignId):
        '''
        Deactivate an active recurring campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to deactivate

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Deactivate_Recurring',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Create_Split(self, recipients, campaignName, subject,
                              senderEmail, senderName, content, splitParts,
                              **kwargs):
        '''
        Create a multivariate split Contactology campaign - used to help
        determine the most effective configuration for your campaigns.

        Required keyword arguments:

        recipients (dict) - A dict which specifies the for your Campaign - can
            include list, group and search
        campaignName (string) - The name of this Campaign - not shown to
            recipients
        subject (string) - The line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        content (dict) - A dict which specifies the of the Campaign email - can
            include html and text
        splitParts (array) - An list of dicts containing override values for
            each split - each dict will cause a new split to be created
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        splitPercent (int) - Defaults to 5. This is the percentage of your
            lists/groups/searches that will get randomly allocated to each
            split.
        authenticate (bool) - Defaults to false. Authentication applies certain
            identifiers to your message to let the receiving servers know where
            the message is coming from. This helps with delivery of large
            mailings to major ISPs and some spam filters who often look for
            these identifiers to determine if a message is legit or not.
        replyToEmail (string) - Defaults to senderEmail. The email address that
            replies to your Campaign should go to. This will be overridden if
            you set trackReplies to true.
        replyToName (string) - Defaults to senderName. The display name of the
            replyToEmail.
        trackReplies (bool) - Defaults to false. Whether or not replies should
            be tracked in your Campaign Report. Setting this to true will
            override your replyToEmail.
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens.
        showInArchive (bool) - Defaults to false. Whether or not this message
            should be show in your message archive.
        viewInBrowser (bool) - Defaults to false. Whether or not this message
            should include a "View In Browser" link.
        trackOpens (bool) - Defaults to true. Whether or not opens for this
            message should be tracked in your Campaign Report.
        trackClickThruHTML (bool) - Defaults to true. Whether or not click
            tracking for links in the HTML body of this message should be
            tracked in your Campaign Report.
        trackClickThruText (bool) - Defaults to true. Whether or not click
            tracking for links in the text body of this message should be
            tracked in your Campaign Report.
        googleAnalyticsName (string) - Defaults to blank. If this is set,
            Google Analytics tracking will be turned on for this message with
            the specified name.
        clickTaleName (string) - Defaults to blank. If this is set, ClickTale
            tracking will be turned on for this message with the specified
            name. Please note: you'll need to have ClickTale setup on your
            web site in order to use this feature.
        clickTaleCustomFields (list) - Defaults to blank. Accepts an list of
            CustomField IDs. clickTaleName must be set when using this
            parameter. Please do not use any personally identifiable
            information when using the ClickTale integration. This might
            include: First Name, Last Name, Company Name, Phone Number and
            Email Address. This policy applies to any other field that could
            identify your email subscriber within ClickTale tracking. Please
            note: you'll need to have ClickTale setup on your web site in order
            to use this feature.
        customUrlParameters (list) - The custom parameters to be appended to
            all urls orgainized into key / value pairs
        footerId (int) - Defaults to your account's default footer. Set this to
            a valid footer ID to cause this campaign to use that footer
        facebookAutopost (dict) - A dict which contains information required to
            automatically post to Facebook upon completion of the campaign
        twitterAutopost (dict) - A dict which contains information required to
            automatically post to Twitter upon completion of the campaign

        Returns int - campaignId The ID for your new Campaign
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Create_Split',
            'recipients': recipients,
            'campaignName': campaignName,
            'subject': subject,
            'senderEmail': senderEmail,
            'senderName': senderName,
            'content': content,
            'splitParts': splitParts,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Update_Split_Parts(self, campaignId, partIds, **kwargs):
        '''
        Update properties of an existing Campaign. Only unsent campaigns in
        Draft status can be Updated

        Required keyword arguments:

        campaignId (int) - The Campaign id. The campaign must be in draft mode
            - an exception will be thrown if not.
        partIds (array) - An list of partIds, each element being a single
            letter A-Z
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        subject (string) - The subject line of the Campaign
        senderEmail (string) - The from email address of the Campaign
        senderName (string) - The from name of the Campaign
        html (string) - The HTML body of your message
        text (string) - The plain text body of your message
        recipientName (string) - The display name of your recipient. Can use
            Personalization Tokens

        Returns struct - Returns a struct of structs, a split ID with
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Update_Split_Parts',
            'campaignId': campaignId,
            'partIds': partIds,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Campaign_Get_Split_Part_Ids(self, campaignId):
        '''
        Get the alphabetic split IDs for the parts of a split campaign

        Required keyword arguments:

        campaignId (int) - The Campaign ID. The campaign must be a split
            campaign

        Optional keyword arguments:

        Returns array - An array of split part IDs
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Get_Split_Part_Ids',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Get_Split_Winner_Report(self, campaignId, **kwargs):
        '''
        Get the Campaign_Report for the split winner/remainder, sent with
        Campaign_Send_Split_Remainder, Campaign_Schedule_Split_Remainder or
        Campaign_Schedule_Split_Winner

        Required keyword arguments:

        campaignId (int) - The Campaign ID. The campaign must be a split
            campaign
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        cached (bool) - Return a cached set of campaign data, defaults to true.
        formatted (bool) - Return the campaign data with formatting applied,
            defaults to false.

        Returns struct - See Campaign_Report
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Get_Split_Winner_Report',
            'campaignId': campaignId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Campaign_Get_Split_Parts_Info(self, campaignId, partIds):
        '''
        Get information for specific splitParts for your MV Split Campaign

        Required keyword arguments:

        campaignId (int) - The Campaign ID. The campaign must be a split
            campaign
        partIds (array) - An list of partIds, each element being a single
            letter A-Z

        Optional keyword arguments:

        Returns struct - Report info
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Get_Split_Parts_Info',
            'campaignId': campaignId,
            'partIds': partIds,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Schedule_Split_Parts(self, campaignId, partIds, time):
        '''
        Schedule specified split parts to send at the given time. Schedules all
        specified parts for the same time

        Required keyword arguments:

        campaignId (int) - The Campaign ID. The campaign must be a split
            campaign in draft mode
        partIds (array) - An list of alphabetic split part IDs
        time (string) - a timeString in UTC timezone

        Optional keyword arguments:

        Returns struct - Returns boolean success and an array of issues
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Schedule_Split_Parts',
            'campaignId': campaignId,
            'partIds': partIds,
            'time': time,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Schedule_Cancel_Split_Parts(self, campaignId, partIds):
        '''
        Clear a Scheduled Campaign's scheduled time and return the Campaign to
        Draft mode

        Required keyword arguments:

        campaignId (int) - The campaign you wish to schedule
        partIds (array) - An list of alphabetic split part IDs

        Optional keyword arguments:

        Returns bool - True on success
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Schedule_Cancel_Split_Parts',
            'campaignId': campaignId,
            'partIds': partIds,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Send_Split_Parts(self, campaignId, partIds):
        '''
        Send specified split parts immediately

        Required keyword arguments:

        campaignId (int) - The Campaign ID. The campaign must be a split
            campaign in draft mode
        partIds (array) - An list of alphabetic split part IDs

        Optional keyword arguments:

        Returns struct - Returns boolean success and an array of issues
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Send_Split_Parts',
            'campaignId': campaignId,
            'partIds': partIds,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Campaign_Send_Split_Test(self, campaignId, partIds,**kwargs):
        '''
        Send a test message for each of the specified split partIds

        Required keyword arguments:

        campaignId (int) - The campaign you wish to test
        partIds (array) - An list of alphabetic split part IDs
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        testEmail (string/list) - A single email or list of email addresses to
            send this test to
        testListId (int/list) - A single listId or list of listIds to send this
            test to - all lists specified must be Test Lists (see
            List_Add_Test)

        Returns bool - True on success
        '''
        args = {
            'key': self.key,
            'method': 'Campaign_Send_Split_Test',
            'campaignId': campaignId,
            'partIds': partIds,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Campaign_Schedule_Split_Remainder(self, campaignId, partId, time):
        '''
        Schedule the 'winning' split manually - the part specified will receive
        the remaining unsent recipients that were not allocated to splits

        Required keyword arguments:

        campaignId (int) - The split campaign for which you wish to schedule
            the remainder
        partId (string) - The of the split part you want the declare as the
            'winner' and allocate remaining recipients to
        time (string) - a timeString in UTC timezone

        Optional keyword arguments:

        Returns struct - Returns boolean success and an array of issues
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Schedule_Split_Remainder',
            'campaignId': campaignId,
            'partId': partId,
            'time': time,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Schedule_Cancel_Split_Remainder(self, campaignId):
        '''
        Clear a Scheduled Split Remainder's scheduled time

        Required keyword arguments:

        campaignId (int) - The campaign you wish to schedule

        Optional keyword arguments:

        Returns bool - True on success
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Schedule_Cancel_Split_Remainder',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Send_Split_Remainder(self, campaignId, partId):
        '''
        Send the 'winning' split manually - the part specified will receive
        the remaining unsent recipients that were not allocated to splits

        Required keyword arguments:

        campaignId (int) - The split campaign for which you wish to send the
            remainder
        partId (string) - The of the split part you want the declare as the
            'winner' and allocate remaining recipients to

        Optional keyword arguments:

        Returns struct - Returns boolean success and an array of issues
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Send_Split_Remainder',
            'campaignId': campaignId,
            'partId': partId,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Schedule_Split_Winner(self, campaignId, time, winCriteria):
        '''
        Schedule the Winner for your split campaign. When the time comes, it
        will evaluate the winCriteria and send the remainder to the winning
        split.

        Required keyword arguments:

        campaignId (int) - The Campaign ID. The campaign must be a split
            campaign. The splits must be complete at the time specified for a
            winner to be scheduled
        time (string) - A timeString in the UTC timezone
        winCriteria (array) - An list of criteria to be evaluated in the order
            specified (these are the same criteria returned in
            Campaign_Get_Split_Comparison)

        Optional keyword arguments:

        Returns bool - True on success
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Schedule_Split_Winner',
            'campaignId': campaignId,
            'time': time,
            'winCriteria': winCriteria,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Schedule_Cancel_Split_Winner(self, campaignId):
        '''
        Cancel a previously scheduled Winner evaluation

        Required keyword arguments:

        campaignId (int) - The Campaign ID. The campaign must be a split
            campaign with a currently scheduled winner.

        Optional keyword arguments:

        Returns bool - True on success
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Schedule_Cancel_Split_Winner',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    def Campaign_Get_Split_Comparison(self, campaignId):
        '''
        Get the Split Comparison report for a split campaign

        Required keyword arguments:

        campaignId (int) - The campaign you wish to test

        Optional keyword arguments:

        Returns struct - Returns a struct of structs, a breakdown of how each
        split performed against each metric - with a 'Sole Winner',
        'Sole Loser', 'Tie', 'Tied Winner' or 'Tied Loser' status for each
        campaign on each metric. Use this data to determine the winner of your
        split campaign
        '''

        args = {
            'key': self.key,
            'method': 'Campaign_Get_Split_Comparison',
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    def HostedAttachment_List(self):
        '''
        List current HostedAttachments

        Required keyword arguments:

        Optional keyword arguments:

        Returns struct - Returns a struct with the filename as the key and a
        list of all campaigns that have the HostedAttachment added as the value
        '''

        args = {
            'key': self.key,
            'method': 'HostedAttachment_List',
        }

        data = self.makeCall(args)
        return data

    @optional
    def HostedAttachment_Add(self, filename, attachment,**kwargs):
        '''
        Add a HostedAttachment to the server

        Required keyword arguments:

        filename (string) - name The and extension for your attachment
        attachment (string) - The body of the attachment
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        base64Encoded (bool) - Specify whether the content is base 64 encoded
            - defaults to false.

        Returns string - Returns the URL of the HostedAttachment for use in
        your Campaigns
        '''
        args = {
            'key': self.key,
            'method': 'HostedAttachment_Add',
            'filename': filename,
            'attachment': attachment,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def HostedAttachment_Add_To_Campaign(self, filename, campaignId):
        '''
        Add a HostedAttachment to a Campaign

        Required keyword arguments:

        filename (string) - The of your existing attachment
        campaignId (int) - The ID of the Campaign in Draft Mode you want to add
            the attachment to

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'HostedAttachment_Add_To_Campaign',
            'filename': filename,
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    def HostedAttachment_Remove_From_Campaign(self, filename, campaignId):
        '''
        Remove an existing HostedAttachment from a Campaign without deleting
        the HostedAttachment from the server

        Required keyword arguments:

        filename (string) - The of the existing HostedAttachment
        campaignId (int) - The ID of the Campaign you want to remove the
            attachment from

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'HostedAttachment_Remove_From_Campaign',
            'filename': filename,
            'campaignId': campaignId,
        }

        data = self.makeCall(args)
        return data

    def HostedAttachment_Delete(self, filename):
        '''
        Delete a HostedAttachment from the server and remove it from all
        Campaigns

        Required keyword arguments:

        filename (string) - The of the existing attachment

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'HostedAttachment_Delete',
            'filename': filename,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Account_Get_Send_Count(self, **kwargs):
        '''
        Get the total number of sent emails for your account

        Required keyword arguments:

        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        startDate (string) - Count only emails sent on or after this date,
            format: YYYY-MM-DD HH:MM:SS
        endDate (string) - Count only emails sent on or before this date,
            format: YYYY-MM-DD HH:MM:SS
        campaignId (int) - Count only sent emails belonging to a specific
            campaign

        Returns int -
        '''
        args = {
            'key': self.key,
            'method': 'Account_Get_Send_Count',
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Account_Get_Hosted_Content_Info(self):
        '''
        Get the quota, used and free space for your account

        Required keyword arguments:

        Optional keyword arguments:

        Returns struct - Returns a struct containing your quota, used and free
        space
        '''

        args = {
            'key': self.key,
            'method': 'Account_Get_Hosted_Content_Info',
        }

        data = self.makeCall(args)
        return data

    def Account_Get_Block_Sends_Remaining(self):
        '''
        Retrieve the number of block sends remaining in a Block Send Quota
        account

        Required keyword arguments:

        Optional keyword arguments:

        Returns int - The number of sends remaining
        '''

        args = {
            'key': self.key,
            'method': 'Account_Get_Block_Sends_Remaining',
        }

        data = self.makeCall(args)
        return data

    def AdvancedCondition_Check_Condition(self, condition):
        '''
        Confirm that an AdvancedCondition for use in SavedSearch or Campaign is
        valid

        Required keyword arguments:

        condition (AdvancedCondition) - A dict following a format defined in
            AdvancedCondition_List_Conditions

        Optional keyword arguments:

        Returns bool -
        '''

        args = {
            'key': self.key,
            'method': 'AdvancedCondition_Check_Condition',
            'condition': condition,
        }

        data = self.makeCall(args)
        return data

    def AdvancedCondition_List_Conditions(self):
        '''
        Returns a list of all of your available AdvancedConditions for use in
Campaign and SavedSearch functions

        Required keyword arguments:

        Optional keyword arguments:

        Returns array - Returns a list of valid AdvancedConditions
        '''

        args = {
            'key': self.key,
            'method': 'AdvancedCondition_List_Conditions',
        }

        data = self.makeCall(args)
        return data

    def AdvancedCondition_Get_SelectedAreas(self):
        '''
        Get Selected Area info for use with Automated Campaigns

        Required keyword arguments:

        Optional keyword arguments:

        Returns array - Returns a list of valid SelectedAreas for your account
        for use with Automated Campaigns
        '''

        args = {
            'key': self.key,
            'method': 'AdvancedCondition_Get_SelectedAreas',
        }

        data = self.makeCall(args)
        return data

    def Util_Get_MQS(self, fromEmail, subject, html, text):
        '''
        Get a Contactology Message Quality Score for an email

        Required keyword arguments:

        fromEmail (string) - The email address your email will be sent from
        subject (string) - The of your email
        html (string) - The HTML body of your message
        text (string) - The plain version of your message

        Optional keyword arguments:

        Returns struct - A struct containing your score and some detailed
        information on any issues encountered (see notes above)
        '''

        args = {
            'key': self.key,
            'method': 'Util_Get_MQS',
            'fromEmail': fromEmail,
            'subject': subject,
            'html': html,
            'text': text,
        }

        data = self.makeCall(args)
        return data

    def Template_List(self, getByFolder=''):
        '''
        Template_List returns a struct of your templates available for use in
        the new Template Controller

        Required keyword arguments:

        getByFolder (string) - Fetch templates by folder

        Optional keyword arguments:

        Returns struct - A struct where the key is the template_name and the
        value is the template_id (Note: This is reversed from most API calls)
        '''

        args = {
            'key': self.key,
            'method': 'Template_List',
            'getByFolder': getByFolder,
        }

        data = self.makeCall(args)
        return data

    def Template_Add(self, name, html):
        '''
        Add a new Template for use with the new Template Controller

        Required keyword arguments:

        name (string) - The of your new template
        html (string) - The HTML content of your new template

        Optional keyword arguments:

        Returns int - The templateId of your new template
        '''

        args = {
            'key': self.key,
            'method': 'Template_Add',
            'name': name,
            'html': html,
        }

        data = self.makeCall(args)
        return data

    def Template_Get_Tokens(self):
        '''
        Get a list of tokens available for use in the new Template Controller

        Required keyword arguments:

        Optional keyword arguments:

        Returns struct - Struct of tokens
        '''

        args = {
            'key': self.key,
            'method': 'Template_Get_Tokens',
        }

        data = self.makeCall(args)
        return data

    def Template_Transfer_Content(self, templateId, content):
        '''
        Transfer content from one template to another. This will only work if
        the templates have been set up in advance to use the same IDs for
        corresponding containers. See the Template Controller documentation

        Required keyword arguments:

        templateId (int) - The template ID that you're moving to
        content (string) - The full HTML of the old template

        Optional keyword arguments:

        Returns string - The full HTML content of the new template, with
        content transferred from the old template where possible
        '''

        args = {
            'key': self.key,
            'method': 'Template_Transfer_Content',
            'templateId': templateId,
            'content': content,
        }

        data = self.makeCall(args)
        return data

    def Template_Get_Content(self, templateId):
        '''
        Get the HTML of a template by ID

        Required keyword arguments:

        templateId (int) - The ID of the template of which you want the content

        Optional keyword arguments:

        Returns string - The full HTML content of the specified template
        '''

        args = {
            'key': self.key,
            'method': 'Template_Get_Content',
            'templateId': templateId,
        }

        data = self.makeCall(args)
        return data

    def Footer_Get_Default(self):
        '''
        Get the content of the default footer set for your account

        Required keyword arguments:

        Optional keyword arguments:

        Returns struct - A struct containing the HTML and Text parts of your
        default footer
        '''

        args = {
            'key': self.key,
            'method': 'Footer_Get_Default',
        }

        data = self.makeCall(args)
        return data

    def Footer_List(self):
        '''
        List all current footers

        Required keyword arguments:

        Optional keyword arguments:

        Returns struct - A struct of footers, with the key being the footer ID
        and the value being the footer name
        '''

        args = {
            'key': self.key,
            'method': 'Footer_List',
        }

        data = self.makeCall(args)
        return data

    def Footer_Get_Contents(self, footerId):
        '''
        Get the HTML and Text for a footer by ID

        Required keyword arguments:

        footerId (int) - The ID of the footer for which you want the contents

        Optional keyword arguments:

        Returns struct - A struct containing the HTML and Text parts of your
        default footer
        '''

        args = {
            'key': self.key,
            'method': 'Footer_Get_Contents',
            'footerId': footerId,
        }

        data = self.makeCall(args)
        return data

    def Footer_Add(self, name, html, text):
        '''
        Add a new footer for use with campaigns

        Required keyword arguments:

        name (string) - The of your new footer
        html (string) - The HTML content of your new footer
        text (string) - The Text content of your new footer

        Optional keyword arguments:

        Returns int - The ID of your new footer
        '''

        args = {
            'key': self.key,
            'method': 'Footer_Add',
            'name': name,
            'html': html,
            'text': text,
        }

        data = self.makeCall(args)
        return data

    def Footer_Update(self, footerId, html, text):
        '''
        Change the HTML and Text parts of an existing footer

        Required keyword arguments:

        footerId (int) - The ID of the footer you want to change
        html (string) - The new HTML content of your footer
        text (string) - The new Text content of your footer

        Optional keyword arguments:

        Returns bool - True on success
        '''

        args = {
            'key': self.key,
            'method': 'Footer_Update',
            'footerId': footerId,
            'html': html,
            'text': text,
        }

        data = self.makeCall(args)
        return data

    def Report_Get_Bulk_Webhooks(self):
        '''
        Report_Get_Bulk_Webhooks will get all of the bulk webhooks report
        stored being stored for you, in case you missed one of the bulk hooks.
        This call only gives you the URLs of the stored reports. You must still
        fetch them.

        Required keyword arguments:

        Optional keyword arguments:

        Returns array - Returns an array of filenames which hold your stored
        bulk hooks
        '''

        args = {
            'key': self.key,
            'method': 'Report_Get_Bulk_Webhooks',
        }

        data = self.makeCall(args)
        return data

    @optional
    def SocialConnection_List(self, **kwargs):
        '''
        List all social connections

        Required keyword arguments:

        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        id (int) - Retrieve a specific social connection
        type (string) - Retrieve only social connections of a certain type,
            valid values: facebook, twitter, googleAnalytics

        Returns struct - A struct of social connections
        '''
        args = {
            'key': self.key,
            'method': 'SocialConnection_List',
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def SocialConnection_Get_Locations(self, id):
        '''
        Get all possible post locations for a specific social connection

        Required keyword arguments:

        id (int) - Retrieve a specific social connection

        Optional keyword arguments:

        Returns struct - A struct of social connections
        '''

        args = {
            'key': self.key,
            'method': 'SocialConnection_Get_Locations',
            'id': id,
        }

        data = self.makeCall(args)
        return data

    def http_build_query(self, params, topkey=''):
        def sentinel(s):
            return s.replace("'", "EC_SingleQuoteSentinelValue")

        if len(params) == 0:
            return ""

        result = ""

        if isinstance(params, dict):
            for key in params.keys():
                newkey = quote(key)
                if topkey != '':
                    newkey = topkey + quote('[' + key + ']')

                if isinstance(params[key], dict):
                    result += self.http_build_query(params[key], newkey)

                elif isinstance(params[key], list):
                    i = 0
                    for val in params[key]:
                        if isinstance(val, dict):
                            for subkey in val.keys():
                                val[subkey] = sentinel(str(val[subkey]))
                        val = quote(str(val).replace('"', '\\"').replace('\'', '"'))
                        idx = quote('['+str(i)+']')
                        result += newkey + idx + "=" + val + "&"
                        i += 1

                # boolean should have special treatment as well
                elif isinstance(params[key], bool):
                    val = quote(str(int(params[key])))
                    result += newkey + "=" + val + "&"

                # assume string (integers and floats work well)
                else:
                    val = quote(sentinel(str(params[key])))
                    result += newkey + "=" + val + "&"

        # remove the last '&'
        if result and topkey == '' and result[-1] == '&':
            result = result[:-1]

        result = result.replace("EC_SingleQuoteSentinelValue", "'")

        return result

    def makeCall(self, args):
        params = self.http_build_query(args)
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain",
            "User-Agent": "Contactology Python Wrapper " + self.version
        }

        if self.useHTTPS:
            conn = httplib.HTTPSConnection(self.host)
        else:
            conn = httplib.HTTPConnection(self.host)
        conn.request("POST", self.path, params, headers)

        response = conn.getresponse()
        if response.status < 200 or response.status >= 300:
            raise Exception('Received HTTP %s error: %s' % (response.status,
                            response.reason))

        data = response.read()
        try:
            data = json.loads(data)
        except ValueError:
            raise Exception('Could not decode JSON: %s' % data)

        if ((isinstance(data, dict) and
             'result' in data and data['result'] == "error")):
            raise Exception("API Error: %s (%s)" % (data['message'],
                            repr(data['code'])))

        return data


class Contactology_Reseller(Contactology):
    @optional
    def Admin_Create_Account(self, clientName, adminEmail, userName, password,
                             homePage, logoUrl, clientAddr1, clientCity,
                             clientState, clientZip, **kwargs):
        '''
        Create a new Contactology account with the given parameters

        Required keyword arguments:

        clientName (string) - Name for the account
        adminEmail (string) - Default email address for the account
        userName (string) - User name for the new account - must be unique and
            no more than 64 characters
        password (string) - Password for the new account
        homePage (string) - URL for the account - will be included in the
            unsubscribe screen
        logoUrl (string) - URL to the logo image - will be included in the
            unsubscribe screen
        clientAddr1 (string) - Physical address for the account - will be
            included in the footer of messages
        clientCity (string) - Physical address for the account - will be
            included in the footer of messages
        clientState (string) - Physical address for the account - will be
            included in the footer of messages
        clientZip (string) - Physical address for the account - will be
            included in the footer of messages
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        clientAddr2 (string) - Client's Street Address Line 2
        clientBusinessName (string) - The client's Business name, defaults to
            provided clientName
        phoneNumber (string) - The client's phone number
        supportEmail (string) - The client's support email address, defaults to
            provided adminEmail
        clientTimezone (string) - The client's timezone, defaults to UTC
        hostedClientLimit (int) - Hosted Client Limit, defaults to 50. Valid
            values: 50, 100
        maximumCustomUsers (int) - Maximum Custom Users, defaults to 3. Valid
            values: 3, 4, 8, 13, 28
        accountType (string) - Account type, defaults to UNLIMITED. Valid
            values: NO_EMAIL, CONTACT_QUOTA, BLOCK_SENDS, UNLIMITED
        contactQuota (int) - Contact quota, defaults to 0. Only valid for
            CONTACT_QUOTA accountType. Valid values: 100, 250, 500, 1000, 2500,
            5000, 7500, 10000, 15000, 20000, 25000
        blockSendQuota (int) - Block send quota, defaults to 0. Only valid for
            BLOCK_SENDS accountType
        contractLength (int) - Contract length in months, defaults to 1. valid
            values: 1, 12
        paymentFrequency (int) - Payment frequency in months, defaults to 1.
            Valid values: 1, 3, 6, 12
        poweredBy (bool) - Control the display of the "Powered By Contactology"
            logo, defaults to false.
        forwardToFriendLink (bool) - Control the display of the "Forward to a
            Friend" link, defaults to true.
        managePreferencesLink (bool) - Control the display of the "Manage
            Preferences" link, defaults to true.
        unsubscribeLink (bool) - Control the display of the "Unsubscribe" link,
            defaults to true.
        aboutListLink (bool) - Control the display of the "About List" link,
            defaults to true.
        optinSource (bool) - Control the display of the "Opt In Source"
            information in the footer, defaults to true.
        surveys (bool) - Enable or disable surveys, defaults to false.
        language (string) - The default language the account will have. Valid
            values are: en, es, fr, ru
        numberFormat (string) - The default number format the account will use.
            Valid values are: us, eu

        Returns int - The user ID of the new account
        '''
        args = {
            'key': self.key,
            'method': 'Admin_Create_Account',
            'clientName': clientName,
            'adminEmail': adminEmail,
            'userName': userName,
            'password': password,
            'homePage': homePage,
            'logoUrl': logoUrl,
            'clientAddr1': clientAddr1,
            'clientCity': clientCity,
            'clientState': clientState,
            'clientZip': clientZip,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Admin_Create_Account_Minimal(self, clientName, adminEmail, userName,
                                     password, **kwargs):
        '''
        Create a new Contactology account using minimal initial information

        Required keyword arguments:

        clientName (string) - Name for the account
        adminEmail (string) - Default email address for the account
        userName (string) - User name for the new account - must be unique and
            no more than 64 characters
        password (string) - Password for the new account
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        clientBusinessName (string) - The client's Business name, defaults to
            provided clientName
        phoneNumber (string) - The client's phone number
        supportEmail (string) - The client's support email address, defaults to
            provided adminEmail
        clientTimezone (string) - The client's timezone, defaults to UTC
        hostedClientLimit (int) - Hosted Client Limit, defaults to 50. Valid
            values: 50, 100
        maximumCustomUsers (int) - Maximum Custom Users, defaults to 3. Valid
            values: 3, 4, 8, 13, 28
        accountType (string) - Account type, defaults to UNLIMITED. Valid
            values: NO_EMAIL, CONTACT_QUOTA, BLOCK_SENDS, UNLIMITED
        contactQuota (int) - Contact quota, defaults to 0. Only valid for
            CONTACT_QUOTA accountType. Valid values: 100, 250, 500, 1000, 2500,
            5000, 7500, 10000, 15000, 20000, 25000
        blockSendQuota (int) - Block send quota, defaults to 0. Only valid for
            BLOCK_SENDS accountType
        contractLength (int) - Contract length in months, defaults to 1. valid
            values: 1, 12
        paymentFrequency (int) - Payment frequency in months, defaults to 1.
            Valid values: 1, 3, 6, 12
        poweredBy (bool) - Control the display of the "Powered By Contactology"
            logo, defaults to false.
        forwardToFriendLink (bool) - Control the display of the "Forward to a
            Friend" link, defaults to true.
        managePreferencesLink (bool) - Control the display of the "Manage
            Preferences" link, defaults to true.
        unsubscribeLink (bool) - Control the display of the "Unsubscribe" link,
            defaults to true.
        aboutListLink (bool) - Control the display of the "About List" link,
            defaults to true.
        optinSource (bool) - Control the display of the "Opt In Source"
            information in the footer, defaults to true.
        surveys (bool) - Enable or disable surveys, defaults to false.
        language (string) - The default language the account will have. Valid
            values are: en, es, fr, ru
        numberFormat (string) - The default number format the account will use.
            Valid values are: us, eu

        Returns int - The user ID of the new account
        '''
        args = {
            'key': self.key,
            'method': 'Admin_Create_Account_Minimal',
            'clientName': clientName,
            'adminEmail': adminEmail,
            'userName': userName,
            'password': password,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Admin_Get_Accounts(self):
        '''
        Get a list of your current clients

        Required keyword arguments:

        Optional keyword arguments:

        Returns struct - Struct of current client accounts { clientId :
        clientName, clientId : clientName }
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Get_Accounts',
        }

        data = self.makeCall(args)
        return data

    @optional
    def Admin_Find_Accounts(self, **kwargs):
        '''
        Get a list of your clients based on parameters

        Required keyword arguments:

        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        createDateStart (string) - Return accounts created on or after
            createDateStart. Format as UTC.
        createDateEnd (string) - Return accounts created on or before
            createDateEnd. Format as UTC.
        status (string) - Current account status, valid values: active,
            disabled.

        Returns struct - Struct of accounts { { "clientId":"1", "clientStatus":
        "active", "clientCreated":"2012-01-01 00:00:00" }, { "clientId":"2",
        "clientStatus":"disabled", "clientCreated":"2012-02-02 02:00:00" }
        '''
        args = {
            'key': self.key,
            'method': 'Admin_Find_Accounts',
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Admin_Get_Account_Info(self, clientId):
        '''
        Admin_Get_Account_Info retrieves all the info about an Account,
        including the Plan information

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify

        Optional keyword arguments:

        Returns struct - Returns a struct of the account's properties
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Get_Account_Info',
            'clientId': clientId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Admin_Modify_Account(self, clientId, **kwargs):
        '''
        Modifies multiple properties of an existing Contactology account
        created by your account. Only fields in optionalParameters will be
        modified

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        clientName (string) - Name for the account
        adminEmail (string) - Default email address for the account
        password (string) - Password for the permanent user account
        homePage (string) - URL for the account
        logoUrl (string) - URL to the logo image
        clientAddr1 (string) - Physical address for the account
        clientAddr2 (string) - Client's Street Address Line 2
        clientCity (string) - Physical address for the account
        clientState (string) - Physical address for the account
        clientZip (string) - Physical address for the account
        clientBusinessName (string) - The Client's Business Name
        phoneNumber (string) - The client's phone number
        supportEmail (string) - The client's support email address
        clientTimezone (string) - The client's timezone
        forwardToFriendLink (bool) - Control the display of the "Forward to a
            Friend" link
        managePreferencesLink (bool) - Control the display of the "Manage
            Preferences" link
        unsubscribeLink (bool) - Control the display of the "Unsubscribe" link
        aboutListLink (bool) - Control the display of the "About List" link
        optinSource (bool) - Control the display of the "Opt In Source"
            information in the footer

        Returns int - The number of fields successfully modified
        '''
        args = {
            'key': self.key,
            'method': 'Admin_Modify_Account',
            'clientId': clientId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Admin_Get_Account_Plan(self, clientId):
        '''
        Admin_Get_Account_Plan returns an struct of Account Plan details for
        one of your clients

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify

        Optional keyword arguments:

        Returns struct - Returns a struct of Account Plan details
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Get_Account_Plan',
            'clientId': clientId,
        }

        data = self.makeCall(args)
        return data

    def Admin_Change_Account_Plan(self, clientId, hostedLimit, maxCustomUsers,
                                  package, accountType, contactQuota,
                                  contractLength, paymentFrequency, poweredBy,
                                  surveys):
        '''
        Change Account Plan allows you to change everything about an Account's
        Plan at once

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify
        hostedLimit (int) - hostedClientLimit Hosted Client Limit. Valid
            values: 50, 100
        maxCustomUsers (int) - maximumCustomUsers Maximum Custom Users, valid
            values: 3, 4, 8, 13, 28
        package (string) - [DEPRECATED] Package is no longer required - an
            empty string will work fine. Previous valid values:
            PACKAGE_CONTACTS_EMAIL, PACKAGE_SURVEYS, PACKAGE_FULL,
            PACKAGE_MIGRATE will be accepted to keep legacy code from breaking
        accountType (string) - Account type, valid values: NO_EMAIL,
            CONTACT_QUOTA, BLOCK_SENDS, UNLIMITED
        contactQuota (int) - Contact quota, valid values: 100, 250, 500, 1000,
            2500, 5000, 7500, 10000, 15000, 20000, 25000
        contractLength (int) - Contract length, valid values: 1, 12
        paymentFrequency (int) - Payment frequency, valid values: 1, 3, 6, 12
        poweredBy (bool) - Display Powered By Contactology logo
        surveys (bool) - optional Enable or disable for the account, defaults
            to false

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Change_Account_Plan',
            'clientId': clientId,
            'hostedLimit': hostedLimit,
            'maxCustomUsers': maxCustomUsers,
            'package': package,
            'accountType': accountType,
            'contactQuota': contactQuota,
            'contractLength': contractLength,
            'paymentFrequency': paymentFrequency,
            'poweredBy': poweredBy,
            'surveys': surveys,
        }

        data = self.makeCall(args)
        return data

    def Admin_Change_Account_Hosted_Limit(self, clientId, hostedLimit):
        '''
        Admin_Change_Account_Hosted_Limit allows you to change the Hosted
            Limit (in Megabytes) for your clients

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify
        hostedLimit (int) - Hosted Limit, valid values: 50, 100

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Change_Account_Hosted_Limit',
            'clientId': clientId,
            'hostedLimit': hostedLimit,
        }

        data = self.makeCall(args)
        return data

    def Admin_Change_Account_Maximum_Custom_Users(self, clientId,
                                                  maxCustomUsers):
        '''
        Admin_Change_Account_Maximum_Custom_Users allows you to change the
        Maximum Custom Users of your clients

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify
        maxCustomUsers (int) - Maximum Custom Users, valid values: 3, 4, 8, 13,
            28

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Change_Account_Maximum_Custom_Users',
            'clientId': clientId,
            'maxCustomUsers': maxCustomUsers,
        }

        data = self.makeCall(args)
        return data

    def Admin_Change_Account_Package(self, clientId, package):
        '''
        Admin_Change_Account_Package allows you to change the Package of your
        clients

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify
        package (string) - Package, valid values: PACKAGE_CONTACTS_EMAIL,
            PACKAGE_SURVEYS, PACKAGE_FULL, PACKAGE_MIGRATE

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Change_Account_Package',
            'clientId': clientId,
            'package': package,
        }

        data = self.makeCall(args)
        return data

    def Admin_Change_Account_Type(self, clientId, accountType):
        '''
        Admin_Change_Account_Type allows you to change the Account Type of
            your clients

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify
        accountType (string) - Account type, valid values: NO_EMAIL,
            CONTACT_QUOTA, BLOCK_SENDS, UNLIMITED

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Change_Account_Type',
            'clientId': clientId,
            'accountType': accountType,
        }

        data = self.makeCall(args)
        return data

    def Admin_Change_Account_Contact_Quota(self, clientId, contactQuota):
        '''
        Admin_Change_Account_Contact_Quota allows you to change the Contact
        Quota of your clients

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify
        contactQuota (int) - Contact quota, valid values: 100, 250, 500, 1000,
            2500, 5000, 7500, 10000, 15000, 20000, 25000

        Optional keyword arguments:

        Returns bool - True on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Change_Account_Contact_Quota',
            'clientId': clientId,
            'contactQuota': contactQuota,
        }

        data = self.makeCall(args)
        return data

    def Admin_Change_Account_Contract_Length(self, clientId, contractLength):
        '''
        Admin_Change_Account_Contract_Length allows you to change the Contract
        Length of your clients

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify
        contractLength (int) - Contract length, valid values: 1, 12

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Change_Account_Contract_Length',
            'clientId': clientId,
            'contractLength': contractLength,
        }

        data = self.makeCall(args)
        return data

    def Admin_Change_Account_Payment_Frequency(self, clientId,
                                               paymentFrequency):
        '''
        Admin_Change_Account_Payment_Frequency allows you to change the Payment
        Frequency of your clients

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify
        paymentFrequency (int) - Payment frequency, valid values: 1, 3, 6, 12

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Change_Account_Payment_Frequency',
            'clientId': clientId,
            'paymentFrequency': paymentFrequency,
        }

        data = self.makeCall(args)
        return data

    def Admin_Change_Account_Powered_By(self, clientId, poweredBy):
        '''
        Admin_Change_Account_Powered_By allows you to toggle the display of the
        Powered By logo for your clients

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify
        poweredBy (bool) - Display Powered By Contactology logo

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Change_Account_Powered_By',
            'clientId': clientId,
            'poweredBy': poweredBy,
        }

        data = self.makeCall(args)
        return data

    def Admin_Change_Account_Surveys(self, clientId, surveys):
        '''
        Admin_Change_Account_Surveys allows you to enable or disable the
        Surveys feature for your clients

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify
        surveys (bool) - Set to true to enable Surveys, false to disable

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Change_Account_Surveys',
            'clientId': clientId,
            'surveys': surveys,
        }

        data = self.makeCall(args)
        return data

    def Admin_Add_Block_Sends(self, clientId, numSendsToAdd):
        '''
        Admin_Add_Block_Sends allows you to add block quota sends to one of
        your clients

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify
        numSendsToAdd (int) - numSendsToAdd

        Optional keyword arguments:

        Returns bool - Returns true on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Add_Block_Sends',
            'clientId': clientId,
            'numSendsToAdd': numSendsToAdd,
        }

        data = self.makeCall(args)
        return data

    def Admin_Suspend_Account(self, clientId):
        '''
        Suspend an Account you created

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify

        Optional keyword arguments:

        Returns bool - true on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Suspend_Account',
            'clientId': clientId,
        }

        data = self.makeCall(args)
        return data

    def Admin_Reinstate_Account(self, clientId):
        '''
        Reinstate an Account you suspended

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify

        Optional keyword arguments:

        Returns bool - true on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Reinstate_Account',
            'clientId': clientId,
        }

        data = self.makeCall(args)
        return data

    def Admin_Delete_Account(self, clientId):
        '''
        Suspend an Account you created. Admin_Delete_Account is an alias of
        Admin_Suspend_Account.

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify

        Optional keyword arguments:

        Returns bool - true on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Delete_Account',
            'clientId': clientId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Admin_Get_Accounts_Completed_Campaigns(self, **kwargs):
        '''
        Get a list of all completed campaigns for your clients

        Required keyword arguments:

        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        sortBy (string) - Sort campaign list for each account by, valid values:
            campaign_id, campaign_name, start_time
        sortDir (string) - Sort direction, valid values: U, D
        startDate (string) - Get only campaigns started on or after this date,
            format: YYYY-MM-DD HH:MM:SS
        endDate (string) - Get only campaigns started on or before this date,
            format: YYYY-MM-DD HH:MM:SS

        Returns struct - An array of clientIds with a value array containing:
        campaign_id, campaign_name, campaign_description, start_time,
        campaign_email_from, campaign_email_from_alias, campaign_email_subject
        '''
        args = {
            'key': self.key,
            'method': 'Admin_Get_Accounts_Completed_Campaigns',
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Admin_Get_Accounts_Sends(self, **kwargs):
        '''
        Get the total number of sends for each of your accounts

        Required keyword arguments:

        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        startDate (string) - Get only campaigns started on or after this date,
            format: YYYY-MM-DD HH:MM:SS
        endDate (string) - Get only campaigns started on or before this date,
            format: YYYY-MM-DD HH:MM:SS

        Returns struct - An array of clientIds each with a value of the total
        sends
        '''
        args = {
            'key': self.key,
            'method': 'Admin_Get_Accounts_Sends',
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Admin_Get_Accounts_List_Count(self):
        '''
        Get the total number of subscribed emails for each list owned by each
        of your accounts

        Required keyword arguments:

        Optional keyword arguments:

        Returns struct - A struct of clientIds each with a value struct of
        listId => count
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Get_Accounts_List_Count',
        }

        data = self.makeCall(args)
        return data

    @optional
    def Admin_Get_Account_Key(self, clientId, **kwargs):
        '''
        Get an API key for one of your accounts

        Required keyword arguments:

        clientId (int) - The account ID number for which you want the API key
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        userName (string) - The username for which you would like the API key

        Returns string - API Key
        '''
        args = {
            'key': self.key,
            'method': 'Admin_Get_Account_Key',
            'clientId': clientId,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    @optional
    def Admin_Send_Message(self, clientIds, shortMessage, **kwargs):
        '''
        Send an Alert Message to a set of your clients

        Required keyword arguments:

        clientIds (array) - An list of Client IDs who will receive the message
        shortMessage (string) - A short message, up to 255 characters
        optionalParameters (dict) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        fullMessage (string) -
        url (string) -
        priority (int) -
        startDate (string) -
        expiresDate (string) -
        messageId (string) -

        Returns  -
        '''
        args = {
            'key': self.key,
            'method': 'Admin_Send_Message',
            'clientIds': clientIds,
            'shortMessage': shortMessage,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Admin_Get_Account_Webhooks(self, clientId):
        '''
        Get the current Webhooks settings for the specified Account

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify

        Optional keyword arguments:

        Returns struct - A struct of Webhook data
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Get_Account_Webhooks',
            'clientId': clientId,
        }

        data = self.makeCall(args)
        return data

    @optional
    def Admin_Set_Account_Webhooks(self, clientId, url, webhooksKey, hooks,
                                   locations, customFieldIds=None, **kwargs):
        '''
        Admin_Set_Account_Webhooks allows you to set the Webhooks information
        for the specified Account

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify
        url (string) - The URL to receive the Webhook
        webhooksKey (string) - webhookKey The Webhook Key passed along with the
            data to verify the origin, this is important for security
        hooks (array) - An list of events you would like to receive Webfor.
            Valid values are: WEBHOOK_SUBSCRIBE, WEBHOOK_UNSUBSCRIBE,
            WEBHOOK_GLOBAL_UNSUBSCRIBE, WEBHOOK_PROFILE_UPDATE,
            WEBHOOK_BOUNCED, WEBHOOK_EMAIL_CHANGED, WEBHOOK_CAMPAIGN_OPENED,
            WEBHOOK_CAMPAIGN_CLICKED, WEBHOOK_CAMPAIGN_SENDING_STARTED,
            WEBHOOK_CAMPAIGN_SENT,
            WEBHOOK_CAMPAIGN_SENT_TO_ADDITIONAL_RECIPIENT, WEBHOOK_REACTIVATED,
            WEBHOOK_LIST_CREATED, WEBHOOK_LIST_DELETED, WEBHOOK_LIST_CHANGED
        locations (array) - An list of Locations a particular Hook can be fired
            from. Valid values are: ContactDirect, Webapp, WebappBulk, System,
            API
        customFieldIds (array) - An list of Custom Field IDs (See:
            Custom_Field_Get_All) - if specified, the values of the specified
            fields will be included in the data payload for any Webhook sending
            contact data
        optionalParameters (array) - Deprecated- use keyword arguments instead

        Optional keyword arguments:

        bulk (bool) - Set to true to enable bulk webhooks rollup
        bulkThreshold (int) - The maximum number of hooks to be included in a
            single payload, valid values 50 to 10000
        bulkJSON (bool) - Send hooks as a single JSON dict rather than a
            newline delimited collection of JSON dicts
        bulkReport (bool) - Save reports for 7 days in case a hook is missed
            (retrieve with Report_Get_Bulk_Webhooks)

        Returns struct - A struct of Webhook data
        '''
        if customFieldIds is None:
            customFieldIds = []

        args = {
            'key': self.key,
            'method': 'Admin_Set_Account_Webhooks',
            'clientId': clientId,
            'url': url,
            'webhooksKey': webhooksKey,
            'hooks': hooks,
            'locations': locations,
            'customFieldIds': customFieldIds,
            'optionalParameters': kwargs.get('optionalParameters'),
        }

        data = self.makeCall(args)
        return data

    def Admin_Deactivate_Account_Webhooks(self, clientId):
        '''
        Deactivate all Webhooks for an account

        Required keyword arguments:

        clientId (int) - The client ID number you want to modify

        Optional keyword arguments:

        Returns bool - True on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Deactivate_Account_Webhooks',
            'clientId': clientId,
        }

        data = self.makeCall(args)
        return data

    def Admin_Get_Purchase_Orders(self):
        '''
        Get Purchase Order data for an account

        Required keyword arguments:

        Optional keyword arguments:

        purchaseOrderId (int) - Purchase order id
        resellerIds (dict) - A dict of reseller ID numbers
        clientIds (dict) - A dict of client ID numbers
        minDate (string) - Find purchase orders created on or after minDate.
            Format as UTC.
        maxDate (string) - Find purchase orders created on or before maxDate.
            Format as UTC.
        paymentType (dict) - The type of payment, valid values: invoice,
            credit_card, automated_credit_card, unknown
        product (dict) - The type of product, valid values: block_sends,
            contact_quota, unlimited, unknown, inbox_analysis
        addOns (dict) - Add-ons changed, valid values: video_mail, surveys,
            branded, users, diskspace
        purchaseOrderStatus (string) - Purchase order status, valid values:
            none, ok, failed, manual
        invoiceId (int) - Invoice id

        Returns struct - A struct of purchase order data
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Get_Purchase_Orders',
        }

        data = self.makeCall(args)
        return data

    def Admin_Get_Inbox_Analysis_Remaining(self, clientId):
        '''
        Get the number of Inbox Analysis Tests remaining for the specified
        Account

        Required keyword arguments:

        clientId (int) - The client ID number for which you want the number of
            remaining tests

        Optional keyword arguments:

        Returns int - The number of Inbox Analysis tests available for use by
        the specified Account
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Get_Inbox_Analysis_Remaining',
            'clientId': clientId,
        }

        data = self.makeCall(args)
        return data

    def Admin_Get_Inbox_Analysis_Tests(self, clientId):
        '''
        Find Inbox Analysis Tests used

        Required keyword arguments:

        clientId (int) - The client ID number for which you want the number of
            remaining tests

        Optional keyword arguments:

        minDate (string) - Find inbox analysis tests run on or after minDate.
            Format as UTC.
        maxDate (string) - Find inbox analysis tests run on or before maxDate.
            Format as UTC.

        Returns struct - The Inbox Analysis tests used
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Get_Inbox_Analysis_Tests',
            'clientId': clientId,
        }

        data = self.makeCall(args)
        return data

    def Admin_Purchase_Inbox_Analysis_Tests(self, clientId, numTests):
        '''
        Purchase additional Inbox Analysis Tests for your the specified Account

        Required keyword arguments:

        clientId (int) - The client ID number for which you are purchasing
            tests
        numTests (int) - The number of tests you are ordering to be added to
            the specified Account

        Optional keyword arguments:

        Returns bool - True on success
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Purchase_Inbox_Analysis_Tests',
            'clientId': clientId,
            'numTests': numTests,
        }

        data = self.makeCall(args)
        return data

    def Admin_Find_Campaigns(self):
        '''
        Get Campaign data for an account

        Required keyword arguments:

        Optional keyword arguments:

        resellerIds (dict) - A dict of reseller ID numbers
        clientIds (dict) - A dict of client ID numbers
        campaignIds (dict) - A dict of campaign ID numbers
        trials (bool) - Return trial accounts; defaults to true.
        minCreationDate (string) - Find clients who were created after this
            date
        maxCreationDate (string) - Find clients who were created before this
            date
        minPurchaseDate (string) - Find clients who upgraded after this date
        maxPurchaseDate (string) - Find clients who upgraded before this date
        minDate (string) - Find campaigns sent on or after minDate. Denoted in
            UTC.
        maxDate (string) - Find campaigns sent on or before maxDate. Denoted in
            UTC.
        minTime (string) - Find campaigns send on or after this time of day.
            Denoted in UTC.
        maxTime (string) - Find campaigns send on or before this time of day.
            Denoted in UTC.
        campaignType (dict) - The type of campaign, valid values: standard,
            recurring_parent, recurring_child, transactional
        minNumSent (int) - Total number sent
        maxNumSent (int) - Total number sent
        minSpamRate (float) - Spam rate percentage (e.g. 1% would be 0.01)
        maxSpamRate (float) - Spam rate percentage (e.g. 1% would be 0.01)
        minOpenRate (float) - Open rate percentage (e.g. 1% would be 0.01)
        maxOpenRate (float) - Open rate percentage (e.g. 1% would be 0.01)
        minBounceRate (float) - Bounce rate percentage (e.g. 1% would be 0.01)
        maxBounceRate (float) - Bounce rate percentage (e.g. 1% would be 0.01)
        minClickRate (float) - Click rate percentage (e.g. 1% would be 0.01)
        maxClickRate (float) - Click rate percentage (e.g. 1% would be 0.01)
        minUnsubRate (float) - Unusubscribe rate percentage (e.g. 1% would be
            0.01)
        maxUnsubRate (float) - Unsubscribe rate percentage (e.g. 1% would be
            0.01)
        sendConfigId (int) - Send confguration ID
        sendingDisabled (string) - Clients with sending disabled. May be one of
            ['any', 'yes', 'no'].
        content (bool) - Retreive the content of the campaign, defaults to true

        Returns struct - A struct of Campaign data
        '''

        args = {
            'key': self.key,
            'method': 'Admin_Find_Campaigns',
        }

        data = self.makeCall(args)
        return data
