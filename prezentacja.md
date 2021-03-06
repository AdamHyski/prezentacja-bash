class: center, middle
![DataArt - Logo](./img/DataArt_Logo.png)
---
class: center, middle

# Konsola  
## głębsze spojrzenie
---
class: center, middle, dataart

## 720p
---
class: dataart
### O mnie

``` yaml
---
- Speaker:
    Name:     Adam Hyski
    Twitter:  @AdamHyski
    GitHub:   github.com/AdamHyski

```
--
Gdzie będzie prezentacja?:
- https://adamhyski.github.io/prezentacja-bash
- https://github.com/AdamHyski/prezentacja-bash

---
class: dataart
# Dlaczego wykład o CLI?
- spotkanie devops?
--

- dlaczego nie mówimy o docker albo aws?

---
class: dataart
# Co to jest CLI?

> CLI: Command-Line Interface


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
class: dataart
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
class: dataart
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
class: dataart
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
class: dataart
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
class: dataart
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
class: dataart
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
class: dataart
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
class: dataart
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
class: dataart
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
EOF # this is just for IDE ;)
```

--

- command <<< Here Strings
``` shell
cat <<< hello world
echo hello world | cat
```
---
class: dataart
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
class: dataart
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
class: dataart
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
MY_EXT_IP=$(curl ipinfo.io/ip)
MY_EXT_IP=`curl ipinfo.io/ip` # deprecated
```

---
class: dataart
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
class: dataart
### Co funkcja zwraca?
``` shell
echo test
test
echo $?
0
```
--
``` shell
rm tmp/*
zsh: lista argumentów za długa: rm
echo $?
127
```
--
``` shell
grep 'tego tam nie ma' /etc/passwd

echo $?
1
```
--

``` shell
exit 127

show_error() {
...
return 10
}
```
---
class: dataart
# Łączenie komend
``` shell
echo hello ; echo world
hello
world
echo hello && echo world
hello
world
echo hello || echo world
hello
```
--
``` shell
[ ! -f running.flag ] && run_script
[ -f running.flag ] || run_script
```
--
``` shell
[ -z $EMPTY_VAR] && run_script
[ -n $NOT_EMPTY_VAR] && run_script
```
---
class: dataart
# Skróty klawiszowe
``` shell
clear
```

`Ctrl` + `l`

--
### koniec STDIN:
``` shell
exit
```

`Ctrl` + `d`
--

### przeszukiwanie historii:
`Ctrl` + `r`
---
class: dataart
# Więcej skrótów
`Atl` + `.` Powtarza ostatni argument z poprzedniej komendy
--

### skakanie po słowach:
.center[![Skakanie](./img/console.jpeg)]

---
class: center, middle

# Find

---
class: dataart
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
class: dataart
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
class: dataart
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
class: dataart
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
class: dataart
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
class: dataart
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

# Pytania?
---
class: center, middle

# Dziękuję
---
class: center, middle
![DataArt - Logo](./img/DataArt_Logo.png)
