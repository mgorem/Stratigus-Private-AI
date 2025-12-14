# Private AI: Cybersecurity and Privacy Challenges in the Age of Generative AI  
*A Remote Group Internship Project – Stratigus Consulting*

## Project Overview

This repository documents a **remote group internship project** conducted in collaboration with **Stratigus Consulting**, focused on exploring the **cybersecurity and privacy challenges of generative AI** and the emerging opportunity for **Private AI** solutions.

As part of this project, the team ultimately developed a **prototype Private AI system** to demonstrate how AI-powered analysis can be performed **locally**, without sending sensitive data to cloud-based large language models. The prototype serves as a practical illustration of the research findings rather than the starting point of the project.

The internship was completed over **three months** by a **team of four students**, following a structured, milestone-driven approach. One team member acted as the **team lead**, responsible for coordinating tasks, managing weekly deliverables, and integrating research, technical, and documentation outputs.

## System Summary (Prototype)

The final prototype developed during the later stages of the internship demonstrates a **local-first AI analysis workflow** designed with privacy and security in mind:

- Users submit a URL or query via a web interface or desktop application.
- Web content is retrieved through a controlled tool rather than direct browsing by the AI model.
- Analysis is performed by a **locally deployed large language model** using **LM Studio**, ensuring data remains within a trusted environment.
- Privacy safeguards, such as detection of potentially sensitive input and optional “no-store” execution, are applied before processing.
- Results are returned to the user interface for review or demonstration.

This system was built incrementally to support research, testing, and education, and is not intended to represent a production-ready AI platform.

## Host Organisation: Stratigus Consulting

**Stratigus Consulting** is a strategy and consulting firm dedicated to solving complex challenges across industries by leveraging innovation, technology, and evidence-based insights. Stratigus supports organisations in navigating disruption, designing scalable solutions, and building resilience in a rapidly changing business environment.

With a focus on future-oriented domains including **cybersecurity**, **artificial intelligence**, **digital transformation**, and **sustainability**, Stratigus combines strategic thinking with hands-on problem solving to deliver measurable outcomes.


## ABOUT THE PROJECT

## Project Name

**Private AI: Cybersecurity and Privacy Challenges in the Age of Generative AI**

## Project Context and Motivation

Generative AI tools such as **OpenAI’s ChatGPT**, **Microsoft Copilot**, and similar cloud-based platforms have become mainstream across industries. While these tools deliver significant productivity gains, they introduce serious **cybersecurity and privacy concerns**, particularly because sensitive data is often processed and stored in the cloud.

For sectors such as:
- Law firms  
- Healthcare providers  
- Financial services  
- Government organisations  

the exposure of confidential or regulated data to cloud-based AI systems presents unacceptable risk.

This project responds to growing interest in **Private AI** — powerful AI systems that run locally, on controlled infrastructure, reducing external data exposure. While platforms such as **LM Studio** enable local AI deployment, many organisations lack clear guidance on:
- Risks and limitations
- Technical requirements
- Secure deployment practices
- Appropriate use cases


## Project Objectives

The internship project was designed to achieve the following objectives:

- Research and analyse cybersecurity and privacy risks associated with mainstream AI platforms.
- Investigate market demand for Private AI across industries and regions.
- Explore and test Private AI platforms, including local LLM deployments.
- Compare cloud-based AI and local AI from a security and privacy perspective.
- Develop educational and strategic resources to support responsible Private AI adoption.
- Provide Stratigus with market-informed insights and recommendations in the Private AI space.


## How the Final System Works (Prototype Overview)

As the project progressed from research into technical exploration, a **prototype Private AI system** was developed to demonstrate key concepts:

1. **User Interaction**  
   Users interact with the system via a web interface or desktop application to submit URLs or analysis queries.

2. **Controlled Web Content Retrieval**  
   Web content is retrieved through a controlled tool function, limiting the AI model’s direct exposure to external inputs.

