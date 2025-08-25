---
layout: default
title: "Identification Problem in Supply-Demand Models"
permalink: /conversations/featured/identification-problem-in-supply-demand-models/
---

# Identification Problem in Supply-Demand Models

[← Back to Conversations](/conversations/) | [← Featured Conversations](/conversations/#featured)

---

# Solving the Identification Problem in Supply and Demand Models

**Created:** 2025-05-13T14:08:32.590971Z
**Updated:** 2025-05-13T15:43:54.154740Z
**UUID:** 605650e3-c9cc-4ae8-9afc-65550c7d597a

---

## User

Can you write a self-contained, simple document explaining what goes wrong if one calibrates a model of supply to price and a model of demand to price, and then tries to solve for market clearing prices?

## Claude

The human is asking me to write a document that explains what goes wrong when someone tries to do the following:
1. Calibrate a model of supply to price (i.e., create a supply function that depends on price)
2. Calibrate a model of demand to price (i.e., create a demand function that depends on price)
3. Try to solve for market clearing prices (i.e., find the price where supply equals demand)

This is an interesting economics/econometrics question about a common mistake in modeling market equilibrium. Let me think about what goes wrong in this approach:

The fundamental issue here is an identification problem. If we observe market data, we're typically observing equilibrium points where supply equals demand. Each observation is a price-quantity pair that represents a market clearing condition. 

When we try to separately estimate supply and demand functions using these equilibrium observations:

1. **Simultaneity bias**: The price is not an exogenous variable that independently determines supply or demand; rather, price and quantity are jointly determined in the market. This creates an endogeneity problem.

2. **Identification challenge**: Without additional information or restrictions, we cannot distinguish between supply and demand shifts just by looking at price-quantity pairs. The observed data points are intersections of supply and demand curves, not the curves themselves.

3. **Circular reasoning**: If we calibrate supply as a function of price and demand as a function of price, we're assuming price is exogenous. But when we then try to solve for the market clearing price, we're treating price as endogenous. This inconsistency creates a logical problem.

4. **Omitted variable bias**: External factors that shift supply or demand curves (like weather for agricultural products, technology changes, income shifts, etc.) need to be included to properly identify the curves.

The correct approach typically involves:
- Using instrumental variables that shift only supply or only demand
- Incorporating exogenous shifters of supply and demand
- Using structural models with identifying restrictions
- Utilizing natural experiments or policy changes that affect only one side of the market

I'll write a document explaining these issues in a clear, self-contained way that someone could understand even if they're not deeply familiar with econometrics.# The Identification Problem in Supply and Demand Models

## The Fundamental Issue

When economists attempt to model markets, a common mistake is to independently calibrate supply and demand functions to price, then solve for market clearing equilibrium. This approach creates a fundamental identification problem.

## What Goes Wrong

### 1. Simultaneity Bias

In real markets, prices and quantities are determined simultaneously through the interaction of supply and demand. When we calibrate supply as a function of price or demand as a function of price, we incorrectly treat price as an exogenous variable when it is, in fact, endogenous.

### 2. The Identification Challenge

When we observe market data, we typically see only equilibrium points where supply equals demand. These observations represent intersections of the supply and demand curves, not the curves themselves. Without additional information, it's impossible to determine whether a price change caused movement along a curve or a shift of the entire curve.

Consider this example:
- We observe that when price is $5, quantity is 100 units
- We observe that when price is $7, quantity is 120 units

Does this mean that:
- Supply increased with higher prices (moving along the supply curve), or
- Demand increased, shifting the demand curve and raising both price and quantity?

From equilibrium data alone, we cannot tell.

### 3. Circular Logic

The approach creates circular reasoning:
- Step 1: We treat price as exogenous when calibrating supply and demand functions
- Step 2: We then try to solve for price as if it were endogenous

This inconsistency makes the resulting model invalid for predicting market behavior.

## The Solution: Proper Identification Strategies

To correctly model supply and demand, economists use several techniques:

1. Instrumental variables that shift only supply or only demand
2. Exogenous shifters (e.g., weather for agricultural supply, income for demand)
3. Natural experiments or policy changes affecting only one side of the market
4. Simultaneous equation methods that explicitly account for the joint determination of price and quantity

By addressing the identification problem directly, these approaches allow us to estimate supply and demand parameters that can reliably predict market outcomes.

## User

Can you make it more mathematical, which keeping simplicity, while also making it less verbose but still pedagogical? Like, *mostly* equations, with enough text to motivate, but *simple* equations.

## Claude

I'll rewrite the document to be more mathematical but still simple and accessible. I'll use basic equations to illustrate the identification problem, with minimal but sufficient text to explain the concepts.

I'll structure it as follows:
1. Brief introduction to the problem
2. Mathematical setup of supply and demand functions
3. The identification problem shown mathematically
4. Simple graphical/mathematical intuition
5. Brief mention of solutions

I'll use simple linear supply and demand functions to illustrate the concepts, as these are easy to understand while still capturing the core problem.# The Identification Problem in Supply and Demand

## Setup

Consider a simple market with linear supply and demand functions:

**Supply:** $Q_s = a + bP$, where $b > 0$

**Demand:** $Q_d = c - dP$, where $d > 0$

Market clearing requires: $Q_s = Q_d$

## The Problem

### Flawed Approach
Suppose we observe equilibrium points $(P_t, Q_t)$ for periods $t = 1,2,...,T$.

If we regress quantity on price:
$Q_t = \alpha + \beta P_t + \epsilon_t$

What does $\beta$ represent? Supply slope $b$? Demand slope $-d$? Neither?

### Mathematical Illustration

For each observation, both equations hold simultaneously:
$Q_t = a + bP_t + \epsilon_{st}$ (Supply)
$Q_t = c - dP_t + \epsilon_{dt}$ (Demand)

At equilibrium:
$a + bP_t + \epsilon_{st} = c - dP_t + \epsilon_{dt}$

Solving for $P_t$:
$P_t = \frac{c - a + \epsilon_{dt} - \epsilon_{st}}{b + d}$

This shows $P_t$ is correlated with both error terms, creating endogeneity.

## Visual Intuition

Consider two equilibrium points $(P_1, Q_1)$ and $(P_2, Q_2)$ where $P_2 > P_1$ and $Q_2 > Q_1$:

`%%%BACKTICK0%%%`

Is this:
- Movement along supply curve? (Demand shifted)
- Movement along demand curve? (Supply shifted)
- Both curves shifted?

Equilibrium data alone cannot tell us.

## Solution Approaches

1. **Instrumental Variables**: Find $Z_s$ affecting only supply and $Z_d$ affecting only demand.

   Supply with instrument: $Q_s = a + bP + γZ_s$
   
   Demand with instrument: $Q_d = c - dP + δZ_d$

2. **Simultaneous Equation Estimation**: Estimate both equations as a system, accounting for endogeneity.

The key insight: To identify both curves, we need exogenous variation that shifts one curve while holding the other fixed.

## User

Can we keep supply and demand separate? Let's say there are two avenues for purchasing the good and two avenues for producing it. Then supply and demand are observed separately.

## Claude

The human is suggesting an interesting variation where supply and demand can be observed separately through different channels or markets. This is a good approach to addressing the identification problem in a simple but mathematical way.

Let me create a revised model where:
1. There are two avenues/channels for purchasing the good (two demand channels)
2. There are two avenues/channels for producing the good (two supply channels)
3. This separation allows us to observe supply and demand independently

This setup could help illustrate why naive calibration fails while keeping the math simple.# Identification Problem with Separate Channels

## Setup

Consider a market with separate observation channels:

### Supply Channels
- Channel 1: $Q_{s1} = a_1 + b_1P + ε_{s1}$
- Channel 2: $Q_{s2} = a_2 + b_2P + ε_{s2}$
- Total Supply: $Q_s = Q_{s1} + Q_{s2} = (a_1 + a_2) + (b_1 + b_2)P + (ε_{s1} + ε_{s2})$

### Demand Channels
- Channel 1: $Q_{d1} = c_1 - d_1P + ε_{d1}$
- Channel 2: $Q_{d2} = c_2 - d_2P + ε_{d2}$
- Total Demand: $Q_d = Q_{d1} + Q_{d2} = (c_1 + c_2) - (d_1 + d_2)P + (ε_{d1} + ε_{d2})$

## The Problem

Suppose we observe $(P_t, Q_{s1,t}, Q_{s2,t}, Q_{d1,t}, Q_{d2,t})$ for periods $t$.

### Naive Calibration Approach:

1. Estimate supply using observed supply quantities:
   $Q_{s,t} = α_s + β_sP_t + u_{s,t}$

2. Estimate demand using observed demand quantities:
   $Q_{d,t} = α_d + β_dP_t + u_{d,t}$

3. Solve for market clearing price:
   $Q_s = Q_d$
   $α_s + β_sP = α_d + β_dP$
   $P^* = \frac{α_d - α_s}{β_s - β_d}$

### The Error:

Even with separate observations of supply and demand quantities, price $P_t$ is determined in the market by:
$Q_{s,t} = Q_{d,t}$
$(a_1 + a_2) + (b_1 + b_2)P_t + (ε_{s1,t} + ε_{s2,t}) = (c_1 + c_2) - (d_1 + d_2)P_t + (ε_{d1,t} + ε_{d2,t})$

Solving for $P_t$:
$P_t = \frac{(c_1 + c_2) - (a_1 + a_2) + (ε_{d1,t} + ε_{d2,t}) - (ε_{s1,t} + ε_{s2,t})}{(b_1 + b_2) + (d_1 + d_2)}$

This shows $P_t$ is still correlated with the error terms in both supply and demand equations, creating endogeneity.

## Mathematical Consequence

When we estimate:
$Q_{s,t} = α_s + β_sP_t + u_{s,t}$

The OLS estimate $β_s$ is biased because:
$cov(P_t, u_{s,t}) ≠ 0$

Similarly for demand estimation.

## Solution

Use exogenous variation that affects only one channel:

1. Supply shifter $Z_s$ that affects only supply: $Q_{s,t} = α_s + β_sP_t + γZ_{s,t} + u_{s,t}$

2. Demand shifter $Z_d$ that affects only demand: $Q_{d,t} = α_d + β_dP_t + δZ_{d,t} + u_{d,t}$

This allows consistent estimation of the supply and demand parameters, leading to valid market clearing predictions.

## User

What's the simplest way to show that error - feature correlation introduces bias?

## Claude

I need to provide a simple mathematical demonstration of how correlation between an error term and an explanatory variable (feature) introduces bias in regression estimates. I'll focus on making this as simple and clear as possible while still being mathematically rigorous.

For a linear regression, the simplest way to show this is to derive the expected value of the OLS estimator and show that it deviates from the true parameter when there's correlation between the error and the explanatory variable.

Let me start with a simple univariate regression model:
y = βx + ε

Where:
- y is the dependent variable
- x is the explanatory variable/feature
- β is the true parameter we want to estimate
- ε is the error term

The OLS estimator for β is:
β̂ = (x'x)^(-1)x'y

If we substitute y = βx + ε:
β̂ = (x'x)^(-1)x'(βx + ε)
β̂ = (x'x)^(-1)x'βx + (x'x)^(-1)x'ε
β̂ = β + (x'x)^(-1)x'ε

Now, taking the expectation:
E[β̂] = E[β + (x'x)^(-1)x'ε]
E[β̂] = β + E[(x'x)^(-1)x'ε]

Under the standard OLS assumption, E[ε|x] = 0, which implies E[x'ε] = 0, and thus:
E[β̂] = β

However, if there is correlation between x and ε, then E[x'ε] ≠ 0, and:
E[β̂] = β + bias

Where bias = E[(x'x)^(-1)x'ε] ≠ 0

This is a clear but somewhat abstract demonstration. I could make it even more concrete with a simple numerical example or by expressing the bias in terms of correlation. I'll go with a simple expression of the bias in terms of correlation for a univariate case.

For a simple univariate regression with one feature x:
β̂ = Σ(x_i·y_i)/Σ(x_i²)

Substituting y_i = βx_i + ε_i:
β̂ = Σ(x_i·(βx_i + ε_i))/Σ(x_i²)
β̂ = βΣ(x_i²)/Σ(x_i²) + Σ(x_i·ε_i)/Σ(x_i²)
β̂ = β + Σ(x_i·ε_i)/Σ(x_i²)

Taking expectations:
E[β̂] = β + E[Σ(x_i·ε_i)/Σ(x_i²)]

For large samples, this converges to:
E[β̂] = β + Cov(x,ε)/Var(x)

If Cov(x,ε) = 0, then E[β̂] = β (unbiased)
If Cov(x,ε) ≠ 0, then E[β̂] ≠ β (biased)

The bias is directly proportional to the covariance between x and ε, and inversely proportional to the variance of x.

This is a very simple and direct demonstration of how correlation between a feature and the error term introduces bias in regression estimates. I'll use this approach in my answer.# Feature-Error Correlation and Bias: A Simple Proof

Consider a linear regression model:

$y = \beta x + \varepsilon$

The OLS estimator is:

$\hat{\beta} = \frac{\sum x_i y_i}{\sum x_i^2}$

## Derivation of Bias

Substituting $y_i = \beta x_i + \varepsilon_i$ into the estimator:

$\hat{\beta} = \frac{\sum x_i (\beta x_i + \varepsilon_i)}{\sum x_i^2}$

$\hat{\beta} = \beta\frac{\sum x_i^2}{\sum x_i^2} + \frac{\sum x_i\varepsilon_i}{\sum x_i^2}$

$\hat{\beta} = \beta + \frac{\sum x_i\varepsilon_i}{\sum x_i^2}$

Taking the expectation:

$E[\hat{\beta}] = \beta + E\left[\frac{\sum x_i\varepsilon_i}{\sum x_i^2}\right]$

For large samples, this converges to:

$E[\hat{\beta}] = \beta + \frac{Cov(x,\varepsilon)}{Var(x)}$

## The Result

If $Cov(x,\varepsilon) = 0$: Estimator is unbiased
$E[\hat{\beta}] = \beta$

If $Cov(x,\varepsilon) \neq 0$: Estimator is biased
$E[\hat{\beta}] = \beta + \text{Bias}$

where $\text{Bias} = \frac{Cov(x,\varepsilon)}{Var(x)}$

## Application to Supply-Demand

In our market model, price $P$ is correlated with both supply and demand errors by construction, as:

$P = \frac{(c_1+c_2)-(a_1+a_2)+(\varepsilon_{d1}+\varepsilon_{d2})-(\varepsilon_{s1}+\varepsilon_{s2})}{(b_1+b_2)+(d_1+d_2)}$

Therefore $Cov(P,\varepsilon_s) \neq 0$ and $Cov(P,\varepsilon_d) \neq 0$

This makes OLS estimates of supply and demand functions biased, invalidating market clearing predictions.

## User

If I were explaining it to someone, could I just say \epsilon = \gamma x + \epsilon_{\mbox{othogonal}} ?

## Claude

Yes, that's a great simplification for explaining the issue. Let me elaborate on this approach:

The notation $\epsilon = \gamma x + \epsilon_{\text{orthogonal}}$ directly decomposes the error term into two parts:
1. A component that is correlated with the regressor x (represented by $\gamma x$)
2. A component that is orthogonal to (uncorrelated with) the regressor (represented by $\epsilon_{\text{orthogonal}}$)

Using this decomposition, I can show the bias very cleanly:

Starting with the linear model:
$y = \beta x + \epsilon$

Substituting the error decomposition:
$y = \beta x + (\gamma x + \epsilon_{\text{orthogonal}})$
$y = (\beta + \gamma) x + \epsilon_{\text{orthogonal}}$

So when we regress y on x, we're actually estimating $(\beta + \gamma)$ rather than just $\beta$.

The bias is exactly $\gamma$, which represents the coefficient in the projection of the error term onto x.

This is a very intuitive way to explain the issue without going through all the algebraic derivations I showed in my previous response. It directly shows that when the error term has a component correlated with x (i.e., when $\gamma \neq 0$), the OLS estimator will be biased.

For the supply and demand context, this means that if we have:
- $Q_s = a + bP + \epsilon_s$ where $\epsilon_s = \gamma_s P + \epsilon_{s,\text{orthogonal}}$
- $Q_d = c - dP + \epsilon_d$ where $\epsilon_d = \gamma_d P + \epsilon_{d,\text{orthogonal}}$

Then when we regress:
- We'll get $\hat{b} = b + \gamma_s$ for supply
- We'll get $\hat{d} = -d + \gamma_d$ for demand

Which biases our estimates and invalidates the market clearing solution.

This is a very simple and intuitive way to explain the problem.# Feature-Error Correlation and Bias: A Minimal Proof

## The Error Decomposition Approach

For any regression $y = \beta x + \epsilon$, we can always decompose the error as:

$\epsilon = \gamma x + \epsilon_{\perp}$

Where:
- $\epsilon_{\perp}$ is orthogonal to $x$ (i.e., $Cov(x, \epsilon_{\perp}) = 0$)
- $\gamma$ measures the correlation between $x$ and $\epsilon$

## The Consequence

Substituting into the original model:

$y = \beta x + (\gamma x + \epsilon_{\perp})$

$y = (\beta + \gamma)x + \epsilon_{\perp}$

When we regress $y$ on $x$, we estimate $(\beta + \gamma)$, not $\beta$.

## Application to Supply-Demand

For supply: $Q_s = a + bP + \epsilon_s$

If $\epsilon_s = \gamma_s P + \epsilon_{s\perp}$, then:
$Q_s = a + (b + \gamma_s)P + \epsilon_{s\perp}$

For demand: $Q_d = c - dP + \epsilon_d$

If $\epsilon_d = \gamma_d P + \epsilon_{d\perp}$, then:
$Q_d = c + (-d + \gamma_d)P + \epsilon_{d\perp}$

Our estimated parameters $(b + \gamma_s)$ and $(-d + \gamma_d)$ are biased, leading to incorrect market clearing solutions.

## In the Market Context

Because $P$ is determined by both supply and demand shocks, it is necessarily correlated with both error terms, making $\gamma_s \neq 0$ and $\gamma_d \neq 0$.

This simple decomposition makes the source and impact of the bias immediately clear.

## User

Could doing all the pairwise regressions be a brute force way to address the issue?

## Claude

The user is asking if doing all pairwise regressions could be a brute force way to address the identification problem in supply and demand models. Let me think about what "all the pairwise regressions" might mean in this context and whether it could solve the issue.

In the supply-demand context with separate channels, we have:
- Supply channels: $Q_{s1}$ and $Q_{s2}$ as functions of price $P$
- Demand channels: $Q_{d1}$ and $Q_{d2}$ as functions of price $P$

Pairwise regressions could mean:
1. Regressing each quantity on price: $Q_{s1}$ on $P$, $Q_{s2}$ on $P$, $Q_{d1}$ on $P$, $Q_{d2}$ on $P$
2. Regressing total supply $Q_s$ on $P$ and total demand $Q_d$ on $P$
3. Regressing quantities on each other: $Q_{s1}$ on $Q_{s2}$, $Q_{d1}$ on $Q_{d2}$, etc.
4. Regressing supply quantities on demand quantities: $Q_{s1}$ on $Q_{d1}$, $Q_{s1}$ on $Q_{d2}$, etc.

The fundamental issue in all these cases remains: the price $P$ is endogenous, determined by the equilibrium condition that total supply equals total demand. As long as we're using observed market prices, the endogeneity problem persists regardless of which quantities we're regressing on price.

However, there might be a way to interpret "pairwise regressions" that could help address the issue. If we have multiple market equilibria observed under different conditions (like different regions, time periods, etc.), we could potentially use these variations to identify the supply and demand parameters.

Let me think about whether pairwise regressions across different market equilibria could help...

If we have multiple markets or time periods with different exogenous shifters affecting either supply or demand, then comparing these different equilibria might allow us to trace out the supply and demand curves. This is essentially what instrumental variables or natural experiments try to do.

But simply doing more regressions with the same endogenous variables won't solve the core identification problem. The key is having exogenous variation that shifts one curve but not the other.

Let me see if I can provide a clear mathematical explanation of whether pairwise regressions could help or not.# Pairwise Regressions: A Brute Force Approach?

## The Pairwise Regression Concept

Consider our model with separate channels:
- Supply: $Q_{s1}$ and $Q_{s2}$
- Demand: $Q_{d1}$ and $Q_{d2}$

The pairwise regression approach would estimate:
- $Q_{s1} = α_{s1} + β_{s1}P + ε_{s1}$
- $Q_{s2} = α_{s2} + β_{s2}P + ε_{s2}$
- $Q_{d1} = α_{d1} + β_{d1}P + ε_{d1}$
- $Q_{d2} = α_{d2} + β_{d2}P + ε_{d2}$

## Why It Doesn't Solve the Problem

The fundamental issue remains: $P$ is correlated with all error terms.

To see this, market clearing requires:
$Q_{s1} + Q_{s2} = Q_{d1} + Q_{d2}$

Substituting our equations:
$(α_{s1} + β_{s1}P + ε_{s1}) + (α_{s2} + β_{s2}P + ε_{s2}) = (α_{d1} + β_{d1}P + ε_{d1}) + (α_{d2} + β_{d2}P + ε_{d2})$

Solving for $P$:
$P = \frac{(α_{d1}+α_{d2})-(α_{s1}+α_{s2})+(ε_{d1}+ε_{d2})-(ε_{s1}+ε_{s2})}{(β_{s1}+β_{s2})-(β_{d1}+β_{d2})}$

This shows $P$ is directly a function of all error terms, making all four regressions biased.

## When Pairwise Comparisons Might Help

If each channel faces different exogenous shifters:
$Q_{s1} = α_{s1} + β_{s1}P + γ_{s1}Z_{s1} + ε_{s1}$
$Q_{s2} = α_{s2} + β_{s2}P + γ_{s2}Z_{s2} + ε_{s2}$
$Q_{d1} = α_{d1} + β_{d1}P + γ_{d1}Z_{d1} + ε_{d1}$
$Q_{d2} = α_{d2} + β_{d2}P + γ_{d2}Z_{d2} + ε_{d2}$

Comparing markets with different values of these shifters can trace out the supply and demand curves.

## The Minimal Solution

Rather than multiple regressions, the key is finding instrumental variables:
- For supply: variables $Z_s$ where $Cov(Z_s,ε_d)=0$ and $Cov(Z_s,P)≠0$
- For demand: variables $Z_d$ where $Cov(Z_d,ε_s)=0$ and $Cov(Z_d,P)≠0$

This achieves identification without the complexity of multiple pairwise regressions.

## User

Also the components of supply and demand on each other

## Claude

The human is suggesting looking at the relationship between components of supply and demand on each other as a potential solution to the identification problem. Let me explore this idea more carefully.

In our model, we have:
- Supply channels: Q_{s1} and Q_{s2}
- Demand channels: Q_{d1} and Q_{d2}

The human seems to be suggesting that we consider regressions between these components, such as:
- Q_{s1} on Q_{d1}
- Q_{s1} on Q_{d2}
- Q_{s2} on Q_{d1}
- Q_{s2} on Q_{d2}

Or possibly:
- Q_{s1} on Q_{s2}
- Q_{d1} on Q_{d2}

Let me think about whether these component-wise regressions could help with identification:

1. For regressions across supply and demand channels (e.g., Q_{s1} on Q_{d1}):
   At market equilibrium, these components are related through price. The relationship would capture both the direct price effect and the indirect effects of any shocks.
   
2. For regressions within supply or demand channels (e.g., Q_{s1} on Q_{s2}):
   These might reveal relationships between different segments of the market on the same side.

The key question is: Do these component-wise relationships provide additional identifying information?

I need to consider if these regressions avoid the endogeneity problem we've been discussing. The challenge is that all these quantities are determined simultaneously with price in equilibrium.

Let me think about this mathematically. If we try to regress Q_{s1} on Q_{d1}:

Q_{s1} = a_1 + b_1P + ε_{s1}
Q_{d1} = c_1 - d_1P + ε_{d1}

We could try to relate them directly:
Q_{s1} = α + βQ_{d1} + u

But since both Q_{s1} and Q_{d1} are functions of P, and P is determined by all error terms in the system, this regression would also suffer from endogeneity.

However, there might be a way to exploit the component structure if there are specific shocks that only affect certain components.# Components of Supply and Demand: Cross-Channel Regression Analysis

## Cross-Channel Regressions

Consider running regressions between supply and demand channels:

- $Q_{s1} = α_{1} + β_{1}Q_{d1} + ε_{1}$
- $Q_{s1} = α_{2} + β_{2}Q_{d2} + ε_{2}$
- $Q_{s2} = α_{3} + β_{3}Q_{d1} + ε_{3}$
- $Q_{s2} = α_{4} + β_{4}Q_{d2} + ε_{4}$

## The Endogeneity Persists

Substituting the original equations:

$Q_{s1} = a_1 + b_1P + ε_{s1}$
$Q_{d1} = c_1 - d_1P + ε_{d1}$

Into the regression $Q_{s1} = α_{1} + β_{1}Q_{d1} + ε_{1}$:

$a_1 + b_1P + ε_{s1} = α_{1} + β_{1}(c_1 - d_1P + ε_{d1}) + ε_{1}$

Rearranging:
$a_1 + b_1P + ε_{s1} = α_{1} + β_{1}c_1 - β_{1}d_1P + β_{1}ε_{d1} + ε_{1}$

$(b_1 + β_{1}d_1)P = α_{1} + β_{1}c_1 - a_1 + β_{1}ε_{d1} + ε_{1} - ε_{s1}$

This shows $Q_{d1}$ is correlated with the error term in the regression, as both depend on $ε_{s1}$ and $ε_{d1}$.

## Within-Channel Regressions

Consider regressions within supply or demand:

- $Q_{s1} = α_s + β_sQ_{s2} + ε_s$
- $Q_{d1} = α_d + β_dQ_{d2} + ε_d$

These also suffer from endogeneity as both components depend on the same price $P$, which is influenced by all error terms.

## A Potential Solution: Hierarchical Identification

If channels operate in sequence with observed intermediate outcomes:

1. First-stage:
   - $Q_{s1} = a_1 + b_1P_{intermediate} + ε_{s1}$
   - $Q_{d1} = c_1 - d_1P_{intermediate} + ε_{d1}$

2. Second-stage:
   - $P_{intermediate} = f(Q_{s1}, Q_{d1})$
   - $Q_{s2} = a_2 + b_2P_{final} + ε_{s2}$
   - $Q_{d2} = c_2 - d_2P_{final} + ε_{d2}$
   - $P_{final} = g(P_{intermediate}, Q_{s2}, Q_{d2})$

This sequential structure could allow identification if intermediate prices and quantities are observed.

## Summary

Simply regressing components against each other doesn't solve the endogeneity problem. The key requirement remains finding exogenous variation (instruments) or exploiting structural features like timing differences that break the simultaneity.



---

[← Back to Conversations](/conversations/) | [← Featured Conversations](/conversations/#featured)
