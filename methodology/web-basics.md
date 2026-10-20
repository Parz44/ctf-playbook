# Grunnleggende web

## Fremgangsmåte

1. Åpne siden og se på kildekoden (Ctrl+U) og utviklerverktøyene. Sjekk alle sidene, også Om oss og Kontakt.
2. Se etter kommentarer, skjulte elementer, rare attributter og base64-strenger.
3. Sjekk `robots.txt` og vanlige stier.
4. Kartlegg mapper hvis nettstedet er innenfor det du har lov til å teste.
5. Brute force av innlogging bare i lab-miljøer der det er tillatt.

## Kartlegge mapper

```bash
gobuster dir --url http://target/ -w /usr/share/wordlists/dirbuster/directory-list.txt
```

## Brute force av innlogging (bare i lab)

```bash
hydra -l admin -P passlist.txt target http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect" -V
```

`F=incorrect` forteller Hydra at et svar som inneholder «incorrect» betyr mislykket innlogging.

## Laste ned filer fra et webshell

```bash
wget <url>
```

## Øving

[PortSwigger Web Security Academy](https://portswigger.net/web-security) er neste steg her.
