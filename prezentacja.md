
class: center, middle

# Konsola  
## głębsze spojrzenie
---
class: center, middle

720p
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
``` shell
whereis rm
rm: /bin/rm /usr/share/man/man1/rm.1.gz
```

]

---
### `rm *`

.left-column[
### Czym jest rm?
### Co może pójść nie tak?

]
.right-column[
sprawdźmy to


]

---
### `rm *`

.left-column[
### Czym jest rm?
### Co może pójść nie tak?
### Co jest argumentem?

]
.right-column[
sprawdźmy to


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
sprawdźmy to


]

---
``` shell
echo rm *
```
???
Tu  jak ktoś używa chwilę konsol powinien się natychmiast lekko skrzywić
--
---

class: center, middle

# Dziękuję
