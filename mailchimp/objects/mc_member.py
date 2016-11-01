# coding=utf-8
import hashlib
import logging

from mailchimp.exceptions import ObjectNotFound, MCListNotFound, MCMemberNotFound
from mailchimp import Request

from .base_object import BaseObject
from .mc_link import MCLink
from .mc_location import MCLocation

logger = logging.getLogger(__name__)


class MCMember(BaseObject):
    item_url = '/lists/{list_id}/members'

    def __init__(self, json_data={}):
        super(MCMember, self).__init__()
        self._update(json_data)

    def _update(self, json_data):
        self.id = json_data.get('id')
        self.email_address = json_data.get('email_address')
        self.unique_email_id = json_data.get('unique_email_id')
        self.email_type = json_data.get('email_type')
        self.status = json_data.get('status')
        self.status_if_new = json_data.get('status_if_new')
        self.merge_fields = json_data.get('merge_fields')
        self.interests = json_data.get('interests')
        self.stats = json_data.get('stats')
        self.ip_signup = json_data.get('ip_signup')
        self.timestamp_signup = self._parse_date(json_data.get('timestamp_signup')) \
            if json_data.get('timestamp_signup') else None
        self.ip_opt = json_data.get('ip_opt')
        self.timestamp_opt = self._parse_date(json_data.get('timestamp_opt')) \
            if json_data.get('timestamp_opt') else None
        self.member_rating = json_data.get('member_rating')
        self.last_changed = self._parse_date(json_data.get('last_changed')) if json_data.get('last_changed') else None
        self.language = json_data.get('language')
        self.vip = json_data.get('vip')
        self.email_client = json_data.get('email_client')
        self.location = MCLocation(json_data.get('location'))
        self.list_id = json_data.get('list_id')
        self.links = [MCLink(link) for link in json_data.get('_links')] if json_data.get('_links') else []

    def to_dict(self):
        return_value = {
            'email_type': self.email_type,
            'status': self.status,
            'merge_fields': self.merge_fields,
            'interests': self.interests,
            'language': self.language,
            'vip': self.vip,
            'location': self.location.to_dict()
        }

        if not self.id:
            return_value['email_address'] = self.email_address
            return_value['status_if_new'] = self.status_if_new
        else:
            return_value['id'] = self.id

        return return_value

    @classmethod
    def get_list_url(cls, list_id):
        """
        Replace the placeholder for the list id with the list id sent to the method - creates a valid url.

        :param list_id: the list to get the url for

        :return: the url for the list
        """
        return cls.item_url.replace("{list_id}", list_id)

    @classmethod
    def get(cls, list_id, member_id):
        """
        Get the member from the mailchimp API. list_id has to be a valid list and member_id should be the
        hash of the members email address.

        :param list_id: the list id to get the member from
        :param member_id: the hashed email address.

        :return: a MCMember object containing the member if successful, raises an MemberNotFound exception otherwise
        """
        try:
            response = Request.get("%s/%s" % (MCMember.get_list_url(list_id), member_id))
            return MCMember(response.json())

        except ObjectNotFound:
            raise MCMemberNotFound(list_id, member_id)

    @classmethod
    def list(cls, list_id, params={}):
        """
        Get the list of members for the list corresponding with the id list_id from the mailchimp API.

        :param list_id: the id of the list to get members from
        :param params: parameters for defining limits for the search - can be used to page result or search for a
        specific status.

        :return: an array of MCMember objects if successful, raises a ListNotFound exception otherwise
        """
        try:
            response = Request.get("%s" % MCMember.get_list_url(list_id), params)
            return [MCMember(member) for member in response.json()['members']]

        except ObjectNotFound:
            raise MCListNotFound(list_id)

    def delete(self):
        """
        Deletes the current member from the list

        :return: True if sucessful
        """
        if not self.id:
            return False

        try:
            Request.delete("%s/%s" % (MCMember.get_list_url(self.list_id), self.id))
            return True

        except Exception as e:
            logger.error("Unable to delete member from list")
            raise e

    def save(self):
        """
        Saves the current member to the list

        :return: True if successful
        """
        hash_value = self.id

        if not self.id:
            md = hashlib.md5()
            md.update(self.email_address.lower().encode("utf-8"))
            hash_value = md.hexdigest()

        try:
            response = Request.put("%s/%s" % (MCMember.get_list_url(self.list_id), hash_value),
                                   self.to_dict())
            self._update(response.json())
            return True

        except Exception as e:
            logger.error("Unable to save member")
            raise e
