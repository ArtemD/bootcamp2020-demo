from django.test import TestCase
import json

class TestPrhapi(TestCase):
    def test_that_form_is_displayed(self):
        response = self.client.get("/prhapi/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "form.html")

    def test_that_api_works_correctly(self):
        test_data = {
            'business_id': '0912797-2'
        }
        response = self.client.post("/prhapi/", data=test_data)
        self.assertContains(response, "Noksu Oy")