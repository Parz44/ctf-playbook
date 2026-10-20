# Nettverksopptak (pcap)

## Fremgangsmåte

1. Åpne opptaket i Wireshark og få oversikt: Statistics > Protocol Hierarchy, Conversations og Endpoints.
2. Søk etter flaggformatet med Edit > Find Packet, med String og «Packet bytes».
3. Filtrer på protokoll og se på innholdet i pakkene. Data skjules ofte der de ikke hører hjemme, for eksempel i ICMP.
4. Følg strømmer for å lese hele samtaler: høyreklikk en pakke > Follow > TCP/HTTP Stream.
5. Hent ut overførte filer med File > Export Objects.

## Finne pakkene som skiller seg ut

I én oppgave var alle pakkene ICMP, og flagget var delt over fire pakker. Det som avslørte dem var en annen verdi i IP-headeren: ECN-feltet var satt til `01` (ECN-Capable Transport). Innholdet i hver av dem var base64 og ble dekodet til `PART_n:...:PARTEND`. Ved å filtrere på denne verdien fant jeg alle delene:

```
ip.dsfield.ecn == 1
```

Lærdom: når pakkene ser like ut, sammenlign feltene i headeren. Den som skiller seg ut, er som regel den interessante.

## Filtre jeg bruker

| Mål | Filter |
| --- | --- |
| HTTP-forespørsler | `http.request` |
| Servernavn i HTTPS (TLS Client Hello) | `tls.handshake.type == 1` |
| All nettrafikk | `http.request or tls.handshake.type == 1` |
| Trafikk fra én maskin | `ip.src == 10.0.50.227` |
| Trafikk til én maskin | `ip.dst == 31.13.90.36` |
| Én TCP-port | `tcp.port == 80` |
| Nye TCP-tilkoblinger | `tcp.flags.syn == 1 and tcp.flags.ack == 0` |
| SMTP med emnelinje | `smtp contains "Subject:"` |
| Flere kildeporter | `udp.srcport in {53 59015 63518}` |
| Utelate en port | `not tcp.port == 25` |
| DNS | `dns` |

## Nyttige visninger

- View > Name Resolution viser domenenavn i stedet for IP-adresser.
- Statistics > Resolved Addresses gir en liste over alle maskinnavn som ble slått opp.
- Statistics > IO Graphs viser topper i trafikken over tid.

## Tegn på infeksjon i trafikken

Skadevare kommuniserer ofte over vanlig HTTP eller TLS. Start med `http.request or tls.handshake.type == 1` og se etter ukjente domener, rare user agents og trafikk med jevne mellomrom (beaconing). Sjekk mistenkelige IP-adresser på AbuseIPDB, Talos eller VirusTotal.
