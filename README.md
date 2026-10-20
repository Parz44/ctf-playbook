# CTF- og DFIR-playbook

Notater, metodikk og løsninger fra CTF-oppgaver og lab-øvelser i digital etterforskning.

Jeg har en bachelorgrad i digital etterforskning (Digital Forensics) fra Noroff (2026). Her samler jeg hvordan jeg faktisk løser oppgaver: hva jeg sjekker først, hvilke verktøy jeg bruker, hva som fungerte og hva som ikke gjorde det. Repoet vokser etter hvert som jeg løser flere oppgaver.

Skoleprosjekter og lab-øvelser fra studiet ligger i [studieprosjekter-dfir](https://github.com/Parz44/studieprosjekter-dfir).

## Innhold

| Mappe | Hva som ligger der |
| --- | --- |
| [methodology](methodology/) | Fremgangsmåte for hver type oppgave. Start med [første sjekker](methodology/00-first-checks.md). |
| [writeups](writeups/) | Løste oppgaver, sortert etter plattform eller arrangement. Flaggene er sensurert. |
| [case-studies](case-studies/) | Lengre etterforskninger, som minneanalyse av en Zeus-infeksjon. |
| [tools](tools/cheatsheet.md) | Kommandoer jeg bruker ofte, med forklaring av hva hvert flagg gjør. |
| [scripts](scripts/) | Små Python- og shell-verktøy jeg har skrevet underveis. |
| [resources](resources.md) | Øvingsplattformer, oppslagsverk og verktøylister. |
| [templates](templates/writeup-template.md) | Malen jeg bruker for nye løsninger. |

## Ferdigheter

| Område | Verktøy og teknikker |
| --- | --- |
| Filanalyse og steganografi | file, exiftool, strings, binwalk, foremost, zsteg, steghide, stepic, hex-editorer, tesseract OCR, polyglot-filer |
| Diskanalyse | Autopsy, The Sleuth Kit (mmls, fls, icat), FTK Imager, ewfmount, montering av VMDK/OVA |
| Minneanalyse | Volatility 2 og 3 (imageinfo, pstree, connscan, printkey, svcscan, malfind) |
| Nettverksanalyse | Wireshark-filtre, følge strømmer, finne data skjult i ICMP-pakker |
| Koding og kryptografi | Base64, hex, binær, morse, Cæsar, XOR med gjentatt nøkkel, MD5-oppslag, CyberChef |
| Grunnleggende reversing | strings, objdump, ltrace, finne hardkodede hemmeligheter |
| Grunnleggende web | lese kildekode, Gobuster, Hydra |
| Linux | find, grep, cut, tr, tar, mount, chroot, skjulte filer, bash-skript |
| SOC og hendelseshåndtering | triage av varsler, oppslag av IOC-er (VirusTotal, AbuseIPDB), persistens i registeret |

## Plattformer og arrangementer

| Plattform eller arrangement | Type | Notater i repoet |
| --- | --- | --- |
| [picoCTF (picoGym)](writeups/picoctf.md) | Øving, jeopardy | 24 løst, mest forensics |
| [CTFlearn](writeups/ctflearn.md) | Øving, jeopardy | Forensics og koding |
| [Cyberlandslaget CTF 2025](writeups/cyberlandslaget-2025.md) | Arrangement, jeopardy | Forensics, reversing, krypto |
| Root-Me | Øving | Bare teknikker, se metodikk. Root-Me tillater ikke publiserte løsninger. |
| CryptoHack | Øving, krypto | Bare teknikker |
| TryHackMe | Øving, rom | SOC Analyst-løypa |
| LetsDefend / Hack The Box | Øving | SOC Analyst-løypa |
| Magnet Virtual Summit 2025 Team CTF (Hexordia) | Arrangement, lag | Mobil- og dataetterforskning (Android, iOS, Chromebook, Windows 11) |
| SAF CTF 2025 (SANS og mnemonic) | Arrangement, jeopardy | |
| helseCTF 2025 | Arrangement, jeopardy | |

## Regler jeg følger her

- Flaggene er byttet ut med `REDACTED`. Det er metoden som er poenget, og publiserte flagg ødelegger oppgaven for andre.
- Ingen løsninger fra plattformer som ber om at løsninger ikke publiseres. Teknikker jeg har lært der, ligger i metodikk-sidene uten navn på oppgaven.
- Uløste oppgaver blir stående, merket som åpne, med det jeg har prøvd. Blindveier er en del av prosessen.
