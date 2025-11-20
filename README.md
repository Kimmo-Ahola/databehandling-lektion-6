# alembic, SQLALchemy, Annotated

Repo som innehåller kodskelett för hur man kan sätta upp sqlalchemy med migrationer mot en databas i MySQL.

## SQLAlchemy
Biblioteket för att kunna koppla Python mot olika databaser.

## alembic
Används för databasmigrationer.
Vi skapar filer som kör upp- och nedgraderingar av vår databas.

## Annotated
Ett smidigare sätt att skriva kolumner i en SQLAlchemy-klass.
Istället för att upprepa oss med mapped_column(....) använder vi oss av sparade variabler.

1. Klona repot
1. Skapa en virtuell miljö
1. Installera: pip install -r requirements.txt
