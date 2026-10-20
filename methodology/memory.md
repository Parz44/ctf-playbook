# Minneanalyse

Et fullt eksempel finner du i [Zeus-casen](../case-studies/zeus-memory-analysis.md).

## Fremgangsmåte

1. Finn ut hva slags minnebilde det er, og hvilken profil som skal brukes.
2. List opp prosessene og se på treet. Se etter rare foreldreprosesser, rare navn og prosesser med nettverkstrafikk.
3. List opp nettverkstilkoblinger, både aktive og lukkede, og koble dem til prosess-ID-er.
4. Sjekk mistenkelige IP-adresser og domener mot trusseletterretning.
5. Se etter persistens i registeret og i tjenester.
6. Se etter injisert kode i den mistenkelige prosessen.

## Volatility 2

```bash
volatility -f mem.dmp imageinfo                              # foreslått profil
volatility -f mem.dmp --profile=<profil> pslist
volatility -f mem.dmp --profile=<profil> pstree              # foreldre- og barneprosesser
volatility -f mem.dmp --profile=<profil> psscan              # finner også skjulte og avsluttede prosesser
volatility -f mem.dmp --profile=<profil> psxview             # sammenligner ulike måter å liste på
volatility -f mem.dmp --profile=<profil> connections         # aktive TCP-tilkoblinger da dumpen ble tatt
volatility -f mem.dmp --profile=<profil> connscan            # også lukkede tilkoblinger
volatility -f mem.dmp --profile=<profil> netscan             # Vista og nyere
volatility -f mem.dmp --profile=<profil> cmdline
volatility -f mem.dmp --profile=<profil> cmdscan
volatility -f mem.dmp --profile=<profil> consoles
volatility -f mem.dmp --profile=<profil> hivelist
volatility -f mem.dmp --profile=<profil> printkey -K "Microsoft\Windows NT\CurrentVersion\Winlogon"
volatility -f mem.dmp --profile=<profil> svcscan > svcscan.txt
volatility -f mem.dmp --profile=<profil> -p <pid> malfind    # injisert kode i en prosess
volatility -f mem.dmp --profile=<profil> -p <pid> impscan    # importerte funksjoner, avslører skjult kode
```

`connections` viser bare det som var åpent da dumpen ble tatt. Et tomt resultat betyr ikke at ingenting har skjedd, så kjør alltid `connscan` i tillegg.

## Volatility 3

```bash
python3 vol.py -f mem.dmp windows.info
python3 vol.py -f mem.dmp windows.pslist | head -n 10
python3 vol.py -f mem.dmp windows.pstree
python3 vol.py -f mem.dmp windows.netscan
python3 vol.py -f mem.dmp windows.malfind --pid <pid>
```

## Raske funn uten Volatility

```bash
strings mem.dmp | grep COMPUTERNAME     # miljøvariabler ligger igjen i minnet
strings mem.dmp | grep -i flag
```

## Hva som ser mistenkelig ut

- `svchost.exe` som kobler seg til en ekstern IP-adresse på port 80.
- En prosess som kjører fra feil sti, eller har feil foreldreprosess.
- `Userinit` i Winlogon-nøkkelen som peker på noe annet enn `userinit.exe`.
- Minneområder som er både kjørbare og skrivbare (`PAGE_EXECUTE_READWRITE`), som `malfind` markerer.
