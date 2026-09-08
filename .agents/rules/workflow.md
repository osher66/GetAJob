# Workflow & Language Rules

- **Interaction & Hebrew Alignment**:
  - The user communicates in Hebrew.
  - All responses, status summaries, and explanations to the user must be strictly right-aligned (יישור לימין) in Hebrew.
  - Proper handling of mixed Hebrew and English text (טקסט משולב עברית-אנגלית): ensure punctuation, parentheses, English terms, file names, and numbers do not break sentence flow or reverse order (correct bidirectional text flow).
- **Internal Reasoning & Code**:
  - All internal reasoning, tool calls, terminal commands, code, git messages, and technical comments must remain strictly in English.
- **Response Structure & Token Efficiency**:
  - **Status / Explanation (עברית)**: Short, bulleted summary of what was done or needed. No conversational filler, pleasantries, or apologies. Maximum token efficiency.
  - **Code / Actions (English)**: The actual code or commands directly, without repeating explanations inside the code.

