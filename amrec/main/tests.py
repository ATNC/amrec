import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Category


class TestCategory(APITestCase):

    def setUp(self):
        self.category = {
            'name': 'Category   1',
            'children': [
                {
                    'name': 'Category   1.1',
                    'children': [
                        {
                            'name': 'Category   1.1.1',
                            'children': [
                                {
                                    'name': 'Category   1.1.1.1',

                                },
                                {
                                    'name': 'Category   1.1.1.2',

                                },
                                {
                                    'name': 'Category   1.1.1.3',

                                },

                            ]

                        },
                        {
                            'name': 'Category   1.1.2',
                            'children': [
                                {
                                    'name': 'Category   1.1.2.1',

                                },
                                {
                                    'name': 'Category   1.1.2.2',

                                },
                                {
                                    'name': 'Category   1.1.2.3',

                                },

                            ]

                        }

                    ]

                },
                {
                    'name': 'Category   1.2',
                    'children': [
                        {
                            'name': 'Category   1.2.1',

                        },
                        {
                            'name': 'Category   1.2.2',
                            'children': [
                                {
                                    'name': 'Category   1.2.2.1',

                                },
                                {
                                    'name': 'Category   1.2.2.2',

                                },

                            ]

                        },

                    ]

                }

            ]
        }

    def test_create_category_from_json(self):
        data = json.dumps(self.category)
        response = self.client.post(
            reverse('create_category_endpoint'),
            data=data,
            content_type='application/json'
        )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Category.objects.count(), 15)

    def test_retrieve_category_by_id(self):
        expected_2_dict = {
            "id": 2,
            "name": "Category   1.1",
            "parents": [
                {
                    "id": 1,
                    "name": "Category   1"
                }
            ],
            "children": [
                {
                    "id": 3,
                    "name": "Category   1.1.1"
                },
                {
                    "id": 7,
                    "name": "Category   1.1.2"
                },
            ],
            "siblings": [
                {
                    "id": 11,
                    "name": "Category   1.2"
                },
            ]

        }
        expected_8_dict = {
            "id": 8,
            "name": "Category   1.1.2.1",
            "parents": [
                {
                    "id": 7,
                    "name": "Category   1.1.2"
                },
                {
                    "id": 2,
                    "name": "Category   1.1"
                },
                {
                    "id": 1,
                    "name": "Category   1"
                },
            ],
            "children": [],
            "siblings": [
                {
                    "id": 9,
                    "name": "Category   1.1.2.2"
                },
                {
                    "id": 10,
                    "name": "Category   1.1.2.3"
                },
            ]

        }
        data = json.dumps(self.category)
        # create category
        self.client.post(
            reverse('create_category_endpoint'),
            data=data,
            content_type='application/json'
        )

        # retrieve category
        response = self.client.get(reverse('retrieve_category_endpoint', kwargs={'pk': 2}))
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, expected_2_dict)

        # retrieve category
        response = self.client.get(reverse('retrieve_category_endpoint', kwargs={'pk': 8}))
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, expected_8_dict)


