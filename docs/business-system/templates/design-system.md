# Design system

One source of truth for every value a surface uses. A build that invents a value is a build that will drift.

## The ideology

1. **Values are decided once, in one place.** If a colour, space, size or radius is not in this file, it does not exist.
2. **Scales, not one-offs.** Spacing, type and radii step in a fixed ladder. A value between two steps is a signal that the ladder is wrong, not that an exception is needed.
3. **Compose, do not fork.** A new screen is built from existing components. A new component is added only when no composition says the same thing.
4. **Accessibility is a floor, not a goal.** Contrast, focus order, keyboard reach and labels apply to every component before it is used.
5. **Every deviation is a decision.** Written here, dated, with the reason. Undocumented deviation is a defect, not a style choice.
6. **Naming describes the job.** `danger-action`, not `red-button`. Colour carries meaning, not decoration.

## Tokens

| Group | Values | Notes |
|---|---|---|
| Colour, surface | | background, raised, sunken, overlay |
| Colour, text | | primary, secondary, muted, inverted |
| Colour, intent | | success, warning, danger, info |
| Spacing | | the ladder, in one unit |
| Type | | size and line-height pairs, weight roles |
| Radius | | |
| Elevation | | |

## Components

| Component | Purpose | States | Built from |
|---|---|---|---|
| | | default, hover, focus, active, disabled, loading, error, empty | |

## Rules a build must follow

- Every value comes from a token. No literal colour, size or spacing in a component.
- Every interactive element has a visible focus state and a keyboard path.
- Every state in the component table is implemented or explicitly out of scope.
- Loading and empty states are designed, not left to defaults.
- Text never carries meaning by colour alone.

## Conformance check

Machine-readable where possible, so review is not an opinion:

- no literal values outside the tokens file
- every component in use appears in the component table
- contrast ratios within their threshold
- every state present, or listed as excluded

## Change log

| Date | Change | Reason | Decided by |
|---|---|---|---|
