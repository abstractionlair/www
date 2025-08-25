---
layout: default
title: "AI Computer Interfaces From Human GUIs to Model-Native Design"
permalink: /conversations/featured/ai-computer-interfaces-from-human-guis-to-model-native-design/
---

# AI Computer Interfaces From Human GUIs to Model-Native Design

[← Back to Conversations](/conversations/) | [← Featured Conversations](/conversations/#featured)

---

# AI Training Data for Computer Interactions

**Created:** 2025-08-02T00:08:53.251815Z
**Updated:** 2025-08-02T00:21:23.043150Z
**UUID:** 2ec5ac91-1c96-42f7-a38f-cdadda99c301

---

## User

I have on right now a video from Dwarkesh where he is giving some personal estimates for various AI ability milestones. A tangent related to computer use has occurred to me. He has pointed out that there isn't abundant training data on computer use. I take this in the sense that people rarely produce media showing how they use a computer including capturing the inputs. But, in addition, I don't think we have a general purpose way of recording the various kinds of inputs in the way that natural language is a general purpose medium for other knowledge. Regarding the latter, would command lines be a more natural mode for LLMs to learn about and use computers?

## Claude

 You raise a fascinating point about the data representation problem for computer use. You're right that we lack a standardized, general-purpose format for capturing the full spectrum of computer interactions - unlike natural language text, which serves as a relatively universal medium.

Command lines do have some compelling advantages for LLM training and use:

1. **Serializable and discrete**: CLI commands are naturally sequential text strings, making them trivial to log, store, and include in training data. Every action has a clear textual representation.

2. **Compositional**: Command line tools follow grammatical patterns (command, flags, arguments) that mirror linguistic structures LLMs already excel at parsing.

3. **Self-documenting**: Many CLI interactions include explicit parameters and options, making the intent more interpretable than coordinate-based clicks.

4. **Reproducible**: A sequence of commands can be re-executed exactly, unlike GUI interactions that might depend on window positions or visual states.

However, CLIs also have limitations as a universal interface:
- Many modern applications simply don't expose CLI equivalents for their functionality
- Spatial/visual tasks (image editing, CAD, etc.) map poorly to text commands
- They lack the discoverability and immediate feedback that GUIs provide

The deeper challenge might be that we need something like a "intermediate representation" for computer interactions - perhaps a structured format that can capture GUI events, CLI commands, API calls, and even direct code execution in a unified way. Some efforts like accessibility APIs (which expose UI elements programmatically) or browser automation frameworks point in this direction, but we're still far from a universal standard.

What aspects of computer use do you think would be most important to capture in such a representation?

## User

Different things for different timescales. For the immediate future we will want to train models to use existing software, websites, etc. But in the future when models are significant or majority clients for other apps we will likely design interfaces specifically for them and I think we need to discover what would be optimal.

## Claude

 That's a really insightful distinction - the transition from "models adapting to human interfaces" to "interfaces designed for models" is profound.

For the near term, we're stuck reverse-engineering human interfaces. This probably means:
- Computer vision to parse GUIs
- Heuristics to understand common UI patterns
- Maybe leveraging accessibility APIs as a middle ground
- Lots of trial-and-error learning

But the long-term possibility is much more interesting. If AI agents become primary users, optimal interfaces might look radically different:

**Structured APIs over visual interfaces**: Instead of rendering pixels for interpretation, applications could expose rich semantic APIs. Imagine Photoshop offering not just "click at coordinates (x,y)" but "adjust_contrast(layer='background', amount=0.3)".

**Declarative over imperative**: Rather than step-by-step instructions, models might work better with goal specifications. Instead of "click file → save as → type filename → click save", just "persist_state(filename='project_v2')".

**Parallel operations**: Human interfaces assume serial attention, but models could potentially handle multiple simultaneous input/output streams. An AI-first interface might expose dozens of operations that can be invoked concurrently.

**Semantic compression**: Where humans need visual metaphors (folders, trash cans), AI interfaces could use dense semantic representations - perhaps even learned embeddings that capture application state more efficiently than any human-readable format.

The really interesting question is: how do we discover what's optimal? We might need to experiment with different interface paradigms and see what enables models to be most effective. It's a bit like how REST APIs emerged as a human-designed pattern that turned out to work well for programmatic access, but we might discover even better patterns when the "programmer" is an AI.



---

[← Back to Conversations](/conversations/) | [← Featured Conversations](/conversations/#featured)
