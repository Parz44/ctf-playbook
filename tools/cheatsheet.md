# Jukselapp for verktøy

Kommandoer jeg bruker ofte. Se [metodikk](../methodology/) for når de skal brukes.

## Filanalyse

| Kommando | Hva den gjør |
| --- | --- |
| `file <f>` | Faktisk filtype ut fra de første bytene |
| `exiftool <f>` | All metadata |
| `exiftool -GPSLatitude -GPSLongitude -DateTimeOriginal -c "%.6f" -n <f>` | GPS og tidspunkt for bildet i desimalgrader |
| `strings <f> \| grep -i flag` | Lesbar tekst som matcher |
| `hexyl <f>` / `xxd <f>` | Hex-visning |
| `binwalk <f>` / `binwalk -e <f>` | Finn / pakk ut innebygde filer |
| `foremost <f>` | Gjenopprett filer ut fra header og footer |
| `zsteg <f.png>` | LSB-data i PNG/BMP |
| `steghide extract -sf <f.jpg>` | Pakk ut steghide-data |
| `stegseek <f.jpg> <ordliste>` | Brute force av steghide-passord |
| `stepic -d -i <f.png> -o ut.txt` | Dekod stepic-data |
| `tesseract <bilde> stdout` | OCR |
| `pdftotext <f.pdf>` | Tekst ut av en PDF |

## Disk

| Kommando | Hva den gjør |
| --- | --- |
| `mmls <bilde>` | Partisjonstabell |
| `fls -r <bilde>` | List filer, også slettede |
| `icat <bilde> <inode> > ut` | Hent ut en fil med inode-nummer |
| `ewfmount <bilde.e01> <mappe>` | Monter en E01 |
| `dcfldd if=<kilde> hash=md5 of=<ut.dd> bs=512 noerror` | Ta bilde av en disk med hash |

## Minne (Volatility 2)

| Plugin | Hva den gjør |
| --- | --- |
| `imageinfo` | Foreslått profil |
| `pslist` / `pstree` / `psscan` | Prosesser |
| `connections` / `connscan` / `netscan` | Nettverk, aktive og lukkede tilkoblinger |
| `cmdline` / `cmdscan` / `consoles` | Kommandoer som ble kjørt |
| `hivelist` / `printkey -K "<nøkkel>"` | Registeret |
| `svcscan` | Tjenester |
| `malfind -p <pid>` | Injisert kode |

## Nettverk

| Filter | Hva det viser |
| --- | --- |
| `http.request` | HTTP-forespørsler |
| `tls.handshake.type == 1` | TLS Client Hello, viser servernavn |
| `ip.addr == <ip>` | Trafikk til eller fra én maskin |
| `tcp.port == <port>` | Én port |
| `tcp.flags.syn == 1 and tcp.flags.ack == 0` | Nye tilkoblinger |
| `frame contains "flag"` | Pakker som inneholder en streng |

## Web

| Kommando | Hva den gjør |
| --- | --- |
| `gobuster dir --url <url> -w <ordliste>` | Finn skjulte mapper |
| `hydra -l <bruker> -P <liste> <host> http-post-form "<sti>:<parametere>:F=<feiltekst>"` | Brute force av innlogging (bare i lab) |
| `nc <host> <port>` | Koble til en TCP-tjeneste |

## Reversing

| Kommando | Hva den gjør |
| --- | --- |
| `strings <program> \| less` | Hardkodet tekst |
| `ltrace -s 100 ./<program>` | Kall til biblioteksfunksjoner, som `strcmp` |
| `objdump -d -S <program>` | Disassembly |

## Koding

| Kommando | Hva den gjør |
| --- | --- |
| `echo '<s>' \| base64 -d` | Dekod base64 |
| `xxd -r -p` | Hex til bytes |
| `sha256sum <f>` / `md5sum <f>` | Hasher |

## Registerverktøy (Windows)

Registry Viewer, RegRipper og FRED for registerfilene `NTUSER.DAT`, `SAM`, `SYSTEM` og `SOFTWARE`.
