#!/usr/bin/env python
# coding=utf-8
#
# hello.py
#
# Pierwszy program w Pythonie.
# W pierwszym wierszu mamy ścieżkę dostępu do interpretera.
# W drugim wierszu informacja o kodowaniu znaków w pliku.
# W Pythonie 3 domyślnie ustawione jest kodowanie UTF-8.
# Dzięki temu można w pliku stosować polskie znaki w napisach.
# Po znaku '#' mamy komentarz do końca wiersza.

print("Hello, world!")   # działa dla Pythona 2 i Pythona 3
# Ustawienie kodowania UTF-8.
# -*- coding: utf-8 -*-   # styl edytora Emacs
# coding: utf-8           # to wystarczy
# coding=utf-8            # to wystarczy
# Ustawienie kodowania ISO dla języka polskiego.
# -*- coding: iso-8859-2 -*-
# Ustawienie ścieżki do Pythona w środowisku wirtualnym i nie tylko.
#!/usr/bin/python       # NIE UWZGLĘDNIA ŚRODOWISKA!
#!/usr/bin/env python
#!/usr/bin/env python2
#!/usr/bin/env python3