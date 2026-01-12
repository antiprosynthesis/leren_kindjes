import operator
import platform
import random
import subprocess

def speak(text, wait=True, alsoPrint=True):
    if alsoPrint:
        print(text, end="", flush=True)
    text = text.replace(" - ", " min ") # hack
    system = platform.system()
    if system == "Darwin":
        proc = subprocess.Popen(["say", "-v", "Xander", text])
    elif system == "Windows":
        proc = subprocess.Popen(["powershell", "-Command", f"Add-Type -AssemblyName System.Speech; $s = New-Object System.Speech.Synthesis.SpeechSynthesizer; $s.SelectVoice('Microsoft Frank'); $s.Speak('{text}')"])
    if proc and wait:
        proc.wait()

print("\033[2J\033[H", end="") # clear
speak("Wat is je naam? ")
name = input()
speak(f"\nDag, {name}!\n\nLaten we sommetjes oplossen!\n\n")
while True:
    while True:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        op = operator.add if random.randint(0, 1) == 0 else operator.sub
        if op(a, b) >= 0 and op(a, b) <= 10:
            break
    while True:
        speak(f"{a} {"+" if op == operator.add else "-"} {b} = ")
        c = input()
        try:
            c = int(c)
        except ValueError:
            speak(f"\n{c} is geen getal!\n\n")
            continue
        if op(a, b) == c:
            print()
            speak(f"{a} {"+" if op == operator.add else "-"} {b} = {c}.", alsoPrint=False)
            speak(f"Goed zo, {name}!\n\n")
            break
        else:
            speak("\nFout! Probeer opnieuw.\n\n")
