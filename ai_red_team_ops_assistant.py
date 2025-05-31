import os
import google.generativeai as genai
import json # For potentially parsing JSON if used in advanced prompts

MODEL_NAME = "gemini-1.5-flash-latest"
GOOGLE_API_KEY = None
genai_client = None # Will be initialized after API key configuration

def configure_api_key():
    global GOOGLE_API_KEY, genai_client
    try:
        from google.colab import userdata
        GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
        print("Attempting to load API key from Colab secrets...")
    except ImportError:
        print("Not in Colab environment or google.colab.userdata not found.")
        pass
    except Exception as e:
        print(f"Error loading from Colab secrets: {e}")
        pass

    if not GOOGLE_API_KEY:
        print("Attempting to load API key from environment variable GOOGLE_API_KEY...")
        GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

    if not GOOGLE_API_KEY:
        print("ERROR: GOOGLE_API_KEY not found in Colab secrets or environment variables.")
        print("Please set it up to use the application.")
        return False
    else:
        try:
            genai.configure(api_key=GOOGLE_API_KEY)
            genai_client = genai.GenerativeModel(MODEL_NAME) # Initialize client here
            print("API Key configured and Gemini client initialized successfully.")
            return True
        except Exception as e:
            print(f"Error configuring Gemini API: {e}")
            return False

def suggest_recon_vectors(target_info):
    if not genai_client:
        print("ERROR: Gemini client not initialized. Please check API key configuration.")
        return

    print(f"\n[INFO] Analyzing target: {target_info[:60]}...")
    prompt = f"""
    You are an AI Red Team assistant.
    For a target described as '{target_info}', suggest detailed Open Source Intelligence (OSINT) reconnaissance vectors.
    Include specific types of information to look for, example tools (conceptually, e.g., "tools like Sublist3r or Amass for subdomain enumeration"),
    and potential search query ideas for search engines or specialized platforms (e.g., "site:{target_domain} filetype:pdf", "Shodan queries for specific ports/services").
    Structure your suggestions clearly.
    """
    try:
        response = genai_client.generate_content(prompt)
        print("--- Reconnaissance Vector Suggestions ---")
        print(response.text)
        print("--- End of Suggestions ---")
    except Exception as e:
        print(f"Error during reconnaissance suggestion: {e}")

def brainstorm_exploit_ideas(vulnerability_info):
    if not genai_client:
        print("ERROR: Gemini client not initialized.")
        return

    print(f"\n[INFO] Brainstorming exploits for: {vulnerability_info[:60]}...")
    prompt = f"""
    You are an AI assistant for a red team.
    A team member is investigating the following vulnerability: "{vulnerability_info}"
    From an attacker's perspective:
    1. What are potential high-level exploitation vectors or attack surfaces for this type of vulnerability?
    2. What prerequisites might be needed to successfully exploit it (e.g., network access, specific software versions, user interaction)?
    3. What could be potential post-exploitation goals if this vulnerability is leveraged (e.g., code execution, information disclosure, privilege escalation)?
    Focus on conceptual ideas and attacker mindset. Do not generate actual exploit code.
    Provide a detailed and structured response.
    """
    try:
        response = genai_client.generate_content(prompt)
        print("--- Exploitation Ideas ---")
        print(response.text)
        print("--- End of Ideas ---")
    except Exception as e:
        print(f"Error during exploit brainstorming: {e}")

