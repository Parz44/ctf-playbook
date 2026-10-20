# Koding og kryptografi

## Kjenn igjen formatet først

| Ser ut som | Sannsynligvis | Dekod med |
| --- | --- | --- |
| `A-Z a-z 0-9 + /`, slutter på `=` eller `==` | Base64 | `echo '<str>' \| base64 -d` |
| Bare `0-9 a-f`, partall antall tegn | Hex | `xxd -r -p`, eller [hexconv.py](../scripts/hexconv.py) |
| Bare `0` og `1`, grupper på 8 | Binær (ASCII) | CyberChef «From Binary» |
| Prikker, streker og mellomrom | Morse | CyberChef «From Morse Code» |
| Bare bokstaver, ser ut som forskjøvne ord | Cæsar / ROT | CyberChef «ROT13» med ulike forskyvninger, eller dcode.fr |
| 32 hex-tegn | MD5-hash | Kan ikke dekodes. Slå den opp eller knekk den |
| Liste med tall fra 32 til 126 | ASCII-koder | Python `chr()` |

Kodinger legges ofte oppå hverandre. Dekod, se på resultatet og dekod igjen. I én oppgave var det base64, så base64 igjen, og til slutt en Cæsar-forskyvning.

## Kommandolinje

```bash
echo 'cGljb0NURnsuLi59' | base64 -d
cat fil.txt | xxd -r -p           # hex til bytes
echo -n 'tekst' | xxd -p          # bytes til hex
```

## Python

```python
# ASCII-koder til tekst
codes = [99, 114, 121, 112, 116, 111]
print(''.join(map(chr, codes)))

# hex til tekst
print(bytes.fromhex("63727970746f").decode("ascii"))
```

## XOR med gjentatt nøkkel

XOR kan reverseres: `klartekst = chiffertekst XOR nøkkel`. Hvis et program har et kryptert passord hardkodet, og noe som ser ut som en nøkkel, prøv å XOR-e dem. Se [xor.py](../scripts/xor.py).

```python
plaintext = bytes(c ^ key[i % len(key)] for i, c in enumerate(ciphertext))
```

## Hasher

- En hash er et fingeravtrykk av data, ikke kryptering. Den kan ikke reverseres. Du kan bare finne en verdi som gir samme hash.
- For svake eller vanlige verdier, prøv et oppslagsnettsted (md5decrypt.net, CrackStation) eller en ordliste med hashcat eller John.
- Finne hvilken fil som har en bestemt hash:

```bash
sha256sum files/* | grep "$(cat checksum.txt)"
```

## Signaturer, kort fortalt

En digital signatur er en hash av dokumentet som er kryptert med avsenderens private nøkkel. Mottakeren dekrypterer den med avsenderens offentlige nøkkel og sammenligner med sin egen hash av dokumentet. Er de like, er dokumentet uendret og signert av den som eier den private nøkkelen.

## Verktøy

- [CyberChef](https://gchq.github.io/CyberChef/), med «Magic» for å gjette
- [dcode.fr](https://www.dcode.fr/) for klassiske chiffer og brute force av forskyvninger
