Til a� keyra forrit �arf a� keyra skr�na mooshak.py
�etta er mini �tg�fa af mooshak og notast vi� Python 3

Til a� breyta hva�a port og IP serverinn er bundinn vi� �arf a� breyta app.run() � mooshak.py

Eins og verkefninu er skila� eru 5 skr��ir notendur � kerfinu. �eir eru geymdir � users.db sem er SQLite3 gagnagrunnur
User 1: admin, pass: admin		User 2: testuser1, pass: test	User 3: testuser2, pass: test
User 4: testuser3, pass test	User 5: hjalti, pass: mar

�a� eru 2 kl�ru� 'projects'  � kerfinu eins og �v� er skila� til a� s�na fram hvernig er gert projects � �v�.
�a� �arf a� sko�a projects subdirectory sem inniheldur undirm�ppur fyrir hvert project.
A�al skjali� fyrir hvert project er skr� sem heitir setup. �egar �a� er opna� �� er formati�:
Title--Description--Project URL--Users--Testcases
Fyrir hverja .cpp skr� sem er keyr� er gefi� a�ra skr� sem inniheldur textann sem � a� koma �t fr� forritinu til samanbur�ar.

Allar skr�r sem notendur uploada fara � folder sem heitir user_files
skjala structure �ar er:	user_files/username/project id/attempt number/
Ni�urst��ur fr� hverju attempt er sett � __results__ sem er ne�st � skjala structure user_files

�a� eru einungis gefin d�mi um hvernig notendur sko�a ni�urst��ur fyrir skilu� verkefni � admin notandanum.

�a� eru moderator accounts og venjulegir accounts. admin og hjalti eru skr��ir sem moderators og hafa a�gang a� /admin s��u
�ar sem �eir geta b�i� til accounts og uppf�rt projects og notendur � kerfinu sem �arf a� kalla � ef �a� er t.d. b�tt vi� e�a breytt projects

Kerfi� sam�ykkir eing�ngu .zip skr�r

// Meira...

TL;DR: python -m pip install -r pip-requirements.txt, keyra mooshak.py og opna https://127.0.0.1:5000