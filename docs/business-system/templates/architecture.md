# Architecture

How this is built, why, and what would make us change it. Written before the first chunk is dispatched, kept current as decisions land.

## Context

What the product does, who uses it, and the constraints that are not negotiable: budget, hosting, regulatory, platform, team size.

## Shape

| Part | Responsibility | Owns which data | Talks to |
|---|---|---|---|

## Boundaries

- What sits inside the boundary and is ours to change freely.
- What sits outside and can only be reached through a stated interface.
- Where data is authoritative, and where it is a copy.

## Interfaces

| Interface | Direction | Contract | Failure behaviour |
|---|---|---|---|

## Decisions

Each decision gets a row. A decision without a rejected alternative is a preference.

| Date | Decision | Alternative rejected | Consequence | Revisit if |
|---|---|---|---|---|

## Failure and recovery

- What fails first under load, and what the user sees.
- What is backed up, how often, and when a restore was last proved.
- What can be rolled back, and what cannot.

## What would make us change it

The conditions under which this document is wrong: a scale threshold, a cost, a platform limit, a requirement that arrives.