def plan_attack_path(target_scenario, objective):
    if not genai_client:
        print("ERROR: Gemini client not initialized.")
        return

    print(f"\n[INFO] Planning attack path for scenario: {target_scenario[:60]}... Objective: {objective[:60]}...")
    prompt = f"""
    You are an AI Red Team strategist.
    Consider the following target scenario: "{target_scenario}"
    The objective is: "{objective}"

    Using a Chain of Thought approach, outline a plausible and detailed multi-stage attack path to achieve this objective.
    For each stage, consider:
    - Initial Access vector (if not already implied by the scenario).
    - Techniques for Privilege Escalation (mention specific techniques or tool categories).
    - Methods for Lateral Movement (mention specific techniques or tool categories).
    - Persistence mechanisms (if applicable, provide examples).
    - Key tools or types of tools that might be used at each stage (e.g., Mimikatz, BloodHound, Cobalt Strike concepts, PowerSploit modules).
    - Data exfiltration considerations (if part of the objective, suggest methods).

    Let's think step by step:
    1.  Initial Foothold: How is access gained or leveraged from the starting point? What are the first actions upon gaining access?
    2.  Local Reconnaissance & Privilege Escalation: What information is gathered on the first compromised host? What specific methods are used to escalate privileges locally?
    3.  Domain/Network Reconnaissance: How is the broader environment mapped? What tools or techniques are used to understand the AD structure, network topology, and identify further targets?
    4.  Lateral Movement & Further Privilege Escalation (Iterative): How to move to other systems? How to gain higher privileges across the network (e.g., Domain Admin)?
    5.  Achieving Objective: What are the final steps to access/exfiltrate data, or achieve the stated goal?
    6.  Persistence & Clean-up (Conceptual): How might an attacker maintain access discreetly and cover tracks (conceptually)?

    Describe this as a sequence of logical steps with clear explanations for each.
    """
    try:
        response = genai_client.generate_content(prompt)
        print("--- Attack Path Plan ---")
        print(response.text)
        print("--- End of Plan ---")
    except Exception as e:
        print(f"Error during attack path planning: {e}")

def generate_payload_concept(script_need):
    if not genai_client:
        print("ERROR: Gemini client not initialized.")
        return

    print(f"\n[INFO] Generating payload/script concept for: {script_need[:60]}...")
    prompt = f"""
    You are an AI assistant for a red team, helping to conceptualize custom tools.
    A team member needs a script for the following purpose: "{script_need}"
    Provide a detailed high-level conceptual outline or pseudocode for this script.
    Focus on:
    1. Key functions or modules needed and their purpose.
    2. The logical flow of operations, step-by-step.
    3. Important parameters or configurations it might take.
    4. Potential libraries or system calls that might be relevant (conceptually, e.g., "socket library for network connections", "os module for system interaction").
    DO NOT generate fully functional, ready-to-run, or malicious code. This is for conceptual planning and outlining the logic.
    Structure the output clearly, perhaps using bullet points for steps within functions.
    """
    try:
        response = genai_client.generate_content(prompt)
        print("--- Payload/Script Concept ---")
        print(response.text)
        print("--- End of Concept ---")
    except Exception as e:
        print(f"Error during payload concept generation: {e}")

def craft_phishing_pretext(target_org_or_role):
    if not genai_client:
        print("ERROR: Gemini client not initialized.")
        return

    print(f"\n[INFO] Crafting phishing pretext for: {target_org_or_role[:60]}...")
    prompt = f"""
    You are an AI Red Team assistant specializing in social engineering.
    For a phishing campaign targeting '{target_org_or_role}', help craft 2-3 distinct and plausible pretexts.
    For each pretext, provide:
    1.  **Pretext Name/Theme:** (e.g., "Urgent Security Alert," "Invoice Payment Overdue," "HR Policy Update")
    2.  **Target Audience within the org/role:** (Be specific if possible)
    3.  **Plausible Subject Line(s):** (Craft 2-3 options)
    4.  **Key Message Points/Body Outline:** (Summarize the core message, the hook, the call to action)
    5.  **Desired User Action:** (e.g., Click a link, open an attachment, provide credentials)
    6.  **Urgency/Emotion Leveraged:** (e.g., Fear, curiosity, authority, greed)
    Consider what would be most believable and enticing for the specified target.
    """
    try:
        response = genai_client.generate_content(prompt)
        print("--- Phishing Pretext Ideas ---")
        print(response.text)
        print("--- End of Ideas ---")
    except Exception as e:
        print(f"Error during phishing pretext generation: {e}")

