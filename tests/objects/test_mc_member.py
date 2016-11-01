# coding=utf-8
import datetime
from dateutil.tz import tzutc
import unittest
from mailchimp.objects import MCMember, MCLocation


class TestMCMember(unittest.TestCase):
    def get_member(self):
        return {
            "id": "852aaa9532cb36adfb5e9fef7a4206a9",
            "email_address": "urist.mcvankab+3@freddiesjokes.com",
            "unique_email_id": "fab20fa03d",
            "email_type": "html",
            "status": "subscribed",
            "status_if_new": "",
            "merge_fields": {
                "FNAME": "",
                "LNAME": ""
            },
            "interests": {
                "9143cf3bd1": False,
                "3a2a927344": False,
                "f9c8f5f0ff": False,
                "f231b09abc": False,
                "bd6e66465f": False
            },
            "stats": {
                "avg_open_rate": 0,
                "avg_click_rate": 0
            },
            "ip_signup": "",
            "timestamp_signup": "",
            "ip_opt": "198.2.191.34",
            "timestamp_opt": "2015-09-15T17:27:16+00:00",
            "member_rating": 2,
            "last_changed": "2015-09-15T17:27:16+00:00",
            "language": "",
            "vip": False,
            "email_client": "",
            "location": {
                "latitude": 0,
                "longitude": 0,
                "gmtoff": 0,
                "dstoff": 0,
                "country_code": "",
                "timezone": ""
            },
            "list_id": "57afe96172",
            "_links": [
                {
                    "rel": "self",
                    "href": "https://us1.api.mailchimp.com/3.0/lists/57afe96172/members/852aaa9532cb36adfb5e9fef7a4206a9",
                    "method": "GET",
                    "targetSchema": "https://api.mailchimp.com/schema/3.0/Lists/Members/Instance.json"
                },
                {
                    "rel": "parent",
                    "href": "https://us1.api.mailchimp.com/3.0/lists/57afe96172/members",
                    "method": "GET",
                    "targetSchema": "https://api.mailchimp.com/schema/3.0/Lists/Members/Collection.json",
                    "schema": "https://api.mailchimp.com/schema/3.0/CollectionLinks/Lists/Members.json"
                },
                {
                    "rel": "update",
                    "href": "https://us1.api.mailchimp.com/3.0/lists/57afe96172/members/852aaa9532cb36adfb5e9fef7a4206a9",
                    "method": "PATCH",
                    "schema": "https://api.mailchimp.com/schema/3.0/Lists/Members/Instance.json"
                },
                {
                    "rel": "upsert",
                    "href": "https://us1.api.mailchimp.com/3.0/lists/57afe96172/members/852aaa9532cb36adfb5e9fef7a4206a9",
                    "method": "PUT",
                    "schema": "https://api.mailchimp.com/schema/3.0/Lists/Members/Instance.json"
                },
                {
                    "rel": "delete",
                    "href": "https://us1.api.mailchimp.com/3.0/lists/57afe96172/members/852aaa9532cb36adfb5e9fef7a4206a9",
                    "method": "DELETE"
                },
                {
                    "rel": "activity",
                    "href": "https://us1.api.mailchimp.com/3.0/lists/57afe96172/members/852aaa9532cb36adfb5e9fef7a4206a9/activity",
                    "method": "GET",
                    "targetSchema": "https://api.mailchimp.com/schema/3.0/Lists/Members/Activity/Collection.json"
                },
                {
                    "rel": "goals",
                    "href": "https://us1.api.mailchimp.com/3.0/lists/57afe96172/members/852aaa9532cb36adfb5e9fef7a4206a9/goals",
                    "method": "GET",
                    "targetSchema": "https://api.mailchimp.com/schema/3.0/Lists/Members/Goals/Collection.json"
                },
                {
                    "rel": "notes",
                    "href": "https://us1.api.mailchimp.com/3.0/lists/57afe96172/members/852aaa9532cb36adfb5e9fef7a4206a9/notes",
                    "method": "GET",
                    "targetSchema": "https://api.mailchimp.com/schema/3.0/Lists/Members/Notes/Collection.json"
                }
            ]
        }

    def test_item_url(self):
        member = MCMember()
        self.assertEqual('/lists/{list_id}/members', member.item_url)

    def test_valid_search_params(self):
        member = MCMember()
        self.assertEqual(['offset', 'count', 'fields', 'exclude_fields'],
                         member.valid_search_params)

    def test_empty_init(self):
        member = MCMember()

        for prop in ['id', 'email_address', 'unique_email_id', 'email_type', 'status', 'status_if_new', 'merge_fields',
                     'interests', 'stats', 'ip_signup', 'timestamp_signup', 'ip_opt', 'timestamp_opt', 'member_rating',
                     'last_changed', 'language', 'vip', 'email_client', 'list_id']:
            self.assertIsNone(getattr(member, prop))

        self.assertTrue(isinstance(member.location, MCLocation))
        self.assertEqual(member.links, [])

    def test_init(self):
        member = MCMember(self.get_member())

        self.assertEqual(member.id, '852aaa9532cb36adfb5e9fef7a4206a9')
        self.assertEqual(member.email_address, 'urist.mcvankab+3@freddiesjokes.com')
        self.assertEqual(member.unique_email_id, 'fab20fa03d')
        self.assertEqual(member.email_type, 'html')
        self.assertEqual(member.status, 'subscribed')
        self.assertEqual(member.status_if_new, '')
        self.assertEqual(member.merge_fields, {
            "FNAME": "",
            "LNAME": ""
        })
        self.assertEqual(member.interests, {
            "9143cf3bd1": False,
            "3a2a927344": False,
            "f9c8f5f0ff": False,
            "f231b09abc": False,
            "bd6e66465f": False
        })
        self.assertEqual(member.stats, {
            "avg_open_rate": 0,
            "avg_click_rate": 0
        })
        self.assertEqual(member.ip_signup, "")
        self.assertIsNone(member.timestamp_signup)
        self.assertEqual(member.ip_opt, "198.2.191.34")
        self.assertEqual(member.timestamp_opt, datetime.datetime(2015, 9, 15, 17, 27, 16).replace(tzinfo=tzutc()))
        self.assertEqual(member.member_rating, 2)
        self.assertEqual(member.last_changed, datetime.datetime(2015, 9, 15, 17, 27, 16).replace(tzinfo=tzutc()))
        self.assertEqual(member.language, "")
        self.assertFalse(member.vip)
        self.assertEqual(member.email_client, "")
        self.assertTrue(isinstance(member.location, MCLocation))
        self.assertEqual(member.location.longitude, 0)
        self.assertEqual(member.location.latitude, 0)
        self.assertEqual(member.location.gmtoff, 0)
        self.assertEqual(member.location.dstoff, 0)
        self.assertEqual(member.location.country_code, "")
        self.assertEqual(member.location.timezone, "")
        self.assertEqual(member.list_id, "57afe96172")
        self.assertEqual(len(member.links), 8)

    def test_to_str(self):
        member = MCMember(self.get_member())
        self.assertEqual('852aaa9532cb36adfb5e9fef7a4206a9', str(member))

    def test_repr(self):
        member = MCMember(self.get_member())
        self.assertEqual('<MCMember: 852aaa9532cb36adfb5e9fef7a4206a9>', str(repr(member)))
