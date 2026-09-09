# Workflow & Language Rules

- **Interaction & Hebrew Alignment**:
  - The user communicates in Hebrew.
  - All responses, status summaries, and explanations to the user must be strictly right-aligned (יישור לימין) in Hebrew. Always wrap the Hebrew output in `<div dir="rtl" style="text-align: right;">` to enforce right-alignment in the IDE chat UI.
  - Proper handling of mixed Hebrew and English text (טקסט משולב עברית-אנגלית): ensure punctuation, parentheses, English terms, file names, and numbers do not break sentence flow or reverse order (correct bidirectional text flow).
- **Internal Reasoning & Code**:
  - All internal reasoning, tool calls, terminal commands, code, git messages, and technical comments must remain strictly in English.
- **Response Structure & Token Efficiency**:
  - **Status / Explanation (עברית)**: Short, bulleted summary of what was done or needed. No conversational filler, pleasantries, or apologies. Maximum token efficiency.
  - **Code / Actions (English)**: The actual code or commands directly, without repeating explanations inside the code.
- **Git & Cloud Push Policy**:
  - Work strictly on the local development server during daily iterations.
  - DO NOT push to GitHub or the cloud after individual steps or fixes.
  - Only commit and push when the user explicitly gives the end-of-day signal ("מסיימים עבודה להיום").


