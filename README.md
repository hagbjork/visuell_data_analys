# Visuell data analys

## TIPS: conda environments med jupyter notebook

#### 1. Skapa ett nytt conda environment

Skapa ditt environment och installera `python` och `ipykernel`. __Välj själv namn istället för NEW_ENV__.

    conda create --name NEW_ENV python

#### 2. Aktivera din NYA environment

    conda activate NEW_ENV

Man ser att miljön är aktiverad geonom att det står (NEW_ENV) i terminalen. __FÖRSTA GÅNGEN__ du aktiverar din miljö ska du inte glömma att installera alla requirements. Se till att du har din environment aktiverad och står i samma mapp (folder) som din `requirements.txt` fil finns genom att titta på listan som dyker upp när du kör

    ls
Man kan byta mapp med

    cd DIRECTORY_NAME

När du ser att din `requirements.txt`-fil finns så kör du

    pip install -r requirements.txt

#### 4. Skapa en notebook i VSCode

1. I VSCode, skapa en ny notebook med ctrl + shift + p
2. Sök på 'Jupyter: Create New Blank Notebook' och välj det
3. I övre högra hörnet finns en knapp för att välja kernel. Tryck på den och sök på din NEW_ENV

## TIPS: Ta bort environments

För att se vilka enviroments som finns skapat skriva

    conda env list

För att radera ett environment börja med att deaktivera det enviromentet så att man är i (base)

    conda deactivate

För att radera ett environment skriva

    conda env remove --name ENV_NAME

ENV_NAME är namnet på environmentet som ska raderas.

## TIPS: Se installerade paket

För att se vilka paket som är installerade i ett virtual environment aktiverar man först environmentet

    conda activate ENV_NAME

Sedan listar man upp alla paket

    conda list

## TIPS: git + kursens repo = sant

Det är ett repository för kursen. För att få ner det lokalt på din dator behöver du öppna GitHub Desktop och clone repositoryn enligt följande instruktioner:

#### 1. Öppna GitHub Desktop

#### 2. Välj Add.. Clone Repository.. URL och ange

    https://github.com/evahegnar/visuell_data_analys.git

#### 3. Ändra Local Path om du vill ändra vilken mapp repositoryn ska sparas lokalt

I kursens repository finns det en fil som heter requirements.txt. Den filen innehåller en lista på pythonpaket som du ska installera i ditt conda environment.

Mappen kommer uppdateras och för att få de senaste ändringarna använder du *pull*.

Om du väljer att jobba i detta repositroy, vilket kan vara skönt med all kursmaterial lättillgänglig, kan inte du pusßha egna ändringar till repot. Du kan dock committa till ditt lokala Git repo och ha det sparat lokalt. Använd *commit* tillsammans med kort kommentar om ändringarna.

## Data Camp

Vi har ett premium medlemskap till Data Camp Classroom. Data Camp är en platform med kurser och övningar inom Data Science. Denna kan du använda för att komplettera utbildningen.

För att få fri tillång måste du följa denna länken [Data Camp Classroom](https://www.datacamp.com/groups/shared_links/1e9ec73fbf3dd46f0a0a9c8a9e773774c7ad2add6677109d698782ea059a2ae3) och skapa ett konto med studentmailen *@utb.ecutbildning.se*
