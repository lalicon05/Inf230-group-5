<<<<<<< HEAD:opgA/description.txt

INF230 worksheet A: OWL ontologies

Discussion planned for 16.9.2026 8.15 - 9.00.
A.1 Human language to RDFS
=======
link: [Oppgave A](https://home.bawue.de/~horsch/teaching/inf230/lab/inf230-oppgaave-A-nb.html)

# INF230-oppgave A: OWL-ontologier

> Diskusjon planlagt 16.9.2026 kl. 8.15 - 9.00.


## A.1 Menneskespråk til RDFS
>>>>>>> 8b7180121ba70c81300d589e5dd489899d76571d:opgA/description.md

Start working on a TTL file that states the following:

<<<<<<< HEAD:opgA/description.txt
    Services can make use of operating equipment. (Read: The relationship type "makes use of" has the domain "service" and the range "operating equipment".)
    If some service is run by some operating equipment, that means that it makes use of that equipment. (Read: The relationship type "is run by" is like "makes use of", but it is more specific.)
    Train services are a kind of service, and trains are a kind of operating equipment.
    The origin and the destination (of a train service) must be a train station.
=======
- Tjenester kan gjøre bruk av driftsutstyr. (Les som: Forholdstypen "gjør bruk av" har domenet "tjeneste" og kodomenet "driftsutstyr".)
- Dersom en tjeneste kjøres av noe driftsutstyr, så innebærer dette at den gjør bruk av det. (Les som: Forholdstypen "kjøres av" likner på, men er mer spesifikk enn "gjør bruk av".)
- Togturer er en type teneste, og tog er en type driftsutstyr.
- Start- og endestasjonen (til en togtur) må være togstasjoner.
>>>>>>> 8b7180121ba70c81300d589e5dd489899d76571d:opgA/description.md

The TTL file must be fully functional; criterion: You can load it correctly into protégé.

<<<<<<< HEAD:opgA/description.txt
Problem A.1 is to be discussed at the presentation session (16.9. 8.15) by group 32.
A.2 ABox in TTL format

Express: There is a train service from Moss to Stabekk departing on (xs:dateTime) 16.9.2026 at 9:54 and reaching its destination at 10:49. The train running on this service has eight coaches. Introduce IRIs for all the individuals mentioned, i.e., don't use any blank nodes.

Problem A.2 is to be discussed at the presentation session (16.9. 8.15) by group 21.
A.3 SPARQL query
=======
## Problem A.1 skal diskuteres under presentasjonstimen (16.9. kl. 8.15) av gruppe 32.
A.2 ABoks i TTL-format

Skriv som ABoks i TTL: 
- Det går en togtur fra Moss til Stabekk, 
  - starter 16.9.2026 kl. 9.54 (xs:dateTime) 
  - og når endestasjonen kl. 10.49. 
- Toget som kjører den tjenesten har åtte vogner. 
- Bruk IRI-er for alle individ, dvs. ikke bruk blanke noder.

## Problem A.2 skal diskuteres under presentasjonstimen (16.9. kl. 8.15) av gruppe 21.


A.3 SPARQL-spørring
>>>>>>> 8b7180121ba70c81300d589e5dd489899d76571d:opgA/description.md

Write a SPARQL query that produces a table with two columns: First, ?time, the arrival date+time of train services at Stabekk (and only there); second, ?coaches, the number of coaches of the trains running the respective services.

You can use protégé to check that it is working, if your installation of protégé has the SPARQL querying plugin.

<<<<<<< HEAD:opgA/description.txt
Problem A.3 is to be discussed at the presentation session (16.9. 8.15) by group 12.
A.4 Human language to OWL
=======
## Problem A.3 skal diskuteres under presentasjonstimen (16.9. kl. 8.15) av gruppe 12.
A.4 Menneskespråk til OWL
>>>>>>> 8b7180121ba70c81300d589e5dd489899d76571d:opgA/description.md

Continue to work with the TTL file and implement the rules:

    Train services are run by trains. (Read: Each train service is run by at least one train, in other words, train service is a subclass of the class of things that are being run by at least one train.)
    Every train service has an origin and a destination.
    If some operating equipment runs a train service, it must be a train. (Read: The intersection of the class operating equipment and the class of things that run a train service is a subclass of the class train. You can use owl:inverseOf to go from "is run by" to "runs" or obverse.)

<<<<<<< HEAD:opgA/description.txt
Problem A.4 is to be discussed at the presentation session (16.9. 8.15) by group 20.
A.5 Competency question
=======
## Problem A.4 skal diskuteres under presentasjonstimen (16.9. kl. 8.15) av gruppe 20.
A.5 Kompetansespørsmål
>>>>>>> 8b7180121ba70c81300d589e5dd489899d76571d:opgA/description.md

Make it so that your ontology can be used to pose the following question: When are trains stopping at some train station (such as Ås stasjon), and what are their destinations?

Prove that this is the case and that the ontology can really be used to express this question.

<<<<<<< HEAD:opgA/description.txt
Problem A.5 is to be discussed at the presentation session (16.9. 8.15) by group 5.
A.6 Aristotelian definitions
=======
## Problem A.5 skal diskuteres under presentasjonstimen (16.9. kl. 8.15) av gruppe 5.
A.6 Aristoteliske definisjoner
>>>>>>> 8b7180121ba70c81300d589e5dd489899d76571d:opgA/description.md

Provide Aristotelian genus-differentia definitions for three concepts from your ontology and include them in the TTL file using skos:definition. Include the superclasses (genera proxima) mentioned in these definitions in your ontology as well.

<<<<<<< HEAD:opgA/description.txt
Problem A.6 is to be discussed at the presentation session (16.9. 8.15) by group 14.
A.7 ABox in JSON-LD format
=======
## Problem A.6 skal diskuteres under presentasjonstimen (16.9. kl. 8.15) av gruppe 14.
A.7 ABoks i JSON-LD-format
>>>>>>> 8b7180121ba70c81300d589e5dd489899d76571d:opgA/description.md

Create a JSON-LD file including the ABox, and only the ABox (i.e., the one from problem A.2). Check that it works with the JSON-LD Playground and that it can be loaded correctly in protégé.

<<<<<<< HEAD:opgA/description.txt
Note that the TTL file that you are creating should contain both the ABox and the TBox (one TTL file, for all the problems together). As opposed to this, the JSON-LD file should contain only the ABox. Also include a brief PDF or other text document to say what you did at what stage; instead of a separate file, you can if you want also do this through comments in the TTL file itself.

Problem A.7 is to be discussed at the presentation session (16.9. 8.15) by group 11.
=======
> Obs: Den ene TTL-fila dere lager (felles for alle deloppgaver) skal både inneholde ABoksen og TBoksen, i motsetning til JSON-LD-fila som bare skal inneholde ABoksen. Også legg ved et kort PDF eller annet tekstdokument for å forklare hva dere gjorde på hvilket steg; i stedet for en separat fil kan dere, dersom dere ønsker, også skrive det som kommentar i selve TTL-fila.

## Problem A.7 skal diskuteres under presentasjonstimen (16.9. kl. 8.15) av gruppe 11.
>>>>>>> 8b7180121ba70c81300d589e5dd489899d76571d:opgA/description.md

Select language
