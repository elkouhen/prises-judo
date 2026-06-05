# Spécification de l'application

## Objectif

L'application « Prises de Judo » est une application Streamlit mobile-first destinée à consulter rapidement des techniques de judo classées par catégorie. Elle doit permettre à un pratiquant, un parent ou un entraîneur de choisir une prise et d'accéder immédiatement à une courte description et à une vidéo YouTube intégrée.

## Utilisateurs cibles

- Judokas débutants ou intermédiaires qui révisent les techniques.
- Entraîneurs qui veulent montrer une prise pendant un cours.
- Parents ou accompagnants qui souhaitent comprendre le nom et le principe d'une technique.

## Fonctionnalités principales

1. Afficher la liste des catégories disponibles à partir du fichier `techniques.json`.
2. Afficher les techniques de la catégorie sélectionnée, triées par nom lisible.
3. Mettre à jour la technique sélectionnée lorsque l'utilisateur change de catégorie.
4. Afficher pour chaque technique :
   - son nom ;
   - sa description courte ;
   - la vidéo YouTube correspondante intégrée en 16:9.
5. Synchroniser la sélection dans l'URL avec les paramètres `category` et `technique` pour permettre le partage d'un lien direct.
6. En orientation paysage sur mobile, afficher la vidéo en plein écran et proposer :
   - un bouton technique précédente ;
   - un bouton technique suivante ;
   - un panneau de navigation ouvrable listant catégories et techniques.

## Données

Les données sont stockées dans `techniques.json`. Chaque entrée doit contenir au minimum :

- `category` : catégorie de technique ;
- `name` : nom technique ;
- `youtube` : URL YouTube ;
- `description` : résumé pédagogique.

Des champs optionnels comme `safety_note` ou `competition_note` peuvent être présents, mais ne sont pas affichés dans la version actuelle.

## Interface

L'interface doit rester légère, lisible et adaptée au mobile. En portrait, l'écran montre le titre, deux sélecteurs compacts, la description et la vidéo. En paysage, les sélecteurs et le titre sont masqués pour maximiser l'espace vidéo. Les contrôles doivent rester visibles, tactiles et utilisables sans déclencher inutilement le clavier mobile.

## Contraintes techniques

- Application Python basée sur Streamlit.
- Chargement local de `techniques.json`.
- Support des formats d'URL YouTube `watch`, `youtu.be` et `shorts`.
- Mise en page responsive via CSS intégré.
- Aucun backend externe requis hors YouTube.

## Critères d'acceptation

- L'application démarre avec `streamlit run prises_judo.py`.
- Une technique est toujours sélectionnée par défaut.
- Les changements de catégorie et de technique mettent à jour l'affichage et l'URL.
- En paysage mobile, la vidéo occupe tout l'écran et la navigation reste accessible.
- Le contrôle `python tests/mobile_layout_check.py` passe lorsque l'application est lancée.
