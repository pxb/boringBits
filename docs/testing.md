# Testing

How BusinessBits skills are tested before release, and what the tests have shown so far. The standard applies to every skill. The results are dated and name the commit they ran against.

## The standard

### What every skill carries

Each skill has `evals/evals.json` with:

- **Eval cases**, at least five: a prompt, the expected output in one sentence, and a list of expectations a grader can mark pass or fail. Cases come from real decisions, rewritten with invented businesses and people. No real client, rate or profile value goes in a case.
- **Trigger queries**, exactly twenty: ten that should fire the skill and ten that shouldn't. The ten that shouldn't are near misses, phrased like requests a neighbouring skill should take.

The local test suite checks this shape on every push.

### Trigger checks

A trigger check asks whether the description alone makes the host pick the right skill.

- One fresh session per query, with the skills installed and nothing attached. The host sees the description only.
- Record which skills fired for every query, not just pass or fail.
- A should-fire query passes when its skill fires. A should-not query passes when its skill stays quiet, whether or not a sibling fires.
- Keep the host clean. Turn off the tester's own skills and settings where the host allows it, and say so when it doesn't.
- When a description is widened to fix a miss, rerun the full set, not only the misses, and report both runs. A score on queries the description was tuned against is a score on seen queries, and the results say so.
- Run on two hosts. A miss both hosts share is usually the query, not the description.

### Evals with and without the skill

An eval run asks whether the skill changes the result.

- Run each case twice on the same model: once with the skill available and once without it.
- Where a case needs a business profile, use a synthetic one built from the profile template and labelled synthetic.
- Grade blind. The grader sees both outputs in random order, isn't told which run had the skill, and marks each expectation pass or fail with a one-line quote from the output.
- Grade with a different model family from the one that ran the cases where possible. If the same model ran and graded, say so.
- A skill passes when it beats its baseline. An expectation the skill never moves is cut or rewritten.

### Install checks

Install one skill on a clean host, following the README, and confirm its supporting files arrive and the skill loads in a fresh session. Record the host and the commit.

### Cost

Every query and every eval run is a model session. A full pass over the five Revenue skills is 100 trigger sessions per host, plus two runs per eval case and the grading. Run a sample first (three should-fire and three should-not queries per skill, two eval cases per skill), and run the full set when the sample is clean or before a release.

### Recording results

Each run records the date, the commit, the host, the model, the sample size and every failure by its text. Results go below, newest first, with their caveats. A result without its caveats isn't reported.

## Results

### BusinessBits Revenue batch 1, November 2026

Five skills: business-setup, enquiry, prospecting, proposal, pipeline.

#### Trigger checks

| Run | Host and model | Queries | Should fire | Should not fire | Total |
| --- | --- | --- | --- | --- | --- |
| Sample | Claude Code, Claude Sonnet | 15 | 7/10, then 9/10 after widening three descriptions | 5/5 | 14/15 |
| Full, run 1 | Claude Code, Claude Sonnet, project settings only | 100 | 41/50 | 50/50 | 91/100 |
| Full, run 2, after widening four descriptions | Claude Code, Claude Sonnet, project settings only | 100 | 45/50 | 50/50 | 95/100 |
| Sample | Hermes, default profile model | 30 | 14/15 | 15/15 | 29/30 |

Run 2 per skill, should fire: business-setup 10/10, enquiry 8/10, pipeline 10/10, proposal 10/10, prospecting 7/10. Every skill stayed quiet on all ten of its should-not queries in both full runs, and each of those queries went to the sibling skill it was written for.

The Claude Code checks ran 215 sessions in all, one per query. The full runs were tested at commit `0e5ad9c` for run 1 and `82e5124` for run 2; the Hermes sample at `82e5124`.

All five run 2 misses name something that wasn't attached: "draft a reply to this enquiry", "write an outreach sequence for these three accounts", "find the right person to contact at this firm". In each, the assistant asked for the missing item first, in the skill's own terms. "Research this company before I reach out to them" missed on both hosts for the same reason.

#### Evals with and without the skill

Hermes, default profile model, synthetic profile, two cases per skill, each run with and without the skills, one blind grader.

| Skill | With | Without |
| --- | --- | --- |
| business-setup | 8/8 | 7/8 |
| enquiry | 10/10 | 5/10 |
| pipeline | 9/10 | 6/10 |
| proposal | 7/7 | 6/7 |
| prospecting | 6/6 | 4/6 |
| **All** | **40/41** | **28/41** |

Every skill beat its baseline. Without the skills, the failures sat in the skills' own ground: quoting a price on an enquiry before checking fit, dropping the closing message and the suppression list, and planning outreach to a company whose parent is already a client. The one failure with the skills: in a pipeline review, a deal with no next step got a new step instead of being flagged as a gap first.

#### Install checks

- Claude Code: the enquiry folder copied into a fresh project; the session listed the skill.
- Hermes: `hermes skills install pxb/boringBits/businessbits/revenue/sales/enquiry` into a clean home worked first time. SKILL.md, the evals and the records reference arrived, the scan passed, and a fresh session loaded the skill.

#### Caveats

- The samples are small: 30 trigger queries and ten eval cases on Hermes, 41 expectations in all.
- On Hermes the same model ran the cases and graded them. A grader from another model family is still owed.
- The Claude Code descriptions were widened against the same 100 queries they were scored on.
- The 15-query sample ran with the tester's own skills also loaded. The full runs excluded them.
- Evals with and without the skill have run on one host only.
