# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker, Talk


class SpeakerDetailTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Darlene Medeiros',
                                   slug='darlene-medeiros',
                                   url='http://darlenemedeiros.com.br',
                                   description='Passionate software developer!')

        t = Talk.objects.create(description=u'Descrição da palestra',
                                title='Título da palestra',
                                start_time='10:00')

        t.speakers.add(s)

        url = r('core:speaker_detail', kwargs={'slug': 'darlene-medeiros'})
        self.resp = self.client.get(url)

    def test_get(self):
        'GET should result in 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template should be core/speaker_detail.html'
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        'Html must contain data.'
        self.assertContains(self.resp, 'Darlene Medeiros')
        self.assertContains(self.resp, 'Passionate software developer!')
        self.assertContains(self.resp, 'http://darlenemedeiros.com.br')
        self.assertContains(self.resp, u'Título da palestra', 1)
        self.assertContains(self.resp, u'/palestras/1/')

    def test_context(self):
        'Speaker must be in context.'
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        url = r('core:speaker_detail', kwargs={'slug': 'john-doe'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
