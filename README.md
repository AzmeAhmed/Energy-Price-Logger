# Swedish Electricity Price & Usage Logger

An application and database solution for logging and analyzing regional electricity prices (öre/kWh) and consumption (kWh) across Swedish bidding zones (SE1-SE4).

## Purpose & Target Audience
* Purpose: Collect and compare regional electricity prices between northern and southern Sweden (Luleå SE1, Stockholm SE3, Göteborg SE3, and Malmö SE4) and link usage to specific household appliances.
* Target Audience: Energy analysts, smart-home users, and households looking to track and optimize electricity costs.

## Tech Stack
* Language: Python 3.10+ (standard libraries `random` and `datetime`)
* Database: MySQL (Phase 2)
* Containers & Cloud: Docker, GitHub Actions, Azure (Phases 3-6)

## Getting Started
1. Navigate to the `src` directory:
   ```bash
   cd src
   ```
2. Run the logger script:
   ```bash
   python energy_logger.py
   ```

## Project Roadmap
- [x] Phase 1: Python Core Logger (SE1-SE4 price and usage simulation)
- [ ] Phase 2: MySQL database, ER diagram, views, and Python integration
- [ ] Phase 3: Docker and Docker Compose setup
- [ ] Phase 4: CI/CD pipeline with GitHub Actions and Azure
- [ ] Phase 5: Automated unit tests (`unittest`)
- [ ] Phase 6: Network security (VNet, NSG, and DNS)
