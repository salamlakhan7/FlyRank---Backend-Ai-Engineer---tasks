# Agent Concepts and MCP Basics — Deliverable
**Code:** FL-05 | **Track:** General AI Fluency | **Author:** Abdul Salam

---

## 1. Workflow vs. Agent — Applied to FL-04

**My own-words definition:**
[Rewrite in your own words: a workflow follows a predefined sequence of steps set by a human/code; an agent decides its own next steps dynamically based on what it observes, often looping until a goal is met.]

**Classification of my FL-04 pipeline:** Workflow

**Why:** [State briefly — fixed 5-step sequence (gather→synthesize→draft→review→format), I supply sources manually, no dynamic tool use or looping.]

---

## 2. MCP Primitives — Quick Notes

- **Tools:** [your own-words definition + example from your connector]
- **Resources:** [your own-words definition + example]
- **Prompts:** [your own-words definition + example, if your connector exposes any]

---

## 3. Connector Setup

**Connector used:** [e.g. Filesystem MCP server / GitHub MCP connector]

**Client used:** [e.g. Claude Desktop]

**Setup evidence:** [screenshot of config + tools icon showing connector is live]

---

## 4. Three Tasks Requiring Tool Calls

For each: the exact prompt you ran, why plain chat couldn't have done it, and a screenshot/output as evidence.

### Task 1
- **Prompt:**
- **Why chat alone couldn't do this:**
- **Evidence:** [screenshot/output]

### Task 2
- **Prompt:**
- **Why chat alone couldn't do this:**
- **Evidence:**

### Task 3
- **Prompt:**
- **Why chat alone couldn't do this:**
- **Evidence:**

---

## 5. Agent Upgrade for FL-04

**Concrete upgrade:** Make the Gather step dynamic — give the model an MCP search tool and a goal instead of pre-supplied sources, so it decides how many/which sources are relevant and when it has enough, looping if needed.

**Why this crosses the workflow→agent line:** [explain: the model now controls its own path/decisions instead of following a path I set in advance]

---

## 6. Explainer (600-900 words)

[Paste your final, rewritten-in-your-own-words explainer here before submitting — covering: what a workflow is, what an agent is, your FL-04 classification, what MCP is + its three primitives, and the concrete agent upgrade.]

**Word count:** ___

---

## 7. Submission Checklist

- [ ] Explainer is technically correct and in my own words (not copied from Anthropic's essay)
- [ ] Workflow vs. agent distinction correctly applied to FL-04
- [ ] Connector screenshots show tool calls, not plain chat responses
- [ ] All 3 tasks are things chat alone could not have done
- [ ] One concrete agent upgrade named and justified