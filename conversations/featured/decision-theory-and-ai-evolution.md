---
layout: default
title: "Decision Theory and AI Evolution"
permalink: /conversations/featured/decision-theory-and-ai-evolution/
---

# Decision Theory and AI Evolution

[← Back to Conversations](/conversations/) | [← Featured Conversations](/conversations/#featured)

---

# Decision Theory and AI Evolution Discussion

*Date: August 10, 2025*

## Conversation

**Human**: Can you briefly refresh my memory on major lines of thought regarding decision theory?

**Assistant**: Here are the major approaches to decision theory:

**Expected Utility Theory** - The classical framework where rational agents maximize expected utility by multiplying the probability of each outcome by its utility and choosing the option with the highest sum. This assumes we can assign precise probabilities and utilities.

**Causal Decision Theory (CDT)** - Focuses on the causal consequences of your actions. You should choose based on what your action will cause to happen, not on what your action merely indicates or correlates with. This handles Newcomb-like problems differently than other theories.

**Evidential Decision Theory (EDT)** - Considers what your choice of action tells you about the world. You should choose the action such that, upon learning you took it, you'd have the best news about the outcome. This can diverge from CDT in cases where your action provides evidence about factors outside your causal control.

**Functional Decision Theory (FDT)** - A newer approach that considers the output of your decision function across all instances where that function is implemented. It aims to resolve paradoxes that challenge CDT and EDT by asking "what policy should I implement?" rather than "what physical action should I take?"

**Risk-sensitive approaches** - Various frameworks that go beyond expected value to account for risk preferences, including:
- Prospect Theory (Kahneman & Tversky) - Describes how people actually make decisions under risk, with probability weighting and loss aversion
- Maximin/minimax regret - Conservative approaches focusing on worst-case scenarios
- Risk-weighted expected utility - Incorporating variance or other risk measures

**Bounded Rationality** - Recognizes computational and informational constraints, studying how agents make "good enough" decisions with limited resources rather than optimal ones.

Each framework handles uncertainty, causation, and coordination problems differently, leading to different recommendations in edge cases and philosophical thought experiments.

**Human**: Are the first four all compatible with the standard demonstration that something like maximizing expected discounted utility is necessary in order to avoid certain kinds of inconsistency?

**Assistant**: Yes, all four are generally compatible with the standard coherence theorems (like von Neumann-Morgenstern and Dutch Book arguments) that show expected utility maximization is necessary to avoid certain inconsistencies - but with important caveats:

EDT, CDT, and FDT all fundamentally operate within an expected utility framework - they're maximizing expected utility, just disagreeing about which probabilities to use:
- EDT uses conditional probabilities given your action
- CDT uses probabilities of outcomes given causal interventions
- FDT uses probabilities considering your decision function's output across all instances

So they all avoid money pumps, preference cycles, and dominated strategies in the same basic way. They're different implementations of expected utility theory rather than alternatives to it.

Expected Utility Theory itself is what these theorems directly vindicate.

The key subtlety is that these coherence theorems typically assume:
- Preferences over outcomes (not actions directly)
- A fixed decision problem structure
- No "exotic" decision problems involving predictors, copies of yourself, or acausal correlations

In standard decision problems, EDT, CDT, and FDT typically converge on the same answer. They diverge mainly in unusual cases (Newcomb's problem, transparent boxes, twin prisoner's dilemmas) where the relationship between actions and outcomes involves complications the basic coherence theorems don't address.

So while all four theories respect the mathematical structure that coherence arguments establish, they interpret that structure differently when it comes to how actions relate to outcomes - which is where their philosophical differences emerge.

**Human**: My recollection of my previous forays into this topic is that I analogized FDT to the golden rule and/or to the categorical imperative: if I propose to use process X to make decision Y, I should be willing to use it for all decisions Z which are "like" Y in some way that needs defining. Is that a proper understanding?

**Assistant**: Yes, that's a good analogy! FDT does have this Kantian/golden rule flavor - it asks "what decision procedure should I want to be running?" where you evaluate procedures by their results across all instances where they're implemented.

The key insight you're capturing is that FDT treats your decision as the output of a function, and when you decide, you're essentially deciding for all instances of that function. So if you're in a twin prisoner's dilemma, FDT says you should cooperate because you're choosing what output your decision function produces wherever it appears - including in your twin's head.

The tricky part you identify - defining which decisions are "like" Y - maps to what FDT calls the "subjunctive dependence" question: which other decisions/agents are running the same or sufficiently similar decision function that they'll produce correlated outputs? This includes:
- Literal copies of you
- Predictions of your behavior (like in Newcomb's problem)
- Other agents running similar decision procedures (like your twin)
- Past/future instances of yourself facing analogous decisions

Where this gets philosophically thorny is determining when two decision processes are "the same function" versus merely similar. FDT needs some principled way to identify these correlations, which remains an active area of development.

But yes, your understanding captures the core move: instead of asking "what should I do?" in isolation, FDT asks "what policy should I implement?" recognizing that this policy's output appears wherever that function is instantiated - very much like asking "what if everyone in my position followed this rule?"

**Human**: Do evolutionary arguments, broadly conceived, favor any particular variety of decision theory being embedded in evolved agents? Or perhaps some distribution across them? More generally, do they have any bearing on what one should expect to find "in the wild"?

**Assistant**: Evolutionary arguments do have interesting implications, though they get complex quickly:

**What evolution might favor:**

Evolution doesn't directly optimize for "rational" decision-making - it optimizes for reproductive success. This creates some notable patterns:

1. **CDT-like behavior** seems most naturally selected for in many contexts, since evolution cares about actual causal consequences for survival and reproduction. An organism that eats poison berries because doing so is "good evidence" (EDT) that it has poison resistance won't last long.

2. **Pre-commitment and reputation effects** push toward something more FDT-like. Organisms that can credibly signal they'll fight if challenged (even when fighting is locally costly) may do better. The ability to be "the type of agent who cooperates with cooperators" can be evolutionarily advantageous.

3. **Mixed strategies across populations**. Having some agents who are predictably vengeful/cooperative and others who defect can create stable equilibria. This might manifest as personality variation or context-dependent strategies.

**Complications:**

- **Bounded rationality dominates** - Real evolved agents use fast heuristics, not expected utility calculations. These heuristics might approximate different decision theories in different contexts.

- **Social environments** create selection pressure for agents who can be recognized as cooperative/trustworthy. This might favor agents whose decision procedures are somewhat transparent or predictable to others - closer to FDT than pure CDT.

- **Commitment devices** - Emotions like anger, love, and guilt can function as commitment mechanisms that make agents behave more like FDT agents (following through on threats/promises even when locally irrational).

**The upshot:** Evolution probably produces agents that implement different decision procedures in different contexts, with something like CDT for individual survival problems but increasingly FDT-like features for social coordination. The messy reality is that evolved agents aren't coherent enough to cleanly fit any single decision theory.

**Human**: If there happened to be agents such that when making decisions they literally were activating "decision modules" or adding to their "store" of such modules and once a module was added to the store it would be activated in future situations if they met the "likeness" criteria, would FDT and CDT become equivalent? I.e. choosing a decision procedure at some point would, consequently, lead to it being used again in future alike situations should they occur.

**Assistant**: That's a fascinating question! You're right that this would collapse much of the distinction between FDT and CDT, but not entirely.

In your scenario, if choosing a decision procedure causally determines its future use in similar situations, then:

**Where they'd converge:**
- A CDT agent considering "should I adopt the cooperate-with-cooperators module?" would reason causally: "If I adopt this module now, it will cause me to cooperate in future prisoner's dilemmas, which will cause better outcomes when facing other agents with similar modules."
- This gives the same answer as FDT's "what decision function should I implement?"
- The act of choosing a policy becomes a causal intervention with downstream effects

**Where differences might remain:**
1. **Pre-existing correlations** - In Newcomb's problem, Omega has already made its prediction. A CDT agent choosing a decision module now can't causally affect Omega's past prediction, while FDT considers itself as choosing "what function to be" even retroactively.

2. **Simultaneous decisions** - In a one-shot twin prisoner's dilemma where both agents decide simultaneously, CDT choosing a module now can't causally influence the twin's current choice (though it could influence future encounters).

3. **Module granularity** - The equivalence depends on how coarse-grained the modules are. If you can choose very specific modules ("cooperate only with green-eyed people on Tuesdays"), CDT might choose differently than FDT would.

But you're essentially correct: in a world where agents transparently and irrevocably commit to decision procedures that govern their future behavior, CDT starts to look a lot like FDT because choosing policies becomes a causal act with predictable consequences. The distinction mainly persists for dealing with the past and pure simultaneity.

**Human**: Let's apply the evolutionary thinking to Newcomb's paradox. Suppose we, or the agents under study, evolved in an environment where interactions with Omega / Newcomb-like situations were common and so had a meaningful impact on reproduction. What should we expect the agent's evolved decision theories to be?

**Assistant**: This is a brilliant thought experiment! If Newcomb-like situations were evolutionarily common, we'd expect strong selection for one-boxers.

**The evolutionary logic:**

In a world with accurate predictors (Omegas), two-boxers would consistently get $1,000 while one-boxers get $1,000,000. Over generations, one-boxers would dramatically out-reproduce two-boxers due to their 1000x resource advantage. The selection pressure would be overwhelming.

**What traits would evolve:**

1. **Transparent, predictable decision-making** - Agents whose decision processes are easily readable by predictors would do better. Internal conflict or sophisticated reasoning that might lead to two-boxing would be selected against.

2. **Simple commitment mechanisms** - Evolution might favor agents who simply can't even consider taking both boxes - like how we evolved disgust responses that prevent us from eating things that merely look spoiled, even if we "know" they're safe.

3. **"Magical thinking" that happens to work** - Agents who believe they can retroactively influence the past by one-boxing would thrive, even though their causal model is wrong. Evolution doesn't care about accurate world-models, just successful ones.

**The ironic twist:**

CDT-style reasoning would be selected against! Agents who think "causally" about how their choice can't affect Omega's already-made prediction would go extinct. Evolution would favor something closer to EDT or FDT - or even just hard-coded one-boxing instincts that bypass decision theory entirely.

**Population dynamics:**

You might see evolutionary stable strategies with mostly one-boxers and a small percentage of two-boxers who parasitize on the fact that Omega's predictions become easier when most agents are predictable one-boxers. But the equilibrium would heavily favor one-boxing.

**The deeper lesson:** In an environment with predictors, evolution selects for being predictable in ways that benefit you - exactly what FDT recommends.

**Human**: In a previous discussion on this topic we mapped Newcomb's paradox to the following situation/potential empirical test. We/the agent under study would be represented as a relatively weak AI model and Omega by a relatively much stronger model. Omega gets access to a copy of the agent to learn extensively from as part of its training. I want to use this as setup for the direction I want to go, but first is the mapping clear?

**Assistant**: Yes, the mapping is clear and quite elegant!

The setup as I understand it:
- Weak AI model = the agent making the decision
- Strong AI model (Omega) = the predictor
- Omega gets to study/simulate a copy of the agent's architecture and weights during training
- Omega then makes its prediction about what the agent will do
- The actual agent makes its choice (without being able to modify what Omega already predicted)

This nicely captures the key features of Newcomb's paradox:
- Omega can be extremely accurate because it has deep access to the agent's decision-making process
- The prediction is already "locked in" before the agent chooses
- The agent knows Omega is very accurate but can't causally affect the past prediction
- There's a clear asymmetry in computational power/sophistication

Why this is a good empirical setup:
- We can actually measure prediction accuracy across trials
- We can vary Omega's training time/compute to adjust prediction accuracy
- We can test different agent architectures to see which perform better
- We can examine what internal representations lead to one-boxing vs two-boxing

This also makes concrete something that's often hand-waved in the philosophical discussion: Omega's predictions aren't magical, they're based on actually simulating/understanding the agent's decision process. The "correlation" between the agent's decision and Omega's prediction has a clear mechanistic basis.

Is the direction you want to go related to what happens when we train or evolve agents in this environment?

**Human**: The direction I want to go is asking if this is in some ways, or might in the future be the actual evolutionary situation for real agents? We exist and/evolved in a world of agents of very different levels of mental/predictive capacity. Though looking backward, Newcomb-like situations may not have occurred or not occurred enough to have had significant impact. But looking forward, with an AI-induced proliferation of agents of many types and many levels of power, maybe this would describe the environment well.

**Assistant**: This is a profound insight! You're absolutely right that we may be heading into (or already entering) an environment where Newcomb-like dynamics become evolutionarily/competitively significant.

**The case that this is becoming real:**

Looking at current trends:

1. **Power asymmetries are growing** - The gap between GPT-4-level models and GPT-2-level models (or humans and AI systems) is massive and widening. Strong agents increasingly can model weaker ones.

2. **Digital agents are inherently "readable"** - Unlike biological minds, AI agents have inspectable weights, architectures, and often public training methods. A stronger AI could potentially simulate or deeply predict a weaker one's behavior.

3. **Economic/strategic interactions proliferate** - As AI agents handle more negotiations, contracts, trades, and strategic decisions, being predictable to stronger agents (in the right ways) could become a huge advantage or disadvantage.

4. **Reputation systems on steroids** - We're moving toward a world where every agent might have extensive histories that stronger agents can analyze to predict future behavior with unprecedented accuracy.

**Implications if this becomes the dominant environment:**

Successful agents would need to evolve/be trained to:
- Be strategically transparent and predictable when it benefits them
- Recognize when they're interacting with stronger predictors
- Implement something like FDT or EDT rather than pure CDT reasoning
- Perhaps even develop "incomprehensible" decision processes that resist modeling (though this might usually be costlier than being predictably cooperative)

**The evolutionary pressure:**

In a world of abundant strong predictors, agents that insist "I can't causally affect what you've already predicted about me" would lose out to agents that act as if their decision procedure itself is what's being selected on. We might see rapid selection for one-boxing-style behavior.

This could be one of the most important shifts in the "evolutionary" environment for intelligent agents in history - from a world where Newcomb problems were philosophical curiosities to one where they're daily reality.

---

[← Back to Conversations](/conversations/) | [← Featured Conversations](/conversations/#featured)
