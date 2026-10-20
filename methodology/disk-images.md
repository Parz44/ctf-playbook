# Diskbilder

## Fremgangsmåte

1. Finn ut hva slags bilde det er: `file <bilde>`. Rå `dd`, E01, VMDK/OVA, FAT16-bilde av en USB-pinne og så videre.
2. Se på partisjonene før noe annet.
3. List opp filer, også slettede.
4. Hent bare ut det som er relevant, og ta [filsjekkene](files-and-stego.md) på det.
5. På større bilder, bruk Autopsy til nøkkelordsøk, tidslinje og kommunikasjonsvisning.

Ta notater underveis. Hvert bilde er forskjellig, og notater skrevet mens du jobber er det du kan stole på senere.

## The Sleuth Kit

```bash
mmls disk.img                  # partisjonstabell, startsektor og størrelse
fls -r disk.img                # list filer rekursivt, slettede er merket med *
fls -o <offset> -r disk.img    # det samme, for en partisjon som starter på <offset>
icat disk.img <inode> > ut     # hent ut en fil med inode-nummer
```

Gjenopprette en slettet fil: `fls -r` viser den slettede filen og inode-nummeret, `icat` skriver den ut, og `exiftool` på resultatet kan vise metadata som hvem som laget den.

## E01-bilder

```bash
sudo apt-get install ewf-tools
mkdir rawimg
ewfmount image.e01 ./rawimg/
file rawimg/ewf1               # rådataene inni E01-filen
```

## Bilder av virtuelle maskiner (OVA/VMDK)

En OVA er et tar-arkiv med en `.ovf`-beskrivelse (XML) og en `.vmdk`-disk.

```bash
tar -xvf root.ova
qemu-img convert -O raw root-disk001.vmdk root-disk.img   # konverter ved behov
sudo losetup -Pf root-disk.img                            # koble til med partisjoner
sudo mount /dev/loop0p1 /mnt/vmdk
ls -la /mnt/vmdk
sudo chroot /mnt/vmdk          # et skall inne i det monterte systemet
```

Inne i systemet, sjekk hjemmemapper og root-mappen med `ls -la` for å finne skjulte filer.

## Ta bilde av en disk

```bash
dcfldd if=/dev/sdb1 hash=md5 of=/media/bevis.dd bs=512 noerror
```

`hash=md5` gir en hash som kan brukes til å kontrollere at bildet er uendret. `noerror` fortsetter ved lesefeil og fyller inn med nuller.

## Autopsy og FTK Imager

- Start enkelt. Se på partisjoner, skjulte partisjoner og hvor mye som ligger i ikke-allokert område.
- Gå gjennom brukere og mapper før du henter ut noe. Er dataene relevante for saken?
- Nøkkelordsøk etter flaggformatet finner ofte flagget raskt i CTF-er.
- Registerfiler som er verdt å hente ut: `NTUSER.DAT` (hva brukeren har gjort, nylig brukte filer) og `SAM` (brukerkontoer). Åpne dem i Registry Viewer, RegRipper eller FRED.
- Sjekk papirkurven og kommunikasjonsfanen.
- Arkiver med uvanlige filendelser kan skjule filer. Sjekk hva de egentlig er med `file`.
