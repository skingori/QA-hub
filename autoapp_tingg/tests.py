from django.test import TestCase
from .services import QaOperations
from .models import APISettings
# Create your tests here.
import unittest
from django.test import Client
import json


class QaTester(unittest.TestCase):
    def setUp(self):
        # APISettings.objects.create()
        # APISettings.objects.create()
        self.client = Client()
        self.file_path = "media/requests_all.json"
        self.response = QaOperations.read_any_file(self.file_path)
        self.actual_result = json.dumps(self.response)
        self.success = self.response["SUCCESS"]

    def test_status_codes_success(self):
        """Test if user gets statusCodes value form the file"""
        assert "statusCodes" in self.actual_result

    def test_success_response(self):
        """Test if user will get a successful response from JSON"""
        self.assertTrue(self.success)

    def test_no_file_found(self):
        """Test if user will get "File not found" if file doesn't exist"""
        response = QaOperations.read_any_file(self.file_path+"++")
        assert "File not found!" in response

    def test_details(self):
        """Test if user can access login path """
        # Issue a GET request.
        response = self.client.get('/login/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 302)

    def test_get_statuses(self):
        """Test if user gets available status codes"""
        status = self.response['DATA']['metaData']['statusCodes']
        self.assertTrue(status, msg="No Status")
