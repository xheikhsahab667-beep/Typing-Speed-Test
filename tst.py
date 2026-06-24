import time
import random
import msvcrt

paragraphs = {
    30: [
        "Python is simple readable and powerful.",
        "Fast typing saves time and improves work.",
        "Practice daily to become a better programmer.",
        "Accuracy is more important than only speed.",
        "Small projects help beginners learn faster.",
    ],
    60: [
        "Python is one of the most popular programming languages because it is simple readable and powerful. Beginners use Python to learn logic and build small useful projects.",
        "Typing speed is important for students programmers writers and office workers. Fast typing saves time but accuracy is also important because fewer mistakes make work easier.",
        "Learning programming takes patience and consistency. Beginners should practice variables input output conditions loops lists and functions by creating useful programs.",
        "Technology has changed the way people study work communicate and do business. Good developers think logically solve problems test programs and keep learning new skills.",
    ],
    120: [
        "Python is one of the most popular programming languages because it is simple readable and powerful. Beginners use Python to learn logic build projects solve problems and understand how real applications work. With regular practice they can create useful tools games websites and automation programs.",
        "Typing speed is important for students programmers writers and office workers. Fast typing saves time but accuracy is also important because fewer mistakes make work easier and cleaner. A good typer focuses on correct words first and then slowly improves speed with regular practice.",
        "Learning programming takes patience and consistency. Beginners should practice variables input output conditions loops lists and functions by creating small useful projects. Programming becomes easier when students write code daily test their programs fix errors and try to understand the logic behind every solution.",
        "Success in programming requires discipline curiosity practice and patience. Mistakes are a normal part of learning because every error teaches something new. Beginners should not fear errors because debugging improves thinking and helps them understand how programs really work in different situations.",
    ],
}


def choose_time():
    print("1. 30 Seconds")
    print("2. 60 Seconds")
    print("3. 120 Seconds")

    choice = input("Choose time: ").strip()
    return {"1": 30, "2": 60, "3": 120}.get(choice, 60)


def style(wpm, acc):
    if acc < 60:
        return "Needs Accuracy Practice"
    elif wpm < 20:
        return "Slow Beginner"
    elif wpm < 35:
        return "Good Beginner"
    elif wpm < 50:
        return "Average Typer"
    elif wpm < 70:
        return "Fast Typer"
    else:
        return "Excellent Typer"


def timed_input(limit):
    text = ""
    start = time.time()

    print("\nStart Typing:\n")
    print("> ", end="", flush=True)

    while time.time() - start < limit:
        if msvcrt.kbhit():
            key = msvcrt.getwch()

            if key == "\r":
                break

            elif key == "\b":
                if text:
                    text = text[:-1]
                    print("\b \b", end="", flush=True)

            else:
                text += key
                print(key, end="", flush=True)

        time.sleep(0.01)

    used = min(time.time() - start, limit)
    return text, used


def check(original, typed):
    original_words = original.split()
    typed_words = typed.split()

    correct = 0

    for i, word in enumerate(typed_words):
        if i < len(original_words) and word == original_words[i]:
            correct += 1

    wrong = len(typed_words) - correct
    missed = max(len(original_words) - len(typed_words), 0)

    return correct, wrong, missed


# Main Program
print("=" * 40)
print("        TYPING SPEED TEST")
print("=" * 40)

limit = choose_time()

paragraph = random.choice(paragraphs[limit])

print("\nType the following paragraph:\n")
print(paragraph)

input("\nPress Enter when ready...")

typed, used = timed_input(limit)

correct, wrong, missed = check(paragraph, typed)

chars = len(typed)
words = len(typed.split())

wpm = (chars / 5) / (used / 60) if used > 0 else 0

acc = (correct / words) * 100 if words > 0 else 0

print("\n\nRESULT")
print("-" * 40)
print(f"Time Limit      : {limit} sec")
print(f"Time Used       : {used:.2f} sec")
print(f"Characters Typed: {chars}")
print(f"Words Typed     : {words}")
print(f"Correct Words   : {correct}")
print(f"Wrong Words     : {wrong}")
print(f"Missed Words    : {missed}")
print(f"Typing Speed    : {wpm:.2f} WPM")
print(f"Accuracy        : {acc:.2f}%")
print(f"Typing Style    : {style(wpm, acc)}")
print("-" * 40)
