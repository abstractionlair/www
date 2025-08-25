---
layout: default
title: "Reasoning Models as Unrolled Neural Networks"
permalink: /conversations/featured/reasoning-models-as-unrolled-neural-networks/
---

# Reasoning Models as Unrolled Neural Networks

[← Back to Conversations](/conversations/) | [← Featured Conversations](/conversations/#featured)

---

# AI Reasoning Model State Sequence

**Created:** 2025-08-05T14:31:44.217165Z
**Updated:** 2025-08-05T14:35:31.897222Z
**UUID:** f5cf7a8e-f97e-4ca4-ac0d-f34605bd0d51

---

## User

This question is inspired by hearing someone else ask Dwarkesh what we really mean when we distinguish reasoning from non-reasoning models. If I think of the sequence of states involved when a reasoning model responds to a query, that is a sequence of states where each state is defined as a set of activations, data in a scratch pad, and data in a context window. Would you agree so far?

## Claude

 Yes, I think that's a reasonable way to characterize the sequence of states, though I'd suggest a small refinement to make it more precise.

For a reasoning model processing a query, each state in the sequence could indeed be characterized by:

1. **Activations** - The neural network's internal representations/hidden states at that point in processing
2. **Scratch pad data** - Any intermediate computations, working memory, or chain-of-thought reasoning that's been explicitly generated
3. **Context window data** - The accumulated tokens/information available to the model at that step

The refinement I'd suggest is clarifying what we mean by "scratch pad" - in many current reasoning models, this is actually just part of the context window where the model writes out its reasoning steps. So you might have:
- The original query
- Any reasoning tokens generated so far
- Any other contextual information

All sitting together in the context window, rather than a truly separate scratch pad memory system.

But yes, conceptually your framing captures the key idea - at each step in processing, the model's state consists of both its internal neural activations and the external/explicit information it has access to and has generated. This provides a concrete way to think about the computational trajectory from query to response.

## User

OK, let's go with your refinement. If we leave practicality aside, could there be mappings which makes that equivalent to some larger network without the "reasoning"? E.g. extra layers being equivalent in some way to the state of the reasoning models which is outside of the activations?

## Claude

 Yes, absolutely! This is a fascinating theoretical question that touches on some deep ideas in computational theory.

In principle, you could imagine "unrolling" or "compiling" a reasoning process into a much larger feedforward network. Here's how this might work:

1. **Temporal unrolling**: Each step of reasoning could correspond to a set of layers in the larger network. So if a reasoning model takes N steps, you might have N groups of layers, each processing the equivalent of one reasoning step.

2. **Scratch pad encoding**: The information that would be written to the context window during reasoning could instead be encoded in the activation patterns between these layer groups. What was explicit text becomes implicit distributed representations.

3. **Conditional computation**: The larger network would need to handle all possible reasoning paths, essentially building in the computation for every possible intermediate thought the reasoning model might generate.

The key insight is that anything computed iteratively can, in principle, be computed by a sufficiently large feedforward network. This is related to why RNNs can be "unrolled" into feedforward networks for fixed sequence lengths.

However, this would likely require an exponentially larger network because:
- You'd need to account for all possible reasoning trajectories
- The network would have to implicitly learn to route information through the right "reasoning paths"
- You lose the efficiency of reusing the same parameters across reasoning steps

So while theoretically possible, it suggests that reasoning models might be a much more parameter-efficient way to achieve certain capabilities - they're essentially using iteration and external memory to avoid needing astronomical numbers of parameters.



---

[← Back to Conversations](/conversations/) | [← Featured Conversations](/conversations/#featured)
