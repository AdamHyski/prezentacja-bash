
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
### `rm *`

.left-column[
### Czym jest rm?

]
.right-column[
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

]

---
### `rm *`

.left-column[
### Czym jest rm?
### Co może pójść nie tak?

]
.right-column[
#### sprawdźmy to
``` shell
rm tmp/*
bash: /bin/rm: Lista argumentów za długa
```

``` shell
getconf ARG_MAX
```


]
---

class: center, middle
![But how - meme](./img/But-how--meme-49242.jpg)

---
### `rm *`

.left-column[
### Czym jest rm?
### Co może pójść nie tak?
### Co jest argumentem?

]
.right-column[
pogadać o bash
#TODO

]

---
### `rm *`

.left-column[
### Czym jest rm?
### Co może pójść nie tak?
### Co jest argumentem?
### Jak to sprawdzić?

]
.right-column[
# TODO

``` shell
echo rm *
```


]
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
find tmp -print0 | xargs -0
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

class: center, middle

# Dziękuję
