# alembic, SQLALchemy, Annotated

## Instruktioner
Repo som innehåller kodskelett för hur man kan sätta upp sqlalchemy med migrationer mot en databas i MySQL.
1. Klona repot
1. Skapa en virtuell miljö
  2. python -m venv venv
  3. aktivera din virtuella miljö  
1. Installera: pip install -r requirements.txt

2. Skapa databas i MySQL Workbench (CREATE DATABASE my_database)
3. Ändra anslutningssträngen mysql_url inuti env.py så att den innehåller din databasinformation
4. kör dessa kommandon
  5. alembic stamp base
  6. alembic upgrade head
7. Databasen är nu skapad med samma kolumner som finns i user.py

## SQLAlchemy
Biblioteket för att kunna koppla Python mot olika databaser.

## alembic
Används för databasmigrationer.
Vi skapar filer som kör upp- och nedgraderingar av vår databas.

## Annotated
Ett smidigare sätt att skriva kolumner i en SQLAlchemy-klass.
Istället för att upprepa oss med mapped_column(....) använder vi oss av sparade variabler.


