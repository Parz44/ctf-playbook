# CTFlearn

Øvingsoppgaver fra [CTFlearn](https://ctflearn.com/). Flaggene er sensurert.

| Oppgave | Kategori | Hovedteknikk |
| --- | --- | --- |
| [Forensics 101](#forensics-101) | Forensics | strings |
| [Taking LS](#taking-ls) | Forensics | Skjulte mapper |
| [exif](#exif-and-wow-so-meta) | Forensics | Metadata |
| [WOW...so meta](#exif-and-wow-so-meta) | Forensics | Metadata |
| [Binwalk](#binwalk) | Forensics | binwalk, foremost, OCR |
| [Git is Good](#git-is-good) | Forensics | Git-historikk |
| [Tux](#tux) | Forensics | Metadata, base64, carving |
| [Simple Steganography](#simple-steganography) | Forensics | steghide, hex |
| [PDF by fdpumyp](#pdf-by-fdpumyp) | Forensics | strings, base64 |
| [Character decode](#character-decode) | Kryptografi | Hex |
| [Base 2 2 the 6](#base-2-2-the-6) | Kryptografi | Base64 |
| [Morse code](#morse-code) | Kryptografi | Morse |
| [Reverse polarity](#reverse-polarity) | Kryptografi | Binær |
| [Rubber Duck](#rubber-duck) | Forensics | Åpen |

---

## Forensics 101

`exiftool` og `file` viste ingenting uvanlig. `strings` på bildet viste flagget på slutten av filen.

## Taking LS

Etter å ha pakket ut zip-filen viste `ls -la` inni mappen en skjult `.ThePassword`-mappe. Den hadde en tekstfil med passordet til PDF-en, og PDF-en hadde flagget.

## exif and WOW so meta

Begge hadde flagget i metadataene til bildet. `exiftool <fil>` var nok.

## Binwalk

```bash
binwalk Untitled.png          # viste zlib-data inni PNG-en
binwalk -e Untitled.png       # ga 29 og 29.zlib, begge uleselige
foremost 29.zlib              # hentet ut en PNG til output/png/
tesseract output/png/00000029.png flag
cat flag.txt
```

Lærdom: når binwalk gir noe uleselig, kjør foremost på resultatet.

## Git is Good

Den utpakkede mappen hadde en `flag.txt`, men den hadde feil flagg. `ls -la` viste en `.git`-mappe.

```bash
strings .git/* | grep flag     # viste at flagget fantes i historikken
git show HEAD                  # endringene i siste commit viste det riktige flagget
```

## Tux

`exiftool` viste en base64-kommentar som ble dekodet til et passord. Det tydet på et passordbeskyttet arkiv skjult i bildet.

```bash
foremost 973
```

Foremost hentet ut en zip, og passordet fra metadataene åpnet den.

## Simple Steganography

Etter standardsjekkene viste `hexyl` et lesbart ord inni hex-dataene. Det ordet var passordet til:

```bash
steghide extract -sf <fil>
```

## PDF by fdpumyp

`exiftool` og `file` viste ingenting. `strings` på PDF-en viste en base64-streng, som ble dekodet til flagget i CyberChef.

## Character decode

`41 42 43 54 46 7B ...` er hex. Dekodet til ASCII er det flagget.

## Base 2 2 the 6

En base64-streng. Dekodet direkte.

## Morse code

Prikker og streker, dekodet med en morseoversetter.

## Reverse polarity

En lang streng med 0 og 1. Delt opp i grupper på 8 bit og gjort om til ASCII.

## Rubber Duck

Status: åpen.
