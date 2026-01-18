# SIMPLE ANDROID BOT
print("🤖 BOT STARTING ON ANDROID")
print("==========================")

# What you want
command = "give me time"  # Change this!

if "give me" in command.lower():
    what = command.lower().replace("give me", "").strip()
    
    from datetime import datetime
    
    if "time" in what:
        print(f"⏰ Time: {datetime.now().strftime('%I:%M %p')}")
    elif "date" in what:
        print(f"📅 Date: {datetime.now().strftime('%B %d, %Y')}")
    elif "hello" in what:
        print("👋 Hello from Android!")
    elif "test" in what:
        print("✅ Bot working on Android!")
    else:
        print(f"❓ Try: give me time/date/hello/test")
else:
    print('Say "give me [something]"')
