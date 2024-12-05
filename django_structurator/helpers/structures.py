
PROJECT_STRUCTURE = {
    
    'docs': [
        'ARCHITECTURE.md',
        'CHANGELOG.md',
        'README.md',
        'TROUBLESHOOTING.md',
        'USAGE.md',
    ],
    
    'requirements': [
        'base.txt',
        'development.txt',
        'production.txt',
        'test.txt',
    ],
    
    'src': {
        
        'config': {
            None : ['__init__.py', 'asgi.py', '.env', '.env.example', 'urls.py', 'wsgi.py'],
            'settings': [
                '__init__.py',
                'base.py',
                'development.py',
                'production.py',
            ],
        },
        
        'apps': [
            '__init__.py'
        ],
        
        'common': [
            '__init__.py',
            'constants.py',
            'helpers.py',
        ],
        
        'media': [],
        
        'static': {
            'js': [],
            'css': [],
            'images': [
                'favicon.ico',
            ],
        },
        'templates': [
            'base.html',
            'index.html'
        ],
        
        None : ['manage.py']
        
    },
    None: ['.gitignore']
}

APP_STRUCTURE = {
    None : [
        '__init__.py',
        'admin.py',
        'apps.py',
        'models.py',
        'tests.py',
        'views.py',
        'urls.py',
    ],
    
    'migrations': [
        '__init__.py'
    ],
}