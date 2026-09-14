
# INF230 worksheet A: OWL ontologies

>_Discussion planned for 16.9.2026 8.15 - 9.00._

## A.1 Human language to RDFS

Start working on a TTL file that states the following:

- Services can make use of operating equipment. (Read: The relationship type "makes use of" has the domain "service" and the range "operating equipment".)
- If some service is run by some operating equipment, that means that it makes use of that equipment. (Read: The relationship type "is run by" is like "makes use of", but it is more specific.)
- Train services are a kind of service, and trains are a kind of operating equipment.
- The origin and the destination (of a train service) must be a train station.

The TTL file must be fully functional; criterion: You can load it correctly into protégé.

>_Problem A.1 is to be discussed at the presentation session (16.9. 8.15) by group 32._

## A.2 ABox in TTL format

Express: 
- There is a train service from Moss to Stabekk departing on (xs:dateTime) 
    - 16.9.2026 at 9:54 and 
    - reaching its destination at 10:49.  
- The train running on this service has eight coaches. 
- Introduce IRIs for all the individuals mentioned, _i.e._, 
- don't use any blank nodes.

>_Problem A.2 is to be discussed at the presentation session (16.9. 8.15) by group 21._

## A.3 SPARQL query

Write a SPARQL query that produces a table with two columns: 
- First, ?time, the arrival date+time of train services at Stabekk (and only there); 
- second, ?coaches, the number of coaches of the trains running the respective services.

You can use protégé to check that it is working, if your installation of protégé has the SPARQL querying plugin.

>_Problem A.3 is to be discussed at the presentation session (16.9. 8.15) by group 12._

## A.4 Human language to OWL

Continue to work with the TTL file and implement the rules:

1. Train services are run by trains. (Read: Each train service is run by at least one train, in other words, train service is a subclass of the class of things that are being run by at least one train.)
2. Every train service has an origin and a destination.
3. If some operating equipment runs a train service, it must be a train. (Read: The intersection of the class operating equipment and the class of things that run a train service is a subclass of the class train. You can use owl:inverseOf to go from "is run by" to "runs" or obverse.)

>_Problem A.4 is to be discussed at the presentation session (16.9. 8.15) by group 20._

## A.5 Competency question

Make it so that your ontology can be used to pose the following question: When are trains stopping at some train station (such as Ås stasjon), and what are their destinations?

Prove that this is the case and that the ontology can really be used to express this question.

>_Problem A.5 is to be discussed at the presentation session (16.9. 8.15) by group 5._

## A.6 Aristotelian definitions (Gabriel)

Provide Aristotelian genus-differentia definitions for three concepts from your ontology and include them in the TTL file using skos:definition. Include the superclasses (genera proxima) mentioned in these definitions in your ontology as well.

>_Problem A.6 is to be discussed at the presentation session (16.9. 8.15) by group 14._

## A.7 ABox in JSON-LD format

Create a JSON-LD file including the ABox, and only the ABox (_i.e._, the one from problem A.2). Check that it works with the JSON-LD Playground and that it can be loaded correctly in protégé.

**Note that the TTL file that you are creating should contain both the ABox and the TBox (one TTL file, for all the problems together).** 
As opposed to this, the JSON-LD file should contain only the ABox. Also include a brief PDF or other text document to say what you did at what stage; instead of a separate file, you can if you want also do this through comments in the TTL file itself.

>_Problem A.7 is to be discussed at the presentation session (16.9. 8.15) by group 11._

[Select language](https://home.bawue.de/~horsch/teaching/inf230/lab/inf230-oppgaave-A.html)