# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Darlene Medeiros',
            cpf='12345678901',
            email='darlene@email.com',
            phone='21-91911919'
        )

    def test_create(self):
        'Subscription must have name, cpf, email, phone.'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription must have automatic created_at.'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Darlene Medeiros', unicode(self.obj))

    def test_paid_default_value_is_False(self):
        'By default paid must be False.'
        self.assertEqual(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force the colision
        Subscription.objects.create(name='Darlene Medeiros',
                                    cpf='12345678901',
                                    email='darlene@email.com',
                                    phone='21-91911919')

    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(name='Darlene Medeiros',
                         cpf='12345678901',
                         email='outro@email.com',
                         phone='21-91911919')
        self.assertRaises(IntegrityError, s.save)

    def test_email_can_repeat(self):
        'Email is not unique anymore'
        s = Subscription.objects.create(name='Darlene Medeiros',
                                        cpf='10234567891',
                                        email='darlene@email.com',
                                        phone='21-91911919')
        self.assertEqual(2, s.pk)
