# Filer og steganografi

## Fremgangsmåte

1. Ta [de første sjekkene](00-first-checks.md): `file`, `exiftool`, `strings`.
2. Gå gjennom metadatafeltene ett og ett. Flagg og base64-strenger gjemmer seg i felt som Comment, Licence, Creator og Author.
3. Se etter innebygde filer med `binwalk`, og pakk dem ut med `binwalk -e` eller `foremost`.
4. Hvis bildet ser normalt ut og ingenting er bygd inn, prøv LSB-verktøy: `zsteg` for PNG, `steghide` for JPEG og `stepic` for noen PNG-oppgaver.
5. Hvis resultatet er et bilde av tekst, bruk OCR i stedet for å lese det med øynene.

## Metadata

```bash
exiftool <fil>
exiftool -GPSLatitude -GPSLongitude -DateTimeOriginal -c "%.6f" -n <fil>   # GPS i desimalgrader
```

GPS-koordinater fra metadata kan slås opp på et kart for å finne ut hvor bildet ble tatt.

Endre metadata, for eksempel tidsstempler:

```bash
exiftool -AllDates="1970:01:01 00:00:00.001" \
  -SubSecCreateDate="1970:01:01 00:00:00.001" \
  -SubSecDateTimeOriginal="1970:01:01 00:00:00.001" \
  -SubSecModifyDate="1970:01:01 00:00:00.001" <fil>
```

## Innebygde filer og carving

```bash
binwalk <fil>                   # viser zlib, zip, png og lignende inni filen
binwalk -e <fil>                # pakker ut til _<fil>.extracted/
binwalk -M --dd=".*" <fil>      # rekursivt, pakk ut alt
foremost <fil>                  # gjenoppretter filer ut fra header og footer, legger dem i ./output/
```

Når `binwalk -e` gir uleselige rådata (som en `29.zlib`-fil), kjør `foremost` på resultatet. Det får ofte frem den egentlige filen.

## LSB og stego-verktøy

```bash
zsteg <fil.png>                        # viser skjult tekst og filer i LSB-lagene
steghide extract -sf <fil.jpg>         # spør om passord, prøv tomt først
stegseek <fil.jpg> <ordliste>          # brute force av steghide-passord, veldig raskt
stepic -d -i <fil.png> -o ut.txt       # dekoder data skjult med stepic
```

Hvis steghide spør om passord, se etter det i hex-dumpen, i metadataene eller i oppgaveteksten.

## OCR

```bash
tesseract <bilde> stdout       # skriv ut teksten i et bilde
tesseract <bilde> ut           # lagrer til ut.txt
```

Tesseract er ikke alltid nøyaktig. Hvis noen tegn ser feil ut, åpne bildet og les det selv (`xdg-open <bilde>`).

## Polyglot-filer

En polyglot er én fil som er gyldig i to formater, for eksempel en PDF som også er en PNG. Sjekk de første bytene i en hex-editor (HxD på Windows), og åpne så filen som hvert av formatene. Hvert format kan inneholde en del av flagget.

## Dokumenter

- `.docx`, `.xlsx`, `.apk` og lignende er zip-filer. Pakk dem ut og søk inni.
- `pdftotext <fil.pdf>` henter ut teksten i en PDF, også tekst som ligger under svarte bokser i et dårlig sensurert dokument.

## Reparere ødelagte filer

Hvis et bilde ikke vil åpne seg, kan filsignaturen være feil. Sammenlign de første bytene med en [liste over filsignaturer](https://en.wikipedia.org/wiki/List_of_file_signatures) og rett dem i `hexedit` eller GHex.
