# Linux for CTF-er

## Finne ting

```bash
find / -iname "uber-secret.txt" 2>/dev/null     # søk etter navn, skjul feilmeldinger om tilgang
grep -rl 'picoCTF' .                             # hvilke filer som inneholder en streng
grep -r --text 'picoCTF{.*}' .                   # skriv ut treffet, også i binærfiler
ls -la                                           # ta med skjulte filer
ls -R | grep flag -B 20                          # hvor i mappetreet en fil ligger
strings * | grep flag
```

## Klippe tekst ut av filer

Et flagg spredt over mange `<tspan>`-elementer i en SVG, ett tegn i hver:

```bash
cat drawing.svg | grep "tspan" | cut -d ">" -f2 | cut -d "<" -f1 | tr -d '\n'
```

- `cut -d ">" -f2` beholder det som kommer etter første `>`
- `cut -d "<" -f1` beholder det som kommer før neste `<`
- `tr -d '\n'` setter tegnene sammen til én linje

## Små skript

```bash
nano get_flag.sh        # første linje: #!/bin/bash
chmod +x get_flag.sh
./get_flag.sh
```

## Arkiver

```bash
unzip fil.zip
gunzip fil.gz
tar -xvf fil.tar
tar -xvjf fil.tbz2 -C ~/ctf/            # x pakk ut, v vis fremdrift, j bzip2, f fil, C målmappe
```

## Git-repoer i oppgaver

En `.git`-mappe betyr at det finnes historikk. Filene slik de er nå har kanskje ikke flagget, men en tidligere commit kan ha det.

```bash
git log
git show HEAD          # siste commit med endringene
git show <commit>
```

## Koble til oppgaver

```bash
nc <host> <port>
ssh ctf-player@<host> -p <port>
```

## Navigere

```bash
cd          # hjemmemappen
cd ..       # opp ett nivå
cd -        # forrige mappe
pwd         # hvor er jeg
```
