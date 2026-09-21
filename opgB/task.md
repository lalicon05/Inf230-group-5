# F230 worksheet B: Ontology design and development

During the second half of September, each group will develop a first working version of a domain ontology, which you can continue to use and further develop for some of the problems further ahead. The groups will work on five different domains of knowledge as follows:

    Groups 1 to 7 work on uncertainties and errors in physical quantities.
    Groups 8 to 14 work on reproducibility of simulation results.
    Groups 15 to 21 work on advanced materials.
    Groups 22 to 28 work on explainability and explanations.
    Groups 29 to 35 work on thermodynamic systems.

Discussion planned for 30.9.2026 8.15 - 9.00.
B.1 Ontology requirements analysis

    Have a brief discussion in your group to decide on the scope of the domain of knowledge, that is, what sort of information and semantics would be inside or outside the domain.
    Think of some knowledge-based system(s), database(s), or other digital platform(s) employing semantic technology that could be developed within the domain of knowledge as you understand it. Now imagine that your work on the domain ontology is part of the overall development work on this system or these systems.
    Draft three personas, that is, abstractions of representative groups of stakeholders (users, developers, or similar) interacting with the system. The idea of a persona here is the one from agile requirements analysis.
    Three members of your group will each impersonate one persona and formulate two competency questions each, so your group has six competency questions. This is much fewer than usual in such processes; it will allow you to fulfill all requirements and still have a small ontology.
    Polish the CQs a bit and agree on them as a group. After this process, effectively, your definition of the domain of knowledge and scope of your ontology is "that which is needed to express the six competency questions."
    See if you are still in line with your vision (point B.1.a), and if not, either agree on revising it as an outcome from your process, or repeat the whole process to make it stay closer to your original plans.

Submit a spreadsheet/tables or a PDF or other text file containing your persona descriptions, competency questions, and (from B.2 and B.3) a note on whether the ontology fulfills the respective requirement. But you do not need to actually write up any CQs in SPARQL or similar. You also do not need to document that you actually went through the sequence of steps suggested above.

Problem B.1 is to be discussed at the presentation session (30.9. 8.15) by group 22. Here you are meant to explain how you went through the process and show your CQs and personas.
B.2 Ontology design and drafting

    Draw up a first listing of concepts and relationship types that you think are necessary to meet your requirements.
    For top-down ontology design, determine for each concept (and, if applicable, relationship type) what universal it would be subsumed under within the foundational ontology DOLCE; you can also use DOLCE Lite, but not DOLCE Ultralite (dul) which has a somewhat different structure.
    For bottom-up ontology design and good practice in terminology, include genus-differentia definitions for at least five concepts such that the superclass (genus proximus) is included in the ontology as well. For this to work, the genus proximus must be broadly within your domain of knowledge, i.e., it should not be too abstract.
    Draft the overall taxonomy for your domain ontology such that it has exactly three levels, i.e., there should be one or multiple classes at the highest level with subclasses and sub-subclasses, but not any further. The taxonomy should be structured as a tree, without diamonds.

You don't need to submit anything separate here, just make sure your genus-differentia definitions are included in the TTL file from B.3 (use skos:definition).

You don't have to make the DOLCE alignment explicit in your ontology or any of the submitted material - this is here just meant as part of the design process. But you can make it explicit if you want; there are several ways to do this - whether or how you do this is your free design choice.

Problem B.2 is to be discussed at the presentation session (30.9. 8.15) by group 13. Here you are meant to explain how you went through the process and show your genus-differentia definitions and grouping of concepts under DOLCE.
B.3 Ontology implementation

Write up the domain ontology in TTL format.

The ontology should at this stage not refer to any external ontologies/namespaces other than the standard ones such as RDF, RDFS, XML schema, OWL, and SKOS, and if you want, the foundational ontology DOLCE (or DOLCE Lite or similar). You can use protégé to make sure the syntax is understood, and FaCT/Hermit reasoners to check for unintended outcomes of inference from rules included in your ontology. Don't use schema.org or connect to any other domain ontologies at this stage of development.

Submit your ontology TTL file.

Problem B.3 is to be discussed at the presentation session (30.9. 8.15) for each of the five domains of knowledge, respectively, by group 3, 9, 16, 24, and 31. Here you are meant to present the ontology that you have developed.

Index