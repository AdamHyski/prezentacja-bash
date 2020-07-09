
class: center, middle

# Konsola  
## głębsze spojrzenie
---
class: center, middle

## 720p
---
.left-column[

### O mnie
]
.right-column[

``` yaml
---
- Speaker:
    Name:     Adam Hyski
    Twitter:  @AdamHyski
    Page:     https://hyski.pl
    Mail:     adam@hyski.pl
    GitHub:   github.com/AdamHyski

```
Gdzie będzie prezentacja?:
- https://github.com/AdamHyski/prezentacja-bash
- [to też ]

]
---

# Dlaczego wykład o CLI?
- spotkanie devops?
--

- dlaczego nie mówimy o docker albo aws?

---
# Co to jest CLI?
```
CLI: Command-Line Interface
```

- konsole
  - SH,
  - BASH,
  - ASH,
  - ZSH,
  - CSH,
  - KSH,
  - ect…
--

- inne konsole
  - node
  - php -a
  - python
  - i wiele innych
---
# Przykład
``` shell
rm *
```
--

- Co może pójść nie tak?

--
- skąd CLI wie czym jest `rm` ?

--
- czym jest `*` dla rm ?

--
- czym jest `*`?

--
- co jest argumentem?  i jak to sprawdzić ?

--
- co jeszcze może pójść nie tak?

---
## Czym jest rm?
#### Gdzie jest?
``` shell
whereis rm
rm: /bin/rm /usr/share/man/man1/rm.1.gz
```
#### Skąd wie że ma tam szukać?
``` shell
echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
```
> W momencie wydania przez użytkownika dowolnego polecenia, system przeszukuje ścieżki po każdym elemencie po kolei (w kierunku od lewej do prawej), szukając nazwy pliku, który pasuje do nazwy wydanego polecenia.
> © wikipedia


---
## Co może pójść nie tak?

``` shell
rm tmp/*
bash: /bin/rm: Lista argumentów za długa
```
--
### To ile może być argumentów?
``` shell
getconf ARG_MAX
2097152
```


---

class: center, middle
![But how - meme](./img/But-how--meme-49242.jpg)

---

## Co jest argumentem?
--

### Ale najpierw czym jest BASH?
> Bash is an sh-compatible command language interpreter that executes commands read from the standard input or from a file. Bash also incorporates useful features from the Korn and C shells (ksh and csh).

--

### Co jest argumentem?  Jak to sprawdzić?


``` shell
echo rm *
```

???
Tu  jak ktoś używa chwilę konsol powinien się natychmiast lekko skrzywić

---
###  Jak to posprzątać?
Wiemy że to nie działa
``` shell
rm tmp/*
bash: /bin/rm: Lista argumentów za długa
```
--
Można tak
``` shell
find tmp -print0 | xargs -0 rm
rm: nie można usunąć 'tmp': Jest katalogiem
ls -a tmp
.  ..
```
--
Można i tak

``` shell
find tmp -type f -exec rm {} \;
```

--
Elegancka metoda

``` shell
find tmp -type f -delete
```
---
class: center, middle

# Wróćmy do teorii


???
Zanim jednak find to chwilę na pipe
---
# Procesy

.center[![Proces: wyjścia i wejście](./img/Process.png)]
--
Procesy można łączyć ze sobą

.center[![Proces: wyjścia i wejście](./img/Cowsey.png)]
``` bash
fortune | cowsay
 _________________________________
/ You are taking yourself far too \
\ seriously.                      /
 ---------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

```
---
# Przekierowania
``` shell
date > log
cat log
śro, 8 lip 2020, 18:06:54 CEST
date > log
cat log
śro, 8 lip 2020, 18:07:09 CEST
```
--
``` shell
date >> log
cat log
śro, 8 lip 2020, 18:07:09 CEST
śro, 8 lip 2020, 18:09:07 CEST

```
---
# STDERR

``` shell
echo foo >> /dev/stderr
```
``` shell
echoerr() { echo "$@" 1>&2; }
echoerr error world
error world
```
--
``` shell
echoerr error world 1>log
error world
wc log
0 0 0 log
du log
0       log
```
- `wc` counts the number of bytes, characters, whitespace-separated words, and newlines in each given file,
- `du` disk usage

