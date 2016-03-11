from distutils.core import setup

exec(open("Lex/version.py").read())

setup(
    name         = "Lex",
    version      = __version__,
    requires     = ['Crypto.Hash'],
    packages     = ['Lex', 'Lex.Chain'],
    package_data = {'Lex': ['htdocs/*']},
    author       = "phm",
    author_email = "phm@woodcoin.org",
    url          = "https://github.com/paulmadore/woodcoin-explorer",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Database :: Front-Ends',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Office/Business :: Financial',
        'Topic :: Security :: Cryptography',
        #'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    use_2to3 = True,    
    description  = "Block explorer for Woodcoin." = """Woodcoin block explorer.""",
    )
