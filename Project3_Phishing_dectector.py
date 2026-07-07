import re
import sys

# Suspect indicators used for string validation and pattern matching
SUSPICIOUS_KEYWORDS = [
    "urgent", "action required", "suspended", "verify your identity",
    "payout", "legal action", "bank details", "claim", "immediate"
]

COMMON_SHORTENERS = ["bit.ly", "tinyurl.com", "t.co", "is.gd", "buff.ly"]



def analyze_message(sender, subject, body):
    """
    Performs algorithmic inspection on an email to isolate red flags,
    detect hidden links/shorteners, and grade risk profile.
    """
    red_flags = []
    is_unsafe = False
    reasons = []

    # 1. Inspect Sender Address for Domain Anomalies
    
    if "paypal" in sender and not sender.endswith("@paypal.com"):
        red_flags.append(f"Spoofed Sender Domain ({sender})")
        reasons.append("The sender claims to be PayPal but uses a deceptive, non-official domain.")

    # Basic heuristic flag for lookalike/external domains used for internal corporate communications
    if sender.endswith(".net") or sender.endswith(".org"):
        if "internal-company" in sender:
            red_flags.append("Suspicious external TLD for internal communication")
            reasons.append("Internal company HR should come from your local domain, not a generic .net address.")

    # 2. Inspect Body Text for Psychological Traps (Urgency, Fear etc)
    body_lower = body.lower()
    found_keywords = [word for word in SUSPICIOUS_KEYWORDS if word in body_lower]
    if len(found_keywords) > 0:
        red_flags.append(f"Urgent/Threatening Language {found_keywords}")
        reasons.append("The message leverages high-pressure language or artificial deadlines to bypass logical thinking.")

    # 3. Advanced Analysis: Detect URLs and Malicious URL Shorteners

    urls = re.findall(r'(https?://\S+)', body)
    for url in urls:
        # Check if URL uses a known shortener service to obscure the actual target destination
        if any(shortener in url for shortener in COMMON_SHORTENERS):
            red_flags.append(f"Obscured URL / URL Shortener Found ({url})")
            reasons.append("The message uses an administrative URL shortener (like bit.ly) to mask where the link truly goes.")
        elif "http://" in url:
            red_flags.append(f"Insecure Hyperlink Protocol ({url})")
            reasons.append("The link transmits information over unencrypted HTTP instead of HTTPS.")

    # Determine structural safety based on findings
    if len(red_flags) > 0:
        is_unsafe = True

    return {
        "is_unsafe": is_unsafe,
        "red_flags": red_flags,
        "reasons": reasons,
        "detected_urls": urls
    }


def generate_employee_checklist():
    """Returns a dynamic security posture checklist for training documentation."""
    return [
        "1. Hover before Clicking: Verify the absolute URL destination match.",
        "2. Analyze the Urgency: Real security requests rarely threaten immediate loss of access in 24 hours.",
        "3. Inspect Sender Rigor: Look for subtle misspellings (e.g., paypa1.com vs paypal.com).",
        "4. Beware of Shared Forms: External tools like Google Forms or Typeform are rarely used for internal payroll adjustments.",
        "5. Treat shortened URLs (bit.ly, tinyurl) as hostile until untrusted sources are parsed."
    ]


# --- INTERACTIVE INTERFACE ---

def main():
    while True:
        print("\n==============================================", flush=True)
        print("🕵️ DECODELABS: PHISHING THREAT DETECTOR ", flush=True)
        print("==============================================", flush=True)
        print("1. Analyze Custom Inbound Email/Message", flush=True)
        print("2. Generate Employee 'Red Flag' Posture Checklist", flush=True)
        print("3. Exit", flush=True)

        sys.stdout.flush()
        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            print("\n--- Custom Inbound Message Inspection ---", flush=True)
            sender = input("Enter Sender Email Address: ").strip()
            subject = input("Enter Subject Line: ").strip()
            print("Enter Message Body (Press Enter when done):")
            body = input().strip()

            analysis = analyze_message(sender, subject, body)

            print("\n---  PARSING MATRIX RESULT ---", flush=True)
            print(f"Original Sender:  {sender}", flush=True)
            print(f"Detected Links:   {analysis['detected_urls']}", flush=True)
            print(f"Threat Score:     {'HIGH RISK 🚨' if analysis['is_unsafe'] else 'LOW RISK ✅'}", flush=True)

            if analysis["is_unsafe"]:
                print("\n🚩 Red Flags Identified:", flush=True)
                for flag in analysis['red_flags']:
                    print(f"   - {flag}", flush=True)
                print("\n Why This Message Is Unsafe:", flush=True)
                for reason in analysis["reasons"]:
                    print(f"   • {reason}", flush=True)
            else:
                print("\nNo obvious phishing anomalies caught by the heuristics engine.", flush=True)

        elif choice == '2':
            print("\nGENERATING ENTERPRISE WORKPLACE POSTURE CHECKLIST:", flush=True)
            checklist = generate_employee_checklist()
            for line in checklist:
                print(line, flush=True)
            print("\n*Use these structural indicators to train teams against human-factor error.*", flush=True)

        elif choice == '3':
            print("\nExiting Threat Matrix Engine. Safe hunting! 🚀", flush=True)
            break
        else:
            print("Invalid choice. Select 1-3.", flush=True)


if __name__ == "__main__":
    main()
