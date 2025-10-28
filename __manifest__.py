{
    'name': 'Base Tailwind Theme',
    # Short description for the apps store.  A detailed description and
    # screenshots are provided in static/description/index.html as per the
    # Odoo vendor guidelines【312700953233289†L240-L256】.
    'description': 'A modern Tailwind‑powered website theme for Odoo that replicates the Base Tailwind corporate template. Includes a fully editable homepage and layouts built with Tailwind CSS.',
    'category': 'Website/Theme',
    'version': '19.0.1.0.0',
    'author': 'Your Company',
    'license': 'LGPL-3',
    # Set a price and currency for the theme.  According to the Odoo vendor
    # guidelines, the minimum price is 9 EUR if the module is paid【338510115502247†L256-L259】.
    # Leaving these keys empty would make the theme free.  Here we set the
    # minimum price in euros.
    'price': 9,
    'currency': 'EUR',
    'depends': ['website'],
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
    # Image(s) used for the cover thumbnail and screenshots in the app store.
    # The first image with a name ending in _screenshot will be used as the
    # big screenshot【312700953233289†L253-L257】.  Additional images can be
    # listed here if desired.
    'images': ['static/description/images/main_screenshot.png'],
    # Declare this module as a theme so it appears in the theme selector
    'auto_install': False,
    'application': False,
    # Optionally define a support email for clients.  This address will
    # be visible to customers who purchase the theme and is recommended by
    # the Odoo Apps guidelines【338510115502247†L256-L263】.
    'support': 'support@example.com',
}