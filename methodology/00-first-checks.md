# Første sjekker

Lærdommen jeg stadig må lære på nytt: ta alltid standardsjekkene før noe annet. De fleste lette og middels vanskelige forensics-oppgaver løses med en av disse.

## 1. Les oppgaven

- Hvilket format har flagget? (`picoCTF{...}`, `DDC{...}`, `flag{...}`)
- Hinter tittelen eller beskrivelsen om en teknikk? «Blast from the past» pekte mot tidsstempler, «Polyglot» mot en fil som er to formater samtidig.
- Jobb på en kopi av filen, aldri originalen: `cp original.jpg original_v2.jpg`

## 2. Finn ut hva filen er

```bash
file <fil>           # hva filen egentlig er, uansett filendelse
exiftool <fil>       # metadata: forfatter, kommentarer, GPS, tidsstempler, rare felt
strings <fil>        # lesbar tekst, ofte flagget eller en base64-streng
strings <fil> | grep -i flag
```

Hvis `file` og filendelsen ikke stemmer overens, åpne filen i en hex-editor og se på de første bytene (magic bytes). En PDF som starter med en PNG-header er en polyglot.

## 3. Se etter skjulte data

```bash
binwalk <fil>        # innebygde filer eller komprimerte data
binwalk -e <fil>     # pakk dem ut
foremost <fil>       # gjenopprett filer ut fra header og footer
zsteg <fil>          # data i minst signifikante bit (LSB) i PNG/BMP
hexyl <fil>          # hex-visning i farger, fin for å oppdage tekst og passord
```

## 4. Søk direkte etter flaggformatet

```bash
grep -r --text 'picoCTF{.*}' .
grep -rl 'picoCTF' big-zip-files/     # hvilken fil som inneholder det
```

## 5. Se etter skjulte filer

```bash
ls -la               # filer som starter med punktum, som .hint.txt eller .ThePassword/
ls -laR | grep flag -B 20
```

## 6. Dekod det du finner

Det som slutter på `=` eller `==` er sannsynligvis base64. Lange strenger med bare 0-9 og a-f er hex. Se [koding og krypto](encoding-and-crypto.md). «Magic» i CyberChef er en god første gjetning.

## 7. Når ingenting virker

- Skriv ned hva du har prøvd. Det sparer tid når du kommer tilbake.
- Les oppgaveteksten på nytt og se etter hint du hoppet over.
- Prøv neste type verktøy: hvis metadata ikke ga noe, prøv carving. Hvis carving ikke ga noe, prøv stego-verktøy.
