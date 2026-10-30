ARTICLES = [
{
'slug': 'dependent-types-for-knowledge',
 'title': 'When your knowledge carries its own proof',
 'eyebrow': 'FOUNDATIONS · DEPENDENT TYPES',
 'summary': 'Move from a graph that stores claims to an interface that requires evidence for the invariants you care about.',
 'body': '''<p>A knowledge graph can record that Alice works for an organisation. It can also record an impossible combination of facts, an outdated identity, or a relationship whose endpoints have the wrong kinds. Different failures need different tools. A schema handles some; a proof about the whole store can handle others.</p>
<h2>Start with types, then let types mention values</h2>
<p>Ordinary types already improve a graph interface. A function expecting a person should not accept a company identifier by accident. A relationship can specify the kinds of its endpoints. Dependent type theory, or DTT, goes further: a type may refer to a particular value. Evidence can therefore concern this exact graph, rather than merely graphs in general.</p>
<p>In Lean, propositions have types too, and a proof is a term checked against its proposition. A useful design is a pair consisting of a graph <code>g</code> and evidence of <code>Valid g</code>. The evidence is tied to the graph it describes. Change the graph, and the old evidence does not automatically certify the replacement. This is a practical application of the <a href="https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/">dependent types explained in Theorem Proving in Lean 4</a>.</p>
<h2>Make the boundary do the work</h2>
<p>Consider an organisation directory with an application rule: a person may have at most one active primary employer. That rule is a deliberate modelling choice, not a universal fact about employment. A candidate update may satisfy all local field types while breaking that global rule.</p>
<p>A certified insertion operation must establish that the resulting store still satisfies the invariant. It can return a new certified store, or a structured rejection that explains which obligation was not discharged. A language model may propose the update and help interpret the rejection, but its confidence does not substitute for the missing evidence.</p>
<aside class="callout"><strong>Design sketch</strong><p>Candidate update → construct the new graph → establish its invariant → return graph plus evidence. If the evidence cannot be produced, preserve the previous certified state.</p></aside>
<h2>Certification is a contract you design</h2>
<p>The difficult work often happens before proving anything: choosing identities, temporal boundaries, equality, and the meaning of absence. Is a relationship an enduring fact or an observation at a particular time? Can two sources disagree without making the store invalid? Explicit observation types and provenance can preserve disagreements while keeping your accepted conclusions coherent.</p>
<p>Not every invariant has an automatic decision procedure. A total checker needs a decidable property, a restricted domain, or supplied certificates that it can verify. Lean does not turn every ontology question into a terminating yes-or-no test. Start with a small invariant whose meaning you can explain and whose enforcement you can test.</p>
<h2>What the proof actually buys you</h2>
<p>The result is conditional: the encoded graph satisfies the encoded property under the assumptions used by the proof. It does not establish that an imported employment record is true, or that your definition captures every business requirement. Keep input provenance, model review, and the proof boundary visible.</p>
<p><a href="https://leanpub.com/bulletproofknowledge-aiagents">Bulletproof Knowledge</a> develops this pattern for agent memory. For the programming background, continue with <a href="https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/">Propositions and Proofs</a>, then compare certified state with the typed persistence interfaces in <a href="https://volland.github.io/typedb-lean/">typedb-lean</a>.</p>'''
},
{
'slug': 'higher-order-logic-and-elpi',
 'title': 'Let logic search. Let Lean check.',
 'eyebrow': 'LEAN + ELPI · REASONING',
 'summary': 'Higher-order terms make binders and relations first-class. Certificates separate finding an answer from trusting it.',
 'body': '''<p>Graph traversal answers useful questions, but knowledge engineering also encounters rules about rules, relations passed as arguments, and temporary assumptions. These are natural places to use higher-order representations. The goal is not to make every graph problem more abstract. It is to represent the structure your problem already has.</p>
<h2>What “higher-order” changes</h2>
<p>A first-order rule talks about individuals and applies named predicates to them. Higher-order logic can also quantify over predicates and functions. For an engineering example, a reusable reachability construction can take the edge relation as an argument: the same pattern can describe reporting lines, dependencies, or containment.</p>
<p>Binders introduce a second practical benefit. A formula such as “for every person, a policy holds” contains a variable with a scope. Encoding that syntax with raw strings creates opportunities for accidental capture and incorrect substitution. Higher-order abstract syntax uses the host language's binding structure to represent the object's binders, reducing the amount of substitution machinery you must implement yourself.</p>
<h2>Where λProlog and ELPI fit</h2>
<p>λProlog is a logic programming language designed around typed higher-order terms and scoped reasoning. ELPI extends that tradition. In the <a href="https://volland.github.io/lean-elpi/">LeanElpi project</a>, the engine is implemented in Lean, with higher-order pattern unification, backtracking, and facilities for hypothetical and universally quantified goals. The pattern restriction matters: general higher-order unification is not a simple decidable operation.</p>
<p>A fresh scoped variable and a temporary hypothesis let a program explore a local reasoning context. Think of checking a function body while temporarily assuming that its argument has a given type. When the local computation ends, the assumption should not leak into the surrounding knowledge base. This makes logic programming particularly useful for language tools and reasoning about structured syntax.</p>
<h2>An answer is not yet a certificate</h2>
<p>A successful search tells you what the search engine found. Certification is another step. LeanElpi exposes an optional LF certification layer that records derivations and translates their signatures into Lean definitions. The resulting proof is then checked by Lean. Ordinary interpreter results do not automatically gain this guarantee merely because the interpreter was written in Lean.</p>
<aside class="callout"><strong>Two separate responsibilities</strong><p>The searcher constructs a candidate derivation. The checker verifies that the derivation establishes the claimed proposition under the chosen rules.</p></aside>
<p>This separation lets you change heuristics, indexing, and search order without making those choices part of the logical justification. A buggy searcher can waste time, miss an answer, or supply an invalid certificate. It should not be able to make a correct checker accept a derivation that its rules do not justify.</p>
<h2>Give failure the right meaning</h2>
<p>Search exhaustion or a timeout is not generally a proof that a statement is false. The search may be incomplete, resource bounded, or operating in a fragment. Expose “not derived” separately from “refuted”, and return counterevidence only when your system really has it.</p>
<p>For a concrete application, <a href="https://volland.github.io/rdf-lean/">LeanRDF</a> uses Elpi to find semantic derivations and a verified checker to validate certificates. Start experimenting with the <a href="https://volland.github.io/lean-elpi/">LeanElpi book and getting-started examples</a>; then use <a href="https://leanpub.com/bulletproofknowledge-aiagents">Bulletproof Knowledge</a> to connect scoped reasoning to agent memory.</p>'''
},
{
'slug': 'the-certified-semantic-stack',
 'title': 'The semantic stack, with evidence at every boundary',
 'eyebrow': 'DEEP DIVE · RDF / OWL / SHACL',
 'summary': 'RDF, RDFS, SPARQL, OWL profiles, and SHACL answer different questions. LeanRDF gives those questions explicit semantics.',
 'body': '''<p>A diagram of the semantic web can look like a ladder: triples at the bottom, ontologies above, logic near the top. For an implementation, it is more useful to ask what each layer promises. Parsing, query evaluation, entailment, and validation are different operations. A certificate must say which operation it justifies.</p>
<h2>1. Represent statements without losing their meaning</h2>
<p>RDF describes graphs using subjects, predicates, and objects, with IRIs, literals, and blank nodes. Blank nodes are not merely convenient global identifiers; their interpretation matters when comparing graphs and checking entailment. <a href="https://www.w3.org/TR/rdf11-mt/">RDF 1.1 Semantics</a> specifies interpretations and several entailment regimes, providing the mathematical target for a formalisation.</p>
<p><a href="https://volland.github.io/rdf-lean/">LeanRDF</a> brings a native RDF model, N-Triples and Turtle parsing, and formal interpretations into Lean. The relevant question becomes precise: does every interpretation satisfying this graph also satisfy the query graph, under the selected regime?</p>
<h2>2. Derive consequences with RDFS</h2>
<p>Suppose a graph states that cats are mammals and that Tom is a cat. RDFS supplies the semantic connection that licenses Tom's membership in the mammal class. A derived triple should be traceable to its premises and the rule used. LeanRDF represents certificates as proof graphs, checks their steps, and connects successful checking to entailment through soundness theorems.</p>
<p>Elpi can perform the exploratory work of finding a derivation. The certificate checker does not need to trust that search procedure. Remember the converse: a failed search is not, by itself, a semantic proof of non-entailment.</p>
<h2>3. Query, infer, and validate deliberately</h2>
<p>SPARQL evaluates queries over data. LeanRDF includes a formal query algebra and an evaluator with a correctness relationship to its declarative semantics. This concerns query evaluation; it should not be described as an automatic proof that the original data is true.</p>
<p>OWL adds ontology vocabulary and richer entailments. The project develops rule reasoning for OWL 2 RL and EL. Name those supported profiles and rules explicitly: that is a narrower, more useful statement than claiming a universal OWL reasoner.</p>
<p>SHACL asks whether a data graph conforms to specified shapes. A requirement such as “every selected person has a name” belongs naturally to validation. It does not have the same meaning as an open-world ontology axiom. The <a href="https://www.w3.org/TR/shacl/">SHACL specification</a> defines this data-graph/shapes-graph relationship. LeanRDF develops SHACL Core semantics and a validator connected to them by proofs.</p>
<h2>4. Keep the proof boundary visible</h2>
<p>A sound checker theorem, an execution of compiled code, and a kernel-checked proof term are related but distinct artifacts. An executable verdict relies on its runtime path. If a theorem uses native evaluation, inspect the resulting assumptions and evaluation mechanism rather than presenting it as ordinary kernel reduction. The project examples document the available routes.</p>
<p>For a deployed agent, retain the input graph, entailment regime, query, certificate, and relevant software versions. That makes the claim reproducible and lets a later checker revisit it. Explore the <a href="https://volland.github.io/rdf-lean/">LeanRDF book, documentation, and worked examples</a>, and inspect the <a href="https://github.com/Volland/rdf-lean">source definitions and soundness theorems</a> when deciding exactly what your application can promise.</p>'''
},
{
'slug': 'choose-your-graph-foundation',
 'title': 'Three graph foundations. One explicit contract.',
 'eyebrow': 'GRAPH ENGINEERING · ARCHITECTURE',
 'summary': 'TypeDB, LadybugDB, and RDF serve different modelling needs. Connect their guarantees deliberately rather than treating them as interchangeable layers.',
 'body': '''<p>“Use a knowledge graph” does not select a data model, a query language, or a trust boundary. An agent might need concurrent structured persistence, a local property graph, or standards-based semantic interchange. These needs overlap, but they do not imply the same architecture.</p>
<h2>TypeDB: model roles and relationships explicitly</h2>
<p>TypeDB is a useful fit when a domain is organised around entities, relations, attributes, and roles. A relation can involve several participants, and the role each plays is part of the model. For organisational knowledge, a person's participation in a project is richer than an unlabelled connection between two identifiers.</p>
<p><a href="https://volland.github.io/typedb-lean/">typedb-lean</a> connects this model to Lean structures and typed transactions. Its interface includes schema generation, decoding into structures, query interpolation, and migration support. Transaction modes encode whether an operation belongs in a read, write, or schema transaction. These are concrete interface guarantees; they are not a proof that every fact in a remote database satisfies an arbitrary application ontology.</p>
<h2>LadybugDB: embed a typed property graph</h2>
<p>A property graph represents nodes and relationships with their properties. An embedded database can suit a local tool or agent that needs graph queries without operating a separate database server. The questions here include path traversal, optional matches, and how nullable values flow through a query.</p>
<p><a href="https://volland.github.io/ladybug-lean/">ladybug-lean</a> describes node and relationship tables in Lean and provides typed Cypher alongside a query builder. The same graph interface can run against LadybugDB or an in-memory implementation. That makes small examples and differential testing easier. The pure backend is a useful development tool, but agreement in tests is not automatically a formal equivalence theorem for every external database behaviour.</p>
<h2>RDF: make semantic interchange explicit</h2>
<p>RDF suits work where shared identifiers, vocabulary, and standard entailment semantics matter. A triple is small; the interpretation of those triples carries much of the system's meaning. RDFS, selected OWL profiles, and SHACL provide different ways to infer or constrain that meaning.</p>
<p><a href="https://volland.github.io/rdf-lean/">LeanRDF</a> focuses on those semantics and the evidence behind results. It is not simply another persistence driver. It supplies a formal model, reasoning and query components, and certificate checking. Its documented oxilite integration is one concrete example of connecting an external engine to certification.</p>
<h2>A project map is not an integration guarantee</h2>
<p>These projects form an ecosystem of complementary tools, not a preassembled pipeline in which every arrow is already implemented. LeanElpi can supply logic programming; Lean supplies types and proof checking; a database supplies persistence. Joining them requires an explicit mapping and a definition of what information crosses each boundary.</p>
<p>Before combining stores, decide how identifiers correspond, which timestamps matter, how null differs from absence, and how a multi-party relation becomes a collection of triples. A lossy translation may erase the very fact a proof needs. Preserve provenance and define a stable snapshot for certification.</p>
<p>Begin with the smallest representation that matches your domain. Use the free mini books on <a href="https://volland.github.io/typedb-lean/">TypeDB and Lean</a> and <a href="https://volland.github.io/ladybug-lean/">LadybugDB and Lean</a> for implementation paths. Add semantic certification where a precise claim deserves a precise justification.</p>'''
},
{
'slug': 'the-trust-boundary-of-agent-memory',
 'title': 'What a certified agent may honestly claim',
 'eyebrow': 'AGENT MEMORY · TRUST',
 'summary': 'Proofs can make reasoning auditable. Their assumptions, inputs, and connection to external actions still need an explicit design.',
 'body': '''<p>An agent's memory changes the cost of a mistake. A false statement in one answer may be forgotten. A false statement committed to persistent memory can become a premise for many future answers. Certification gives us a way to control that propagation, provided we describe the guarantee precisely.</p>
<h2>Separate observation, acceptance, and consequence</h2>
<p>A source says that a person works at a company. That is an observation about a source. Accepting the employment relationship as a current fact is another operation. Deriving that the person is subject to a particular policy is a third. Collapsing these stages into a single graph edge makes provenance and disagreement hard to recover.</p>
<p>A useful memory model keeps observations alongside their source, time, and interpretation. An acceptance policy determines which observations may support the current working model. A reasoning layer derives consequences from that model. None of these decisions should be hidden behind a confidence score whose meaning changes between models.</p>
<h2>Put proof obligations at the write and read boundaries</h2>
<p>On a write, require evidence that the proposed state satisfies the chosen invariant. On a read, require evidence that the claimed answer follows from the accepted state and rules. The design in <a href="https://leanpub.com/bulletproofknowledge-aiagents">Bulletproof Knowledge</a> connects these two boundaries to Lean and logic programming. Its <a href="https://github.com/Volland/bulletproof-knowledge">companion repository</a> is the place to inspect the executable implementation.</p>
<p>A rejected update can become useful feedback. The agent can correct a type mismatch, revise an entity mapping, or present a source conflict to a person. It must not silently weaken the invariant or invent a new axiom simply to make the candidate pass. Changes to the model itself deserve a separate review path.</p>
<h2>Ask what each certificate is bound to</h2>
<p>A valid proof about yesterday's graph is not automatically a valid proof about today's graph. Associate a certificate with the exact input state, query, schema, rules, and assumptions it uses. If another transaction changes a relevant fact between checking and committing, the application needs transactional coordination or a recheck against the new snapshot.</p>
<p>The same principle applies to an external action. Proving that a payment was authorised does not prove that a payment API executed it exactly once. The effects of network calls, database commits, and file writes need their own operational controls and evidence. Keep those controls connected to the formal model without claiming that a theorem has reached beyond its scope.</p>
<h2>Inspect the assumptions, not just the green result</h2>
<p>Lean checks a theorem in an environment of definitions and assumptions. A placeholder proof, an inconsistent axiom, or a theorem about the wrong encoding can defeat the intended assurance. Review theorem statements and dependencies. When using a compiled checker or native evaluation, document the runtime mechanisms included in the trust boundary.</p>
<p>Likewise, distinguish a search that found no answer from a proof that no answer exists. <a href="https://volland.github.io/lean-elpi/">LeanElpi</a> and <a href="https://volland.github.io/rdf-lean/">LeanRDF</a> illustrate how search can produce evidence for a separate checker, but the application's reporting still determines what users hear.</p>
<p>The strongest honest promise is specific: this conclusion follows from this recorded model under these stated assumptions, and here is the evidence. That is a valuable foundation for reliable agents without confusing formal consistency with complete knowledge of the world.</p>'''
}
]