---
# STDIN
- command < file
``` shell
mysql company_db < dump.sql
cat dump.sql | mysql company_db
pv dump.sql | mysql company_db
```
--
- command << here-document
``` shell
cat <<EOF >lorem
> lorem iopsum
> sit ammen
> EOF
cat lorem
lorem iopsum
sit ammen
# this is just for IDE ;)
EOF
```

--

- command <<< Here Strings
``` shell
cat <<< hello world
echo hello world | cat
```
---
# xargs
### Jak połączyć ze sobą jeżeli jedna z komend spodziewa się argumentu a dostaje STDIN?
--

``` shell
cut -d: -f1 < /etc/passwd | sort | xargs echo
cut -d: -f1 /etc/passwd | sort | xargs echo
```
???
jeżeli nie  będzie ostatniego `|`  to użytkownicy będą w nowych liniach
---
class: center, middle

# Skrypty

---
# Podstawy
##  #! (Hash-Bang) - Interpreter
``` shell
#!/bin/bash
```
--
``` shell
#/usr/bin/python3
```
--
``` shell
#!/usr/bin/env python3
```
---
# ZMIENNE
``` bash
SOME_VAR="some value"  # Nie ma tu spacji !

echo $SOME_VAR
echo "Możemy ją użyć tak $SOME_VAR"
echo "albo tak ${SOME_VAR}"
echo 'Tak jej nie użyjemy ${SOME_VAR} $SOME_VAR'
cat << EOD
> tak też zadziała:
> $SOME_VAR
> tu jakiś kontekst
> EOD
EOD # For IDE ;)
cat <<< $SOME_VAR
```
--
``` bash
MY_EXT_VAR=$(curl ipinfo.io/ip)
MY_EXT_VAR=`curl ipinfo.io/ip`
```

---
# Funkcje
### Definicja
``` bash
show_error() {
textred=$(tput setaf 1)
colorreset=$(tput sgr0)
ERROR_MSG="$@"
  cat << EOF
${textred}
###
#  ${ERROR_MSG}
###${colorreset}
EOF
}
```

---
### Co funkcja zwraca?
``` shell
echo test
test
echo $?
0
```

---
# Skróty klawiszowe
``` shell
clear
```

`Ctrl` + `L`

--
## koniec STDIN
``` shell
exit
```

`Ctrl` + `D`

--

---

class: center, middle

# Find

---
## Wróćmy do find
### podstawy

``` shell
find /etc -name '*.conf'
find /etc -iname 'nginx.conf'
find /etc -name '*.d' -type d
find /etc -not -name '*.conf'
```
--
`-not` == `!`
`-iname` case-insensitive
---
## Szukanie po typie
### Pliki:
``` shell
find . -type f
```
--
### Katalogi:
``` shell
find . -type d
```
--
### Linki:
``` shell
find . -type l
```
---
## Szukanie po właścicielu
### User
- `-user` szuka po nazwie usera (ew. po id)
- `-uid` szuka po id usera

``` shell
find /etc -name '*.conf' -user root
find /etc -name '*.conf' -user 1000
find /etc -uid 1000  
find /etc -not -user 0  2>/dev/null

```
--
### Group
- `-group` szuka po nazwie grupy (ew. po id)
- `-gid` szuka po id grupy

``` shell
find /var/log  -group adm
find /var/log  -group 4
find /var/log -gid 4  
find /var/log -not -uid 0  2>/dev/null
```
---
# Szukanie po rozmiarze
- `-empty` szuka pustych plików

--

### Mniej niż:
``` shell
find .  -size -4k
```
--

### Więcej niż:
``` shell
find .  -size +100M
```

---
# Szukanie po czasie  
### Zmieniony w ciągu ostatnich 15 minut:
``` shell
find . -mmin -15
```
--

### Nie zmieniony w ciągu ostatnich 90 dni:
``` shell
find . -mtime +90
```
--

### starszy niż plik
``` shells
find . -newer index.php
```

---
# Szukanie - wykonywanie komend

- `-exec` wykonuje komendę na wyniku wyszukiwania

``` shell
find . -name  '*.sh' -exec chmod +x {} \;
```
--

### pipe

``` shell
find . -name  '*.sh' -print0 | xargs -0 chmod +x
```
należy uważać z nazwami plików zawierającymi znaki specjalne jaki i spacje



---
class: center, middle

# Dziękuję
