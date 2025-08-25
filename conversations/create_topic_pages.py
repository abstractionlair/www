#!/usr/bin/env python3

# Topic configurations with descriptions
topics = {
    "transformer-architecture": {
        "title": "Transformer Architecture Conversations",
        "description": "Deep technical discussions about transformer models, attention mechanisms, tokenization, and architectural innovations. These conversations explore both theoretical foundations and practical implementations of transformer-based systems.",
        "topics": [
            "Multi-token planning mechanisms",
            "Information flow in transformer architectures",
            "Attention mechanism mathematics and intuition",
            "Tokenization strategies and embeddings",
            "Context window management",
            "Decoder architectures and continuous representations",
            "Vector-space thinking for reasoning models"
        ]
    },
    "ai-consciousness-philosophy": {
        "title": "AI Consciousness & Philosophy Conversations",
        "description": "Philosophical explorations of machine consciousness, AI ethics, moral frameworks, and the nature of AI experience. These conversations probe fundamental questions about intelligence, awareness, and ethical considerations in AI systems.",
        "topics": [
            "Machine consciousness and self-awareness",
            "AI ethics and moral frameworks",
            "Epistemic humility and uncertainty",
            "Philosophy of mind applied to AI",
            "Emergent behaviors and consciousness",
            "Meta-ethics and AI moral status",
            "Brain-AI comparisons and constraints"
        ]
    },
    "ai-safety-alignment": {
        "title": "AI Safety & Alignment Conversations",
        "description": "Critical discussions on existential risk, alignment theory, and strategies for beneficial AI development. These conversations address fundamental challenges in ensuring AI systems remain aligned with human values and beneficial outcomes.",
        "topics": [
            "Existential risk analysis",
            "Alignment theory and methods",
            "Decision theory in AI systems",
            "Gradual vs sudden AI risk scenarios",
            "Economic impacts of transformative AI",
            "Meta-ethics and value alignment",
            "Safety frameworks and evaluation"
        ]
    },
    "claude-projects-meta": {
        "title": "Claude Projects Optimization Conversations",
        "description": "Meta-level optimization of Claude Projects, custom instructions, context management, and persistent memory strategies. These conversations explore how to maximize the effectiveness of AI assistants through systematic optimization.",
        "topics": [
            "Project knowledge architecture",
            "Custom instruction optimization",
            "Context preservation strategies",
            "Meta-frameworks for AI assistants",
            "Persistent memory emulation",
            "Cross-project knowledge integration",
            "Iterative optimization methods"
        ]
    },
    "ai-tool-development": {
        "title": "AI Tool Development Conversations",
        "description": "Building AI-powered tools, APIs, SDKs, and development frameworks. These conversations cover practical implementation of AI systems, from API integration to multi-model orchestration.",
        "topics": [
            "Claude API integration",
            "Multi-model conversation systems",
            "SDK development and documentation",
            "Tool orchestration architectures",
            "AI-assisted development workflows",
            "Graph-based conversation models",
            "MVP planning and implementation"
        ]
    },
    "ai-quantitative-finance": {
        "title": "Quantitative Finance & AI Conversations",
        "description": "Applications of AI to financial modeling, market analysis, and trading systems. These conversations explore the intersection of machine learning, statistical methods, and financial markets.",
        "topics": [
            "Neural networks for market modeling",
            "Oil market analysis and prediction",
            "Portfolio optimization strategies",
            "Bayesian methods in finance",
            "Trading system architecture",
            "Market microstructure modeling",
            "Risk analysis and forecasting"
        ]
    },
    "ai-statistical-methods": {
        "title": "AI Statistical Methods Conversations",
        "description": "Advanced statistical techniques, Bayesian inference, and mathematical methods in AI contexts. These conversations dive deep into the mathematical foundations underlying modern AI systems.",
        "topics": [
            "Bayesian inference and modeling",
            "Forecasting and time series analysis",
            "Shapley values and attribution",
            "Statistical error decomposition",
            "Kalman filters and state estimation",
            "Functional integrals and particle methods",
            "Mathematical paradoxes in statistics"
        ]
    },
    "ai-architecture-advanced": {
        "title": "Advanced AI Architectures Conversations",
        "description": "Exploration of cutting-edge architectures including Mixture of Experts, reasoning models, and novel computational approaches. These conversations push the boundaries of current AI architectural paradigms.",
        "topics": [
            "Mixture of Experts (MoE) systems",
            "Reasoning models and modular architectures",
            "Dynamic model growth and evolution",
            "Vector-space reasoning approaches",
            "Distributed precision architectures",
            "Neural architecture search",
            "Brain-inspired AI designs"
        ]
    },
    "ai-decision-theory": {
        "title": "AI Decision Theory Conversations",
        "description": "Game theory, rational choice, decision-making frameworks and their applications to AI systems. These conversations explore how AI systems can and should make decisions under uncertainty.",
        "topics": [
            "Functional decision theory",
            "Newcomb's paradox variations",
            "Minmax and utility maximization",
            "Information theory applications",
            "Rational choice frameworks",
            "Epistemic decision making",
            "AI transformation dynamics"
        ]
    },
    "ai-capabilities-limits": {
        "title": "AI Capabilities & Limits Conversations",
        "description": "Understanding model capabilities, limitations, context windows, and performance characteristics. These conversations provide practical insights into what current AI systems can and cannot do.",
        "topics": [
            "Context window management",
            "Model finetuning mechanics",
            "Training data reuse patterns",
            "API capabilities and constraints",
            "Multi-role conversation handling",
            "Reasoning display modes",
            "Performance optimization strategies"
        ]
    },
    "ai-code-review": {
        "title": "AI Code Review & Analysis Conversations",
        "description": "AI-assisted code analysis, technical debt resolution, and software development methodologies. These conversations demonstrate practical applications of AI in software engineering.",
        "topics": [
            "Systematic codebase analysis",
            "Technical debt identification",
            "Code quality assessment",
            "API integration patterns",
            "Development methodology with AI",
            "Verification and testing strategies",
            "Architecture evaluation"
        ]
    }
}

# Template for each topic page
page_template = """---
layout: page
title: {title}
permalink: /conversations/{slug}/
---

# {title}

[← Back to Conversations Index](/conversations/)

## Overview

{description}

## Topics Covered

{topics_list}

---

## Full Conversations

{{% raw %}}
{{% include_relative ../test_unlinked/curated/{slug}/CONSOLIDATED_{slug}.md %}}
{{% endraw %}}

---

[← Back to Conversations Index](/conversations/)"""

# Generate pages
for slug, config in topics.items():
    topics_list = "\n".join([f"- {topic}" for topic in config["topics"]])
    
    content = page_template.format(
        title=config["title"],
        slug=slug,
        description=config["description"],
        topics_list=topics_list
    )
    
    filename = f"/Users/scottmcguire/www/conversations/{slug}.md"
    print(f"Creating {filename}")
    
    with open(filename, 'w') as f:
        f.write(content)

print("\nAll topic pages created successfully!")
print("\nNote: For ai-tool-development, you may want to manually add a note about the DID_NOT_FIT_IN_CONTEXT subdirectory.")