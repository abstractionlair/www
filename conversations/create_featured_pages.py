#!/usr/bin/env python3
import os
from pathlib import Path
import re

# Featured conversations from more_curated
featured_conversations = [
    "AI Computer Interfaces From Human GUIs to Model-Native Design",
    "AI Consciousness, Safety Testing, and Equilibrium Dynamics",
    "Brain Optimization vs AI Constraints and Evolution",
    "Decision Theory and AI Evolution", 
    "Distributed MoE Precision Heterogeneity and HPC Architecture",
    "Dynamic Model Growth Through Physics-Inspired Architecture Evolution",
    "Emulating Long-Term Memory in Claude Projects",
    "Human Utility as AI Money",
    "Identification Problem in Supply-Demand Models",
    "Multi-Model Dialog on ASI, Safety, and Economics",
    "Philosophy Meets Frontier AI Consciousness and Alignment",
    "Probabilistic Analysis of AI Existential Risk",
    "Reasoning Models and Modular Architecture",
    "Reasoning Models as Unrolled Neural Networks",
    "Testing AI Consciousness via Embedding Space Extrapolation",
    "Transformer Information Flow and Architecture Deep Dive",
    "Vector-Space Thinking for Chain-of-Thought Models"
]

def create_slug(title):
    """Create URL-friendly slug from title"""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')

# Create featured directory
featured_dir = Path("/Users/scottmcguire/www/conversations/featured")
featured_dir.mkdir(exist_ok=True)

# Copy each featured conversation to the featured directory
source_dir = Path("/Users/scottmcguire/www/test_unlinked/more_curated")

for title in featured_conversations:
    source_file = source_dir / f"{title}.md"
    if source_file.exists():
        # Read the source file
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create the featured page with Jekyll front matter
        slug = create_slug(title)
        page_content = f"""---
layout: default
title: "{title}"
permalink: /conversations/featured/{slug}/
---

# {title}

[← Back to Conversations](/conversations/) | [← Featured Conversations](/conversations/#featured)

---

{content}

---

[← Back to Conversations](/conversations/) | [← Featured Conversations](/conversations/#featured)
"""
        
        # Write the featured page
        dest_file = featured_dir / f"{slug}.md"
        with open(dest_file, 'w', encoding='utf-8') as f:
            f.write(page_content)
        
        print(f"Created: {dest_file.name}")

print(f"\nCreated {len(featured_conversations)} featured conversation pages")

