import operator
import platform
import random
import subprocess

def speak(text, wait=True, alsoPrint=True):
    if alsoPrint:
        print(text, end="", flush=True)
    text = text.replace(" - ", " min ") # hack
    text = text.replace(" x ", " maal ") # hack
    text = text.replace(" : ", " gedeeld door ") # hack
    system = platform.system()
    if system == "Darwin":
        proc = subprocess.Popen(["say", "-v", "Xander", text])
    elif system == "Windows":
        proc = subprocess.Popen(["powershell", "-Command", f"Add-Type -AssemblyName System.Speech; $s = New-Object System.Speech.Synthesis.SpeechSynthesizer; $s.SelectVoice('Microsoft Frank'); $s.Speak('{text}')"])
    if proc and wait:
        proc.wait()

ops = [operator.add, operator.sub, operator.mul, operator.floordiv]
op_names = ["+", "-", "x", ":"]

print("\033[2J\033[H", end="") # clear
speak("Wat is je naam? ")
name = input()
speak(f"\nDag, {name}!\n\nLaten we sommetjes oplossen!\n\n")
while True:
    op_i = random.randint(0, len(ops) - 1)
    op = ops[op_i]
    op_name = op_names[op_i]
    while True:
        if op == operator.mul:
            a = random.randint(0, 10)
            b = random.randint(0, 10)
        elif op == operator.floordiv:
            b = random.randint(1, 10)
            a = random.randint(0, 10)*b
        else:
            a = random.randint(0, 100)
            b = random.randint(0, 100)
        if op(a, b) >= 0:
            break
    while True:
        speak(f"{a} {op_name} {b} = ")
        c = input()
        try:
            c = int(c)
        except ValueError:
            speak(f"\n{c} is geen getal!\n\n")
            continue
        if op(a, b) == c:
            print()
            speak(f"{c}", alsoPrint=False)
            break
        else:
            speak("\nFout! Probeer opnieuw.\n\n")
