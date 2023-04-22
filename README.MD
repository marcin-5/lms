# LMS - Learning Management System

## Algorytm implementacji funkcjonalności w Django:
1. Czy potrzebuje django app?
   - `python manage.py startapp <app label>`
   - Następnie dodać do settings.py -> INSTALLED_APPS
2. Czy potrzebuje dane?
   - Stworzyć modele w models.py (Django Models ORM)
   - Robię migracje: `python manage.py makemigrations <app label>`
   - Aplikuję zmianę scheme db `python manage.py migrate <app label>`
   - Piszę Unit tests
3. Czy potrzebuje zarządzać danymi z CMS (content management system, Django Admin)?
   - rejestruje modele w admin.py
4. Czy potrzebuje wprowadzania danych od użytkownika?
   - Django Forms, plik forms.py
5. Czy potrzebuje obsłużyć request?
   - Tworzę logikę w views.py za pomocą funkcji albo klasy
6. Czy potrzebuję html?
   - Django templates, tworze pliki html -> './templates/<app label>/<file>.html'
7. Czy potrzebuje router?
   - tworze lokalne urls.py, pamiętam o app_name i name do każdego endpoint
8. Podpinam lokalne urls.py do globalnych 'include'
9. Podpinam widok do menu w templatkach
10. Profit! Ide testować.