3. **Local AI Processing**  
   Analysis is performed by a **locally deployed LLM** using LM Studio, ensuring data remains on the user’s machine or controlled environment.

4. **Security and Privacy Safeguards**  
   The system includes safeguards such as:
   - Prompt constraints to mitigate prompt injection risks
   - Detection of potentially sensitive input
   - Optional redaction and “no-store” (ephemeral) execution modes

5. **Results and Demonstration**  
   Outputs are returned to the user interface and can optionally be logged for demonstration and audit purposes.

This prototype serves as a **technical proof of concept**, supporting the broader research and educational goals of the project.


## Project Milestones and Weekly Progression

### Milestone 1 – Market Research & Problem Framing
**Weeks 1–4**

- Introduction to Stratigus and project objectives
- Review of the current AI landscape, focusing on cloud-based tools
- Identification of cybersecurity and privacy risks through literature and case studies
- Mapping of high-risk sectors (law, healthcare, finance, government)
- Design and distribution of surveys to understand market attitudes
- Analysis of survey responses to refine project scope

**Deliverable:** Interim Market Research Report


### Milestone 2 – Technical Exploration
**Weeks 5–7**

- Exploration of Private AI tools such as LM Studio
- Comparison of cloud-based AI vs local AI from a security perspective
- Testing local LLM capabilities and limitations
- Examination of prompt injection and indirect prompt risks
- Documentation of hardware, software, and operational requirements
- Development of conceptual data-flow diagrams (cloud vs local)

**Deliverables:**  
- Technical Comparison Report  
- Draft Startup Guide (early version)


### Milestone 3 – Education & Resource Development
**Weeks 8–9**

- Drafting educational materials for non-technical audiences
- Refinement of startup guidance for deploying Private AI locally
- Design of explainer content and supporting diagrams
- Early development of user interaction concepts (web and desktop)

**Deliverable:** Draft Toolkit (Guide + Content Drafts)


### Milestone 4 – Digital Platform & Communications
**Weeks 10–11**

- Development of a simple digital platform to host resources
- Introduction of backend structure to support demonstrations
- Implementation of basic privacy and security controls
- Containerisation and environment-based configuration
- Drafting a communications plan for Private AI education

**Deliverables:**  
- Website / Platform Prototype  
- Draft Communications Plan


### Milestone 5 – Final Integration & Presentation
**Week 12**

- Integration of research, technical findings, and educational content
- Refinement of prototype system and user interfaces
- Final documentation and reporting
- Preparation of final presentation for Stratigus Consulting

**Deliverables:**  
- Final Report  
- Educational Video  
- Website / Toolkit  
- Final Presentation


## DevOps and Engineering Practices (Later Stages)

DevOps practices were introduced **after research and feasibility were validated**, including:

- Git-based collaboration and version control
- Environment-driven configuration
- Docker and Docker Compose for reproducible deployment
- Separation of frontend, backend, and AI processing
- Basic health checks and service orchestration

These practices support scalability and demonstrate practical deployment considerations.


## Project Outcomes

By the end of the internship, the team delivered:

- A comprehensive analysis of AI cybersecurity and privacy risks
- Market insights into Private AI demand
- A technical and startup guide for local AI deployment
- Educational content for business audiences
- A prototype digital platform demonstrating Private AI concepts
- Strategic recommendations for Stratigus Consulting


## Learning Outcomes

This project provided hands-on experience in:

- Cybersecurity and privacy analysis
- AI risk assessment and mitigation
- Consulting-style research and reporting
- Technical prototyping of AI systems
- Team collaboration and leadership
- DevOps foundations and deployment practices


## Disclaimer

This repository contains a **research-driven prototype** developed for educational and internship purposes. It is not intended for production deployment without further security review, governance controls, and operational hardening.

## Conclusion

The Private AI internship project demonstrates how organisations can move from **problem identification and research** to **practical, privacy-aware AI solutions**. By combining market analysis, technical experimentation, and educational resource development, the project highlights both the risks of mainstream AI platforms and the opportunities presented by Private AI.



