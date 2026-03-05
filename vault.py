from cryptography.fernet import Fernet
import os

# --- MINI-STEP A: The Key Maker ---
def create_key():
    # This creates a unique key
    key = Fernet.generate_key()
    # This saves the key into a file named 'secret.key'
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("A new Master Key has been created and saved as 'secret.key'!")

# --- MINI-STEP B: Checking for the Key ---
# We only want to create a key if one doesn't already exist
if not os.path.exists("secret.key"):
    create_key()
else:
    print("Master Key found! We are ready to scramble some files.")

# --- MINI-STEP C: Testing the Scrambler ---
# Let's load the key we just made
with open("secret.key", "rb") as key_file:
    my_key = key_file.read()

# Create our "Scrambling Tool" using our key
scrambler = Fernet(my_key)

# Scramble a secret message!
secret_message = "This is a secret for the future".encode()
scrambled_text = scrambler.encrypt(secret_message)

print("--- TEST RESULTS ---")
print(f"Original: This is a secret for the future")
print(f"Scrambled: {scrambled_text}")


import datetime

# --- MINI-STEP A: The "Today" Marker ---
# This creates a file that saves exactly when you last ran this script.
def check_in():
    # 'w' means OverWrite (erase the old date and put the new one)
    with open("last_seen.txt", "w") as f:
        f.write(str(datetime.datetime.now()))
    print("Check-in successful! Your 'Heartbeat' is updated (and storage is saved).")

# --- MINI-STEP B: The "Counting" Logic ---
def check_timer(days_to_wait):
    # 1. Read the last time we saw you
    if os.path.exists("last_seen.txt"):
        with open("last_seen.txt", "r") as f:
            last_seen_str = f.read()
            last_seen_time = datetime.datetime.fromisoformat(last_seen_str)
        
        # 2. Compare "Last Seen" to "Right Now"
        time_passed = datetime.datetime.now() - last_seen_time
        days_passed = time_passed.days
        
        print(f"Days since last check-in: {days_passed}")
        
        # 3. Check if it's time to open the vault
        if days_passed >= days_to_wait:
            print("ALERT: Timer expired! Releasing the vault...")
            return True # This means "Yes, open it!"
        else:
            print(f"Vault is still locked. You have {days_to_wait - days_passed} days left.")
            return False # This means "Stay locked."
    else:
        # If the file doesn't exist, we create it for the first time
        check_in()
        return False

# --- RUN THE TEST ---
check_in() # Run this to mark "Today"
is_expired = check_timer(30) # Check if 30 days have passed




import smtplib
from email.message import EmailMessage

def send_the_legacy(secret_data):
    msg = EmailMessage()
    msg['Subject'] = "🔒 Digital Inheritance: Automatic Release"
    msg['From'] = "arunt@example.com"  # <--- PUT YOUR GMAIL ADDRESS HERE
    msg['To'] = "friend@example.com"    # <--- PUT THE RECEIVER'S EMAIL HERE
    
    # The message they will receive
    content = f"""
    This is an automated message from the Digital Vault.
    The owner has not checked in for 30 days.
    
    ENCRYPTED DATA:
    {secret_data}
    """
    msg.set_content(content)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            # USE YOUR NEW APP PASSWORD HERE:
            smtp.login("arunt@example.com", "abto wyqv jbcu irrn") 
            
            smtp.send_message(msg)
            print("🚀 SUCCESS: The Legacy Message has been sent!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

# This part triggers the email if the timer is up
if is_expired:
    send_the_legacy(scrambled_text)
    
    
    
    # --- THE FINAL BRAIN ---
if is_expired:
    # This only runs if the 30 days are up!
    # We send the scrambled secret we made earlier
    send_the_legacy(scrambled_text)
else:
    # This runs every day while you are active
    print("Vault is secure. No email sent today.")