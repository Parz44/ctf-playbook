# picoCTF (picoGym)

Øvingsoppgaver fra [picoCTF](https://picoctf.org/). Flaggene er sensurert.

| Oppgave | Kategori | Vanskelighet | Hovedteknikk |
| --- | --- | --- | --- |
| [Verify](#verify) | Forensics | Lett | SHA256-sammenligning |
| [Secret of the Polyglot](#secret-of-the-polyglot) | Forensics | Lett | Polyglot PDF/PNG |
| [CanYouSee](#canyousee) | Forensics | Lett | Metadata, base64 |
| [Scan Surprise](#scan-surprise) | Forensics | Lett | QR-kode |
| [information](#information) | Forensics | Lett | Metadata, base64 |
| [Glory of the Garden](#glory-of-the-garden) | Forensics | Lett | Søk i hex-editor |
| [interencdec](#interencdec) | Kryptografi | Lett | Base64 i flere lag, Cæsar |
| [First Find](#first-find) | General skills | Lett | find |
| [Big Zip](#big-zip) | General skills | Lett | grep -r |
| [Magikarp Ground Mission](#magikarp-ground-mission) | General skills | Lett | Navigering i Linux |
| [WebDecode](#webdecode) | Web | Lett | Kildekode, base64 |
| [PW Crack 1](#pw-crack-1) | General skills | Lett | Lese et Python-skript |
| [PW Crack 2](#pw-crack-2) | General skills | Lett | Hex-kodet passord |
| [Mob psycho](#mob-psycho) | Forensics | Middels | Pakke ut APK, hex |
| [PcapPoisoning](#pcappoisoning) | Forensics | Middels | Søk i Wireshark |
| [hideme](#hideme) | Forensics | Middels | zsteg, foremost |
| [St3g0](#st3g0) | Forensics | Middels | zsteg |
| [Lookey here](#lookey-here) | Forensics | Middels | grep |
| [Redaction gone wrong](#redaction-gone-wrong) | Forensics | Middels | pdftotext |
| [flags are stepic](#flags-are-stepic) | Forensics | Middels | stepic |
| [Enhance!](#enhance) | Forensics | Middels | Klippe tekst ut av SVG |
| [Sleuthkit Intro](#sleuthkit-intro) | Forensics | Middels | mmls |
| [RED](#red) | Forensics | Middels | zsteg, base64 |
| [FindAndOpen](#findandopen) | Forensics | Middels | pcap, zip-passord |
| [Blast from the past](#blast-from-the-past) | Forensics | Middels | Endre tidsstempler (åpen) |

---

## Verify

Oppgaven var å finne den ene filen i `files/` som hadde samme SHA256 som `checksum.txt`, og dekryptere den med `decrypt.sh`.

```bash
sha256sum files/* | grep "$(cat checksum.txt)"
```

Dette regner ut hashen til alle filene og beholder bare linjen som matcher.

## Secret of the Polyglot

Filen hadde endelsen `.pdf`. I HxD viste headeren at den også var en gyldig PNG. Åpnet som PDF viste den andre halvdel av flagget, og åpnet som PNG viste den første halvdel. Sammen: `picoCTF{REDACTED}`.

## CanYouSee

En zip med ett bilde. Ingenting synlig i selve bildet, men `exiftool` viste en base64-streng i et URL-felt. Dekodet ga den flagget.

## Scan Surprise

Bildet var en QR-kode. Skanning ga flagget direkte.

## information

`exiftool cat.jpg` viste en base64-streng i Licence-feltet. Dekodet var det flagget.

## Glory of the Garden

Åpnet `garden.jpg` i en hex-editor og søkte etter `CTF`. Flagget lå etter bildedataene, helt på slutten av filen. `strings garden.jpg | tail` viser det samme.

## interencdec

Teksten så ut som base64. Første dekoding ga en Python bytes-streng med en ny base64-streng inni. Dekoding av den ga `wpjvJAM{...}`, som har formen til et flagg med forskjøvne bokstaver. En Cæsar-forskyvning til starten ble `picoCTF` ga flagget.

Lærdom: når en dekoding gir noe som fortsatt ser kodet ut, fortsett.

## First Find

```bash
find / -iname "uber-secret.txt" 2>/dev/null
cat <sti>
```

## Big Zip

```bash
grep -rl 'picoCTF' big-zip-files/
```

Dette viser bare filen som inneholder flagget.

## Magikarp Ground Mission

Koblet til oppgavemaskinen med SSH og flyttet meg mellom mapper for å samle tre deler av flagget, med `cd`, `cd ..`, `cd -`, `pwd` og `ls`.

## WebDecode

Så på kildekoden til siden. Om oss-siden hadde et attributt med en base64-streng. Dekodet var det flagget.

## PW Crack 1

Lastet ned sjekkeskriptet og det krypterte flagget med `wget`. Skriptet hadde passordet i klartekst. Ved å kjøre skriptet med det passordet ble flagget dekryptert.

## PW Crack 2

Samme oppsett, men passordet i skriptet var skrevet som hex-koder. Dekoding av hex ga passordet.

## Mob psycho

Filen var en APK, som er en zip.

```bash
unzip mobpsycho.apk -d apk
cd apk
strings * | grep flag                 # pekte mot res/color/flag.txt
ls -R | grep flag -B 20               # bekreftet stien
cat res/color/flag.txt | xxd -r -p    # innholdet var hex
```

## PcapPoisoning

Lastet opptaket inn i Wireshark og søkte i pakkeinnholdet etter `flag`. Flagget lå i innholdet til en TCP-pakke.

## hideme

```bash
file flag.png        # ingenting uvanlig
zsteg flag.png       # viste et arkiv skjult i bildet
foremost flag.png    # hentet ut en zip til output/zip/
unzip output/zip/00000007.zip
```

Zip-filen hadde en `secret/`-mappe med en ny PNG. `tesseract` klarte ikke å lese den sikkert, så jeg åpnet bildet og leste flagget selv.

## St3g0

`file` og `exiftool` viste ingenting. `zsteg pico.flag.png` skrev ut flagget med en gang.

## Lookey here

En stor tekstfil.

```bash
grep pico anthem.flag.txt
```

## Redaction gone wrong

PDF-en hadde svarte bokser over teksten, men teksten lå fortsatt i filen.

```bash
pdftotext fil.pdf
grep pico fil.txt
```

## flags are stepic

Siden viste mange flagg, og ett av landene fantes ikke (Upanzi). `exiftool` på det bildet viste ingenting. Navnet på oppgaven pekte mot verktøyet `stepic`.

```bash
stepic -d -i upanzi.png -o flag.txt
cat flag.txt
```

## Enhance!

`file` viste en SVG. `cat` viste enkelttegn inni `<tspan>`-elementer som til sammen så ut som et flagg.

```bash
cat drawing.flag.svg | grep "tspan" | cut -d ">" -f2 | cut -d "<" -f1 | tr -d '\n'
```

Jeg lagret dette som et lite bash-skript så det kunne kjøres igjen.

## Sleuthkit Intro

```bash
gunzip disk.img.gz
mmls disk.img
nc <host> <port>     # spurte etter størrelsen på Linux-partisjonen
```

Svaret med partisjonslengden fra `mmls` ga flagget.

## RED

`zsteg red.png` viste en base64-streng som gjentok seg i LSB-dataene. Dekodet i CyberChef ga den flagget.

## FindAndOpen

En zip og en pcap. Oppgaven hintet om at nøkkelen lå i opptaket. I Wireshark fant jeg en base64-streng som ble dekodet til første del av flagget, som også var passordet til zip-filen. Filen i zip-en hadde hele flagget.

## Blast from the past

Status: notatene er ufullstendige, må tas opp igjen.

Oppgaven går ut på å endre alle tidsstemplene i et bilde til en gitt verdi og sende det inn. Fremgangsmåten så langt:

```bash
cp original.jpg original_v2.jpg
exiftool -AllDates="1970:01:01 00:00:00.001" \
  -SubSecCreateDate="1970:01:01 00:00:00.001" \
  -SubSecDateTimeOriginal="1970:01:01 00:00:00.001" \
  -SubSecModifyDate="1970:01:01 00:00:00.001" original_v2.jpg
```

Neste steg: finn ut hvilket tidsstempel sjekkeren fortsatt avviser. Noen leverandørspesifikke felt dekkes ikke av `-AllDates` og må kanskje endres i en hex-editor.
