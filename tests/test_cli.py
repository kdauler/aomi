import unittest
import aomi.cli

class OpParserTest(unittest.TestCase):
    def enabled_options(self, operations, option):
        for op in operations:
            self.assertTrue(aomi.cli.parser_factory(op).has_option(option))

    def disabled_options(self, operations, option):
        for op in operations:
            self.assertFalse(aomi.cli.parser_factory(op).has_option(option))

    def test_secretfile_option(self):
        self.enabled_options(['seed'], '--secretfile')
        self.disabled_options(['environment',
                               'extract_file',
                               'aws_environment',
                               'template'], '--secretfile')


    def test_policies_option(self):
        self.enabled_options(['seed'], '--policies')
        self.disabled_options(['environment',
                               'extract_file',
                               'aws_environment',
                               'template'], '--policies')


    def test_secrets_option(self):
        self.enabled_options(['seed'], '--secrets')
        self.disabled_options(['environment',
                               'extract_file',
                               'aws_environment',
                               'template'], '--secrets')


    def test_mount_only_option(self):
        self.enabled_options(['seed'], '--mount-only')
        self.disabled_options(['environment',
                               'extract_file',
                               'aws_environment',
                               'template'], '--mount-only')


    def test_prefix_option(self):
        self.enabled_options(['environment'], '--prefix')
        self.disabled_options(['seed',
                               'aws_environment',
                               'template'
                               'extract_file'], '--prefix')


    def test_prefix_option(self):
        self.enabled_options(['environment',
                              'template'], '--add-prefix')
        self.disabled_options(['seed',
                               'extract_file',
                               'aws_environment'], '--add-prefix')

    def test_suffix_option(self):
        self.enabled_options(['environment',
                              'template'], '--add-suffix')
        self.disabled_options(['seed',
                               'extract_file',
                               'aws_environment'], '--add-suffix')


    def test_merge_path_option(self):
        self.enabled_options(['environment',
                              'template'], '--merge-path')
        self.disabled_options(['seed',
                               'extract_file',
                               'aws_environment'], '--merge-path')


    def test_no_merge_path_option(self):
        self.enabled_options(['environment',
                              'template'], '--no-merge-path')
        self.disabled_options(['seed',
                               'extract_file',
                               'aws_environment'], '--no-merge-path')

    def test_verbose_option(self):
        self.enabled_options(['environment',
                              'seed',
                              'extract_file',
                              'aws_environment',
                              'template'], '--verbose')

    def test_metadata_option(self):
        self.enabled_options(['environment',
                              'seed',
                              'extract_file',
                              'aws_environment',
                              'template'], '--metadata')

    def test_lease_option(self):
        self.enabled_options(['environment',
                              'seed',
                              'extract_file',
                              'aws_environment',
                              'template'], '--lease')

    def test_export_option(self):
        self.enabled_options(['environment', 'aws_environment'], '--export')
        self.disabled_options(['seed',
                               'extract_file',
                               'template'], '--export')
        
    def test_extra_vars_option(self):
        self.enabled_options(['template', 'seed'], '--extra-vars')
        self.disabled_options(['environment',
                               'extract_file',
                               'aws_environment'], '--extra-vars')

    def test_extra_vars_file_option(self):
        self.enabled_options(['template', 'seed'], '--extra-vars-file')
        self.disabled_options(['environment',
                               'extract_file',
                               'aws_environment'], '--extra-vars-file')
