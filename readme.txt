Shromazdiste ruznych skriptu co demonstruji principy probirane na IAP u Kyncla

Postupne jak se budu pripravovat na zkousku sem budu hazet vsechno co budu zkouset. Kdyz najdu cas tak to bude mit i nejakou stabni kulturu ale slibit to nedovedu

Release note Python
https://www.python.org/downloads/release/python-380/
A instalacka:
https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe

Pri instalaci nedoporucuju instalovat do defaultniho umisteni
a pro aktualniho uzivatele. Nainstalujte pro vsechny uzivatele
defalntne umisteno v C:\Program Files\Python38
Nezapomente zaskrtnout nasledujici:
    # Add Python to PATH
    # Install for all users
    # Enable long path in windows registry
Nazvy davam dohromady jen koncepcne co to dela. If in doubt UTFG.

Doporuceny editor pro zacatek:
https://notepad-plus-plus.org/downloads/v7.8.2/
Jednoduche a funguje to.
Az nainstalujete, zaskrtnout v Nastaveni/Volby/Syntaxe tab zamenit
za 4 mezery(Python coding standard).
NOTE: pokud mate zdrojaky co maji odsazeni udelane znaky TAB tak to pobezi taky
Ale dodrbe se to v prvni moment kdy narazite na nekoho kdo dodrzuje coding standard.
Tak ho pouzivejte taky.

Vyvojove prostredi Eclipse:
https://www.eclipse.org/downloads/
Doporucuju edici pro C/C++, teda pokud nemate ambice uzit Java.
Pokud se teda Java da kvalifikovat jako programovaci jazyk.
Bohuzel pro beh eclipsu potrebujete java runtime environment.
Predpokladam ze jste ho nekdy na neco uz potrebovali tak bud vite jak
nainstalovat nebo vygoogllite.

V kazdem pripade budete potrebovat doplnek PyDev:
https://www.pydev.org/manual_101_install.html
Poradne proctete, je tam step-by-step navod jak na to.

Instalace pythonovskych balicku:

1) spustit pod adminem konzoli(cmd)
2) prepnout se do slozky s projektem
3) copy-paste-enter nasledujici command

pip install -r requirements.txt --upgrade