# Cyberlandslaget CTF 2025

Jeopardy-CTF med et virtuelt lab-miljø fra Campfire Security. Flaggformat `DDC{...}`. Flaggene er sensurert.

| Oppgave | Kategori | Status |
| --- | --- | --- |
| [Straba](#straba) | Forensics, nettverk | Løst |
| [Efterforskningen](#efterforskningen) | Forensics, disk | Løst |
| [outXORcing](#outxorcing) | Reversing, krypto | Løst |
| [The professor's Lost Note](#the-professors-lost-note) | Forensics | Løst |
| [Shutter Trace](#shutter-trace) | Forensics, OSINT | Løst |
| [Hasher is back](#hasher-is-back) | Krypto | Løst |
| [Masahiro Hara](#masahiro-hara) | Forensics | Åpen |
| [fde-bootloader](#fde-bootloader) | Forensics, minne | Åpen |
| Leaky Store | Web | Ikke startet |

---

## Straba

En pcap full av ICMP-pakker. Flagget lå sannsynligvis i innholdet, men de fleste pakkene så like ut.

Da jeg gikk gjennom dem, hadde pakke 34 en annen IP-header: ECN-feltet var satt til `01` (ECN-Capable Transport). Innholdet var base64 og ble dekodet til `PART_2:...:PARTEND`. Et søk etter samme ECN-verdi fant tre pakker til med del 1, 3 og 4. Satt sammen i riktig rekkefølge ga de flagget.

```
ip.dsfield.ecn == 1
```

Lærdom: når pakkene ser like ut, sammenlign feltene i headeren. Den som skiller seg ut, er den interessante.

## Efterforskningen

En `.img`-fil. Åpnet den i Autopsy og gjorde et nøkkelordsøk etter `DDC`. Flagget kom raskt opp.

## outXORcing

Oppgavefilen var et program som het `access-control`.

```bash
file access-control                  # 64-bits PIE, dynamisk lenket, med debug-informasjon
strings access-control | less        # interessant: enc_password og et navn
objdump -d -S access-control | grep -A 20 -B 10 <adressen til sjekkefunksjonen>
```

Disassembleringen viste at input ble sammenlignet med en kryptert byte-liste. Navnet fra `strings` var nøkkelen. XOR av listen med nøkkelen ga nesten hele flagget. Det siste tegnet var kuttet av, men resten av flagget gjorde det lett å gjette. Skript: [xor.py](../scripts/xor.py).

## The professor's Lost Note

```bash
ls -la Professor_Notes      # viste en skjult .hint.txt
cat Professor_Notes/.hint.txt
```

## Shutter Trace

```bash
ls -la Clue_Folder                 # skjult hintfil
cat Clue_Folder/<skjult fil>       # en base64-streng
echo '<streng>' | base64 --decode  # «The photo is hidden in the Evidence Folder as a jpg file»
ls -la Evidence_Folder/*.jpg
exiftool Evidence_Folder/<bilde>.jpg
```

Creator-feltet i metadataene var flagget.

## Hasher is back

Oppgaven ga en MD5-hash av innholdet i flagget. Et MD5-oppslag på nett fant det opprinnelige ordet, som ble satt inn i flaggformatet.

Lærdom: MD5 av et vanlig ord er ingen hemmelighet. Oppslagstabeller finner det på sekunder.

## Masahiro Hara

Status: åpen.

Oppgavefilen var `flag.png`. Ingen nyttige metadata. `binwalk flag.png` viste zlib-data inni PNG-en. Jeg fant ikke flagget.

Neste steg: Masahiro Hara fant opp QR-koden, så bildet kan være en ødelagt eller delvis QR-kode. Prøv `zsteg`, sjekk PNG-blokkene med `pngcheck -v`, og se om zlib-dataene kan pakkes ut til QR-moduler.

## fde-bootloader

Status: åpen.

Oppgaven hadde tre filer:

- `mem.dump`: en minnedump, kan inneholde prosessminne eller nøkler
- `hda.img`: et diskbilde, kanskje kryptert
- `run-qemu.sh`: et skript for å starte disken i QEMU

Jeg begynte med minnedumpen, men kom ikke lenger. Navnet tyder på full diskkryptering, så den sannsynlige veien er å finne krypteringsnøkkelen i minnet og bruke den til å låse opp diskbildet.
