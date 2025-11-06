{
    'name': 'Tailwind Theme',
    # Short description for the apps store. A detailed description and
    # screenshots are provided in static/description/index.html
    'description': 'A modern Tailwind powered website theme for Odoo. Includes a fully editable homepage and layouts built with Tailwind CSS.',
    'category': 'Theme/Creative',
    'version': '19.0.1.0.0',
    'author': 'Kiuw',
    'license': 'LGPL-3',
    # Price and currency for the theme
    'price': 9,
    'currency': 'EUR',
    'depends': ['website'],
    'installable': True,
    'data': [
        'views/assets.xml',
        'views/home.xml',
    ],
    'assets': {
        # Include the Tailwind CSS framework from a CDN and any custom assets
        'web.assets_frontend': [
            # Tailwind CSS – loaded via CDN to match the original template
            'https://cdn.jsdelivr.net/npm/tailwindcss@3.1.8/dist/tailwind.min.css',
            # Custom font definitions or variables could be added here if needed
        ],
    },
    # Cover thumbnail and screenshots for the app store
    'images': ['static/description/images/main_screenshot.png'],
    # Declare this module as a theme so it appears in the theme selector
    'auto_install': False,
    'application': False,
    # Support email for customers
    'support': 'julesndanga7@gmail.com',
}