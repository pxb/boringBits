# Open questions

Each one changes what gets built. None is answered yet.

1. **Is 43 the right size?** The merge rule is mechanical and the routing rule is enforced, but neither has been tested against how an assistant actually chooses between similar skills. The test is a manifest and ten realistic situations, checking whether the chosen skill matches the intended one.
2. **The portability claim is unproven.** Nothing here has been applied twice from the same file on two different assistants. Until it has, "host-neutral" is a design intention, not a result.
3. **Which track first?** Revenue has money attached this month. Build is the largest gap and the one that pays if the business ships software.
4. **Must the shared rules close before the bodies?** Evidence, authority and state are specified in [06-conventions.md](06-conventions.md) but no skill has been tested against them under pressure.
5. **How is a skill tested?** There are no fixtures. A skill with no fixture cannot be regression-tested when the assistant or the model changes.
6. **What does the manifest cost?** Every skill in an index costs tokens whether or not it is loaded. That was measured for a twelve-skill set and never answered for forty-three.
7. **What is the honest boundary of a skill?** Some functions here are judgement and some are arithmetic wearing judgement's clothes. The second kind belongs in a verifier, and drawing that line well is the difference between a system that works and one that sounds like it does.
