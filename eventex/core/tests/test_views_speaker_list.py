# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker


class SpeakerListTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Darlene Medeiros',
                                   slug='darlene-medeiros',
                                   url='http://darlenemedeiros.com.br',
                                   description='Passionate software developer!')

        self.resp = self.client.get(r('core:speaker_list'))

    def test_get(self):
        'GET must result in 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template should be core/speaker_list.html'
        self.assertTemplateUsed(self.resp, 'core/speaker_list.html')

    def test_html(self):
        'Html should list speakers.'
        self.assertContains(self.resp, u'Darlene Medeiros', 1)
        self.assertContains(self.resp, u'/palestrantes/darlene-medeiros', 1)
        self.assertContains(self.resp, u'Passionate software developer!', 1)
