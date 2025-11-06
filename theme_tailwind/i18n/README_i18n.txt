===========================================
TRADUCTIONS / TRANSLATIONS - Tailwind Theme
===========================================

Ce dossier contient les fichiers de traduction pour le thème.
This folder contains translation files for the theme.

📁 FICHIERS ACTUELS / CURRENT FILES:
------------------------------------
- fr.po : Traduction française (French translation) - PARTIEL
- README_i18n.txt : Ce fichier (This file)

⚠️ IMPORTANT:
-------------
Les fichiers .po actuels sont PARTIELS et contiennent uniquement les nouvelles
fonctionnalités (formulaire de contact, snippets, navigation).

Pour une traduction COMPLÈTE du fichier home.xml avec tous les textes,
vous devez générer le fichier .pot complet avec Odoo.

🔧 COMMENT GÉNÉRER LE FICHIER .POT COMPLET:
-------------------------------------------

1. Installer le module sur une instance Odoo 19:
   
   cd /chemin/vers/odoo
   ./odoo-bin -d nom_base_donnees -i theme_tailwind

2. Exporter le fichier POT:
   
   ./odoo-bin -d nom_base_donnees \
              --i18n-export=addons/theme_tailwind/i18n/theme_tailwind.pot \
              --modules=theme_tailwind

3. Créer les traductions pour chaque langue:
   
   # Pour le français
   cp theme_tailwind/i18n/theme_tailwind.pot theme_tailwind/i18n/fr.po
   
   # Pour l'espagnol
   cp theme_tailwind/i18n/theme_tailwind.pot theme_tailwind/i18n/es.po
   
   # Etc.

4. Éditer les fichiers .po pour ajouter les traductions:
   
   Ouvrez chaque .po et traduisez les msgid en msgstr:
   
   msgid "Get Started Now"
   msgstr "Commencez maintenant"  # Pour fr.po
   msgstr "Empezar ahora"         # Pour es.po

5. Mettre à jour les traductions dans Odoo:
   
   ./odoo-bin -d nom_base_donnees \
              --i18n-overwrite \
              --i18n-import=addons/theme_tailwind/i18n/fr.po

🌍 LANGUES RECOMMANDÉES:
------------------------
Pour maximiser les ventes, traduisez au minimum en:

1. Anglais (en) - DÉFAUT (textes actuels dans les templates)
2. Français (fr) - ✅ Traduction partielle fournie
3. Espagnol (es) - À créer
4. Allemand (de) - À créer
5. Arabe (ar) - À créer

📝 EXEMPLE DE TRADUCTION DANS home.xml:
---------------------------------------

AVANT (texte en dur):
<h1>We specialize in UI/UX, Web Development, Digital Marketing.</h1>

APRÈS (traduisible):
<h1 t-esc="_('We specialize in UI/UX, Web Development, Digital Marketing.')"/>

OU:

<h1>
    <t t-esc="_('We specialize in UI/UX, Web Development, Digital Marketing.')"/>
</h1>

⚠️ NOTE IMPORTANTE:
-------------------
Les fichiers home.xml, contact_form.xml, snippets.xml et header.xml
utilisent DÉJÀ les fonctions de traduction avec t-esc="_(...)"

Seul home.xml contient encore des textes en dur qui doivent être convertis.

🎯 PROCHAINE ÉTAPE:
-------------------
1. Générer le .pot complet avec Odoo (voir étape 2 ci-dessus)
2. Créer les .po pour toutes les langues souhaitées
3. Traduire tous les strings dans chaque .po
4. Importer les traductions dans Odoo
5. Tester avec différentes langues

💡 OUTILS UTILES:
-----------------
- Poedit: https://poedit.net/ (éditeur graphique de .po)
- Weblate: https://weblate.org/ (traduction collaborative)
- Transifex: https://www.transifex.com/ (plateforme de traduction)

📧 SUPPORT:
-----------
Pour toute question: julesndanga7@gmail.com
