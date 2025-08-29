---
layout: default
title: "Modular MoE Architecture with Swappable Middle Layers"
permalink: conversations/featured/modular-MoE-architecture-with-swappable-middle-layers/
---

# Modular MoE Architecture with Swappable Middle Layers
 
 [← Back to Conversations](/conversations/) | [← Featured Conversations](/conversations/#featured)

---

## User

In a prior conversation I think I brought up the idea of implementing a MoE model where each expert was really a separate model, with explicit communication between them. A problem there is that we would need to agree on the communication language/protocol. If we made that the input-output language it would likely be inefficient. One motivation for this was to each model to be tuned separately, e.g. different numbers of bits for the activation values. I have a new brainstormy idea for this, though it gives up the possibility of different bit depths. What if, having decided that we would have L layers before the experts, we trained a general purpose non-MoE, model with L+M+N layers, then removed the M intermediate layers, inserted replacement layers (could be a different number than M) and trained on just one topic, creating one of our experts. The idea here is that the first training essentially defines two "languages" at the transition points between the input and middle layers, and then the middle and output layers. Creating an architecture where the middle part is swappable. I just realized this will need a routing mechanism, or a mechanism to choose between different outputs of middle layers. Probably more to flesh out. But what do you think so far?

## Claude

I found our previous conversations! Looking at your new brainstormy idea about creating swappable middle layers through pre-training, this is quite clever and addresses some of the communication protocol challenges we discussed before.

Your approach of training an L+M+N layer model first and then creating experts by swapping out the M middle layers is interesting because:

**Strengths:**
- **Implicit protocol definition**: The pre-training naturally defines the "communication languages" at the L→M and M→N boundaries through learned representations, avoiding the need to explicitly design a protocol
- **Compatibility guarantee**: All experts would speak the same "language" at these interfaces since they're all trained to connect to the same L and N layer blocks
- **Modular specialization**: Each expert could be fine-tuned on specific domains while maintaining interface compatibility

**Challenges and considerations:**

**Routing mechanism:** You're right that you'll need routing. A few options:
- Add a lightweight gating network at layer L that learns to route to different M-layer experts
- Use a separate small "router" model that examines the L-layer output
- Could even use similarity matching between the L-layer output and stored expert "signatures"

**Training dynamics:** The initial L+M+N training would need to create sufficiently general representations at the boundaries. If the original M layers are too specialized, the replacement experts might struggle to adapt.

**Capacity constraints:** The L and N layers become bottlenecks - they need to be general enough to work with all possible expert modules. This might limit how specialized each expert can become.

**Output combination:** If you route to multiple experts, you'd need a mechanism to combine their outputs before feeding to layer N. Weighted averaging? Attention-based combination?

An interesting variation might be to train the initial model with dropout or other regularization specifically at the L→M and M→N boundaries to encourage more robust, general representations there. You could even train with multiple different M sections from the start, teaching L and N to work with variety.

This feels like it could be more practical than fully separate models with explicit protocols, while still allowing modular expert development. Have you thought about how you'd handle the case where different experts might want different numbers of middle layers (M₁, M₂, etc.)?

## User

I think that last part is just a natural part of this. The outer layers don't have any dependence on or sensitivity to the depth of the middle network. I think.

## Claude

You're absolutely right! That's a key insight - once you've defined those interface "languages" at layers L and L+N, the middle section becomes a black box. The outer layers just care about:
- L produces some representation
- N expects some representation as input

What happens in between - whether it's M layers, M+5 layers, or M/2 layers - shouldn't matter as long as the middle section transforms the L output into something N can consume.

This is actually quite elegant because it means:

**Variable depth experts:** You could have a shallow 2-layer expert for simple pattern matching, and a deep 20-layer expert for complex reasoning, all working with the same L and N blocks

**Architecture flexibility:** The middle experts don't even need to be transformers - could be convolutions, state space models, retrieval mechanisms, or hybrid architectures

**Computational efficiency:** Route simple queries to shallow experts and complex ones to deeper experts, getting adaptive compute without the usual complexity

The main constraint would be ensuring the middle section preserves the expected dimensionality and "semantic space" that N expects. But that's just a training objective, not an architectural limitation.

This reminds me a bit of Universal Transformer's adaptive computation, but inverted - instead of deciding how many times to apply the same layer, you're choosing which depth/architecture of middle section to use. And the pre-training approach to establish the interfaces is much cleaner than trying to define them manually.

Have you thought about whether you'd want the router to be able to select multiple experts in parallel (like traditional MoE) or just pick one expert path per forward pass?

## User

I haven't. Mostly this idea was just about automatically generating interfaces through which different models could communicate or, expressed differently, to make the cooperating models orthogonal. Now that I've typed this, how do traditional MoEs work?

## Claude

Traditional MoEs work quite differently from your swappable-middle-layers idea! Let me break down the standard approach:

**Traditional Sparse MoE (like in Switch Transformer or Mixtral):**

**Expert placement:** Experts typically replace the FFN (feedforward network) portion of transformer layers. So you still have attention → FFN, but the FFN is now multiple parallel experts.

**Routing mechanism:** A learned gating network (usually just a linear layer + softmax) takes the token representation and outputs weights for each expert. Common approaches:
- Top-k routing: Select the k highest-weighted experts (often k=1 or 2)
- Token-choice: Each token chooses its experts
- Sometimes expert-choice: Each expert chooses which tokens to process

**Combination:** The outputs from selected experts are weighted-summed:
output = Σ (gate_weight[i] * expert[i](input))

**Load balancing:** Various tricks to ensure all experts get used:
- Auxiliary loss terms to encourage balanced routing
- Capacity limits per expert
- Random routing noise during training

**Key difference from your idea:** In traditional MoE, the experts are parallel alternatives at the same position in the network, not sequential modules. They all:
- Take the same input format
- Produce the same output format
- Operate at the same "level" of abstraction
- Are trained jointly from the start

Your approach is fundamentally different - you're creating truly modular, sequential processing stages that can be developed independently. Traditional MoEs don't give you that orthogonality/independence you're after. The experts in traditional MoE are more like "different ways to do the same transformation" rather than "different specialized modules that can be composed."

Your idea is closer to mixture of depths or pathways than mixture of experts in the traditional sense. It's actually quite novel in how it uses pre-training to establish the interfaces!

## User

Regarding bit depth, I imagine there could be special step down or step up layers which could learn what to do.

## Claude

Yes! That's a clever addition. Step-down/step-up layers could act as learned quantization and dequantization functions that are much smarter than simple rounding or scaling.

**Step-down (high → low precision):**
- Learn which information is critical to preserve vs what can be discarded
- Could learn different compression strategies for different types of information
- Might even learn to "pack" information differently knowing it'll be unpacked later

**Step-up (low → high precision):**
- Learn to intelligently reconstruct/hallucinate the missing precision
- Could learn priors about what the full-precision values likely were
- Essentially learning an informed "decompression" function

This would let you mix bit depths in your modular architecture:
L layers (FP16) → step-down → M expert (INT8) → step-up → N layers (FP16)

Or even more interestingly, the step-down/up layers could be expert-specific and trained alongside each expert module. So an expert focused on counting or logic might learn different quantization strategies than one focused on semantic similarity.

The step-down layer could even be part of the routing decision - the router could consider both which expert to use AND what precision to run it at, with corresponding step-down/up layers for each precision level.

This reminds me of learned tokenization or VAE encoders/decoders, but applied to precision rather than vocabulary or latent spaces. The model learns its own optimal way to compress and decompress between precision levels rather than using fixed quantization schemes.

Have you seen any research on learned quantization layers like this? It seems like it should exist but I'm not immediately recalling examples where it's been done quite this way.

## User

I have not. New idea: suppose we added or marked a neuron at the end of the initial layer which controlled which intermediate experts to run, or at first probably how to weight them. My mental picture now is as follows. Consider the usual graphical view of a network in two dimensions, where one axis is distance into the input message and the other is progression through the network. Now imagine we add a dimension which allows a stack of our middle/expert layers. At first they could all run and at the end results be combined using that/those strength neurons from the initial layer. So they "skip over" the middle layers. This is important. Then after the model learns which middle layer/experts it likes for different questions, training for which would be done with all the middle layers active, we would then add a transformation to those weighting neurons to force only a limited number of non-zero values. I believe there is a name for that.

## Claude

This is a really elegant idea! You're essentially creating a "routing highway" where the routing decision from layer L bypasses the middle experts entirely and goes straight to the combination mechanism at the merge point.

The visual is compelling - in your 3D network view:
- X-axis: position in sequence
- Y-axis: depth through network
- Z-axis: stack of parallel experts

And critically, the routing weights travel along a "bypass path" from L directly to the merge point, skipping over the middle computation entirely.

**The training progression makes a lot of sense:**

**Phase 1: All experts run, soft weighting**
- Router neurons at layer L output weights for each expert
- All experts process in parallel
- Outputs combined using these L-layer weights
- Network learns which experts are useful for what

**Phase 2: Sparsify the routing**
- Apply sparsification to force only top-k experts
- The transformation you're thinking of is probably sparsemax or top-k with straight-through estimator
- Could also use techniques like:
  - Gumbel-softmax with temperature annealing
  - Entmax (generalizes softmax and sparsemax)
  - Hard concrete distribution

**Why this "skip-over" design is important:**
- The routing decision is made with full L-layer context
- The combination weights are consistent with that same context
- No information bottleneck through the experts themselves
- The routing/weighting signal doesn't degrade through the middle layers

This avoids a problem in traditional MoE where the gating network only sees the immediate input to that layer, not the broader context from earlier layers. Your approach maintains that full context for both routing AND combination.

You could even extend this to have multiple routing neurons that control different aspects - one for expert selection, another for combination strategy, maybe another for precision level per your earlier idea.

## User

What scale would we need for a toy model so that it was actually informative about the workability of this?

## Claude

For a genuinely informative toy model, you'd want something small enough to iterate quickly but complex enough to show the key phenomena. Here's what I'd suggest:

**Minimum viable scale:**
- ~50-100M total parameters
- L (initial): 4-6 layers
- M (middle/experts): 4-6 layers each, with 4-8 different experts
- N (final): 4-6 layers
- Hidden dim: 512-768
- Attention heads: 8-12

**Why this scale:**
- **Complex enough for specialization:** Below ~50M parameters, models tend to be too capacity-constrained to develop meaningful specialization - every parameter gets heavily overloaded
- **Multiple behaviors to route between:** You need enough task diversity that different experts can actually specialize. A tiny model working on toy tasks won't show realistic routing patterns
- **Still tractable:** You could train this on a single A100 or 2-4 consumer GPUs, iterating in hours/days not weeks

**Critical test cases to include:**
- Tasks with obvious modalities (code, math, natural language, structured data)
- Varying complexity levels (simple extraction vs multi-step reasoning)
- Cases where multiple experts should collaborate vs single expert suffices

**Key metrics to track:**
- Does routing converge to consistent patterns?
- Do experts actually specialize or remain redundant?
- Does the sparsification phase (Phase 2) cause catastrophic forgetting?
- How much does the "skip-over" routing path help vs local routing?

**Dataset suggestions:**
Could use something like a mini version of The Pile with clearly distinct data types, or create a synthetic dataset with controllable task types that should obviously route to different experts.

You might even start with just 2-3 experts to debug the architecture, then scale to 4-8 once the basic routing/combination mechanism works.

Would this scale be feasible for your compute budget? You could probably get initial signal at even half this size (~25M parameters) if needed.
