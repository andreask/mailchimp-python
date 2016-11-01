# coding=utf-8
import json
import unittest
import responses
from mailchimp.exceptions import ObjectNotFound
from mailchimp import Request
from mailchimp.config import mailchimp_config


class TestRequest(unittest.TestCase):
    def setUp(self):
        mailchimp_config.api_key = 'a65a65a65a65a65a56a5a6-us1'

    def test_get_headers(self):
        self.assertEqual(Request.get_headers(), {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def test_delete(self):
        with responses.RequestsMock() as rsps:
            rsps.add(responses.DELETE, 'https://us1.api.mailchimp.com/3.0/instance/1',
                     status=204, content_type='application/json')

            response = Request.delete('https://us1.api.mailchimp.com/3.0/instance/1')
            self.assertEqual(response.status_code, 204)
            self.assertEqual(b'', response.content)

            self.assertEqual(1, len(rsps.calls))
            self.assertEqual("https://us1.api.mailchimp.com/3.0/instance/1", rsps.calls[0].request.url)
            self.assertEqual("application/json", rsps.calls[0].request.headers['Accept'])
            self.assertEqual("application/json", rsps.calls[0].request.headers['Content-Type'])
            self.assertEqual("Basic dXNlcm5hbWU6YTY1YTY1YTY1YTY1YTY1YTU2YTVhNi11czE=",
                             rsps.calls[0].request.headers['Authorization'])

    def test_delete_with_relative_url(self):
        with responses.RequestsMock() as rsps:
            rsps.add(responses.DELETE, 'https://us1.api.mailchimp.com/3.0/instance/1',
                     status=204, content_type='application/json')

            response = Request.delete('/instance/1')
            self.assertEqual(response.status_code, 204)
            self.assertEqual(b'', response.content)

            self.assertEqual(1, len(rsps.calls))
            self.assertEqual("https://us1.api.mailchimp.com/3.0/instance/1", rsps.calls[0].request.url)
            self.assertEqual("application/json", rsps.calls[0].request.headers['Accept'])
            self.assertEqual("application/json", rsps.calls[0].request.headers['Content-Type'])
            self.assertEqual("Basic dXNlcm5hbWU6YTY1YTY1YTY1YTY1YTY1YTU2YTVhNi11czE=",
                             rsps.calls[0].request.headers['Authorization'])

    def test_get(self):
        with responses.RequestsMock() as rsps:
            rsps.add(responses.GET, 'https://us1.api.mailchimp.com/3.0/instance',
                     json={"Instances": [{"Id": 1}, {"Id": 2}]}, status=200,
                     content_type='application/json')

            response = Request.get('https://us1.api.mailchimp.com/3.0/instance')
            response_json = response.json()
            self.assertTrue("Instances" in response_json.keys())
            for item in response_json['Instances']:
                self.assertTrue("Id" in item.keys())

            self.assertEqual(1, len(rsps.calls))
            self.assertEqual("https://us1.api.mailchimp.com/3.0/instance", rsps.calls[0].request.url)
            self.assertEqual("application/json", rsps.calls[0].request.headers['Accept'])
            self.assertEqual("application/json", rsps.calls[0].request.headers['Content-Type'])
            self.assertEqual("Basic dXNlcm5hbWU6YTY1YTY1YTY1YTY1YTY1YTU2YTVhNi11czE=",
                             rsps.calls[0].request.headers['Authorization'])

            rsps.add(responses.GET, 'https://us1.api.mailchimp.com/3.0/instance/1',
                     json={"Instance": {"Id": 1}}, status=200,
                     content_type='application/json')

            response = Request.get('https://us1.api.mailchimp.com/3.0/instance/1')
            response_json = response.json()
            self.assertTrue("Instance" in response_json.keys())
            self.assertTrue("Id" in response_json['Instance'].keys())
            self.assertEqual(1, response_json['Instance']['Id'])

            self.assertEqual(2, len(rsps.calls))
            self.assertEqual("https://us1.api.mailchimp.com/3.0/instance/1", rsps.calls[1].request.url)
            self.assertEqual("application/json", rsps.calls[1].request.headers['Accept'])
            self.assertEqual("application/json", rsps.calls[1].request.headers['Content-Type'])
            self.assertEqual("Basic dXNlcm5hbWU6YTY1YTY1YTY1YTY1YTY1YTU2YTVhNi11czE=",
                             rsps.calls[1].request.headers['Authorization'])

    def test_get_with_relative_url(self):
        with responses.RequestsMock() as rsps:
            rsps.add(responses.GET, 'https://us1.api.mailchimp.com/3.0/instance',
                     json={"Instances": [{"Id": 1}, {"Id": 2}]}, status=200,
                     content_type='application/json')

            response = Request.get('/instance')
            response_json = response.json()
            self.assertTrue("Instances" in response_json.keys())
            for item in response_json['Instances']:
                self.assertTrue("Id" in item.keys())

            self.assertEqual(1, len(rsps.calls))
            self.assertEqual("https://us1.api.mailchimp.com/3.0/instance", rsps.calls[0].request.url)
            self.assertEqual("application/json", rsps.calls[0].request.headers['Accept'])
            self.assertEqual("application/json", rsps.calls[0].request.headers['Content-Type'])
            self.assertEqual("Basic dXNlcm5hbWU6YTY1YTY1YTY1YTY1YTY1YTU2YTVhNi11czE=",
                             rsps.calls[0].request.headers['Authorization'])

            rsps.add(responses.GET, 'https://us1.api.mailchimp.com/3.0/instance/1',
                     json={"Instance": {"Id": 1}}, status=200,
                     content_type='application/json')

            response = Request.get('/instance/1')
            response_json = response.json()
            self.assertTrue("Instance" in response_json.keys())
            self.assertTrue("Id" in response_json['Instance'].keys())
            self.assertEqual(1, response_json['Instance']['Id'])

            self.assertEqual(2, len(rsps.calls))
            self.assertEqual("https://us1.api.mailchimp.com/3.0/instance/1", rsps.calls[1].request.url)
            self.assertEqual("application/json", rsps.calls[1].request.headers['Accept'])
            self.assertEqual("application/json", rsps.calls[1].request.headers['Content-Type'])
            self.assertEqual("Basic dXNlcm5hbWU6YTY1YTY1YTY1YTY1YTY1YTU2YTVhNi11czE=",
                             rsps.calls[1].request.headers['Authorization'])

    def test_get_404(self):
        with responses.RequestsMock() as rsps:
            rsps.add(responses.GET, 'https://us1.api.mailchimp.com/3.0/instance/4',
                     json={'type': 'Not found'}, status=404, content_type='application/json')

            with self.assertRaises(ObjectNotFound):
                Request.get('https://us1.api.mailchimp.com/3.0/instance/4')

    def test_put(self):
        with responses.RequestsMock() as rsps:
            rsps.add(responses.PUT, 'https://us1.api.mailchimp.com/3.0/instance',
                     json={"Instance": {"Id": 1}}, status=200,
                     content_type='application/json')

            response = Request.put('https://us1.api.mailchimp.com/3.0/instance', {"Id": 1})
            response_json = response.json()
            self.assertTrue("Instance" in response_json.keys())
            self.assertTrue("Id" in response_json['Instance'].keys())
            self.assertEqual(1, response_json['Instance']['Id'])

            self.assertEqual(1, len(rsps.calls))
            self.assertEqual("https://us1.api.mailchimp.com/3.0/instance", rsps.calls[0].request.url)
            self.assertEqual(json.dumps({"Id": 1}), rsps.calls[0].request.body.decode("utf-8"))
            self.assertEqual("application/json", rsps.calls[0].request.headers['Accept'])
            self.assertEqual("application/json", rsps.calls[0].request.headers['Content-Type'])
            self.assertEqual("Basic dXNlcm5hbWU6YTY1YTY1YTY1YTY1YTY1YTU2YTVhNi11czE=",
                             rsps.calls[0].request.headers['Authorization'])

    def test_put_with_relative_url(self):
        with responses.RequestsMock() as rsps:
            rsps.add(responses.PUT, 'https://us1.api.mailchimp.com/3.0/instance',
                     json={"Instance": {"Id": 1}}, status=200,
                     content_type='application/json')

            response = Request.put('/instance', {"Id": 1})
            response_json = response.json()
            self.assertTrue("Instance" in response_json.keys())
            self.assertTrue("Id" in response_json['Instance'].keys())
            self.assertEqual(1, response_json['Instance']['Id'])

            self.assertEqual(1, len(rsps.calls))
            self.assertEqual("https://us1.api.mailchimp.com/3.0/instance", rsps.calls[0].request.url)
            self.assertEqual(json.dumps({"Id": 1}), rsps.calls[0].request.body.decode("utf-8"))
            self.assertEqual("application/json", rsps.calls[0].request.headers['Accept'])
            self.assertEqual("application/json", rsps.calls[0].request.headers['Content-Type'])
            self.assertEqual("Basic dXNlcm5hbWU6YTY1YTY1YTY1YTY1YTY1YTU2YTVhNi11czE=",
                             rsps.calls[0].request.headers['Authorization'])

    def test_post(self):
        with responses.RequestsMock() as rsps:
            rsps.add(responses.POST, 'https://us1.api.mailchimp.com/3.0/instance',
                     json={"Instance": {"Id": 1}}, status=200,
                     content_type='application/json')

            response = Request.post('https://us1.api.mailchimp.com/3.0/instance', {"Id": 1})
            response_json = response.json()
            self.assertTrue("Instance" in response_json.keys())
            self.assertTrue("Id" in response_json['Instance'].keys())
            self.assertEqual(1, response_json['Instance']['Id'])

            self.assertEqual(1, len(rsps.calls))
            self.assertEqual("https://us1.api.mailchimp.com/3.0/instance", rsps.calls[0].request.url)
            self.assertEqual(json.dumps({"Id": 1}), rsps.calls[0].request.body.decode("utf-8"))
            self.assertEqual("application/json", rsps.calls[0].request.headers['Accept'])
            self.assertEqual("application/json", rsps.calls[0].request.headers['Content-Type'])
            self.assertEqual("Basic dXNlcm5hbWU6YTY1YTY1YTY1YTY1YTY1YTU2YTVhNi11czE=",
                             rsps.calls[0].request.headers['Authorization'])

    def test_post_with_relative_url(self):
        with responses.RequestsMock() as rsps:
            rsps.add(responses.POST, 'https://us1.api.mailchimp.com/3.0/instance',
                     json={"Instance": {"Id": 1}}, status=200,
                     content_type='application/json')

            response = Request.post('/instance', {"Id": 1})
            response_json = response.json()
            self.assertTrue("Instance" in response_json.keys())
            self.assertTrue("Id" in response_json['Instance'].keys())
            self.assertEqual(1, response_json['Instance']['Id'])

            self.assertEqual(1, len(rsps.calls))
            self.assertEqual("https://us1.api.mailchimp.com/3.0/instance", rsps.calls[0].request.url)
            self.assertEqual(json.dumps({"Id": 1}), rsps.calls[0].request.body.decode("utf-8"))
            self.assertEqual("application/json", rsps.calls[0].request.headers['Accept'])
            self.assertEqual("application/json", rsps.calls[0].request.headers['Content-Type'])
            self.assertEqual("Basic dXNlcm5hbWU6YTY1YTY1YTY1YTY1YTY1YTU2YTVhNi11czE=",
                             rsps.calls[0].request.headers['Authorization'])
