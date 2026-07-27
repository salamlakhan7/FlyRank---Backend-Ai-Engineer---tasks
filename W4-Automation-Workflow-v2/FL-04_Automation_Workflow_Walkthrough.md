# Ship an Automation Workflow v2 — Walkthrough
**Code:** FL-04 | **Track:** General AI Fluency | **Author:** Abdul Salam

---

## 1. Pipeline Overview

**Chosen pipeline:** Weekly Backend & AI Engineering Industry Brief

**Why this pipeline:** [1-2 sentences — e.g. "I regularly track backend/AI news manually across multiple sites; this saves that time and produces something reusable."]

### Step Diagram

```
[Raw Sources]
     |
     v
STEP 1: GATHER        -> numbered source list
     |
     v
STEP 2: SYNTHESIZE     -> key facts per source, tagged
     |                    [Backend] [AI/ML] [Tooling] [Other]
     v
STEP 3: DRAFT           -> 4-6 section written brief
     |
     v
STEP 4: REVIEW          -> flagged issues / unsupported claims
     |
     v
STEP 5: FORMAT           -> final publish-ready brief
```

**Human review checkpoint:** [Where a person must check the output before it's trusted/published — e.g. after Step 4, before publishing.]

---

## 2. Tool(s) Used

- [ ] Claude Project (structured instructions)
- [ ] NotebookLM
- [ ] Custom GPT
- [ ] n8n workflow
- [ ] Other: ___________

**Configuration / prompt used:**

```
[Paste your exact Claude Project custom instructions or other tool config here —
this should be the final version you actually ran, not a draft.]
```

---

## 3. The Five Runs

For each run, capture: input, output (or a link/screenshot), time taken, and anything that broke.

### Run 1
- **Input:** [sources/topic used]
- **Output:** [link, paste, or summary of what was produced]
- **Time taken:** ___ min
- **Issues/notes:** [anything that broke, needed manual fixing, or surprised you]

### Run 2
- **Input:**
- **Output:**
- **Time taken:** ___ min
- **Issues/notes:**

### Run 3
- **Input:**
- **Output:**
- **Time taken:** ___ min
- **Issues/notes:**

### Run 4
- **Input:**
- **Output:**
- **Time taken:** ___ min
- **Issues/notes:**

### Run 5 (brand-new input, not used to design the pipeline)
- **Input:**
- **Output:**
- **Time taken:** ___ min
- **Issues/notes:**

---

## 4. Time Accounting

| Item | Time |
|---|---|
| Setup (writing/testing instructions, configuring tool) | ___ min |
| Run 1 | ___ min |
| Run 2 | ___ min |
| Run 3 | ___ min |
| Run 4 | ___ min |
| Run 5 | ___ min |
| **Total (pipeline)** | ___ min |
| **Estimated time doing this manually (per run x5)** | ___ min |
| **Net time saved** | ___ min |

Be honest here — include setup/debugging time. A pipeline that takes 3 hours to build to save 10 minutes/week still has value, but say so plainly.

---

## 5. Known Failure Points

List where the pipeline breaks or produces unreliable output, and what a human must catch:

1. **Failure point:** [e.g. "Synthesize step sometimes merges two distinct facts from one source into one, losing nuance."]
   **Required human check:** [e.g. "Always compare synthesized bullet count to source count before drafting."]

2. **Failure point:**
   **Required human check:**

3. **Failure point:**
   **Required human check:**

---

## 6. Summary

[2-3 sentences: does this pipeline work end-to-end on a new input? Is it worth using again? What would you change next time?] 