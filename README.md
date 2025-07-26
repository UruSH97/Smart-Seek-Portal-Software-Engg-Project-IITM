# Smart-Seek-Portal-Software-Engg-Project-IITM
# Enhancing Programming Education Using Generative AI – SEEK Portal Integration

## Overview

This project explores the **integration of Generative AI (GenAI)** into the IIT Madras **SEEK learning portal** to elevate the self-learning experience for programming students. It addresses pain points like generic feedback, lack of real-time support, and static content delivery by proposing intelligent, interactive GenAI-powered solutions.

---

## Problem Statement

While the SEEK portal is central to student engagement in the IITM BS Degree Program, it currently:
- Offers minimal, generic feedback in programming tests.
- Lacks personalized or real-time support during practice sessions.
- Provides static, one-way content consumption.

---

## Project Goals

- Propose and prototype **effective GenAI-based feedback** for code submissions.
- Develop solutions for **real-time support during programming practice.**
- Create **interactive learning content** from static materials like PDFs or video lectures.

---

## Key Features & Ideas Proposed

### 1. AI-Powered Feedback System
- Analyze learner code using LLMs (e.g., GPT-4, CodeT5)
- Generate feedback beyond test-case failure:
  - Error explanation
  - Code efficiency suggestion
  - Missed edge cases
  - Time-space trade-offs

### 2. In-Editor Support Bot
- Integrate a GenAI chatbot within code editors
- Allows learners to ask conceptual or syntax-level questions
- Provides code snippets, hints, and clarification in real time

### 3. Interactive Content Generation
- Convert static content (PDFs, slides, or videos) into:
  - Quizzable flashcards
  - Conversational summaries
  - Auto-generated practice problems

### 4. Personalized Learning Analytics
- Use learner history to generate:
  - Adaptive coding challenges
  - Feedback on common mistakes
  - Personalized learning path suggestions

---

## Technologies Explored

- **OpenAI GPT-4**, **Mistral-7B**, **CodeT5+**
- **LangChain**, **LlamaIndex**, **Haystack** for content indexing
- **Streamlit / Gradio** for prototyping user interfaces
- **FastAPI** for backend microservices
- **GitHub Copilot / VS Code AI extensions** for embedding support

---

## Methodology

- Reviewed learner pain points through feedback forums and assignment logs.
- Identified integration points in the SEEK portal (assignment results, quizzes, documents).
- Designed prototypes with real code submissions and static PDFs.
- Conducted feasibility analysis of LLM-based API integration with existing SEEK backend.

---

## Project Deliverables

- Concept Prototypes
- GenAI Prompt Engineering Tests
- UI Mockups for:
  - Code feedback screen
  - Chatbot-enabled practice area
  - AI-generated quiz modules
- Design Document
- Final Presentation Deck

---

## Benefits

- Increases learner engagement and autonomy
- Enables formative feedback loops beyond test-case failures
- Promotes deeper understanding through explainable AI
- Democratizes access to support by reducing mentor load

---

## Future Scope

- Plugin-based integration with SEEK IDE
- Multi-language programming support (Python, C++, Java)
- AI-powered plagiarism detection + originality feedback
- On-device inference for privacy-preserving feedback

---

## License

This project is an academic submission under the **Software Engineering Project** of the IIT Madras BS Degree Program.


