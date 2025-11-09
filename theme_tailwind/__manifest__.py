{
    'name': 'Tailwind Business Theme',
    'summary': 'Modern, high-converting website theme for startups and businesses',
    # Detailed description and screenshots in static/description/index.html
    'description': '''
        Launch a stunning, high-converting website in minutes. Premium Tailwind-powered theme with 10+ pre-built sections: 
        Hero, Services, About, Pricing, Portfolio, Testimonials, Blog & Contact. Fully responsive & customizable with 
        Odoo's drag-and-drop builder. Perfect for startups, agencies, SaaS & online businesses. No coding required!
    ''',
    'category': 'Theme',
    'version': '19.0.1.0.0',
    'author': 'Kiuw',
    'license': 'LGPL-3',
    # Price and currency for the theme
    'price': 30,
    'currency': 'EUR',
    'depends': ['theme_common'],
    'installable': True,
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/snippets/s_cover.xml',
    ],
    # Cover thumbnail and screenshots for the app store
    'images': ['static/description/images/main_screenshot.png'],
    # Declare this module as a theme so it appears in the theme selector
    'auto_install': False,
    # Support email for customers
    'support': 'julesndanga7@gmail.com',
}