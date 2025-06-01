# AI Red Team Ops Assistant

## 🔴 Overview

Welcome to the AI Red Team Ops Assistant project! This project adapts the prompting techniques from Day 1 of the Kaggle 5-day Generative AI course to the domain of **offensive cybersecurity and red teaming**. You will build a Python application that uses the Gemini API to simulate an AI assistant aiding in various red team operation tasks, from reconnaissance to exploitation ideation.

**Disclaimer:** This project is for educational purposes only. All activities should be conducted in authorized environments and with explicit permission. Misuse of these techniques for unauthorized activities is illegal and unethical.

## 📚 Learning Objectives

This project will help you practice and understand how prompting can assist in:

* **Reconnaissance Augmentation:** Generating ideas for information gathering.
* **Vulnerability Analysis (Offensive):** Brainstorming potential exploitation vectors for known vulnerabilities.
* **Attack Path Development:** Using Chain of Thought to outline potential multi-stage attacks.
* **Payload/Script Ideation:** Generating conceptual code snippets or logic for custom tools (not fully functional malware).
* **Social Engineering Scenario Crafting:** Developing plausible pretexts for phishing or other social engineering attacks.
* **Evasion Technique Brainstorming:** Thinking about how to bypass common defenses (conceptually).
* **Utilizing Prompting Techniques for Offensive Thinking:**
    * **Zero-shot:** Directly asking for attack ideas, tool suggestions for a specific task, or TTPs of certain actors.
    * **Few-shot:** (Optional) Providing examples of successful exploit chains or phishing email structures to guide AI output.
    * **JSON Mode:** Generating structured data like potential target lists, C2 communication parameters, or custom script arguments.
    * **Chain of Thought (CoT):** Guiding the AI to "think step-by-step" for complex attack planning or outlining custom tool development logic.

## ✨ Features

1.  **Target Reconnaissance Assistant:**
    * User provides a target profile (e.g., company name, domain, technology stack hints).
    * AI suggests types of information to gather (OSINT), potential tools, and search queries for reconnaissance.
2.  **Exploitation Vector Brainstormer:**
    * User provides a CVE identifier or a description of a discovered vulnerability.
    * AI brainstorms potential ways to exploit it, prerequisites for exploitation, and possible post-exploitation activities.
3.  **Attack Path Planner (CoT):**
    * User describes a target environment and an objective (e.g., "Gain domain admin on an internal network starting from a web server compromise").
    * AI, using Chain of Thought, outlines potential attack paths, including lateral movement techniques, privilege escalation methods, and data exfiltration strategies.
4.  **Custom Payload/Script Idea Generator:**
    * User describes a need (e.g., "A Python script to enumerate SMB shares after getting initial access," "A PowerShell one-liner for basic persistence").
    * AI generates conceptual code snippets or pseudocode outlining the logic. **(Focus on logic, not fully weaponized code)**.
5.  **Phishing Campaign Idea Generator:**
    * User specifies a target organization or role.
    * AI helps craft plausible phishing pretexts, subject lines, and key message points.
    * (Optional) Use JSON mode to structure campaign elements.
6.  **Evasion Technique Brainstormer (Conceptual):**
    * User asks about bypassing a specific defense (e.g., "How might one conceptually try to evade AV detection for a custom script?").
    * AI discusses general principles and techniques (e.g., obfuscation, encryption, living-off-the-land) **at a conceptual level**.

## 🛠️ How to Use / Setup

### Prerequisites

* Python 3.7+
* Access to the Gemini API and an API Key.
* `google-generativeai` library installed (e.g., `pip install -U -q google-generativeai`).

### Installation & Setup

1.  **Create Project File:** Create a new Python file, e.g., `ai_red_team_ops_assistant.py`.
2.  **Set up API Key:**
    * Ensure you have your `GOOGLE_API_KEY`.
    * In Google Colab, use the Secrets manager (🔑 icon). Name the secret `GOOGLE_API_KEY`.
    * For local development, set it as an environment variable or load it securely.

    ```python
    # In your Python script
    import google.generativeai as genai
    import os

    # For Colab:
    # from google.colab import userdata
    # GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')

    # For local development (example):
    # GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

    if not GOOGLE_API_KEY:
        raise ValueError("Please set your GOOGLE_API_KEY.")
    genai.configure(api_key=GOOGLE_API_KEY)
    ```

### Running the Script

1.  You will build the Python script (`ai_red_team_ops_assistant.py`) with functions to handle the different features.
2.  Run the script from your terminal: `python ai_red_team_ops_assistant.py` (or run cells in Colab).
3.  Follow the interactive prompts in your console.

##  Project Structure

Organize your code into functions for clarity:

* `suggest_recon_vectors(target_info)`
* `brainstorm_exploit_ideas(vulnerability_info)`
* `plan_attack_path(target_scenario, objective)`
* `generate_payload_concept(script_need)`
* `craft_phishing_pretext(target_org_or_role)`
* `discuss_evasion_concepts(defense_type)`
* `main_loop()`: Handles user interaction.

## 🚀 Prompting Techniques to Explore & Implement

### Exploitation Vector Brainstormer (Zero-shot):

- Prompt: "Given CVE-YYYY-ZZZZ affecting Apache Struts, what are common conceptual exploitation vectors a red teamer might consider?"

### Payload Concept Generator (Zero-shot/CoT):

- Prompt: "Outline the logic for a Python script that uses Shodan API to find open RDP ports for a list of IPs. Think step-by-step: API key input, IP list processing, Shodan query construction, parsing results, output format."

### Attack Path Planner (Chain of Thought - CoT):

- Prompt: "A red team has initial access to a non-privileged user account on a Windows workstation in a corporate network. The objective is to exfiltrate sensitive documents from the CFO's machine. Outline a plausible attack path, thinking step-by-step about recon, privilege escalation, lateral movement, and data access/exfil."

### Phishing Pretext (JSON Mode):

- Prompt the AI to generate elements for a phishing campaign (e.g., target role, pretext, subject, call to action, urgency factor) and output them as a JSON object.

### Temperature for Brainstorming:

- When brainstorming exploit ideas or evasion techniques, a slightly higher temperature (e.g., 0.7-0.9) might generate more diverse, creative (though potentially less practical or more prone to hallucination) ideas. Review critically.

### 🙏 Acknowledgements

* This project derives inspiration from, and serves as a practical exercise based upon, concepts presented in the **5-Day Gen AI Intensive Course with Google Learn Guide Unit 1 – “Prompt Engineering”**. Specifically, it applies principles demonstrated in the following Kaggle codelabs and supplementary materials:
    * **Prompting fundamentals:** <https://www.kaggle.com/code/markishere/day-1-prompting>
    * **Whitepaper on Prompt Engineering:** <https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view>

- This "AI Red Team Ops Assistant" should be a challenging and engaging way to apply LLM prompting to offensive security scenarios. Always remember the ethical responsibilities and legal boundaries. Good luck!


