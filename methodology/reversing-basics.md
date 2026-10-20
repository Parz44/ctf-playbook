# Grunnleggende reversing

Jeg er tidlig i læringen av reverse engineering. Dette er fremgangsmåten som har fungert på nybegynnerprogrammer så langt.

## Fremgangsmåte

1. `file <program>` for å se arkitektur, om programmet er strippet, og om det har debug-informasjon.
2. `strings <program> | less` for hardkodede passord, nøkler, variabelnavn og meldinger.
3. Kjør programmet med `ltrace` for å se kall til biblioteksfunksjoner som `strcmp`, som ofte viser hva programmet forventer som input.
4. Disassembler den interessante funksjonen med `objdump`.
5. Gjenskap logikken i Python hvis hemmeligheten er kodet.

```bash
file access-control
strings access-control | less
ltrace ./access-control
ltrace -s 100 ./access-control                       # lengre strenger i utskriften
objdump -d -S access-control | grep -A 20 -B 10 <adresse>
```

## Eksempel: hardkodet passord med XOR

Et 64-bits PIE-program med debug-informasjon hadde strenger som `enc_password` og et navn som viste seg å være nøkkelen. `objdump` viste at programmet sammenlignet input med en kryptert byte-liste. XOR av bytene med nøkkelen ga flagget. Skriptet ligger i [xor.py](../scripts/xor.py).

Lærdom: navn i `strings`-utskriften er hint. En variabel som heter `enc_password` forteller at det finnes noe å dekryptere.

## Verktøy på Windows

- HxD for hex-redigering
- PE-bear for å se på PE-headere og importer
