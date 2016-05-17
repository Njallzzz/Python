Til að keyra forrit þarf að keyra skrána mooshak.py
Þetta er mini útgáfa af mooshak og notast við Python 3

Til að breyta hvaða port og IP serverinn er bundinn við þarf að breyta app.run() í mooshak.py

Eins og verkefninu er skilað eru 5 skráðir notendur í kerfinu. Þeir eru geymdir í users.db sem er SQLite3 gagnagrunnur
User 1: admin, pass: admin		User 2: testuser1, pass: test	User 3: testuser2, pass: test
User 4: testuser3, pass test	User 5: hjalti, pass: mar

Það eru 2 kláruð 'projects'  í kerfinu eins og því er skilað til að sýna fram hvernig er gert projects í því.
Það þarf að skoða projects subdirectory sem inniheldur undirmöppur fyrir hvert project.
Aðal skjalið fyrir hvert project er skrá sem heitir setup. Þegar það er opnað þá er formatið:
Title--Description--Project URL--Users--Testcases
Fyrir hverja .cpp skrá sem er keyrð er gefið aðra skrá sem inniheldur textann sem á að koma út frá forritinu til samanburðar.

Allar skrár sem notendur uploada fara í folder sem heitir user_files
skjala structure þar er:	user_files/username/project id/attempt number/
Niðurstöður frá hverju attempt er sett í __results__ sem er neðst í skjala structure user_files

Það eru einungis gefin dæmi um hvernig notendur skoða niðurstöður fyrir skiluð verkefni á admin notandanum.

Það eru moderator accounts og venjulegir accounts. admin og hjalti eru skráðir sem moderators og hafa aðgang að /admin síðu
Þar sem þeir geta búið til accounts og uppfært projects og notendur í kerfinu sem þarf að kalla á ef það er t.d. bætt við eða breytt projects

Kerfið samþykkir eingöngu .zip skrár

// Meira...

TL;DR: python -m pip install -r pip-requirements.txt, keyra mooshak.py og opna https://127.0.0.1:5000