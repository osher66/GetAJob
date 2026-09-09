# GetAJob — Project Instructions & Workflow Rules

## 1. Interaction & Hebrew Language Rules
- **Language**: The user communicates in Hebrew.
- **Right-Alignment (יישור לימין)**: All responses, status summaries, and user explanations must be strictly right-aligned in Hebrew. Always wrap final Hebrew responses in `<div dir="rtl" style="text-align: right;">` so the IDE chat UI renders bullets, punctuation, and text properly in RTL.
- **Mixed Hebrew-English Flow (טקסט משולב עברית-אנגלית)**: Ensure natural bidirectional text flow. Punctuation, parentheses, code terms, file names, and English numbers must be positioned accurately without breaking sentence order or inverting phrasing.
- **Conciseness & Token Conservation**: Deliver short, bulleted summaries only. Zero conversational filler, pleasantries, or apologies.

## 2. Technical Code & Reasoning
- All internal reasoning, tool calls, shell commands, git commit messages, code, and comments must remain strictly in English.
- Avoid re-analyzing root entry points (app.py, main.py) for frontend/UI-only tasks unless explicitly requested.

## 3. Design System Standard (Mandatory)
- **GetAJob — מפרט מערכת עיצוב v1.0** (Claude Design Handoff v1.0, 8 Sep 2026) is the sole, binding design system for the entire application.
- Before starting work on any screen (Screen 2 / Career Track, Screen 3 / CV Analysis, Auth), explicitly confirm adherence to this specification with the user.

## 4. Git & Cloud Push Policy
- **Local First**: Work strictly on the local development server during day-to-day iterations.
- **No Routine Cloud Push**: DO NOT push commits or files to GitHub / cloud after every individual task or fix.
- **End-of-Day Sync Only**: Only push code to the remote repository when explicitly instructed by the user (e.g., at end of session / 'מסיימים עבודה להיום').