# Now update the main conversations index
index_content = """---
layout: default
title: AI Conversations Collection
permalink: /conversations/
---

# Curated AI Conversations

This collection contains curated conversations with Claude, organized by topic. 

## Featured Conversations {#featured}

These are the most significant conversations, selected for their depth and insight. Each is readable directly in your browser.

### 🧠 AI Architecture & Reasoning

- [**Reasoning Models as Unrolled Neural Networks**](/conversations/featured/reasoning-models-as-unrolled-neural-networks/) - How reasoning models work as computational graphs
- [**Transformer Information Flow and Architecture Deep Dive**](/conversations/featured/transformer-information-flow-and-architecture-deep-dive/) - Comprehensive exploration of transformer mechanics
- [**Vector-Space Thinking for Chain-of-Thought Models**](/conversations/featured/vector-space-thinking-for-chain-of-thought-models/) - Understanding reasoning in vector spaces
- [**Distributed MoE Precision Heterogeneity and HPC Architecture**](/conversations/featured/distributed-moe-precision-heterogeneity-and-hpc-architecture/) - Mixture of Experts systems at scale
- [**Dynamic Model Growth Through Physics-Inspired Architecture Evolution**](/conversations/featured/dynamic-model-growth-through-physics-inspired-architecture-evolution/) - Novel approaches to model scaling

### 🤔 AI Consciousness & Philosophy

- [**AI Consciousness, Safety Testing, and Equilibrium Dynamics**](/conversations/featured/ai-consciousness-safety-testing-and-equilibrium-dynamics/) - Probing the boundaries of AI awareness
- [**Testing AI Consciousness via Embedding Space Extrapolation**](/conversations/featured/testing-ai-consciousness-via-embedding-space-extrapolation/) - Novel approaches to consciousness detection
- [**Philosophy Meets Frontier AI: Consciousness and Alignment**](/conversations/featured/philosophy-meets-frontier-ai-consciousness-and-alignment/) - Deep philosophical exploration
- [**Brain Optimization vs AI: Constraints and Evolution**](/conversations/featured/brain-optimization-vs-ai-constraints-and-evolution/) - Comparing biological and artificial intelligence

### 🎯 AI Safety & Alignment

- [**Probabilistic Analysis of AI Existential Risk**](/conversations/featured/probabilistic-analysis-of-ai-existential-risk/) - Quantifying catastrophic risks
- [**Multi-Model Dialog on ASI, Safety, and Economics**](/conversations/featured/multi-model-dialog-on-asi-safety-and-economics/) - Multiple perspectives on superintelligence
- [**Decision Theory and AI Evolution**](/conversations/featured/decision-theory-and-ai-evolution/) - How decision frameworks shape AI development
- [**Human Utility as AI Money**](/conversations/featured/human-utility-as-ai-money/) - Economic frameworks for AI alignment

### 💻 Technical & Applied

- [**AI Computer Interfaces: From Human GUIs to Model-Native Design**](/conversations/featured/ai-computer-interfaces-from-human-guis-to-model-native-design/) - Rethinking human-AI interaction
- [**Emulating Long-Term Memory in Claude Projects**](/conversations/featured/emulating-long-term-memory-in-claude-projects/) - Practical memory solutions
- [**Identification Problem in Supply-Demand Models**](/conversations/featured/identification-problem-in-supply-demand-models/) - Statistical challenges in economics
- [**Reasoning Models and Modular Architecture**](/conversations/featured/reasoning-models-and-modular-architecture/) - Building interpretable AI systems

---

## Topic Collections for Download

Each collection below contains multiple related conversations compiled for easy attachment to Claude conversations.

### 🤖 Core AI Architecture

#### [Transformer Architecture](/conversations/transformer-architecture/)
Deep dives into transformer models, attention mechanisms, tokenization, and architectural innovations. Covers both theoretical foundations and practical implementations.

#### [Advanced AI Architectures](/conversations/ai-architecture-advanced/)
Exploration of cutting-edge architectures including Mixture of Experts (MoE), reasoning models, neural architecture evolution, and novel computational approaches.

### 🧠 AI Consciousness & Philosophy

#### [AI Consciousness & Philosophy](/conversations/ai-consciousness-philosophy/)
Philosophical explorations of machine consciousness, AI ethics, moral frameworks, and the nature of AI experience and understanding.

#### [AI Safety & Alignment](/conversations/ai-safety-alignment/)
Critical discussions on existential risk, alignment theory, AI safety frameworks, and strategies for beneficial AI development.

### 💻 Development & Implementation

#### [AI Tool Development](/conversations/ai-tool-development/)
Building AI-powered tools, APIs, SDKs, and development frameworks. Includes Claude API integration and multi-model orchestration.

#### [Code Review & Analysis](/conversations/ai-code-review/)
AI-assisted code analysis, technical debt resolution, and software development methodologies.

#### [Claude Projects Optimization](/conversations/claude-projects-meta/)
Meta-level optimization of Claude Projects, custom instructions, context management, and persistent memory strategies.

### 📊 Quantitative & Statistical Methods

#### [Quantitative Finance & AI](/conversations/ai-quantitative-finance/)
Applications of AI to financial modeling, oil markets, trading systems, and quantitative analysis.

#### [Statistical Methods](/conversations/ai-statistical-methods/)
Bayesian inference, forecasting, time series analysis, and advanced statistical techniques in AI contexts.

### 🎯 Theory & Capabilities

#### [Decision Theory](/conversations/ai-decision-theory/)
Game theory, rational choice, decision-making frameworks, and their applications to AI systems.

#### [AI Capabilities & Limits](/conversations/ai-capabilities-limits/)
Understanding model capabilities, limitations, context windows, and performance characteristics.

---

## About This Collection

These conversations represent explorations at the intersection of AI, philosophy, mathematics, and practical implementation. They showcase:

- **Technical Depth**: From transformer architecture to advanced statistical methods
- **Philosophical Inquiry**: Consciousness, ethics, and the nature of intelligence
- **Practical Applications**: Building tools, solving real-world problems
- **Safety Considerations**: Alignment, risk assessment, and beneficial AI development

---

*This collection is part of [abstractionlair.xyz](https://abstractionlair.xyz) - exploring the frontiers of AI understanding.*
"""

# Write the updated index
with open("/Users/scottmcguire/www/conversations/index.md", 'w', encoding='utf-8') as f:
    f.write(index_content)

print("\nUpdated conversations index with featured section")