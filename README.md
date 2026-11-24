# Swedish Electricity Price & Usage Logger

Applikation och databaslösning för att logga och analysera elpriser (öre/kWh) och elförbrukning (kWh) i Sveriges elområden (SE1–SE4).

## Syfte och målgrupp
* Syfte: Samla in och jämföra regionala elpriser mellan norra och södra Sverige (Luleå SE1, Stockholm SE3, Göteborg SE3 och Malmö SE4) samt koppla förbrukningen till olika hushållsapparater.
* Målgrupp: Energianalytiker, smart-home-användare och hushåll som vill få bättre koll på sina elkostnader.

## Teknisk stack
* Språk: Python 3.10+ (standardbiblioteken random och datetime)
* Databas: MySQL (Fas 2)
* Container och moln: Docker, GitHub Actions, Azure (Fas 3–6)

## Kom igång
1. Gå in i src-mappen:
   ```bash
   cd src
   ```
2. Kör skriptet:
   ```bash
   python energy_logger.py
   ```

## Projektstatus
- [x] Fas 1: Python Core Logger (SE1–SE4 pris- och förbrukningssimulering)
- [ ] Fas 2: MySQL-databas, ER-diagram, vyer och Python-koppling
- [ ] Fas 3: Docker och Docker Compose
- [ ] Fas 4: CI/CD med GitHub Actions och Azure
- [ ] Fas 5: Enhetstester (unittest)
- [ ] Fas 6: Nätverkssäkerhet (VNet, NSG och DNS)