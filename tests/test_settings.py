import unittest
from uiplib import settings


class SettingsTest(unittest.TestCase):

    def setUp(self):
        self.parseSettings = settings.ParseSettings([])

    def test_get_settings_from_cli(self):

        # Service and UI should not be mixed
        args = ['--service', 'start', '--ui']
        settings = self.parseSettings.get_settings_from_cli(args)
        self.assertIsNotNone(settings['error'])

        # No of images and offline should not be mixed
        args = ['--no-of-images', '20', '--offline']
        settings = self.parseSettings.get_settings_from_cli(args)
        self.assertIsNotNone(settings['error'])

        # Test-1
        args = ['--no-of-images', '20']
        settings = self.parseSettings.get_settings_from_cli(args)
        self.assertEqual(settings['no-of-images'], '20')

        # Test-2
        args = ['--service', 'stop']
        settings = self.parseSettings.get_settings_from_cli(args)
        self.assertEqual(settings['service'], 'stop')

        # Test-3
        args = ['--offline', '--ui', '--flush']
        settings = self.parseSettings.get_settings_from_cli(args)
        self.assertEqual(settings['offline'], True)
        self.assertEqual(settings['ui'], True)
        self.assertEqual(settings['flush'], True)

        # Test-4
        with self.assertRaises(SystemExit):
            args = ['--something']
            settings = self.parseSettings.get_settings_from_cli(args)