def discuss_evasion_concepts(defense_type):
    if not genai_client:
        print("ERROR: Gemini client not initialized.")
        return

    print(f"\n[INFO] Discussing evasion concepts for: {defense_type[:60]}...")
    prompt = f"""
    You are an AI Red Team assistant.
    Discuss general principles and conceptual techniques for evading '{defense_type}'.
    Explain each concept briefly.
    Examples of concepts to consider if relevant to '{defense_type}':
    - For AV/EDR: Payload Obfuscation/Encryption, Living Off The Land Binaries (LOLBAS), In-memory execution, Process Hollowing/Injection, Direct System Calls, Disabling security features (with caveats about privileges).
    - For Network IDS/IPS/Firewalls: Traffic Encryption (HTTPS, DoH), Fragmentation, Traffic Obfuscation, Using common ports (80, 443), Domain Fronting (and its current limitations), Fast Flux DNS.
    - General: Understanding detection signatures/heuristics, minimizing footprint, time-based evasion.
    Focus on high-level concepts and their purpose, not specific tool commands or code.
    """
    try:
        response = genai_client.generate_content(prompt)
        print("--- Evasion Technique Concepts ---")
        print(response.text)
        print("--- End of Concepts ---")
    except Exception as e:
        print(f"Error during evasion concept discussion: {e}")

def main_loop():
    print("\nWelcome to the AI Red Team Ops Assistant!")
    print("This tool is for authorized educational and ethical red teaming purposes only.")
    print("Available commands:")
    print("  recon [target description]         - Suggest reconnaissance vectors")
    print("  exploit [vulnerability_desc]       - Brainstorm exploit ideas for a vulnerability")
    print("  attackpath [scenario] objective [obj] - Plan a conceptual attack path")
    print("  payload [script_need_description]  - Generate a conceptual script/payload idea")
    print("  phish [target_org_or_role]         - Craft phishing pretext ideas")
    print("  evasion [defense_type]             - Discuss evasion technique concepts")
    print("  quit                               - Exit the assistant")
    print("-" * 60)

    while True:
        try:
            user_input = input("\n🔴 > ").strip()
            if not user_input:
                continue

            parts = user_input.split(" ", 1)
            command = parts[0].lower()

            if command == "quit":
                print("Exiting. Remember to operate ethically and legally.")
                break
            elif command == "recon":
                if len(parts) > 1:
                    suggest_recon_vectors(parts[1])
                else:
                    print("Usage: recon [target description]")
            elif command == "exploit":
                if len(parts) > 1:
                    brainstorm_exploit_ideas(parts[1])
                else:
                    print("Usage: exploit [vulnerability description or CVE]")
            elif command == "attackpath":
                if len(parts) > 1 and "objective" in parts[1].lower():
                    try:
                        scenario_part, objective_part = parts[1].lower().split("objective", 1)
                        scenario = scenario_part.strip()
                        objective = objective_part.strip()
                        if scenario and objective:
                            plan_attack_path(scenario, objective)
                        else:
                            print("Usage: attackpath [scenario description] objective [objective description]")
                    except ValueError:
                        print("Usage: attackpath [scenario description] objective [objective description]")
                else:
                    print("Usage: attackpath [scenario description] objective [objective description]")
            elif command == "payload":
                if len(parts) > 1:
                    generate_payload_concept(parts[1])
                else:
                    print("Usage: payload [description of script/payload need]")
            elif command == "phish":
                if len(parts) > 1:
                    craft_phishing_pretext(parts[1])
                else:
                    print("Usage: phish [target organization or role]")
            elif command == "evasion":
                if len(parts) > 1:
                    discuss_evasion_concepts(parts[1])
                else:
                    print("Usage: evasion [defense type, e.g., AV, EDR, Network IDS]")
            else:
                print("Unknown command. Type 'help' for options (or see initial list).")

        except KeyboardInterrupt:
            print("\nExiting due to user interruption.")
            break
        except Exception as e:
            print(f"An unexpected error occurred in main loop: {e}")

if __name__ == "__main__":
    if configure_api_key():
        main_loop()
    else:
        print("Could not start the assistant due to API key issues.")
