# SOC-triage

Fem spørsmål jeg bruker når jeg ser på et varsel, fra SOC Analyst-løypene på TryHackMe og LetsDefend.

1. **Hva skjedde?** Les varselet. Hva utløste det? Sammenstill med logger fra endepunkt, nettverk og applikasjoner. Er det et ekte funn eller en falsk alarm?
2. **Hvorfor skjedde det?** Finn angrepsvektoren: phishing, feilkonfigurasjon eller en sårbarhet som ikke er patchet. Lag en tidslinje. Passer det med kjente taktikker og teknikker?
3. **Hva annet er i faresonen?** Hvilke maskiner, brukere og data er involvert? Har angriperen beveget seg videre i nettverket? Hva er konsekvensen for virksomheten?
4. **Bør det eskaleres eller begrenses nå?** Hvor alvorlig er det (løsepengevirus, datalekkasje)? Kan det stoppes raskt? Gi riktige personer tydelig informasjon.
5. **Hva kan vi gjøre bedre neste gang?** Gjennomgang etter hendelsen, oppdatere playbooks, patche, forbedre deteksjon og opplæring.

## Sjekke indikatorer

| Indikator | Hvor jeg sjekker |
| --- | --- |
| IP-adresse | AbuseIPDB, Talos Intelligence, VirusTotal |
| Filhash | VirusTotal, MetaDefender (OPSWAT) |
| Domene eller URL | VirusTotal |
| CVE | NVD, leverandørens sikkerhetsvarsler |

## Grunnleggende om phishing

Forfalskning av e-post (spoofing) får en melding til å se ut som den kommer fra en avsender man stoler på. SPF, DKIM og DMARC hjelper med å avgjøre om avsenderen er ekte. Sjekk dem i e-postheaderne.
