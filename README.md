# prises-judo

Application Streamlit mobile-first qui liste des techniques de judo par catégorie. Lorsqu'une prise est sélectionnée, l'application affiche une description rapide et une vidéo YouTube.

### Comment l'utiliser

1. Installez les dépendances

   ```bash
   pip install -r requirements.txt
   ```

2. Lancez l'application

   ```bash
   streamlit run prises_judo.py
   ```

3. En haut de la page, choisissez une catégorie puis une prise.

4. La page montre une description de la technique et intègre la vidéo YouTube.

### Vérification mobile

Lancez l'application, puis exécutez le contrôle Playwright :

```bash
python tests/mobile_layout_check.py
```
