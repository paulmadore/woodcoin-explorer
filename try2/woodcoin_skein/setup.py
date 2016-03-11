from distutils.core import setup, Extension

log_skein_module = Extension('log_skein',
                               sources = ['_skeinmodule.c',
                                          'skein.c'],
                               include_dirs=['.'])

setup (name = 'log_skein',
       version = '0.4',
       description = 'Bindings for Skein proof of work used by Woodcoin',
       ext_modules = [log_skein_module])