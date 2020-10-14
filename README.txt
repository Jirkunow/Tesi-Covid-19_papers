Guida rapida
Recupero dei dati
wget https://aida.kmi.open.ac.uk/downloads/network_data_codiv.zip
In tale cartella trovi:
papers_covid.json
authors: insieme di json corrispondente alle informazioni di un autore e i paper da lui scritti (insieme ad altri collaboratori)

CSV necessari (presenti già nella cartella ma ricreabili):
csv/covid_plus_2015_2020.csv
csv/id_paper_covid_bool.csv 

file binari necessari (strutture-autori)
authors_info.picke: primo livello: tutti gli id autori presenti nella cartella authors/ secondo livello: Nome, Nomero Papers. Terzo livello (solo NumPapers): anno1, anno2 etc. quarto livello: numero paper scritti nell’anno
esempio:
authors_info[345]: Name: Giorgio NumPapers: {2015:8, 2017:7}
authors_collaborators.pickle:
struttura con primo livello di chiavi tutti gli autori presenti nella cartella authors/ secondo livello di chiavi tutti gli anni in cui gli autori hanno scritto un paper / terzo livello di chiavi tutti i collaboratori dell’autore (dal 2015 al 2020) = numero di collaborazioni.
esempio:
authors_collaborators[789]:{2015:{456:9}}
authors_collaborators[789]=2015, 2016 ;authors_collaborators[789][2015]=456,678,567;
authors_collaborators[789][2015][456]=9 numero collaborazioni nell’anno 2015
authors_collaborators[789][2015][678]=0 numero collaborazioni nell’anno 2015 (non hanno collaborato in quell’anno)

versione no e yes covid (solo dati relativi ai papers scritti sul covid)

authors_analysis.py → tutte le funzioni necessarie 

covid_plus_grafo.py → esempio per la creazione dei grafi

struct_authors_cosine.py → esempio per la creazione di data_all.csv, data_no_papers_covid.csv, data_yes_papers_covid.csv

IMPORTANTE:
soprattutto per la parte dei grafi, non eliminare il file all’interno di JARS (se vuoi da mettere da i jars di spark) -- per libreria graphframes
