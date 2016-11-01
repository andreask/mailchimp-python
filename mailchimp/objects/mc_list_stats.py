# coding=utf-8
from .base_object import BaseObject


class MCListStats(BaseObject):
    item_url = None

    def __init__(self, json_data={}):
        super(MCListStats, self).__init__()
        self.member_count = None
        self.unsubscribe_count = None
        self.cleaned_count = None
        self.member_count_since_send = None
        self.unsubscribe_count_since_send = None
        self.cleaned_count_since_send = None
        self.campaign_count = None
        self.campaign_last_sent = None
        self.merge_field_count = None
        self.avg_sub_rate = None
        self.avg_unsub_rate = None
        self.target_sub_rate = None
        self.open_rate = None
        self.click_rate = None
        self.last_sub_date = None
        self.last_unsub_date = None

        if json_data:
            self.member_count = json_data['member_count']
            self.unsubscribe_count = json_data['unsubscribe_count']
            self.cleaned_count = json_data['cleaned_count']
            self.member_count_since_send = json_data['member_count_since_send']
            self.unsubscribe_count_since_send = json_data['unsubscribe_count_since_send']
            self.cleaned_count_since_send = json_data['cleaned_count_since_send']
            self.campaign_count = json_data['campaign_count']
            self.campaign_last_sent = json_data['campaign_last_sent']
            self.merge_field_count = json_data['merge_field_count']
            self.avg_sub_rate = json_data['avg_sub_rate']
            self.avg_unsub_rate = json_data['avg_unsub_rate']
            self.target_sub_rate = json_data['target_sub_rate']
            self.open_rate = json_data['open_rate']
            self.click_rate = json_data['click_rate']
            self.last_sub_date = self._parse_date(json_data['last_sub_date']) if json_data['last_sub_date'] else None
            self.last_unsub_date = self._parse_date(json_data['last_unsub_date']) \
                if json_data['last_unsub_date'] else None